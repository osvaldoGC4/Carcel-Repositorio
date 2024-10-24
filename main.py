from common.conexion import Conexion
from controller.celda import CeldaController
from controller.interno import InternoController
from controller.actividad import ActividadController
from controller.personal import PersonalController
from controller.transferencia import TransferenciaController
from controller.visita import VisitaController
from controller.visitante import VisitanteController
from controller.visitaMultiple import VisitaMultipleController
from controller.delito import DelitoController
from controller.reglasN import ReglasNController
from models.celda import Celda
from models.interno import Interno
from models.actividad import Actividad
from models.personal import Personal
from models.transferencia import Transferencia
from models.visita import Visita
from models.visitante import Visitante
from models.visitaMultiple import VisitaMultiple
from models.delito import Delito


def menu_principal():
    print("Bienvenido al Sistema Penitenciario")
    print("Seleccione la entidad para realizar pruebas:")
    print("1. Celda")
    print("2. Interno")
    print("3. Actividad")
    print("4. Personal")
    print("5. Transferencia")
    print("6. Visita")
    print("7. Visitante")
    print("8. Visita Múltiple")
    print("9. Internos Por Celda")
    print("10. Motivo Condena Interno")
    print("0. Salir")
    return input("Ingrese el número de la opción deseada: ")

def ejecutar_pruebas_celda(celdaController: CeldaController):
    itemCelda = Celda(20, "Prueba", 25, "Disponible")
    print("############# crear_celda ####################")
    celdaController.crear_celda(itemCelda)
    print("############# obtener_celdas ####################")
    celdaController.obtener_celdas()
    itemCelda.set_Capacidad(8)
    print("############# actualizar_celda ####################")
    celdaController.actualizar_celda(itemCelda)
    print("############# obtener_celda ####################")
    celdaController.obtener_celda(itemCelda.get_ID_Celda())
    print("############# eliminar_celda ####################")
    celdaController.eliminar_celda(itemCelda.get_ID_Celda())
    print("############# obtener_celdas ####################")
    celdaController.obtener_celdas()

def ejecutar_pruebas_interno(internoController: InternoController):
    itemInterno = Interno(20, "Andrei", "2023-01-01", "Activo", 2, None)
    print("############# crear_interno ####################")
    internoController.crear_interno(itemInterno)
    print("############# obtener_internos ####################")
    internoController.obtener_internos()
    itemInterno.set_Estado("Liberado")
    print("############# actualizar_interno ####################")
    internoController.actualizar_interno(itemInterno)
    print("############# obtener_interno ####################")
    internoController.obtener_interno(itemInterno.get_ID_Interno())
    print("############# eliminar_interno ####################")
    internoController.eliminar_interno(itemInterno.get_ID_Interno())
    print("############# obtener_internos ####################")
    internoController.obtener_internos()

def ejecutar_pruebas_actividad(actividadController: ActividadController):
    itemActividad = Actividad(20, "artesania", "Deporte", "09:00-10:00")
    print("############# crear_actividad ####################")
    actividadController.crear_actividad(itemActividad)
    print("############# obtener_actividades ####################")
    actividadController.obtener_actividades()
    itemActividad.set_Nombre("Actividad Cultural")
    print("############# actualizar_actividad ####################")
    actividadController.actualizar_actividad(itemActividad)
    print("############# obtener_actividad ####################")
    actividadController.obtener_actividad(itemActividad.get_ID_Actividad())
    print("############# eliminar_actividad ####################")
    actividadController.eliminar_actividad(itemActividad.get_ID_Actividad())
    print("############# obtener_actividades ####################")
    actividadController.obtener_actividades()

def ejecutar_pruebas_personal(personalController: PersonalController):
    itemPersonal = Personal(20, "Enrique de jesus", "Supervisor", "07:00-16:00", "Activo")
    print("############# crear_personal ####################")
    personalController.crear_personal(itemPersonal)
    print("############# obtener_personales ####################")
    personalController.obtener_personal()
    itemPersonal.set_Estado("Inactivo")
    print("############# actualizar_personal ####################")
    personalController.actualizar_personal(itemPersonal)
    print("############# obtener_personal ####################")
    personalController.obtener_personal_por_id(itemPersonal.get_ID_Personal())
    print("############# eliminar_personal ####################")
    personalController.eliminar_personal(itemPersonal.get_ID_Personal())
    print("############# obtener_personales ####################")
    personalController.obtener_personal()

def ejecutar_pruebas_transferencia(transferenciaController: TransferenciaController):
    itemTransferencia = Transferencia(20, 1, 2, 3, "Cambio de celda")
    print("############# crear_transferencia ####################")
    transferenciaController.crear_transferencia(itemTransferencia)
    print("############# obtener_transferencias ####################")
    transferenciaController.obtener_transferencias()
    itemTransferencia.set_Motivo("Reubicación")
    print("############# actualizar_transferencia ####################")
    transferenciaController.actualizar_transferencia(itemTransferencia)
    print("############# obtener_transferencia ####################")
    transferenciaController.obtener_transferencia(itemTransferencia.get_ID_Transferencia())
    print("############# eliminar_transferencia ####################")
    transferenciaController.eliminar_transferencia(itemTransferencia.get_ID_Transferencia())
    print("############# obtener_transferencias ####################")
    transferenciaController.obtener_transferencias()

