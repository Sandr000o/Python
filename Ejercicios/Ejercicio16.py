#Crear una función para evaluar un número y realizar una operación

def diferencia(numero):
    if(numero<=15):
        resultado=(15-numero)
        return(resultado)
    else:
        resultado=pow((15-numero),2)
        return resultado
        
resultado=diferencia(12)
print(resultado)
