#Valores de una lista
vocabulario=["mejorar","castigar","defenestrar"]
numeros=[17,123]
vacio=[]

print(vocabulario,numeros,vacio)

#Acceso a elementos
numeros[1]=5
print(numeros[3-2])

jinetes=["guerra","hambre","peste","muerte"]
i=0
while(i<len(jinetes)):
    print(jinetes[i])
    i+=1
    
#Longitud (tamaño) de una lista
tamaño=len(jinetes)
print(tamaño)
    
lista=["spam!",1,["Brie","Roquefort","Pol le vaq"],[1,2,3,4,5,6]]
print(len(lista))
j=0
while(j<len(lista)):
    print(len(lista[3]))
    j+=1

#. ¿que ocurre si envıa un entero a len? , da error ya que no un int no tiene longitud

#Pertenencia a una lista

print("peste" in jinetes)
print("libertinaje" in jinetes)
print("libertinaje" not in jinetes)

#Listas y bucles for

for jinete in jinetes:
    print(jinete)
    
for numero in range(20):
    if(numero%2==0):
        print(numero)

for fruta in ["platano","manzana","membrillo"]:
    print("Me gustan las "+fruta+"s")
    

#Operaciones con listas

a=[1,2,3]
b=[4,5,6]
c=a+b

print(c)

c[0]*4
print(c)

#Porciones
lista=["a","b","c","d","e","f"]
print(lista[1:3])
print(lista[:4])
print(lista[3:])
print(lista[:])

#Las listas son mutables
fruta=["plátano","manzana","membrillo"]
fruta[0]="pera"
fruta[-1]="naranja"
print(fruta)

lista[1:3]=["x","y"]
print(lista)

lista[1:3]=[]
print(lista)

lista[1:1]=["b","c"]
print(lista)

lista[6:6]=["g","h"]
print(lista)

#Borrando una lista
a=["uno","dos","tres"]
del a[1]
print(a)

del lista[1:4]
print(lista)

#Objetos y valores
a="banana"
b="banana"
print(id(a))
print(id(b))

a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))

#Alias
a=[1,2,3]
b=a
b[1]=5
print(a)

#Clonar listas
a=[1,2,3]
b=a[:]
b[1]=5
print(a)
print(b)

#Listas como parámetros

def cabeza(lista):
    return lista[0]

numeros=[1,2,3]

print(cabeza(numeros))

def borraCabeza(lista):
    del lista[0]
    
print(numeros)

def cola(lista):
    return lista[1:]

resto=cola(numeros)
print(resto)

resto[2:2]=[5]

print(resto)
print(numeros)

#Listas anidadas

lista=["Hola",2.0,5,[10,20]]
print(lista[3][:])
elt=lista[3]
print(elt[0])

#Matrices
matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz[1])

#Cadenas y listas
cancion="La lluvia de sevila..."
separacion=cancion.split("via")
print(separacion)

print(separacion.join("-"))

