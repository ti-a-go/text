import uuid
from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


# Mapped[int] = mapped_column(primary_key=True)


class Entity:

    def __init__(self, doc_id: str, start: int, end: int, label: str):
        self.doc_id = doc_id
        self.start = start
        self.end = end
        self.label = label


class Sentence:

    def __init__(self, doc_id: str, start: int, end: int):
        self.doc_id = doc_id
        self.start = start
        self.end = end


class Token:
    def __init__(
        self,
        doc_id: str,
        token_id: int,
        start: int,
        end: int,
        tag: str,
        pos: str,
        morph: str,
        lemma: str,
        dep: str,
        head: int,
    ):
        self.doc_id = doc_id
        self.id = token_id
        self.start = start
        self.end = end
        self.tag = tag
        self.pos = pos
        self.morph = morph
        self.lemma = lemma
        self.dep = dep
        self.head = head


class Document(Base):
    __tablename__ = "document"

    doc_id: Mapped[str] = mapped_column(String(38))
    genre: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))
    text: Mapped[str] = mapped_column(String())

    # entities: Mapped[List["Entity"]] = relationship(back_populates="entity", cascade="all, delete-orphan")
    # sentences: Mapped[List["Sentence"]] = relationship(back_populates="entity", cascade="all, delete-orphan")
    # tokens: Mapped[List["Token"]] = relationship(back_populates="entity", cascade="all, delete-orphan")
