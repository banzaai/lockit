import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from backend.database import db
from Resources.user_routes import UserRegistration, UserLogin
from Resources.business_routes import BusinessRegistration

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize CORS and the database
CORS(app)
db.init_app(app)  # Initialize SQLAlchemy with the app

bcrypt = Bcrypt(app)
api = Api(app)

# Add API routes
api.add_resource(UserRegistration, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(BusinessRegistration, "/register-business")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all database tables
    app.run(debug=True)
