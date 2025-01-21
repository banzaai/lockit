from backend.database import db  # Import db instance

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    businesses = db.relationship('Business', backref='city', lazy=True)

    def __repr__(self):
        return f'<City {self.name}>'
