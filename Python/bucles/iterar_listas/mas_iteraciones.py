
frutas=["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena="Hola"
numeros=[2,5,8,10]

#Evitando que se coma una banana con la sentencia continue
for fruta in frutas:
    if(fruta=='banana'):
        continue 
    print(f"Me voy a comer una {fruta}")
    
#Evitar que el bucle siga ejecutandose, el else no se ejecuta tampoco después del break
for fruta in frutas:
    if(fruta=='naranja'):
        break 
    print(f"Me voy a comer una {fruta}")
    print("Ya no puedes seguir comiendo porque le hizo daño la naranja")
    
#Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#For en una sola línea de código, esta no es la forma correcta
numerosDuplicados = list()
for numero in numeros:
    numerosDuplicados.append(numero*2)
print(numerosDuplicados) 

#Forma correcta
numero_duplicados=[x*2 for x in numeros]
print(numero_duplicados)
