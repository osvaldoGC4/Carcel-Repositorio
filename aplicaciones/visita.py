from flask import Blueprint, request
from aplicaciones.baseController import BaseController

class VisitaController(BaseController):
    def __init__(self, app):
        super().__init__('visita')
        visita_blueprint = Blueprint('visita', __name__)
        visita_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        visita_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        visita_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        visita_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        visita_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(visita_blueprint, url_prefix='/visita')

    # Rutas de actualización y eliminación que admiten parámetros adicionales
    def update_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.delete(id, extra_params)