def ejecutar_pruebas_visita(visitaController: VisitaController):
    itemVisita = Visita(20, 1, 1, "2024-9-30", "10:00", 30)
    print("############# crear_visita ####################")
    visitaController.crear_visita(itemVisita)
    print("############# obtener_visitas ####################")
    visitaController.obtener_visitas()
    itemVisita.set_Duracion(60)
    print("############# actualizar_visita ####################")
    visitaController.actualizar_visita(itemVisita)
    print("############# obtener_visita ####################")
    visitaController.obtener_visita(itemVisita.get_ID_Visita())
    print("############# eliminar_visita ####################")
    visitaController.eliminar_visita(itemVisita.get_ID_Visita())
    print("############# obtener_visitas ####################")
    visitaController.obtener_visitas()

def ejecutar_pruebas_visitante(visitanteController: VisitanteController):
    itemVisitante = Visitante(20, "Maria Lopez", "Hermana", "12345678")
    print("############# crear_visitante ####################")
    visitanteController.crear_visitante(itemVisitante)
    print("############# obtener_visitantes ####################")
    visitanteController.obtener_visitantes()
    itemVisitante.set_Relacion("Prima")
    print("############# actualizar_visitante ####################")
    visitanteController.actualizar_visitante(itemVisitante)
    print("############# obtener_visitante ####################")
    visitanteController.obtener_visitante(itemVisitante.get_ID_Visitante())
    print("############# eliminar_visitante ####################")
    visitanteController.eliminar_visitante(itemVisitante.get_ID_Visitante())
    print("############# obtener_visitantes ####################")
    visitanteController.obtener_visitantes()

def ejecutar_pruebas_visita_multiple(visitaMultipleController: VisitaMultipleController):
    itemVisitaMultiple = VisitaMultiple(1, 1)
    print("############# crear_visita_multiple ####################")
    visitaMultipleController.crear_visita_multiple(itemVisitaMultiple)
    print("############# obtener_visitas_multiple ####################")
    visitaMultipleController.obtener_visitas_multiples()
    print("############# eliminar_visita_multiple ####################")
    visitaMultipleController.eliminar_visita_multiple(itemVisitaMultiple.get_ID_Visita(), itemVisitaMultiple.get_ID_Visitante())
    print("############# obtener_visitas_multiple ####################")
    visitaMultipleController.obtener_visitas_multiples()

def ejecutar_pruebas_interno_por_celda(reglasNcontroller: ReglasNController):
    print("############# obtener_internos_por_celda ####################")
    reglasNcontroller.contar_reclusos_por_celda()

def ejecutar_pruebas_motivo_condena(reglasNcontroller: ReglasNController):
    id_interno = int(input("Ingrese el ID del Interno: "))
    id_delito = int(input("Ingrese el ID del Delito: "))
    print("############# motivo condena ####################")
    reglasNcontroller.obtener_condena_por_interno_y_delito(id_interno, id_delito)

if __name__ == '__main__':
    while True:
        opcion = menu_principal()
        
        if opcion == '1':
            conexion = Conexion()
            celdaController = CeldaController()
            ejecutar_pruebas_celda(celdaController)
        elif opcion == '2':
            conexion = Conexion()
            internoController = InternoController()
            ejecutar_pruebas_interno(internoController)
        elif opcion == '3':
            conexion = Conexion()
            actividadController = ActividadController()
            ejecutar_pruebas_actividad(actividadController)
        elif opcion == '4':
            conexion = Conexion()
            personalController = PersonalController()
            ejecutar_pruebas_personal(personalController)
        elif opcion == '5':
            conexion = Conexion()
            transferenciaController = TransferenciaController()
            ejecutar_pruebas_transferencia(transferenciaController)
        elif opcion == '6':
            conexion = Conexion()
            visitaController = VisitaController()
            ejecutar_pruebas_visita(visitaController)
        elif opcion == '7':
            conexion = Conexion()
            visitanteController = VisitanteController()
            ejecutar_pruebas_visitante(visitanteController)
        elif opcion == '8':
            conexion = Conexion()
            visitaMultipleController = VisitaMultipleController()
            ejecutar_pruebas_visita_multiple(visitaMultipleController)
        elif opcion == '9':
            conexion = Conexion()
            reglasNController = ReglasNController()
            ejecutar_pruebas_interno_por_celda(reglasNController)
        elif opcion == '10':
            conexion = Conexion()
            reglasNController = ReglasNController()
            ejecutar_pruebas_motivo_condena(reglasNController)
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
