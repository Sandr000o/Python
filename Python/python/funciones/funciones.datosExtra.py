def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'

r=frase("Sandro","Reyes","Capo")
print(r)

#Utilizar keywords arguments
r2=frase(apellido="Reyes",nombre="Sandro",adjetivo="Crack")
print(r2)

#Definir argumentos 
def frase2(nombre,apellido,adjetivo="tonto"):
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'
r3=frase2("Sandro","Reyes")
print(r3)