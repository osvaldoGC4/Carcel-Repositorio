from flask import Flask, request, jsonify
import jwt

from aplicaciones.celda import CeldaController
from aplicaciones.interno import InternoController
from aplicaciones.actividad import ActividadController
from aplicaciones.personal import PersonalController
from aplicaciones.transferencia import TransferenciaController
from aplicaciones.visita import VisitaController
from aplicaciones.visitante import VisitanteController
from aplicaciones.visitaMultiple import VisitaMultipleController
from aplicaciones.delito import DelitoController
from aplicaciones.internoActividad import InternoActividadController
from aplicaciones.condena import CondenaController
from aplicaciones.informeDisciplina import InformeDisciplinaController
from aplicaciones.auth import AuthController
from aplicaciones.reglasN import ReglasNController

app = Flask(__name__)
app.config["SECRET_KEY"] = "KJhisdy8787798udfsd56f4s5d4fsdf"

@app.before_request
def verify_token():
    # Lista de rutas públicas que no requieren autenticación
    public_routes = ['auth.token']  
    
    # Verificar si la ruta no es pública
    if request.endpoint not in public_routes:
        token = request.headers.get("Authorization")
        print(token)
        if not token:
            return jsonify({"Error": "Token faltante"}), 401
        try:
            jwt.decode(token.replace('Bearer ', ''), app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"Error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"Error": "Token inválido"}), 401

# Registro de los controladores
CeldaController(app)
InternoController(app)
ActividadController(app)
PersonalController(app)
TransferenciaController(app)
VisitaController(app)
VisitanteController(app)
VisitaMultipleController(app)
DelitoController(app)
InternoActividadController(app)
InformeDisciplinaController(app)
CondenaController(app)
ReglasNController(app)
AuthController(app)

if __name__ == "__main__":
    app.run('localhost', 4040)