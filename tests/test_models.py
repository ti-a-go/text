import pytest

from src.app import models
from fixtures import spacy_doc_in_json_format

Document = models.Document


class TestDocument:

    @pytest.fixture()
    def get_doc_as_dict(self):
        return spacy_doc_in_json_format

    def test_create_document(self):
        # Given
        genre = "genre"
        author = "author"
        text = "text"
        ents = [{"start": 0, "end": 1}]
        sents = [{"start": 0, "end": 1}]
        tokens = [{"start": 0, "end": 1}]

        # When
        document = Document.create(genre, author, text, ents, sents, tokens)

        # Then
        assert document.text == text
