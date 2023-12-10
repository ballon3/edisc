from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Flashcard(BaseModel):
    word: str
    meaning: str

# In-memory data store (replace with database in production)
flashcards = [
    {"word": "你好", "meaning": "Hello"},
    {"word": "谢谢", "meaning": "Thank you"},
    # Add more flashcards here
]

@router.get("/flashcards/", response_model=List[Flashcard])
def get_flashcards():
    return flashcards

@router.post("/practice/")
def practice(translation: str):
    correct_translation = "你好"
    return {"correct": translation == correct_translation}

@router.get("/progress/")
def progress(correct_answers: int):
    # You might want to store and retrieve this from a database
    return {"correct_answers": correct_answers}
