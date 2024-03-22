import spacy

nlp = spacy.load("pt_core_news_lg")


def create_document(text: str):
    doc = nlp(text)
    return doc.to_json()
