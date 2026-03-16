# Get used to these imports (you gonna be using it for 10 weeks)
from fastapi import FastAPI
from app.models import NoteCreate
from app.models import Note
from app.fake_db import notes
from fastapi import Query
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastNotes app is running"}

@app.post("/notes")
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
        "archived": note.archived
    }
    
    notes.append(new_note)
    return new_note

@app.get("/notes", response_model=list[Note])
def get_notes(
    limit: int = Query(default= 10, le = 10), 
    offset: int = Query(default=0, ge=0),
    archived: Optional[bool] = None ): # limit to retrieving first 10 notes

    filtered_notes = notes
    if archived is not None:
        filtered_notes = [note for note in notes if note['archived'] == archived]
    
    return filtered_notes[offset: offset + limit]

@app.get("/notes/{id}")
def get_note(id: int):
    for note in notes:
        if note['id'] == id:
            return note
    
    return {"message": "note not found"}

@app.delete("/notes/{id}")
def delete_note(id: int):
    for index, note in enumerate(notes):
        if note['id'] == id:
            return notes.pop(index)
    
    return {'message': 'note not found'}

# using PUT right now but will be implement PATCH method later
@app.put('/notes/{id}')
def update_note(id: int, updated_note: NoteCreate):
    for index, note in enumerate(notes):
        if note['id'] == id:
            notes[index]["title"] = updated_note.title
            notes[index]["content"] = updated_note.content

            return notes[index]
    
    return {"message": "note not found"}