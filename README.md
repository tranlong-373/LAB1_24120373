# AI Chatbot API

## 1. Thông tin sinh viên

- Họ và tên: `Trần Thiện Long`
- MSSV: `24120373`
- Lớp: `24CTT4`

## 2. Tên mô hình và liên kết mô hình trên Hugging Face

- Model sử dụng: `Qwen/Qwen2.5-0.5B-Instruct`
- Link model: `https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct`

## 3. Mô tả tương quan về chức năng của hệ thống

Project này xây dựng một hệ thống chatbot API bằng FastAPI. API có nhiệm vụ tiếp nhận nội dung từ người dùng, gọi mô hình ngôn ngữ được cung cấp trên Hugging Face thông qua thư viện Transformers, và trả về kết quả dưới định dạng JSON.

Mô hình là một chatbot hỏi đáp thông minh, Người dùng có thể ra câu hỏi và chatbot sẽ đưa ra câu trả lời.

## 4. Hướng dẫn cài đặt

Tạo môi trường ảo, kích hoạt môi trường và cài đặt các thư viện cần thiết:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 5. Hướng dẫn chạy chương trình

Chạy API:

```bash
uvicorn app.main:app --reload
```

sau khi chạy có thẻ mở các địa chỉ để kiểm tra:

- API: <http://127.0.0.1:8000>
- docs: <http://127.0.0.1:8000/docs>

Chạy test API:

```bash
pytest test_api.py -v
```

## 6. Hướng dẫn gọi API và ví dụ request/response

### GET /

```bash
curl http://127.0.0.1:8000/
```

### GET /health

```bash
curl http://127.0.0.1:8000/health
```

### POST /generate

## Có 2 cách test

- Cách 1: Dùng curl

```bash
curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d "{\"message\":\"Hãy giới thiệu ngắn gọn về FastAPI.\"}"
```

- Cách 2: Lên docs để thao tác

Request:

```json
{
  "message": "Hãy giới thiệu về bản thân bạn."
}
```

Response:

```json
{
  "model": "Qwen/Qwen2.5-0.5B-Instruct",
  "input": "Hãy giới thiệu về bản thân bạn.",
  "output": "Xin chào! Tôi là một trợ lý AI được tạo ra để giúp đỡ người dùng trong nhiều lĩnh vực khác nhau như tư vấn, hỗ trợ giải trí và nhiều hơn nữa. Tôi rất vui được lắng nghe và chia sẻ thông tin với mọi người."
}
```

Nếu `message` rỗng, API trả lời `400`.
Nếu model lỗi, API trả lời `500`.

## 7. Hướng dẫn dùng Pinggy để demo public

Sau khi API đang chạy ở `localhost:8000`, mở một terminal khác và chạy lệnh sau:

```bash
ssh -p 443 -R0:127.0.0.1:8000 free.pinggy.io
```

Pinggy sẽ cung cấp một đường dẫn public để truy cập từ Internet

- Ví dụ: `https://xxxxx.pinggy.link/docs`

## 8. Video demo

[![Xem video](https://techvccloud.mediacdn.vn/280518386289090560/2021/7/5/api-la-gi-1-640x322-16254795881731210500168-0-30-322-603-crop-16254795955021767193036.jpg)](https://youtu.be/aWLfDh3C-js?si=zlSrjjm-IKelPijr)
