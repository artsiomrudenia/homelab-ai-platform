from fastapi import FastAPI

app = FastAPI(title="homelab-ai-platform", version="0.1.0")


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.get("/info")
def info() -> dict:
    return {
        "project": "homelab-ai-platform",
        "description": "Reference platform for self-hosted AI services",
        "domain": "homelab",
    }
