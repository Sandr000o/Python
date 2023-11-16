import calculadora as calcu

a=input("Ingrese el primer valor : ")
b=input("Ingrese el segundo valor : ")
ope=input("Elija la operación, 1)Sumar 2)Restar 3)Dividir 4)Multiplicar : ")

r=calcu.Calcular(a,b,ope)
print(r)

import saludar as salu
nom=input("Ingresa el nombre : ")
print(salu.Saludo(nom))