from __future__ import annotations

from dataclasses import dataclass

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


@dataclass(frozen=True)
class GenerationConfig:
    max_new_tokens: int = 256
    temperature: float = 0.7
    top_p: float = 0.9


class ChatbotService:
    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-0.5B-Instruct",
        config: GenerationConfig | None = None,
    ) -> None:
        self.model_name = model_name
        self.config = config or GenerationConfig()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self._tokenizer = None
        self._model = None
        self.system_prompt = "Bạn là trợ lí AI hỏi đáp thân thiện, hãy trả lời rõ ràng, ngắn gọn và dễ hiểu!."

    def _load_model(self) -> None:
        if self._tokenizer is not None and self._model is not None:
            return

        self._tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self._model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
        )
        self._model.to(self.device)
        self._model.eval()

    def is_ready(self) -> bool: #endpont health check
        return self._tokenizer is not None and self._model is not None

    def get_model_name(self) -> str:
        return self.model_name

    def generate(self, message: str) -> str:
        cleaned_message = message.strip()
        if not cleaned_message:
            raise ValueError("'Message' Không được để trống hoặc chỉ chứa khoảng trắng.")

        self._load_model()

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": cleaned_message},
        ]

        prompt = self._tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        inputs = self._tokenizer(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self._model.generate(
                **inputs,
                max_new_tokens=self.config.max_new_tokens,
                temperature=self.config.temperature,
                top_p=self.config.top_p,
                do_sample=True,
                pad_token_id=self._tokenizer.eos_token_id,
                eos_token_id=self._tokenizer.eos_token_id,
            )

        generated_tokens = outputs[0][inputs["input_ids"].shape[-1] :]
        result = self._tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

        if not result:
            raise RuntimeError("Model không tạo được nội dung trả lời.")

        return result


chatbot_service = ChatbotService()
