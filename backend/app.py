from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from dotenv import load_dotenv
from backend.database import db
import os
from backend.Resources.user_routes import UserRegistration, UserLogin
from backend.Resources.business_routes import BusinessRegistration

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize CORS, Database, and Migrate
# Add the frontend URL explicitly here to avoid issues
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)  # Adds migration support

bcrypt = Bcrypt(app)
api = Api(app)

# Register API endpoints
api.add_resource(UserRegistration, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(BusinessRegistration, "/register-business")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
