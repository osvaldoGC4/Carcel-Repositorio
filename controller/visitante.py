from flask import Blueprint, request
from controller.baseController import BaseController

class VisitanteController(BaseController):
    def __init__(self, app):
        super().__init__('visitante')
        visitante_blueprint = Blueprint('visitante', __name__)
        visitante_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        visitante_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        visitante_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        visitante_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        visitante_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(visitante_blueprint, url_prefix='/visitante')

    def update_route(self, id):
        extra_params = request.args.to_dict()
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()
        print(extra_params)
        return self.delete(id, extra_params)
