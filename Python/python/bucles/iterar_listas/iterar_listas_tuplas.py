
animales=["perro","gato","cocodrilo","loro","pez"]
numeros=[10,23,25,14]
celulares=["S21","14Pro","LG","Xiaomi"]

#Los métodos también funcionan con tuplas
#La variable animal solo existen dentro del bloque del for
for animal in animales:
     print(f"Ahora la variable animal almacena el valor {animal} ")
     
for num in numeros:
    resultado=num*10
    print(f"El {num} multiplicado por 2 es igual a : {resultado}")

#Función para iterar 2 listas, ambas listas deben tener la misma cantidad de elementos
#De lo contrario solo iterara la cantidad de veces en que ambas coincidan
#Osea que si uno tiene 4 elemento y el otro 5 solo mostrara 4 elementos en ambos

for numero,animal,celular in zip(animales,numeros,celulares):
    print(f"recorriendo la lista 1 : {numero}")
    print(f"recorriendo lista 2 : {animal}")
    print(f"recorriendo lista 3 : {celular}")
    
#Iterar un rango, si le pasas 2 parametros empieza en el primero y termina en el segundo
#Si solo le pasas uno empieza desde el 0 a uno menos que el número que le indicaste
for num in range(6):
    print(num)
    
#Forma no óptima para recorres listas
for num in range(len(celulares)):
    print(celulares[num])
    
#Forma correcta de recorrer una lista con su índice
#Al hacer esto num se convierte en una tupla donde asocia un indice a los elementos de la lista
#Empezando desde 0
for num in enumerate(animales):
    indice=num[0]
    valor= num[1]
    print(f"Indice {indice} valor {valor}")
    
#Usando el for/else
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual : {numero}")
else:
    print("El bucle ya termino")