#Calcular la suma de tres números e incluir una condicion de igualdad

def sumar(a,b,c):
    suma=a+b+c
    if(a==b==c):
        suma*=3
        return suma
    else:
        return suma
    
a=sumar(3,4,5)
print(a)

b=sumar(4,4,4)
print(b)