import json
from typing import cast

from sqlmodel import SQLModel, Session, select

from app.db import engine
from app.models import Term, Definition as Def, Term_Definition


def create_db():
    SQLModel.metadata.create_all(engine)


def get_term_id(session: Session, key: str) -> int:
    query = select(Term).where(Term.key == key)
    term = session.exec(query).one()
    return cast(int, term.id)


def get_definition_id(session: Session, def_: str) -> int:
    query = select(Def).where(Def.definition == def_)
    definition = session.exec(query).one()
    return cast(int, definition.id)


def insert_data():
    with open("dico.json", mode="r", encoding="utf-8") as json_file:
        dico = json.load(json_file)

    all_terms = set()
    all_defs = set()

    for entry in dico:
        all_terms.add((entry["key"], entry["term"]))
        all_defs.update([def_ for def_ in entry["definitions"]])

    with Session(engine) as session:
        all_terms = [Term(key=key, term=term) for key, term in all_terms]
        all_defs = [Def(definition=def_) for def_ in all_defs]

        session.add_all(all_terms)
        session.add_all(all_defs)

        for entry in dico:
            term_id = get_term_id(session, entry["key"])

            for def_ in entry["definitions"]:
                def_id = get_definition_id(session, def_)
                session.add(Term_Definition(term_id=term_id, definition_id=def_id))

        session.commit()


def main():
    create_db()
    insert_data()


if __name__ == "__main__":
    main()
