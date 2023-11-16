class Animal():
    def comer(self):
        print("Estoy comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Estoy amamantando")
    
class Ave(Animal):
    def volar(self):
        print("Estoy volando")
        
class Murcielago(Mamifero,Ave):
    pass
m=Murcielago()
m.amamantar()
m.comer()
m.volar()

    