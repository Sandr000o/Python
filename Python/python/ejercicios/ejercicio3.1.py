
cant=input("Ingrese la cantidad de alumnos que asistieron : ")
alumnos=[]
def ordenar(cant):
    for i in range(int(cant)):
        nombre=input(f"Ingrese el nombre {1+i} : ")
        edad=input(f"Ingrese la edad del compañero {i+1} : ")
        alumno=nombre,edad
        alumnos.append(alumno)
    alumnos.sort(key=lambda x:x[1])
    asistente=alumnos[0][0]
    profesor=alumnos[-1][0]
    return asistente,profesor
    


asistente,profesor=ordenar(cant)
print(f"El nombre del asistente es : {asistente}")
print(f"El nombre del profesor es : {profesor}")