from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select

from app.db import get_session
from app.models import TermBase, Term, Entry

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "Dictionnaire des idées reçues."


@app.get("/entries", response_model=list[TermBase])
def get_entries(session: Session = Depends(get_session)):
    query = select(Term).order_by(Term.key)
    terms = session.exec(query)
    terms = [TermBase(key=term.key, term=term.term) for term in terms]
    return terms


@app.get("/entries/{key}", response_model=Entry)
def get_entry(key: str, session: Session = Depends(get_session)):
    query = select(Term).where(Term.key == key)
    term = session.exec(query).one()
    defs = [d.definition for d in term.definitions]
    entry = Entry(key=term.key, term=term.term, definitions=defs)
    return entry
