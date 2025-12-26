from fastapi import FastAPI

app = FastAPI()

@app.post('/ask')
def ask(q: dict):
    return {'answer': 'This is a mock AI response', 'confidence': 'medium'}
