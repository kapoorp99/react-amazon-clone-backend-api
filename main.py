from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello, this is Prakhar Kapoor here"}
