from fastapi import FastAPI, HTTPException

from app.schemas import GenerateRequest, GenerateResponse
from app.services.chatbot_service import chatbot_service

app = FastAPI(title="AI Chatbot API", version="1.0.0")


@app.get("/")
def root():
    return {
        "name": "AI Chatbot API",
        "model": chatbot_service.get_model_name(),
        "message": "API đang hoạc động.",
        "endpoints": ["/", "/health", "/generate"],
    }


@app.get("/health")
def health():
    return {
        "status": "ok - API đang hoạt động.",
        "model": chatbot_service.get_model_name(),
        "loaded": chatbot_service.is_ready(),
    }


@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="'Message' Không được để trống hoặc chỉ chứa khoảng trắng.")

    try:
        output_text = chatbot_service.generate(request.message)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Lỗi khi sinh câu trả lời từ Model: {exc}",
        ) from exc

    return GenerateResponse(
        model=chatbot_service.get_model_name(),
        input=request.message.strip(),
        output=output_text,
    )
