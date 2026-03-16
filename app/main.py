# Get used to this line (you gonna be using it for 10 weeks)
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastNotes app is running"}