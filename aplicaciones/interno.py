from flask import Blueprint, request
from aplicaciones.baseController import BaseController

class InternoController(BaseController):
    operacionCrud = None

    def __init__(self, app):
        super().__init__('interno')
        interno_blueprint = Blueprint('interno', __name__)
        interno_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        interno_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        interno_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        interno_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        interno_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(interno_blueprint, url_prefix='/interno')

     # Rutas de actualización y eliminación que admiten parámetros adicionales
    def update_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.delete(id, extra_params)