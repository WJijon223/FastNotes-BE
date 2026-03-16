from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str
    archived: bool = False

class Note(NoteCreate):
    id: int