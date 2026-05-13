# services/base_service.py
class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, record_id):
        return self.repository.get_by_id(record_id)

    def create(self, data):
        return self.repository.create(**data)

    def update(self, record_id, data):
        return self.repository.update(record_id, **data)

    def delete(self, record_id):
        return self.repository.delete(record_id)