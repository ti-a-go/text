from fastapi import APIRouter

from controllers import DocumentController
from schemas import CreateDocumentRequestBody, CreateDocumentResponseBody

router = APIRouter()


@router.post("/doc")
def create_document(body: CreateDocumentRequestBody) -> CreateDocumentResponseBody:
    return DocumentController.create_document(body)


@router.get("/doc/{doc_id}")
def get_document(doc_id):
    return DocumentController.get_document(doc_id)


@router.get("/docs")
def list_documents():
    return DocumentController.list_documents()


@router.get("/doc/search")
def search_document():
    return DocumentController.search_document()
