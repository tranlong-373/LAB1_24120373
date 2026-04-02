import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="AI Chatbot API",
    description="FastAPI API that sends prompts to a local Qwen model through Ollama.",
    version="1.0.0",
)

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen-chat"


class GenerateRequest(BaseModel):
    message: str = Field(..., description="User message sent to the chatbot.")


class GenerateResponse(BaseModel):
    model: str
    input: str
    output: str


def _extract_ollama_error(response: requests.Response) -> str:
    try:
        error_data = response.json()
    except ValueError:
        text = response.text.strip()
        return text or "Khong doc duoc noi dung loi tu Ollama."

    if isinstance(error_data, dict):
        return str(error_data.get("error") or error_data.get("message") or error_data)

    return "Phan hoi loi tu Ollama khong dung dinh dang mong doi."


@app.get("/")
def root():
    return {
        "name": "AI Chatbot API",
        "model": MODEL_NAME,
        "message": "API dang hoat dong.",
        "endpoints": ["/", "/health", "/generate"],
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": MODEL_NAME,
        "ollama_url": OLLAMA_URL,
    }


@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    cleaned_message = request.message.strip()
    if not cleaned_message:
        raise HTTPException(status_code=400, detail="Truong 'message' khong duoc de rong.")

    payload = {
        "model": MODEL_NAME,
        "prompt": cleaned_message,
        # stream=False de Ollama tra ve mot JSON hoan chinh thay vi tung manh du lieu.
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Khong the ket noi toi Ollama: {exc}",
        ) from exc

    if response.status_code != 200:
        error_message = _extract_ollama_error(response)
        raise HTTPException(
            status_code=500,
            detail=f"Ollama tra ve loi {response.status_code}: {error_message}",
        )

    try:
        data = response.json()
    except ValueError as exc:
        raise HTTPException(
            status_code=500,
            detail="Ollama tra ve du lieu khong phai JSON hop le.",
        ) from exc

    output_text = str(data.get("response", "")).strip()
    if not output_text:
        raise HTTPException(
            status_code=500,
            detail="Ollama khong tra ve truong 'response' hop le.",
        )

    return GenerateResponse(
        model=MODEL_NAME,
        input=cleaned_message,
        output=output_text,
    )
