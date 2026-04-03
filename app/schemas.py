from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    message: str = Field(..., description="Nội dung người gửi cho chatbot", example="Xin chào, Hãy tự giới thiệu về bản thân bạn.")


class GenerateResponse(BaseModel):
    model: str
    input: str
    output: str
