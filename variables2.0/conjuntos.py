
#Creando un conjunto con set
#Solo podemos meter tuplas dentro de un conjunto ya que no se puede manipular los datos al igual que en este
#A diferencia de lista y diccionarios que si permiten la manipulación
conjunto= set(["Dato1",("Datoenlista1","Datoenlista2")])
print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
#Se tiene que usan frozenset par crear un conjunto congelado
conjunto1=frozenset(["dato1","dato2"])
conjunto2={conjunto1,"dato3"}
print(conjunto2)

#Teoría de conjuntos 

conjunto3={1,3,5,7}
conjunto4={1,3,7}

#Verificamos si conjunto4 es subconjunto de conjunto3
resultado=conjunto4.issubset(conjunto3)
print(resultado)

#Otra forma es la siguiente
r2=conjunto4 <= conjunto3
print(r2)


#Verificamos si conjunto3 es superconjunto de conjunto4
r=conjunto3.issuperset(conjunto4)
print(r)

#Otra forma es la siguiente
r3=conjunto4 <= conjunto3
print(r3)

#Verificar si un conjunto tiene almenos un elemento en común con otro
r4=conjunto4.isdisjoint(conjunto1)
print(r4)