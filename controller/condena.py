from flask import Blueprint, request
from controller.baseController import BaseController

class CondenaController(BaseController):
    operacionCrud = None

    def __init__(self, app):
        super().__init__('condena')
        condena_blueprint = Blueprint('condena', __name__)
        condena_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        condena_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        condena_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        condena_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        condena_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(condena_blueprint, url_prefix='/condena')

     # Rutas de actualización y eliminación que admiten parámetros adicionales
    def update_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.delete(id, extra_params)