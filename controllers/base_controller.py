# controllers/base_controller.py
from flask import request, jsonify
from flask.views import MethodView

class BaseController(MethodView):
    def __init__(self, service, schema=None):
        self.service = service
        self.schema = schema # Optional: for formatting JSON responses

    def get(self, record_id=None):
        if record_id:
            record = self.service.get_by_id(record_id)
            if not record:
                return jsonify({"error": "Not found"}), 404

            return jsonify(self.schema.dump(record)), 200

        records = self.service.get_all()
        return jsonify(self.schema.dump(records, many=True)), 200

    def post(self):
        data = request.get_json()
        record = self.service.create(data)
        return jsonify({"status": "success", "id": record.id}), 201

    def delete(self, record_id):
        success = self.service.delete(record_id)
        if success:
            return jsonify({"status": "deleted"}), 200
        return jsonify({"error": "Not found"}), 404