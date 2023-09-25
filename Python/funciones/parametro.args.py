
#Forma no óptima de sumar valores
def suma(lista):
    sumados=0
    for numero in lista:
        sumados+=numero
    return sumados

r1=suma([4,8,5,10,20])
print(r1)

#Forma óptima para sumar utilizando el parámetro args
def sumar(*numeros):
    return sum(numeros)
    
r2=sumar(4,5,6,7,8,9)
print(r2)