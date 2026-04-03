# AI Chatbot API

## 1. Thong tin sinh vien

- Ho va ten: `[DIEN HO TEN]`
- MSSV: `[DIEN MSSV]`
- Lop: `[DIEN LOP]`

## 2. Ten mo hinh va lien ket toi mo hinh tren Hugging Face

- Model su dung: `Qwen/Qwen2.5-0.5B-Instruct`
- Link model: `https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct`

## 3. Mo ta ngan ve chuc nang cua he thong

Project xay dung chatbot API bang FastAPI. API nhan tin nhan tu nguoi dung, goi model tu Hugging Face bang Transformers va tra ket qua ve JSON.

## 4. Huong dan cai dat thu vien

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 5. Huong dan chay chuong trinh

```bash
uvicorn app.main:app --reload
```

Chay test API:

```bash
pytest test_api.py -v
```

## 6. Huong dan goi API va vi du request/response

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
  "model": "Qwen/Qwen2.5-0.5B-Instruct",
  "input": "Hay gioi thieu ngan gon ve FastAPI.",
  "output": "FastAPI la framework Python hien dai giup xay dung API nhanh va de phat trien."
}
```

Neu `message` rong, API tra loi `400`.
Neu model loi, API tra loi `500`.

## 7. Huong dan dung Pinggy de demo public

```bash
ssh -p 443 -R0:127.0.0.1:8000 free.pinggy.io
```

## 8. Lien ket video demo

- Video demo: `[DIEN LINK VIDEO DEMO]`
