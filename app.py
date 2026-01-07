from flask import Flask, jsonify, render_template
import docker
import datetime

app = Flask(__name__)
client = docker.from_env()
low = docker.APIClient(base_url="unix://var/run/docker.sock")


def bytes_to_mb(value):
    return round(value / (1024 * 1024), 2)


@app.route("/")
def index():
    return render_template("index.html")


# -------------------- CONTAINERS --------------------
@app.route("/containers")
def containers():
    containers = client.containers.list(all=True)
    data = []

    for c in containers:
        stats = {}
        if c.status == "running":
            s = c.stats(stream=False)
            cpu_delta = s["cpu_stats"]["cpu_usage"]["total_usage"] - \
                        s["precpu_stats"]["cpu_usage"]["total_usage"]
            system_delta = s["cpu_stats"]["system_cpu_usage"] - \
                           s["precpu_stats"]["system_cpu_usage"]
            cpu_percent = (cpu_delta / system_delta) * len(
                s["cpu_stats"]["cpu_usage"]["percpu_usage"]
            ) * 100 if system_delta > 0 else 0

            mem_usage = s["memory_stats"]["usage"]
            mem_limit = s["memory_stats"]["limit"]

            stats = {
                "cpu_percent": round(cpu_percent, 2),
                "memory_used_mb": bytes_to_mb(mem_usage),
                "memory_limit_mb": bytes_to_mb(mem_limit)
            }

        ports = c.attrs["NetworkSettings"]["Ports"]
        exposed_ports = list(ports.keys()) if ports else []

        data.append({
            "id": c.short_id,
            "name": c.name,
            "image": c.image.tags[0] if c.image.tags else "<none>",
            "status": c.status,
            "created": c.attrs["Created"],
            "ports": exposed_ports,
            "mounts": c.attrs["Mounts"],
            "env": c.attrs["Config"]["Env"],
            "network_mode": c.attrs["HostConfig"]["NetworkMode"],
            "restart_policy": c.attrs["HostConfig"]["RestartPolicy"],
            "stats": stats
        })

    return jsonify({
        "total_containers": len(containers),
        "containers": data
    })


# -------------------- IMAGES --------------------
@app.route("/images")
def images():
    images = client.images.list()
    total_size = sum(img.attrs["Size"] for img in images)

    data = []
    for img in images:
        data.append({
            "id": img.short_id.replace("sha256:", ""),
            "tags": img.tags if img.tags else ["<none>"],
            "size_mb": bytes_to_mb(img.attrs["Size"]),
            "created": img.attrs["Created"]
        })

    return jsonify({
        "total_images": len(images),
        "total_size_mb": bytes_to_mb(total_size),
        "images": data
    })


# -------------------- DOCKER HOST INFO --------------------
@app.route("/host")
def host_info():
    info = client.info()
    version = client.version()

    return jsonify({
        "os": info["OperatingSystem"],
        "kernel_version": info["KernelVersion"],
        "architecture": info["Architecture"],
        "cpu_cores": info["NCPU"],
        "total_memory_mb": bytes_to_mb(info["MemTotal"]),
        "docker_version": version["Version"],
        "storage_driver": info["Driver"]
    })


# -------------------- DISK USAGE --------------------
@app.route("/disk")
def disk_usage():
    usage = low.df()

    return jsonify({
        "images_size_mb": bytes_to_mb(usage["ImagesSize"]),
        "containers_size_mb": bytes_to_mb(usage["ContainersSize"]),
        "volumes_size_mb": bytes_to_mb(usage["VolumesSize"]),
        "build_cache_mb": bytes_to_mb(usage["BuildCache"])
    })


# -------------------- SYSTEM STATS --------------------
@app.route("/stats")
def stats():
    running = client.containers.list()
    all_containers = client.containers.list(all=True)
    images = client.images.list()

    stopped = len([c for c in all_containers if c.status != "running"])

    return jsonify({
        "running_containers": len(running),
        "stopped_containers": stopped,
        "total_containers": len(all_containers),
        "total_images": len(images)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
