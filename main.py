from flask import Flask, request
from flask_cors import cross_origin

import stripe

stripe.api_key = "sk_test_51IPPOjEooHcYP2S6glE8nJafR8DyZUb59RwkRDoIr1I5pFQgOQqd2XaoRC4woWRZ04BhMadDGMhAPNJE1jTnxUqE00ogkh1oYx"

app = Flask(__name__)


@app.route('/payments/create', methods=['POST'])
@cross_origin()
def process_payment():
    total_amount = request.args['total']
    if total_amount == '0':
        error_message = "Payment amount should not be zero"
        return error_message
    else:
        payment_intent = stripe.PaymentIntent.create(
            amount=total_amount,
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
        print(payment_intent.client_secret)
        return payment_intent.client_secret


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=False)
