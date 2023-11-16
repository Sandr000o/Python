class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def datos(self):
        print(f"Nombre del estudiante : {self.nombre}\nEdad del estudiante : {self.edad}")
              
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    
    def mostrarGrado(self):
        print(f"El grado del estudiante es : {self.grado}")
        
estudiante=Estudiante("Juan",22,3)
estudiante.datos()
estudiante.mostrarGrado()
