
lista=["Hola soy dalto","Soy Dalto",True,1.85]

#Método para agregar un elemento al final de la lista

lista.append("Tu mama")

print(lista)

#Método para contar la cantidad de veces que se encuentra el elemento que le indicamos
r2=lista.count("Soy Dalto")
print(r2)

#Función para contar los elementos de la lista
r3=len(lista)
print(r3)


#Método para ingresar un elemento colocandole el índice en que querremos que se coloque
lista.insert(2,"Este es el índice 2")
print(lista)

#Metódo para eliminar los elementos de acuerdo al índice, si quieres empezar a eliminar desde el último empiezas con el -1,-2 y así sucesivamente
lista.pop(-1)
print(lista)

#Método para eliminar un elemento indicandole el valor que querremos eliminar
lista.remove(True)
print(lista)

#Método para ordenar los elementos de mayor a menor, solo número y TRUE=1,FALSE=0;
lista2=[True,29,21,3,14,56,False]
lista2.sort()
print(lista2)

#Método para ordenar los elementos de mayor a menor (Solo números)

lista2.sort(reverse=True)
print(lista2)

#Método para invertir la posición de elementos, no los ordena, solo invierte la posición, aca no importa el tipo de elemento que sea

lista.reverse()
print(lista)

#Método para agregar más de un elemento a la vez como lista
lista.extend(["Agregar","Lista"])
print(lista)

#Método para eliminar todos los datos de la lista
#lista.clear();
print(dir(("adad",4)))