from datetime import datetime
from backend.database import db  # Import db instance

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
