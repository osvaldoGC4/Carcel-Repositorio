from flask import Blueprint, request
from controller.baseController import BaseController

class ActividadController(BaseController):
    operacionCrud = None

    def __init__(self, app):
        super().__init__('actividad')
        actividad_blueprint = Blueprint('actividad', __name__)
        actividad_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        actividad_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        actividad_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        actividad_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        actividad_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(actividad_blueprint, url_prefix='/actividad')

     # Rutas de actualización y eliminación que admiten parámetros adicionales
    def update_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.delete(id, extra_params)