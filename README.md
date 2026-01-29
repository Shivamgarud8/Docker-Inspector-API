# 🐳 Docker-Health-Guard  - Docker & Host Health Monitoring System

 ***Docker-Health-Guard*** is a **Flask-based Docker monitoring agent** that runs on any Linux server and provides **real-time visibility into Docker containers, images, disk usage, and host system health** via REST APIs and a simple web UI.

It is designed to be **lightweight**, **self-hosted**, and **easy to deploy using Docker**.

---
## 🧰 Tech Stack & Tools

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containers-blue?logo=docker)
![Linux](https://img.shields.io/badge/Linux-Server-yellow?logo=linux)
![REST API](https://img.shields.io/badge/API-JSON-brightgreen)
![Port](https://img.shields.io/badge/Port-5000-blue)
---

## 🚀 Features

### 🔹 Container Monitoring
- Total containers (running + stopped)
- Per-container details:
  - Container ID & name
  - Image name
  - Status (running / exited)
  - CPU usage (%)
  - Memory usage & limit (MB)
  - Exposed ports
  - Mounts
  - Environment variables
  - Network mode
  - Restart policy
  - Creation timestamp

### 🔹 Image Analytics
- Total Docker images
- Image size (MB)
- Image tags
- Image creation time
- Total disk space used by images

### 🔹 Docker Host Information
- Operating system
- Kernel version
- Architecture
- CPU cores
- Total system memory
- Docker version
- Storage driver

### 🔹 Disk Usage (Docker Level)
- Images disk usage
- Containers disk usage
- Volumes disk usage
- Build cache usage

### 🔹 System Summary Stats
- Running containers
- Stopped containers
- Total containers
- Total images

---


---

## 🧩 Project Overview

DockPulse monitors:

- **Containers:** running/stopped, CPU & memory usage, ports, mounts, env vars, restart policy  
- **Images:** tags, size, creation time, total disk usage  
- **Docker Host:** OS, kernel, architecture, CPU cores, memory, Docker version  
- **Disk Usage:** containers, images, volumes, build cache  
- **System Summary:** total containers, running, stopped, total images

---

## 🧱 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/DockPulse.git
cd DockPulse
```

---
👩‍🏫 **Guided and Supported by [Trupti Mane Ma’am](https://github.com/iamtruptimane)**  
---

👨‍💻 **Developed By:**  
**Shivam Garud**  
🧠 *DevOps & Cloud Enthusiast*  
💼 *Automating deployments, one pipeline at a time!*  
🌐 [GitHub Profile](https://github.com/Shivamgarud8)
🌐 [Medium blog](https://medium.com/@shivam.garud2011)
