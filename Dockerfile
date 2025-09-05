# Use amazonlinux:2023 as base image
FROM amazonlinux:2023

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Note: In production environment, you would install pip via package manager:
# RUN dnf update -y && dnf install -y python3-pip && dnf clean all

# For environments with network restrictions, use ensurepip:
RUN python3 -m ensurepip --upgrade

# Install uv for dependency management
RUN python3 -m pip install uv

# Set work directory
WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY src/ ./src/

# Install dependencies and create virtual environment
RUN uv sync --frozen

# Create a non-root user for security
RUN adduser --system --no-create-home appuser

# Change ownership of the app directory
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port 8000
EXPOSE 8000

# Health check using python to avoid external dependencies
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD uv run python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=10)" || exit 1

# Run the application using uv
CMD ["uv", "run", "python", "-m", "uvicorn", "src.parakeet.main:app", "--host", "0.0.0.0", "--port", "8000"]