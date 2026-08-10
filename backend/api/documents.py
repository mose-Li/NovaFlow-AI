from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

service = DocumentService()


# 上传文件
@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    try:

        content = await file.read()

        return service.upload_document(
            original_filename=file.filename,
            mime_type=file.content_type,
            file_bytes=content,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# 获取全部文档
@router.get("/")
async def list_documents():

    return service.list_documents()


# 删除文档
@router.delete("/{document_id}")
async def delete_document(document_id: int):

    try:

        return service.delete_document(document_id)

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )