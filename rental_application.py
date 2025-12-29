"""rental_application.py

Minimal local API server (FastAPI) to test from:
- Same computer (localhost)
- Same Wi‑Fi / LAN (your machine's LAN IP)

Run examples (macOS):
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt

  # Local-only (safer):
  uvicorn rental_application:app --host 127.0.0.1 --port 8000 --reload

  # LAN access (same Wi‑Fi):
  uvicorn rental_application:app --host 0.0.0.0 --port 8000 --reload

Test:
  curl http://127.0.0.1:8000/nuestro_API/test_endpoint
"""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Rental Application API", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/nuestro_API/test_endpoint")
def test_endpoint() -> dict:
    variable = "Just a message string"
    # Return JSON-serializable payload
    return {"success_message": variable}


class EchoIn(BaseModel):
    text: str


@app.post("/nuestro_API/echo")
def echo(payload: EchoIn) -> dict:
    return {"you_sent": payload.text}


@app.get("/nuestro_API/add")
def add(a: float, b: float) -> dict:
    return {"a": a, "b": b, "sum": a + b}
