
def Calcular (a,b,ope):
    
    a=int(a)
    b=int(b)
    ope=ope.lower()
    if(ope=="sumar"):
        r=a+b
    elif(ope=="restar"):
        r=a-b
    elif(ope=="dividir"):
        if(b==0):
            return "No se puede dividir entre 0"
        else:
            r=a/b
    elif(ope=="multiplicar"):
         r=(a*b)
    else:
        return f"No se puede realizar la operación de {ope}, no es válida"

    ope=ope.capitalize()
    return f"El resultado de {ope} es {r}"
