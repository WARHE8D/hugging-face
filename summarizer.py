# summarizer.py
from transformers import pipeline
from fastapi import FastAPI, Request
from pydantic import BaseModel

summarizer = pipeline("summarization")

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: TextInput):
    summary = summarizer(input.text, max_length=130, min_length=30, do_sample=False)
    return {"summary": summary[0]['summary_text']}

# to start server: python -m uvicorn summarizer:app --host 0.0.0.0 --port 8000