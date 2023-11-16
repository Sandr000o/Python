
#Funciones integradas por python
numeros=[4,7,1,42,15]

#Encontrando el número mayor de una lista
nMayor=max(numeros)
print(nMayor)

#Encontrando en el número menor de una lista
nMenor=min(numeros)
print(nMenor)

#Redondeando a 6 decimales
numero=round(12.345678,2)
print(numero)

#Retorna False ->0, vacío , False, ninguno,None | True, cadena, datos no vacios
r1=bool("")
print(r1 )
r2=bool(["Hola"])
print(r2)

#Retorna True, si todos los valores son verdaderos 
rAll=all([r1,r2])
print(rAll)

#Suma total de los valores de un iterable
sTotal=sum(numeros)
print(sTotal)