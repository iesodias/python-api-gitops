from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import platform

app = FastAPI(
    title="Python API",
    description="Simple API for Platform Engineering labs",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Hello from CI/CD Pipeline!",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "dev")
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "hostname": platform.node(),
        "python_version": platform.python_version()
    }

@app.get("/info")
async def info():
    return {
        "app": "python-api-gitops",
        "version": "1.0.0",
        "python": platform.python_version(),
        "platform": platform.system(),
        "hostname": platform.node()
    }
