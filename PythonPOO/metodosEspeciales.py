class Persona():
    def __init__(self,nombre,edad):   
        self.nombre=nombre
        self.edad=edad
    
    """__str__ permite que al llamar al objeto en vez de darnos el
        valor que almacena nos envie lo que hayamos definido """
    def __str__(self):
        return f"Persona({self.nombre},{self.edad})"
    
    def __repr__(self):
        return f'("{self.nombre}",{self.edad})'
    
    def __add__(self,otro):
        nuevo_valor=self.edad+otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
sandro=Persona("Sandro",22)
pedro=Persona("Pedro",23)
luis=Persona("Luis",20)
print(sandro)

repre=repr(sandro)
print(repre)

nueva_persona=sandro+pedro+luis
print(nueva_persona.edad)
