"""
FastAPI application for the Parakeet service.
"""
from fastapi import FastAPI

app = FastAPI(
    title="Parakeet API",
    description="A simple FastAPI application that responds 'I'm a Parakeet'",
    version="0.1.0"
)


@app.get("/hello")
async def hello():
    """Return a greeting from the parakeet."""
    return {"message": "I'm a Parakeet"}


@app.get("/health")
async def health_check():
    """Health check endpoint for Kubernetes."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)