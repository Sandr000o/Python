diccionario = {
    "nombre" : 'sandro',
    "apellido" :'reyes',
    "edad" : 23
}

#Acá obtenemos las claves asignadas a los valores del diccionario
claves=diccionario.keys()
print(claves)

#Acá obtenmos los valores asignadas a las claves
valores = diccionario.values()
print(valores)

#Obtenemos el valor de acuerdo a la llave que tiene dicho valor
#Al usar get evitamos que nos lance un error al buscar una llave que no existe, simplemente nos devolvera "none"
valor=diccionario.get("edad")
print(valor)


#También podemos asignar claves númericas

diccionario2= {
    0:"Sandro",
    1:"Reyes",
    2:23
}
print(diccionario2[0])

#Eliminar todos los elementos
diccionario2.clear()
print(diccionario2)

#Para eliminar un elemento del diccionario, pasandole la clave
diccionario.pop('apellido')
print(diccionario)

#Obtener un elemento dict_items iterable
diccionario_iterable = diccionario.items();
print(diccionario_iterable)
