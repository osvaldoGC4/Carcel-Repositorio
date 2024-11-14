from flask import Blueprint, request
from aplicaciones.baseController import BaseController

class VisitaMultipleController(BaseController):
    def __init__(self, app):
        super().__init__('visitaMultiple')
        visitaMultiple_blueprint = Blueprint('visitaMultiple', __name__)
        visitaMultiple_blueprint.add_url_rule('/', view_func=self.getAll, methods=["GET"])
        visitaMultiple_blueprint.add_url_rule('/<int:id>', view_func=self.getById, methods=["GET"])
        visitaMultiple_blueprint.add_url_rule('/', view_func=self.create, methods=["POST"])
        visitaMultiple_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        visitaMultiple_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(visitaMultiple_blueprint, url_prefix='/visitaMultiple')

    def update_route(self, id):
        extra_params = request.args.to_dict()
        return self.update(id, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()
        return self.delete(id, extra_params)
