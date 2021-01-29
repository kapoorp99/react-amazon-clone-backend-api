from fastapi import FastAPI
import stripe
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}
