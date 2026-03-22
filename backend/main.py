from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS (so your frontend doesn't get blocked)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Quotes data
quotes = [
    {"text": "Code never lies.", "author": "Unknown"},
    {"text": "First solve the problem.", "author": "John Johnson"},
    {"text": "Programs must be written for people.", "author": "Harold Abelson"},
    {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"}
]

# API endpoint
@app.get("/quote")
def get_quote():
    return random.choice(quotes)