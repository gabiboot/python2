class enca:
    def __init__(self):
        self.__numero = 0

    def operacion(self):
        print( self.__numero + 10)    

    def resultado(self):
        return self.__numero
    
ejemplo = enca()
ejemplo.operacion()