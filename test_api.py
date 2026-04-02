import os

import pytest
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
TIMEOUT = 30


def call_api(method: str, path: str, **kwargs) -> requests.Response:
    url = f"{BASE_URL}{path}"
    try:
        return requests.request(method, url, timeout=TIMEOUT, **kwargs)
    except requests.RequestException as exc:
        pytest.fail(
            f"Khong the ket noi toi API tai {url}. "
            f"Hay chay uvicorn truoc khi test. Chi tiet: {exc}"
        )


def test_root() -> None:
    response = call_api("GET", "/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "AI Chatbot API"
    assert data["model"] == "qwen-chat"
    assert "/generate" in data["endpoints"]


def test_health() -> None:
    response = call_api("GET", "/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["model"] == "qwen-chat"


def test_generate_empty_message() -> None:
    response = call_api("POST", "/generate", json={"message": ""})
    assert response.status_code == 400
    assert "khong duoc de rong" in response.json()["detail"]


def test_generate_whitespace_message() -> None:
    response = call_api("POST", "/generate", json={"message": "   "})
    assert response.status_code == 400
    assert "khong duoc de rong" in response.json()["detail"]


def test_generate_valid_message() -> None:
    prompt = "Hay gioi thieu ngan gon ve FastAPI."
    response = call_api("POST", "/generate", json={"message": prompt})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["model"] == "qwen-chat"
    assert data["input"] == prompt
    assert isinstance(data["output"], str)
    assert data["output"].strip() != ""
