import os

import pytest
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
TIMEOUT = 120
MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"


def call_api(method: str, path: str, **kwargs) -> requests.Response:
    url = f"{BASE_URL}{path}"
    try:
        return requests.request(method, url, timeout=TIMEOUT, **kwargs)
    except requests.RequestException as exc:
        pytest.fail(
            f"Không thẻ kết nối API tại {url}. "
            f"Hãy chạy uvicorn trước khi test. Chi tiết: {exc}"
        )


def test_root() -> None:
    response = call_api("GET", "/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "AI Chatbot API"
    assert data["model"] == MODEL_NAME
    assert "/generate" in data["endpoints"]


def test_health() -> None:
    response = call_api("GET", "/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["model"] == MODEL_NAME


def test_generate_empty_message() -> None:
    response = call_api("POST", "/generate", json={"message": ""})
    assert response.status_code == 400
    assert "Không được để trống" in response.json()["detail"]


def test_generate_valid_message() -> None:
    prompt = "Hãy giới thiệu về bản thân bạn."
    response = call_api("POST", "/generate", json={"message": prompt})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["model"] == MODEL_NAME
    assert data["input"] == prompt
    assert isinstance(data["output"], str)
    assert data["output"].strip() != ""
