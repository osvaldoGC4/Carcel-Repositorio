import json
from flask import Blueprint, request
from controller.baseController import BaseController
from common.encriptador import EncriptadorAES

class CeldaController(BaseController):
    operacionCrud = None

    def __init__(self, app):
        ## self.encriptar = EncriptadorAES()
        super().__init__('celda')
        celda_blueprint = Blueprint('celda', __name__)
        celda_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        celda_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        celda_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        celda_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        celda_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(celda_blueprint, url_prefix='/celda')

    # Rutas de actualización y eliminación que admiten parámetros adicionales
    def update_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.delete(id, extra_params)
