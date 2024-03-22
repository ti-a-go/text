from app import models

Document = models.Document


class TestDocument:

    def test_create_document(self):
        genre = "genre"
        author = "author"
        text = "text"
        ents = [{"start": 0, "end": 1}]
        sents = [{"start": 0, "end": 1}]
        tokens =[{"start": 0, "end": 1}]

        document = Document.create(genre, author, text, ents, sents, tokens)

        assert document.text == text
