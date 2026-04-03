from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    message: str = Field(..., description="Noi dung nguoi dung gui cho chatbot.")


class GenerateResponse(BaseModel):
    model: str
    input: str
    output: str
