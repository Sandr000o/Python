#Imprimir calendario para un año y mes específico

import calendar

agnio=int(input("Introduzca el año : "))
mes=int(input("Introduzca el mes : "))

print(calendar.month(agnio,mes))