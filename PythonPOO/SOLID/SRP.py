"""
SRP=Single Responsability Particple
Este principio nos dice que cada clase debe encargarse de hacer
solo lo que le conscierne y no sobrecargarlo
"""

class Auto():
    def __init__(self,tanque):
        self.posicion=0
        self.tanque=tanque
         
    def mover(self,distancia):
        if(self.tanque.obtener_combustible>= distancia/2):
            self.posicion+=distancia
            self.tanque.usar_combustible(distancia)
            print ("Haz movido el auto exitosamente")
        else:
            print("No tiene suficiente combustible")
            
    @property       
    def obtener_posicion(self):
        return self.posicion
            
class  TanqueDeCombustible():
    def __init__(self):
        self.combustible=100
        
    def agregar_combustible(self,cantidad):
        self.combustible+=cantidad
        print(f"Agrego {cantidad} de combustible ahora tiene : {self.combustible}")
    
    @property
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,distancia):
        self.combustible-=distancia/2
        
tanque=TanqueDeCombustible()
autito=Auto(tanque)

print(autito.obtener_posicion)
autito.mover(10)
print(autito.obtener_posicion)
autito.mover(20)
print(autito.obtener_posicion)
autito.mover(60)
print(autito.obtener_posicion)
autito.mover(100)
print(autito.obtener_posicion)
autito.mover(60)
tanque.agregar_combustible(60)
autito.mover(60)
print(autito.obtener_posicion)