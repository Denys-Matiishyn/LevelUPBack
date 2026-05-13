
from ma import ma
from models.reviews.reviews import Reviews

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reviews
        include_fk = True
        load_instance = True