from common.conexion import Conexion
class crud:
    def __init__(self) -> None:
        self.conexion = Conexion()
    
    def execInsert(self, entity, objectData) -> str:
        self.conexion.conectar()
        spName = "DynamicInsert"
        response = self.conexion.execSP(spName, [entity, objectData])
        self.conexion.cerrar()
        return response[0][0]

    def execSelect(self, entity, stringFieldSelect, stringFieldOtherOptions):
        self.conexion.conectar()
        spName = "DynamicSelect"
        response = self.conexion.execSP(spName, [entity, stringFieldSelect, stringFieldOtherOptions])
        self.conexion.cerrar()
        return response
    
    def execUpdate(self, entity, stringFieldUpdate,  stringCondition):
        self.conexion.conectar()
        spName = "DynamicUpdate"
        response = self.conexion.execSP(spName, [entity, stringFieldUpdate, stringCondition])
        self.conexion.cerrar()
        return response[0][0]
    
    def execDelete(self, entity, stringCondition):
        self.conexion.conectar()
        spName = "DynamicDelete"
        response = self.conexion.execSP(spName, [entity, stringCondition])
        self.conexion.cerrar()
        return response[0][0]