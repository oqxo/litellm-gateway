
# 🚀 AI Gateway (LiteLLM + Caddy + PostgreSQL)

A local OpenAI-compatible AI gateway built using:
- LiteLLM (LLM routing + API server)
- PostgreSQL (DB backend)
- Caddy (reverse proxy + HTTPS)
- Custom portal UI

---

## 🧱 Architecture

```
https://portal.ai.gateway
        │
      Caddy (TLS + Reverse Proxy)
        │
   LiteLLM Gateway (:4000)
        │
   PostgreSQL Database
```

---

## ⚙️ Features

- OpenAI-compatible API (`/v1`)
- Virtual API keys
- Multi-provider routing (OpenAI, etc.)
- Batch API support
- Health monitoring
- Custom landing page (`www/index.html`)
- Local HTTPS with trusted cert (Caddy internal CA)

---

## 📦 Setup

### 1. Clone project

```bash
git clone <repo-url>
cd litellm-gateway
```

---

### 2. Start services

```bash
docker compose up -d
```

---

### 3. Install & run Caddy

```bash
scoop install caddy
caddy run
```

---

### 4. Map local domain (Windows)

Edit:

```
C:\Windows\System32\drivers\etc\hosts
```

Add:

```
127.0.0.1 portal.ai.gateway
```

---

### 5. Access

| Service | URL |
|--------|-----|
| Gateway UI | https://portal.ai.gateway |
| API Base | https://portal.ai.gateway/v1 |
| Health | https://portal.ai.gateway/health |
| Swagger | https://portal.ai.gateway/docs |
| OpenAPI | https://portal.ai.gateway/openapi.json |

---

## 🔐 Auth

Use virtual keys:

```
sk-xxxx
```

Python example:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://portal.ai.gateway/v1",
    api_key="sk-xxxx"
)
```

---

## 🧠 Notes

- Uses Caddy internal CA (no real domain needed)
- Fully local / offline capable
- Swagger available at `/docs`

---

## 🚀 Future upgrades

- Usage tracking
- Rate limiting
- Cost dashboard
- Role-based keys
