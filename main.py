from fastapi import FastAPI
import stripe
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

stripe.api_key = "sk_test_51ICjFIGOe2LN572AJ6Ivmu47c1tbLETmMCvi7tDXyZ5201vje9kqFcRSjyblWrjUEK792qJkNe84zeldGqgAwApH00ebOStQB6"
origins = [
    "http://0.0.0.0:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Hello, this is Prakhar Kapoor here"}


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
    x = JSONResponse(content=json_compatible_item_data)
    return x
