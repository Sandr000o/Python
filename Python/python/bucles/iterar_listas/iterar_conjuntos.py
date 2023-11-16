
animales={"perro","gato","cocodrilo","loro","pez"}
numeros={10,23,25,14}
celulares={"S21","14Pro","LG","Xiaomi"}

#
for numero,animal,celular in zip(animales,numeros,celulares):
    print(f"recorriendo la lista 1 : {numero}")
    print(f"recorriendo lista 2 : {animal}")
    print(f"recorriendo lista 3 : {celular}")
    
#Iterar un rango, si le pasas 2 parametros empieza en el primero y termina en el segundo
#Si solo le pasas uno empieza desde el 0 a uno menos que el número que le indicaste
#No funciona en conjuntos
for num in range(6):
    print(num) 
    
#Forma correcta de recorrer un conjunto con su índice
#Al hacer esto num se convierte en una tupla donde asocia un indice a los elementos de la lista
#Empezando desde 0
#Con esto se puede iterar listas,conjuntos,tuplas
for num in enumerate(animales):
    indice=num[0]
    valor= num[1]
    print(f"Indice {indice} valor {valor}")
    
#Usando el for/else
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual : {numero}")
else:
    print("El bucle ya termino")