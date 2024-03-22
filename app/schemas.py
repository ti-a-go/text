from pydantic import BaseModel


class CreateDocumentBody(BaseModel):
    text: str
    author: str
    genre: str
