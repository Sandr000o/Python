#Obtener fecha y hora del sistema
import datetime

ahora=datetime.datetime.now()

print(ahora)

print(ahora.strftime('%d/%m/%y %H:%M:%S'))