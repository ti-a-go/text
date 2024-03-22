from pydantic import BaseModel


class CreateDocumentRequestBody(BaseModel):
    text: str
    author: str
    genre: str


class CreateDocumentResponseBodyEntity:
    doc_id: str
    start: int
    end: int
    label: str


class CreateDocumentResponseBodySentence:
    doc_id: str
    start: int
    end: int


class CreateDocumentResponseBodyToken:
    doc_id: str
    token_id: int
    start: int
    end: int
    tag: str
    pos: str
    morph: str
    lemma: str
    dep: str
    head: int


class CreateDocumentResponseBody(BaseModel):
    doc_id: str
    genre: str
    author: str
    text: str
    ents: list[CreateDocumentResponseBodyEntity]
    sents: list[CreateDocumentResponseBodySentence]
    tokens: list[CreateDocumentResponseBodyToken]
