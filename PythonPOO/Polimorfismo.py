
class Gato():
    def sonido(self):
        return 'Miau'
    

class Perro():
    def sonido(self):
        return 'Wuao'
    
gato=Gato()
perro=Perro()

def hacer_sonido(animal):
   return animal.sonido()

print(hacer_sonido(perro))

num1=3
num2=4.4

resultado=num1+num2
print(resultado)
print(type(num1))
print(type(num2))
print(type(resultado))


def recorrer(elemento): 
    for i in elemento:
        print(i)
        
lista1=[1,2,3,4,5]
lista2=["hola","maquina"]
texto="Escamilla"

recorrer(lista2)

