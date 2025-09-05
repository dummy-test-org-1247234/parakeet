"""
Unit tests for the Parakeet FastAPI application.
"""
import pytest
from fastapi.testclient import TestClient
from src.parakeet.main import app

client = TestClient(app)


def test_hello_endpoint():
    """Test the /hello endpoint returns the correct message."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "I'm a Parakeet"}


def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_openapi_schema():
    """Test that OpenAPI schema is accessible."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    openapi_schema = response.json()
    assert openapi_schema["info"]["title"] == "Parakeet API"
    assert "/hello" in openapi_schema["paths"]


def test_docs_endpoint():
    """Test that docs endpoint is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_hello_response_content_type():
    """Test that /hello endpoint returns JSON."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


def test_nonexistent_endpoint():
    """Test that nonexistent endpoints return 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404