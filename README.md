# 🚀 Multi-Stage Docker Deployment Guide

This project supports Docker-based deployment for the following environments:

- ✅ Beta
- ✅ Stage
- ✅ Production

---

## 📦 Prerequisites

- Docker installed
- Docker Compose (optional)
- Application environment files, secrets, and credentials as required

---

## 🧪 BETA ENVIRONMENT

### 🔨 Build Image

```bash
docker build -f Dockerfile -t your-app-name:beta .
```

### ▶️ Run Container

```bash
docker run -d \
  --name your-app-beta \
  -p 8001:8000 \
  your-app-name:beta
```

---

## 🧪 STAGE ENVIRONMENT

### 🔨 Build Image

```bash
docker build -f Dockerfile_stage -t your-app-name:stage .
```

### ▶️ Run Container

```bash
docker run -d \
  --name your-app-stage \
  -p 8002:8000 \
  your-app-name:stage
```

---

## 🏁 PRODUCTION ENVIRONMENT

### 🔨 Build Image

```bash
docker build -f Dockerfile_prod -t your-app-name:prod .
```

### ▶️ Run Container

```bash
docker run -d \
  --name your-app-prod \
  -p 8003:8000 \
  your-app-name:prod
```

---

## ✅ Check Running Containers

```bash
docker ps
```

## ❌ Stop & Remove Container

```bash
docker stop <container_name> && docker rm <container_name>
```

## 🧼 Remove Image

```bash
docker rmi your-app-name:<env>
```

---

## 💡 Tips

- Adjust `-p` ports based on your environment setup.
- Use `.env` files for injecting environment variables if needed.
- You can also create a `docker-compose.yml` for managing multiple environments.
