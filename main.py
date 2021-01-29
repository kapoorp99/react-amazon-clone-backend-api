from fastapi import FastAPI
import stripe
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

origins = [
    "https://amazon-react-clone-backend.herokuapp.com",
]

stripe.api_key = "sk_test_51ICjFIGOe2LN572AJ6Ivmu47c1tbLETmMCvi7tDXyZ5201vje9kqFcRSjyblWrjUEK792qJkNe84zeldGqgAwApH00ebOStQB6"


@app.get("/")
def home():
    return {"message": "Hello this is Prakhar here"}


@app.post("/payments/create/")
async def process_payment(total: str):
    totalf = int(total)
    payment_intent = stripe.PaymentIntent.create(
        amount=totalf,
        currency="usd",
        payment_method_types=["card"],
        description="Software development services",
        shipping=dict(
            name="Prakhar Kapoor",
            address=dict(
                line1="510 Townsend St",
                postal_code="98140",
                city="San Francisco",
                state="CA",
                country="US",
            ),
        ))
    json_compatible_item_data = jsonable_encoder(payment_intent.client_secret)
    return JSONResponse(content=json_compatible_item_data)
