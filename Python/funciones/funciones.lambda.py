
numeros=[1,2,3,4,5,6,7,8,9]

#Lambda nos permite simplificar la función sin tener la necesidad de colocar el return
multiplicando=lambda x : x*2
print(multiplicando(8))

def multiplicar(x):
    return x*2 
print(multiplicar(5))

#Creando función común que diga si es par o no
def esPar(num):
    if(num%2==1):
        return True
    
#Usando filter con una función común
nPar =filter(esPar,numeros)
print(list(nPar))

