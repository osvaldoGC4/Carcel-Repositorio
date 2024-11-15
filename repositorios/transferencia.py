from flask import Blueprint, request
from aplicaciones.baseController import BaseController

class TransferenciaRepositorio:
    def __init__(self, app):
        super().__init__('transferencia')
        transferencia_blueprint = Blueprint('transferencia', __name__)
        transferencia_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        transferencia_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        transferencia_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        transferencia_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        transferencia_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(transferencia_blueprint, url_prefix='/transferencia')

    # Rutas de actualización y eliminación que admiten parámetros adicionales
    def update_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.delete(id, extra_params)