# Demo

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Run with Docker

```bash
docker build -t homelab-ai-platform:local .
docker run --rm -p 8080:8080 homelab-ai-platform:local
```

## Deploy with manifests

```bash
kubectl apply -f manifests/deployment.yaml
kubectl get pods,svc -l app=homelab-ai-platform
```

## Deploy with Helm

```bash
helm upgrade --install homelab-ai-platform ./helm/homelab-ai-platform
```
