from common.conexion import Conexion

class Crud:
    def __init__(self) -> None:
        self.conexion = Conexion()
    
    def execInsert(self, entity, objectData) -> bool:
        self.conexion.conectar()
        spName = "DynamicInsert"
        response = self.conexion.execSP(spName, [entity, objectData])
        self.conexion.cerrar()
        return response

    def execSelect(self, entity, stringFieldSelect, stringFieldOtherOptions):
        self.conexion.conectar()
        spName = "DynamicalSelect"
        response = self.conexion.execSPResult(spName, [entity, stringFieldSelect, stringFieldOtherOptions])
        # Agregar print para ver lo que devuelve el SP
        return response
    
    def execUpdate(self, entity, stringFieldUpdate,  stringCondition):
        self.conexion.conectar()
        spName = "DynamicalUpdate"
        response = self.conexion.execSP(spName, [entity, stringFieldUpdate, stringCondition])
        self.conexion.cerrar()
        return response
    
    def execDelete(self, entity, stringCondition):
        self.conexion.conectar()
        spName = "DynamicDelete"
        response = self.conexion.execSP(spName, [entity, stringCondition, None, None, None])
        self.conexion.cerrar()
        return response