from datetime import datetime
from backend.database import db  # Import db instance

class Business(db.Model):
    __tablename__ = 'businesses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)  # New city reference
    name_business = db.Column(db.String(255), nullable=False)
    subscription_plan = db.Column(db.String(50), default='free')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    discounts = db.relationship('Discount', backref='business', lazy=True)

    def __repr__(self):
        return f'<Business {self.name_business}>'
