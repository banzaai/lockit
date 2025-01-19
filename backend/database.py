from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    businesses = db.relationship('Business', backref='owner', lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'

# ✅ Corrected Business Model
class Business(db.Model):
    __tablename__ = 'businesses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name_business = db.Column(db.String(255), nullable=False)
    subscription_plan = db.Column(db.String(50), default='free')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    discounts = db.relationship('Discount', backref='business', lazy=True)

    def __repr__(self):
        return f'<Business {self.name_business}>'

# ✅ Corrected Discount Model
class Discount(db.Model):
    __tablename__ = 'discounts'

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable=False)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    discount_percent = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(50), default='active')

    def __repr__(self):
        return f'<Discount {self.title}>'
