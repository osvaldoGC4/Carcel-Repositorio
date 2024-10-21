class ReglasN:
    def __init__(self, ID_Interno=None, ID_Delito=None):
        self._ID_Interno = ID_Interno
        self._ID_Delito = ID_Delito
    
    def get_ID_Interno(self):
        return self._ID_Interno
    
    def get_ID_Delito(self):
        return self._ID_Delito
