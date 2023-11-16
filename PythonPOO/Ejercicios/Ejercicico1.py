class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")
        
pedro=Estudiante("Pedro",22,3)
print(pedro.edad)

nombre=input("Digame su nombre : ")
edad=input("Digame su edad : ")
grado=input("Digame su grado : ")

estudiante=Estudiante(nombre,edad,grado)
print(f"""
      El estudiante se llama {estudiante.nombre}\n
      El estudiante tiene {estudiante.edad}\n
      El estudiante esta en el grado {estudiante.grado}
      """)

estudiar=input("Ingrese el texto : ")
if(estudiar.lower()=="estudiar"):
    estudiante.estudiar()
    
