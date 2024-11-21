import datetime
import jwt
from flask import Blueprint, request, jsonify

class AuthService:
    def __init__(self, app):
        auth_blueprint = Blueprint('auth', __name__)
        auth_blueprint.add_url_rule('/token', view_func=self.token, methods=["POST"])
        app.register_blueprint(auth_blueprint, url_prefix='/auth')

    def token(self):
        try:
            datos = request.json
            admin_user = 'admin_carcel'
            admin_password = 'Qwer.1234'
            key = 'KJhisdy8787798udfsd56f4s5d4fsdf'

            # Validación de usuario y contraseña
            if "User" not in datos or datos["User"] != admin_user:
                return jsonify({"Error": "El usuario es incorrecto"}), 400
            if "Password" not in datos or datos["Password"] != admin_password:
                return jsonify({"Error": "La contraseña es incorrecta"}), 400

            # Generación del token con expiración
            encoded = jwt.encode(
                {
                    "Usuario": admin_user,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
                },
                key,
                algorithm="HS256"
            )
            return jsonify({"Token": encoded, "Response": "Ok"}), 200

        except Exception as ex:
            return jsonify({"Error": str(ex)}), 400
