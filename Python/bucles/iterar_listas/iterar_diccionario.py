diccionario = {
    "nombre" :'sandro',
    "apellido": 'reyes',
    "edad" : 23
}

#Recorriendo diccionario para obtener las claves
for key in diccionario:
    print(f"La clave es : {key}")

#Recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key=datos[0]
    value=datos[1]
    print(f"La clave es : {key} y el valor es : {value}")