"""
DIP=Dependency inversion principle
Los módulos de alto nivel no deben depender de los módulos de bajo nivel
Las abstracciones no deben depender de los detalles
Los detalles deben depender de las abastracciones
"""

# class Diccionario():
#     def verificar_palabra(self,palabra):
#         #Lógica para verificar palabras
#         self.palabra=palabra
    

# class CorrectorOrtografico():
#     def __init__(self):
#         self.diccionario=Diccionario()
        
#     def corregir_texto(self,texto):
#         #Usamos el diccionario para corregir el texto
#         pass
    
        
"""
La clase más importante en este caso es CorrectorOrtografico() y no Diccionario()

"""

from abc import ABC,abstractmethod

class VerificarOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass
    
class Diccionario(VerificarOrtografico):
    #Lógica para verificar palabra si está en el diccionario
    def verificar_palabra(self, palabra):
        pass
        
        
class ServicioOnline(VerificadorOrtografico):
    def verificar_pálabra(self,palabra):
        #Lógica para verificar palabra si está en el diccionario 
        pass
    
class VerificadorOrtografico():
    def __init__(self,verificador):
        self.verificador=verificador
        
    def corregir_texto(self,texto):
        #Usamos verificador para corregir el texto
        pass
    
        