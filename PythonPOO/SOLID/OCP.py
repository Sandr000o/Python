"""
OCP=Opened/Closed participle
Este princicipio debe permitirnos agregar mas funcionalidades
pero no modificar las que ya existen

"""
class Notificador():
    def __init__(self,usuario,mensaje):
        self.usuario=usuario
        self.mensaje=mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")
        
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.SMS}")
        
class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.whatsapp}")
        
class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.twitter}")

"""
En este caso la clase notificar nos indica que se debe enviar un mensajes de alguna
forma, si no usaramos el principio SOLID tendríamos que estar modificado la función
en lugar de eso creamos clases que hereden de la clase principal y vamos modificando las
funciones en cada clase

"""