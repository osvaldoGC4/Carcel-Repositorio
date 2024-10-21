from common.conexion import Conexion
from controller.celda import CeldaController
from controller.interno import InternoController
from controller.actividad import ActividadController
from controller.personal import PersonalController
from controller.transferencia import TransferenciaController
from controller.visita import VisitaController
from controller.visitante import VisitanteController
from controller.visitaMultiple import VisitaMultipleController
from models.celda import Celda
from models.interno import Interno
from models.actividad import Actividad
from models.personal import Personal
from models.transferencia import Transferencia
from models.visita import Visita
from models.visitante import Visitante
from models.visitaMultiple import VisitaMultiple

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
    print("0. Salir")
    return input("Ingrese el número de la opción deseada: ")

def ejecutar_pruebas_celda(celdaController):
    itemCelda = Celda(1, "Medellin", 5, "Disponible")
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

def ejecutar_pruebas_interno(internoController):
    itemInterno = Interno(1, "Juan Perez", "2023-01-01", "Activo", 1, None)
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

def ejecutar_pruebas_actividad(actividadController):
    itemActividad = Actividad(1, "Actividad Recreativa", "Deporte", "09:00-10:00")
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

def ejecutar_pruebas_personal(personalController):
    itemPersonal = Personal(1, "Carlos Gomez", "Supervisor", "08:00-16:00", "Activo")
    print("############# crear_personal ####################")
    personalController.crear_personal(itemPersonal)
    print("############# obtener_personales ####################")
    personalController.obtener_personales()
    itemPersonal.set_Estado("Inactivo")
    print("############# actualizar_personal ####################")
    personalController.actualizar_personal(itemPersonal)
    print("############# obtener_personal ####################")
    personalController.obtener_personal(itemPersonal.get_ID_Personal())
    print("############# eliminar_personal ####################")
    personalController.eliminar_personal(itemPersonal.get_ID_Personal())
    print("############# obtener_personales ####################")
    personalController.obtener_personales()

def ejecutar_pruebas_transferencia(transferenciaController):
    itemTransferencia = Transferencia(1, 1, 2, "2024-10-20", "Cambio de celda")
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

def ejecutar_pruebas_visita(visitaController):
    itemVisita = Visita(1, 1, 1, "2024-10-20", "10:00", 30)
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

def ejecutar_pruebas_visitante(visitanteController):
    itemVisitante = Visitante(1, "Maria Lopez", "Hermana", "12345678")
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

def ejecutar_pruebas_visita_multiple(visitaMultipleController):
    itemVisitaMultiple = VisitaMultiple(1, 1)
    print("############# crear_visita_multiple ####################")
    visitaMultipleController.crear_visita_multiple(itemVisitaMultiple)
    print("############# obtener_visitas_multiple ####################")
    visitaMultipleController.obtener_visitas_multiple()
    print("############# eliminar_visita_multiple ####################")
    visitaMultipleController.eliminar_visita_multiple(itemVisitaMultiple.get_ID_Visita())
    print("############# obtener_visitas_multiple ####################")
    visitaMultipleController.obtener_visitas_multiple()

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
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
