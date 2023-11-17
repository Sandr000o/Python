from abc import ABC,abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años y soy del género {self.sexo}"
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        return f"Estoy estudiando : {self.actividad}"
    
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        return f"Actualmente estoy trabajando en el rubro de : {self.actividad}"
    
lucas=Estudiante("Lucas",22,"Masculino","programación")
print(lucas.hacer_actividad())
print(lucas.presentarse())

pedrito=Trabajador("Pedro",24,"No binario","programación")
print(pedrito.hacer_actividad())
print(pedrito.presentarse())
