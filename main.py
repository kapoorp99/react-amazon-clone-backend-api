from fastapi import FastAPI
import stripe

app = FastAPI()

stripe.api_key = "sk_test_51ICjFIGOe2LN572AJ6Ivmu47c1tbLETmMCvi7tDXyZ5201vje9kqFcRSjyblWrjUEK792qJkNe84zeldGqgAwApH00ebOStQB6"


@app.get('/')
def home():
    return {"message": "Hello, this is Prakhar Kapoor here"}
