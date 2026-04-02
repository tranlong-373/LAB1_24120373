from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_MODEL_FILE = "qwen2.5-3b-instruct.gguf"
ALLOWED_SOURCE_FILES = [
    "qwen2.5-3b-instruct-q4_k_m.gguf",
    "qwen2.5-3b-instruct-q5_k_m.gguf",
]
DEFAULT_SOURCE_FILE = "qwen2.5-3b-instruct-q4_k_m.gguf"
HUGGING_FACE_URL = "https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF"
HUGGING_FACE_FILES_URL = "https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/tree/main"


def main() -> None:
    expected_path = PROJECT_ROOT / EXPECTED_MODEL_FILE

    print("Huong dan chuan bi model")
    print(f"1. Mo link: {HUGGING_FACE_URL}")
    print(f"2. Hoac vao tab files: {HUGGING_FACE_FILES_URL}")
    print("3. Tai mot trong hai file sau:")
    for file_name in ALLOWED_SOURCE_FILES:
        print(f"   - {file_name}")
    print(f"   Mac dinh nen dung: {DEFAULT_SOURCE_FILE}")
    print(f"4. Dat file vao thu muc project va doi ten thanh: {EXPECTED_MODEL_FILE}")
    print("5. Chay: ollama create qwen-chat -f Modelfile")

    if expected_path.exists():
        print(f"\nDa tim thay model: {expected_path}")
        return

    print("\nChua tim thay file model voi ten chuan.")
    for file_name in ALLOWED_SOURCE_FILES:
        candidate = PROJECT_ROOT / file_name
        if candidate.exists():
            print(
                f"Da tim thay {candidate.name}. Hay doi ten thanh "
                f"{EXPECTED_MODEL_FILE} truoc khi chay Ollama."
            )
            return

    print("Repo hien khong chua file .gguf nao.")


if __name__ == "__main__":
    main()
