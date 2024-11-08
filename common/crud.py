from common.conexion import Conexion

class Crud:
    def __init__(self) -> None:
        self.conexion = Conexion()
    
    def execInsert(self, NombreSP, objectData) -> bool:
        self.conexion.conectar()
        ##spName = "DynamicInsert"
        spName = NombreSP
        response = self.conexion.execSP(spName, [objectData])
        self.conexion.cerrar()
        return response

    def execSelect(self, nombreSP, stringFieldSelect):
        self.conexion.conectar()
        ##spName = "DynamicalSelect"
        spName = nombreSP
        response = self.conexion.execSPResult(spName, [stringFieldSelect])
        # Agregar print para ver lo que devuelve el SP
        return response
    
    def execUpdate(self, NombreSP, stringFieldUpdate,  stringCondition):
        self.conexion.conectar()
        ##spName = "DynamicalUpdate"
        spName = NombreSP
        response = self.conexion.execSP(spName, [stringFieldUpdate, stringCondition])
        self.conexion.cerrar()
        return response
    
    def execDelete(self, nombreSP, stringCondition):
        self.conexion.conectar()
        ##spName = "DynamicDelete"
        spName = nombreSP
        response = self.conexion.execSP(spName, [stringCondition])
        self.conexion.cerrar()
        return response