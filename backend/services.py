# services.py
import stripe
from flask import jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Stripe API Key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Stripe Payment Processing
def process_payment(amount: float):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert to cents
            currency="usd",
            payment_method_types=["card"],
        )
        return jsonify({"client_secret": payment_intent.client_secret}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
