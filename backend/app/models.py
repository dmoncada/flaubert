from dataclasses import dataclass
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


@dataclass
class Entry:
    key: str
    term: str
    definitions: list[str]


class Term_Definition(SQLModel, table=True):
    term_id: int = Field(foreign_key="term.id", primary_key=True)
    definition_id: int = Field(foreign_key="definition.id", primary_key=True)


class Definition(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    definition: str


class TermBase(SQLModel):
    key: str
    term: str


class Term(TermBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    definitions: list[Definition] = Relationship(link_model=Term_Definition)
