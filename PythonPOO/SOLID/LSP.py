"""
LSP=Liskov's sustitution principle
Principio de sustitución de Liskow
Las class derivadas tienen que ser sustituibles por su clase base

"""

# class Ave():
#     def volar(self):
#         return "Estoy volando"
        
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"


# def hacer_volar(ave=Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
class AveNoVolador(Ave):
    pass

"""
En la clase Ave deberiamos especificar todas las caracteristicas y funciones entre
las aves que pueden volar y no, y las que vuelan deben tener caracteríticas especificas
en su clase AveVoladora y NoVoladora, esto quiere decir que debemos asegurarnos de que
la clase base debe tener todas las características comunes de las clases que herederan de esta
"""