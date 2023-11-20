#Exponer el uso básico de la funcion print

print("Este es un ejemplo básico")
print("Sirve para ver en consola", end=" ")
print("Como pusimos end=' ' ya no tiene salto de línea ")
print("Las comas","colocan un espacio","entre cada cadena de texto","por defecto")
print("Con el atributo sep='-'","podemos establecer que ira","entre cada cadena",sep="-")
print('{} es {}'.format('Python','Tremendo!'))

numeros=[2,3,5,7,11]

print(numeros)

capitales={'Colombia':'Bogota',
           'Peru':'Lima',
           'Ecuador':'Quito',
           'Bolivia':'La paz',
           'Argentina':'Buenos aires'}

print(capitales)