#Crear una funcion para determinar si un número es cercano a 1000 ó 2000

def determinar(numero):
    d1=abs(2000-numero)
    d2=abs(1000-numero)
    if(d1<d2):
        return("Esta más cerca de 2000")
    elif(d1>d2):
        return "Esta mas cerca de 1000"
    else:
        return "Se encuentra igual de cerca para ambos"
    
resultado=determinar(1500)
print(resultado)