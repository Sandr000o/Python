
class Persona:
    def __init__(self,nombre,apellido,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.nacionalidad=nacionalidad
    
    def saludar(self):
        return f"Hola mi nombre es {self.nombre},mi apellido {self.apellido}, soy {self.nacionalidad} "

    def talento(self):
        return ("Mi talento es poder volar")
    
    def hablar(self):
        print("Estoy hablando")

class Empleado(Persona):
    def __init__(self,nombre,apellido,nacionalidad,salario,puesto):
        super().__init__(nombre,apellido,nacionalidad)
        self.salario=salario
        self.puesto=puesto
    
    def saludar(self):
         return f"Hola mi nombre es {self.nombre},mi apellido {self.apellido}, soy {self.nacionalidad} , mi sueldo es {self.salario}, mi puesto es {self.puesto}"

e=Empleado("Luis","Perez","Peruano",1500,"Practicante")

e.talento()
        
class Estudiante(Persona):
    def __init__(self,nombre,apellido,nacionalidad,edad,grado,seccion):
        super().__init__(nombre,apellido,nacionalidad)
        self.edad=edad
        self.grado=grado
        self.seccion=seccion
    
    def curso(self):
        return f'Mi grado es {self.grado} y mi sección es {self.seccion}'
        
    
es=Estudiante('Pedro','Reyes','Peruano',22,7,"A")
print(es.curso())

#Herencia múltiple

class Artista():
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def mostrarHabilidad(self):
        return(f"Mi habilidad es : {self.habilidad}")
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,apellido,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,apellido,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa
    
    def mostrarHabilidad(self):
        return ("No tengo jaja")        
    
    def presentarse(self):
        return f"Soy {self.nombre} y mi habilidad es {self.habilidad} y trabajo en {self.empresa}"

roberto=EmpleadoArtista("Roberto","Martinez","Peruano","Cantar",100000,"Programador")

print(roberto.presentarse())