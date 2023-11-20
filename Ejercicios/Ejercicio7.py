#Obtener la extensión de un archivo especificado por el usuario
import sys
nombre_archivo=input("Ingrese el nombre del archivo : ")
separador=nombre_archivo.split(".")
print("La extensión del archivo es :",f".{separador[-1]}")