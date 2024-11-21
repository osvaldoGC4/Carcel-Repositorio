from flask import Blueprint, request
from servicios.base import BaseService
from repositorios.actividad import ActividadRepositorio
class ActividadController(BaseService):
    repository = ActividadRepositorio()
    def __init__(self, app):
        super().__init__('actividad')
        actividad_blueprint = Blueprint('actividad', __name__)
        actividad_blueprint.add_url_rule('/', view_func=self.getAll_route, methods=["GET"])
        actividad_blueprint.add_url_rule('/<int:id>', view_func=self.getById_route, methods=["GET"])
        actividad_blueprint.add_url_rule('/', view_func=self.create_raoute, methods=["POST"])
        actividad_blueprint.add_url_rule('/<int:id>', view_func=self.update_route, methods=["PATCH"])
        actividad_blueprint.add_url_rule('/<int:id>', view_func=self.delete_route, methods=["DELETE"])
        app.register_blueprint(actividad_blueprint, url_prefix='/actividad')

    def getAll_route(self):
        return self.getAll(self.repository) # Este repositorio debe seguir la firma de la interfaz
     # Rutas de actualización y eliminación que admiten parámetros adicionales
    def update_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.update(id, self.repository, extra_params)

    def delete_route(self, id):
        extra_params = request.args.to_dict()  # Captura cualquier parámetro extra en la URL
        return self.delete(id, self.repository, extra_params)
    
    def getById_route(self, id):
        return self.getById(id, self.repository)
    
    def create_raoute(self):
        return self.create(self.repository)