
#Clases con atributos 
class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara
    
    def llamar(self):
        print(f"Llamando desde un {self.modelo}")
    
    def cortar(self):
        print(f"Cortando desde un {self.modelo}")
    
celular1=Celular("Samsung","S23","48MP")
celular2=Celular("Apple","Iphone 15 pro","96MP")

celular1.llamar()

 
#Mamifero

class Animal:
    def comer(self):
        return f'El animal esta comiendo'
    
class Mamifero(Animal):
    def amamantando(self):
        return f'El animal esta amamantando'

class Ave(Animal):
    def volando(self):
        return f'El animal esta volando'
    
class Murcielago(Mamifero,Ave):
    pass

m=Murcielago()

print(m.comer())
print(m.amamantando())
print(m.volando())

print(Murcielago.mro())