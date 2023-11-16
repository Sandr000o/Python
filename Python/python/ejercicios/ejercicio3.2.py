
primos=[]
c=input("Ingrese el límite de primos ")

def esPrimo(c):
    for i in range(2,c):
        if c%i==0 :return False
    return True

def primosHasta(c):
    primos=[]
    for i in range(2,int(c)):
        resultado=esPrimo(i)
        if(resultado==True):
            primos.append(i)
    return primos

resultado=primosHasta(c)
print(resultado)