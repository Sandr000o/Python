#Obtener un conjunto de números separadaos por coma y crear una lista

def crearLista(cadena):
    separado=cadena.split(",")
    print(type(separado))
    print(separado)
    
numeros=input("Escribar varios números separados por ',' : ")

crearLista(numeros)