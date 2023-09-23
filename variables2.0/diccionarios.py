
#Creando diccionarios
diccionarios=dict(nombre="lisandro",apellido="reyes")
print(diccionarios)

#Crearlo usando dir nos permite crear diccionarios vacios
diccionario=dict()
print(type(diccionario))

#Las listas no pueden ser claves porque son iterables al igual que los conjuntos
#Las tuplas si pueden ser claves
dictionary={("rancio","rencio"):"jajaj"}
print(type(dictionary))
print(dictionary)

#Los conjuntos si pueden ser claves si los congelamos con la función frozenset
dictionary2={frozenset({"rancio","rencio"}):"jajaj"}
print(type(dictionary2))
print(dictionary2)

#Crear diccionarios con fromkeys(), tiene que estar entre llaves como una lista para que no nos de error
dictionary3=dict.fromkeys(["nombre","apellido","edad"])
print(dictionary3)


#Crear diccionarios con fromkeys(), con dos parametros fijos
dictionary4=dict.fromkeys(["nombre","apellido","edad"],"Valor fijado")
print(dictionary4)