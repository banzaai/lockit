from flask import jsonify

from backend.database import db
from backend.models.user import User
from backend.models.business import Business
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class UserService:
    @staticmethod
    def register_user(data):
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        phone = data.get("phone")
        is_business = data.get("is_business", False)
        business_name = data.get("business_name", None)

        if User.query.filter_by(email=email).first():
            return jsonify({"message": "User already exists"}), 400

        if not password:
            return jsonify({"message": "Password is required"}), 400

        if not name:
            return jsonify({"message": "Name is required"}), 400

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        try:
            new_user = User(name=name, email=email, password_hash=hashed_password, phone=phone)
            db.session.add(new_user)
            db.session.commit()

            if is_business and business_name:
                new_business = Business(user_id=new_user.id, name_business=business_name)
                db.session.add(new_business)
                db.session.commit()

            return jsonify({"message": "Registration successful!"}), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"message": f"Error occurred: {str(e)}"}), 500

    @staticmethod
    def login_user(data):
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()
        if not user:
            return {"message": "User not found"}, 404

        if bcrypt.check_password_hash(user.password_hash, password):
            return {"message": "Login successful!"}, 200
        else:
            return {"message": "Incorrect password"}, 401
