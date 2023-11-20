#Obtener la representación inversa de una cadena de caracteres

def cadenaInversa(texto):
    for i in range(len(texto)-1,-1,-1):
        print(texto[i],end="")
        
cadena="Python"
print(cadena[::-1])
    