from fastapi import FastAPI

from controllers import DocumentController
from schemas import CreateDocumentBody


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/doc")
def create_document(body: CreateDocumentBody):
    return DocumentController.create_document(body)


@app.get("/doc/{doc_id}")
def get_document(doc_id):
    return DocumentController.get_document(doc_id)


@app.get("/docs")
def list_documents():
    return DocumentController.list_documents()


@app.get("/doc/search")
def search_document():
    return DocumentController.search_document()