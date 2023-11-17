
# Falto el profe y los pibes van a armar la clase
#Pedir edad y nombre de los compañeros que asistieron a clase

compañeros=[]
list=[]
cCompañeros =int(input("Ingrese la cantidad de compañeros : "))
for i in range(cCompañeros):
    nombre= input(f"Ingrese el nombre del compañero {i+1} : ")
    edad =int(input(f"Ingrese la edad del compañero {i+1} : "))
    compañero=(nombre,edad)
    compañeros.append(compañero)
compañeros.sort(key=lambda x :x[1])
asistente = compañeros[0][0]
profesor = compañeros[-1][0]
print(asistente,profesor)


    