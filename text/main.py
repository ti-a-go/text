from fastapi import FastAPI

from router import router
from schemas import CreateDocumentRequestBody, CreateDocumentResponseBody
from controllers import DocumentController


app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "Hello"}


@app.post("/doc")
def create_document(body: CreateDocumentRequestBody):
    if body.genre == "quote":
        return "quote"
    return DocumentController.create_document(body)
