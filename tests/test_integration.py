"""
Integration tests for the Parakeet FastAPI application.
"""
import pytest
import httpx
import asyncio
from unittest.mock import patch
import subprocess
import time
import signal
import os


class TestParakeetIntegration:
    """Integration tests that test the full application."""
    
    @pytest.fixture(scope="class")
    def server_process(self):
        """Start the FastAPI server for integration testing."""
        # Start the server in a subprocess
        process = subprocess.Popen(
            ["uv", "run", "python", "-m", "uvicorn", "src.parakeet.main:app", "--host", "127.0.0.1", "--port", "8001"],
            cwd="/home/runner/work/parakeet/parakeet",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to start
        time.sleep(2)
        
        # Verify server is running
        try:
            response = httpx.get("http://127.0.0.1:8001/health", timeout=5)
            if response.status_code != 200:
                process.terminate()
                raise Exception("Server failed to start properly")
        except Exception as e:
            process.terminate()
            raise Exception(f"Server failed to start: {e}")
        
        yield process
        
        # Cleanup
        process.terminate()
        process.wait()

    def test_hello_endpoint_integration(self, server_process):
        """Test /hello endpoint with real HTTP request."""
        response = httpx.get("http://127.0.0.1:8001/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "I'm a Parakeet"}

    def test_health_endpoint_integration(self, server_process):
        """Test health endpoint with real HTTP request."""
        response = httpx.get("http://127.0.0.1:8001/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

    def test_multiple_concurrent_requests(self, server_process):
        """Test multiple concurrent requests to ensure the app handles load."""
        async def make_request():
            async with httpx.AsyncClient() as client:
                response = await client.get("http://127.0.0.1:8001/hello")
                return response.status_code, response.json()

        async def test_concurrent():
            tasks = [make_request() for _ in range(10)]
            results = await asyncio.gather(*tasks)
            
            for status_code, json_response in results:
                assert status_code == 200
                assert json_response == {"message": "I'm a Parakeet"}

        # Run the async test
        asyncio.run(test_concurrent())

    def test_server_responds_to_different_methods(self, server_process):
        """Test that server handles different HTTP methods appropriately."""
        # GET should work
        response = httpx.get("http://127.0.0.1:8001/hello")
        assert response.status_code == 200
        
        # POST should return method not allowed
        response = httpx.post("http://127.0.0.1:8001/hello")
        assert response.status_code == 405

    def test_openapi_docs_integration(self, server_process):
        """Test that OpenAPI documentation is accessible."""
        response = httpx.get("http://127.0.0.1:8001/docs")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        
        response = httpx.get("http://127.0.0.1:8001/openapi.json")
        assert response.status_code == 200
        openapi_schema = response.json()
        assert openapi_schema["info"]["title"] == "Parakeet API"