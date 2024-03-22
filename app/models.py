import uuid


class Entity:

    def __init__(self, doc_id: str, start: int, end: int, label: str):
        self.doc_id = doc_id
        self.start = start
        self.end = end
        self.label = label


class Sentence:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Token:
    def __init__(self, id: int, start: int, end: int, tag: str, pos: str, morph: str, lemma: str, dep: str, head: int):
        self.id = id
        self.start = start
        self.end = end
        self.tag = tag
        self.pos = pos
        self.morph = morph
        self.lemma = lemma
        self.dep = dep
        self.head = head


class Document:
    def __init__(self, id: str, genre: str, author: str, text: str, ents: list[Entity], sents: list[Sentence], tokens: list[Token]):
        self.id = id
        self.genre = genre
        self.author = author
        self.text = text
        self.ents = ents
        self.sents = sents
        self.tokens = tokens

    @staticmethod
    def create(genre: str, author: str, text: str, ents: list[dict], sents: list[dict], tokens: list[dict]):
        entities = [Entity(ent["doc_id"], ent["start"], ent["end"], ent["label"]) for ent in ents]

        sentences = [Sentence(sent["start"], sent["end"]) for sent in sents]

        tokens_ = [Token(token["id"], token["start"], token["end"], token["tag"], token["pos"], token["morph"], token["lemma"], token["dep"], token["head"]) for token in tokens]

        return Document(str(uuid.uuid4()), genre, author, text, entities, sentences, tokens_)
