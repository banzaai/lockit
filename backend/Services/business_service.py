from backend.database import db
from backend.models.business import Business
from backend.models.city import City

class BusinessService:
    @staticmethod
    def create_business(data):
        name_business = data.get("name_business")
        user_id = data.get("user_id")
        city_name = data.get("city_name")

        if not name_business or not user_id or not city_name:
            return {"message": "Missing required fields"}, 400

        # Find or create the city
        city = City.query.filter_by(name=city_name).first()
        if not city:
            city = City(name=city_name)
            db.session.add(city)
            db.session.commit()

        # Create business linked to the city
        new_business = Business(name_business=name_business, user_id=user_id, city_id=city.id)
        db.session.add(new_business)
        db.session.commit()

        return {"message": "Business registered successfully!"}, 201
