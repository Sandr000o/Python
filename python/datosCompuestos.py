lista = ["LucasDalto","Soy Dalto",True,1.85]
tupla=("LucasDalto","Soy Dalto",True,1.85)

#Datos de la lista pueden ser modificados, datos de las tuplas son constantes
#Mostrar todos los datos
print(lista)

#Mostrar solo uno

print(lista[0])

#Modificar valores de la lista

lista[0]="Maquinola";
print(lista[0])


#Creando un conjunto (set)
#Al igual que las tuplas no se pueden modificar 
#No se pueden repetir valores
#No se muestran los valores individuales de esta manera "conjunto[2]"
#Se puede iterar usando un bucle
conjunto = {"LucasDalto","Soy Dalto",True,1.85,"Soy dalto"}
print(conjunto)

#Creando un diccionario (dic)
diccionario = { 
     'nombre' : 'Lucas Dalto',
     'canal' : 'Soy lucas',
     'esta_emocionado' : True,
     'altura' : 1.84,
     'dato_duplicado' : 'Soy lucas'             
} 

print(diccionario["altura"])

#type() nos sirve para saber el tipo de dato que es 

tipoDato=type(conjunto)
print(tipoDato)