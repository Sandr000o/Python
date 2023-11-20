"""
ISP=Interface Segregation Principle
Tenemos que eliminar las dependencias que no vamos a utilizar,
no debemos forzar a usar las interfaces
"""

from abc import ABC,abstractclassmethod

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass
    
class Humano(Trabajador,Durmiente,Comedor):
    def comer(self):
        print("El humano esta comiendo")
        
    def dormir(self):
        print("El humano esta durmiendo")
        
    def trabajar(self):
        print("El humano esta trabajando")
        
class Robot(Trabajador):  
    def trabajar(self):
        print("El robot esta trabajando")
        
robot=Robot()
robot.trabajar()

humano=Humano()
humano.comer()    
"""
Esto esta mal porque la clase Robot() se ve obligada a implementar los métodos comer y dormir, pero 
no lo hacen, por ende sería mejor modificar y separar en clase Comedor() y Dormidor()
"""

