import flask;

from common.conexion import Conexion
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

from aplicaciones.reglasN import ReglasNController


if __name__ == "__main__":
    app = flask.Flask(__name__)
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
    app.run('localhost', 4040);


