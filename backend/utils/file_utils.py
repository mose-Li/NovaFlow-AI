import hashlib
import uuid
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

# 企业版支持的文件类型
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".md",
    ".csv",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".json",
    ".xml",
}


def generate_filename(original_filename: str) -> str:
    """
    生成UUID文件名
    """
    suffix = Path(original_filename).suffix.lower()
    return f"{uuid.uuid4()}{suffix}"


def calculate_sha256(file_bytes: bytes) -> str:
    """
    计算SHA256
    """
    return hashlib.sha256(file_bytes).hexdigest()


def validate_extension(filename: str) -> str:
    """
    验证文件类型
    """
    suffix = Path(filename).suffix.lower()

    if suffix not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {suffix}"
        )

    return suffix