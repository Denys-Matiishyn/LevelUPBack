from flask import Blueprint

from controllers.base_controller import BaseController
from services.base_service import BaseService
from repositories.base_repository import BaseRepository
from models.reviews.reviews import Reviews
from shemas.review_schema import ReviewSchema

review_repo = BaseRepository(Reviews)
review_service = BaseService(review_repo)
review_schema = ReviewSchema()


class ReviewsController(BaseController):
    def __init__(self):
        super().__init__(service=review_service, schema=review_schema)

reviews_bp = Blueprint('reviews', __name__)
review_view = ReviewsController.as_view('reviews_api')

reviews_bp.add_url_rule('/', defaults={'record_id': None}, view_func=review_view, methods=['GET'])
reviews_bp.add_url_rule('/', view_func=review_view, methods=['POST'])
reviews_bp.add_url_rule('/<int:record_id>', view_func=review_view, methods=['GET', 'PUT', 'DELETE'])
