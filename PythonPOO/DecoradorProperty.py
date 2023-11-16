class Persona():
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self._edad=edad
    
    @property
    def nombre(self):
        return self._nombre
        
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre=nuevo_nombre
    
    @nombre.deleter
    def nombre(self):
        del self._nombre
   
    
dalto=Persona("Lucas",24)
nombre=dalto.nombre
print(nombre)
dalto.nombre="Pepito"
nombre=dalto.nombre
print(nombre)
del dalto.nombre
nombre=dalto.nombre
print(nombre)