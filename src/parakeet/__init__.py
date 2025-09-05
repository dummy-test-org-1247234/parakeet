"""
Parakeet FastAPI Application
"""
from .main import app

def main() -> None:
    """Entry point for the application."""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
