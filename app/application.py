import spacy

from schemas import CreateDocumentBody


nlp = spacy.load("pt_core_news_lg")


def create_document(body: CreateDocumentBody):
    pass
