from flask import Blueprint

from controllers.base_controller import BaseController
from services.base_service import BaseService
from repositories.base_repository import BaseRepository
from models.services.services import Service
from shemas.service_schema import ServiceSchema

services_repo = BaseRepository(Service)
service_service = BaseService(services_repo)
service_schema = ServiceSchema()


class ReviewsController(BaseController):
    def __init__(self):
        super().__init__(service=service_service, schema=service_schema)

service_bp = Blueprint('service', __name__)
service_view = ReviewsController.as_view('service_api')

service_bp.add_url_rule('/', defaults={'record_id': None}, view_func=service_view, methods=['GET'])
service_bp.add_url_rule('/', view_func=service_view, methods=['POST'])
service_bp.add_url_rule('/<int:record_id>', view_func=service_view, methods=['GET', 'PUT', 'DELETE'])
