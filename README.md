# AI Chatbot API

## 1. Thong tin sinh vien

- Ho va ten: `[DIEN HO TEN]`
- MSSV: `[DIEN MSSV]`
- Lop: `[DIEN LOP]`

## 2. Ten mo hinh va lien ket

- Model: `Qwen2.5-3B-Instruct-GGUF`
- Link: `https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/tree/main`
- Ten model trong project: `qwen-chat`

## 3. Mo ta ngan

Project xay dung API chatbot bang FastAPI. API nhan cau hoi, gui sang Ollama de chay model local dang GGUF, sau do tra ket qua ve dang JSON. Co the public localhost bang Pinggy de demo.

## 4. Huong dan cai dat thu vien

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 5. Huong dan chuan bi model

1. Mo link model tren Hugging Face:

```text
https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/tree/main
```

1. Tai file mac dinh:

```text
qwen2.5-3b-instruct-q4_k_m.gguf
```

Co the dung `qwen2.5-3b-instruct-q5_k_m.gguf` neu muon.

1. Dat file vao thu muc goc cua project.
1. Doi ten file thanh:

```text
qwen2.5-3b-instruct.gguf
```

1. Tao model bang Ollama:

```bash
ollama create qwen-chat -f Modelfile
```

Khong dua file `.gguf` vao repo.

## 6. Huong dan chay chuong trinh

1. Chay API:

```bash
uvicorn app.main:app --reload
```

1. Chay test:

```bash
pytest test_api.py -v
```

1. Neu can public localhost bang Pinggy:

```bash
ssh -p 443 -R0:127.0.0.1:8000 free.pinggy.io
```

## 7. Huong dan goi API va vi du request/response

### GET /

```bash
curl http://127.0.0.1:8000/
```

### GET /health

```bash
curl http://127.0.0.1:8000/health
```

### POST /generate

Request:

```json
{
  "message": "Hay gioi thieu ngan gon ve FastAPI."
}
```

Response:

```json
{
  "model": "qwen-chat",
  "input": "Hay gioi thieu ngan gon ve FastAPI.",
  "output": "FastAPI la framework Python hien dai giup xay dung API nhanh va de viet."
}
```

Neu `message` rong, API tra loi `400`.
Neu Ollama loi, API tra loi `500`.

## 8. Lien ket video demo

- Video demo: `[DIEN LINK VIDEO DEMO]`
