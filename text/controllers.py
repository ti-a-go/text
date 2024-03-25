from schemas import CreateDocumentRequestBody
from service import create_document


class DocumentController:

    @staticmethod
    def create_document(body: CreateDocumentRequestBody):
        return create_document(body.text)

    @staticmethod
    def get_document(doc_id):
        return {
            "id": doc_id,
            "text": "Minhi vidis é um livris abertis.",
            "author": "Mussum",
            "genre": "quote",
        }

    @staticmethod
    def list_documents():
        return [
            {
                "id": "84323e2e-0f14-45d4-b83b-9685c12c9629",
                "text": "Minhi vidis é um livris abertis.",
                "author": "Mussum",
                "genre": "quote",
            }
        ]

    @staticmethod
    def search_document():
        return [
            {
                "id": "84323e2e-0f14-45d4-b83b-9685c12c9629",
                "text": "Minhi vidis é um livris abertis.",
                "author": "Mussum",
                "genre": "quote",
            }
        ]
