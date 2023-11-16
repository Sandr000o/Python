class Auto():
    def __init__(self):
        self._estado="apagado"
    
    def encencer(self):
        self._estado="encender"
        print("El auto esta encendido") 
        
    def conducir(self):
        if self._estado=="apagado":
            self.encencer()
        print("Conduciendo el auto")

mi_auto=Auto()

mi_auto.conducir()   
    