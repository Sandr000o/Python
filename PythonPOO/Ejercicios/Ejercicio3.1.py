class Personaje():
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre=nombre
        self.fuerza=fuerza
        self.velocidad=velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza : {self.fuerza}, Velocidad : {self.velocidad})"
    
    def __add__(self,otro_pj):
        nuevo_nombre=self.nombre+"-"+otro_pj.nombre
        nueva_fuerza=round(pow((self.fuerza+otro_pj.fuerza)/2,1.5))
        nueva_velocidad=round(pow((self.velocidad+otro_pj.velocidad)/2,1.5))
        return(Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad))

def mostrarPersonajes(personajes):
    if  len(personajes)==0:
         print("Aún no se ha creado un personajes")
    else:
        print("Personajes disponibles : ")
        for i, personaje in enumerate(personajes):
             print(f"{i+1}. {personaje}")
    
def crearPersonajes():
    nombre=input("Ingrese el nombre del personaje : ")
    fuerza=float(input("Ingrese la fuerza de : "))
    velocidad=float(input("Ingrese la velocidad de : "))
    return Personaje(nombre,fuerza,velocidad)

def borrarPersonaje(personajes,numero):
    del personajes[numero-1]
    
personajes=[]
        
while True:
    print("\tMENÚ\n1. Crear Personaje")
    print("2. Fusionar Personaje")
    print("3. Mostrar Personaje")
    print("4. Eliminar Personaje")
    print("5. Salir")
    opcion=input("Seleccione una de las opciones : ")
    
    if(opcion=='1'):
        personaje_nuevo=crearPersonajes()
        personajes.append(personaje_nuevo)
        print("Personaje creado con exito")
    elif(opcion=='2'):
        if(len(personajes)<2):
            print("Para fusionar debe tener al menos 2 personajes")
        else:
            mostrarPersonajes(personajes)
            pj1=int(input("Ingrese el número del primer personaje : "))
            pj2=int(input("Ingrese el número del segundo personaje : "))
            
            if(1<=pj1 <=len(personajes)) and (1<=pj2<=len(personajes) and pj1!=pj2):
                personaje1=personajes[pj1-1]
                personaje2=personajes[pj2-1]
                personaje_fusionado=personaje1+personaje2
                personajes.append(personaje_fusionado)
            else:
                print("Selección inválida. Asegúrese de elegir personajes válidos.")
    elif(opcion=='3'):
        mostrarPersonajes(personajes)
    
    elif(opcion=='4'):
        mostrarPersonajes(personajes)
        pj1=int(input("Ingrese el número del persona a borrar"))
        if(1<=pj1 <=len(personajes)):
            borrarPersonaje(personajes,pj1)
        mostrarPersonajes(personajes)
    elif(opcion=='5'):
        print("Hasta luego!")
        break
    else:
        print("No eligió una opcion válida")