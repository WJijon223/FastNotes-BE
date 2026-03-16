# Get used to this line (you gonna be using it for 10 weeks)
from fastapi import FastAPI
from app.models import NoteCreate
from app.models import Note
from app.fake_db import notes

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastNotes app is running"}

@app.post("/notes")
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content
    }
    
    notes.append(new_note)
    return new_note

@app.get("/notes", response_model=list[Note])
def get_notes():
    return notes

@app.get("/notes/{id}")
def get_note(id: int):
    for note in notes:
        if note['id'] == id:
            return note
    
    return {"message": "note not found"}