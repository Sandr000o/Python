class MiClase():
    def __init__(self):
        self._atributo_privado="Valor"
        self.__atributo_muy_privado="Muy valor"
        
    def getValor(self):
        print(self.__atributo_muy_privado)
        
    def setValor(self,nuevo_atributo):
        self.__atributo_muy_privado=nuevo_atributo
        
objeto=MiClase()
print(objeto._atributo_privado)
objeto.getValor()
objeto.setValor("Nuevo muy valor")
objeto.getValor()