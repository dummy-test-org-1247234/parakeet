# Parakeet FastAPI Application

A simple FastAPI application that responds "I'm a Parakeet" from the `/hello` endpoint.

## Features

- FastAPI web framework with OpenAPI documentation
- GET `/hello` endpoint that returns `{"message": "I'm a Parakeet"}`
- Health check endpoint at `/health`
- Unit and integration tests
- Docker containerization using amazonlinux:2023
- Kubernetes deployment with 2 replicas
- Dependency management with UV

## Quick Start

### Development

1. Install dependencies using uv:
```bash
uv sync --extra test
```

2. Run the application:
```bash
uv run python -m uvicorn src.parakeet.main:app --host 0.0.0.0 --port 8000
```

3. Access the application:
- API: http://localhost:8000/hello
- Health: http://localhost:8000/health  
- Docs: http://localhost:8000/docs

### Testing

Run unit tests:
```bash
uv run pytest tests/test_unit.py -v
```

Run integration tests:
```bash
uv run pytest tests/test_integration.py -v
```

Run all tests:
```bash
uv run pytest -v
```

### Docker

Build the Docker image:
```bash
docker build -t parakeet:latest .
```

Run the container:
```bash
docker run -p 8000:8000 parakeet:latest
```

### Kubernetes Deployment

Deploy to Kubernetes with 2 replicas and load balancer:
```bash
kubectl apply -f deployment.yaml
```

This creates:
- A deployment with 2 replicas
- A ClusterIP service for internal communication
- A LoadBalancer service for external access

## API Endpoints

- `GET /hello` - Returns `{"message": "I'm a Parakeet"}`
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation
- `GET /openapi.json` - OpenAPI schema

## Project Structure

```
.
├── src/
│   └── parakeet/
│       ├── __init__.py
│       └── main.py          # FastAPI application
├── tests/
│   ├── __init__.py
│   ├── test_unit.py         # Unit tests
│   └── test_integration.py  # Integration tests  
├── pyproject.toml           # UV dependencies and config
├── Dockerfile              # Container definition
├── deployment.yaml         # Kubernetes deployment
└── README.md
```
