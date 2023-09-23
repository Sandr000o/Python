
cadena1="Hola+soy sandro"
cadena2="hola"

#Metodo para volver a mayuscula una cadena de texto

r1=cadena1.upper()
print(r1)

#Método para volver a minúscula una cadena de texto

r2=cadena2.lower()
print(r2)

#Método para solo colocar el primer carácter a minúscula

r3=cadena2.capitalize();
print(r3)

#Método para contar la cantidad de carácteres que ingresemos a buscar
r4=cadena1.count("a")
print(r4)

#Método para que me devuelva el indice donde se encontro el valor que ingrese a buscar
r5=cadena1.index("a")
print(r5)

#Método para remplazar un carácter o una cadena por otra
r6=cadena1.replace("H","C")
print(r6)


#Método para convertir en una lista un cadena, si no se le pasa cual sera el caracter de separación por defecto es el espacio

r7=cadena1.split(" ")
print(r7)

#Función para contar la cantidad de carácteres de una cadena

r8=len(cadena1)
print(r8)
