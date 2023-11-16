#Abriendo el archivo con with open
with open("archivos\\texto.txt",encoding="UTF-8") as archivo:
    #Asginamos el contenido a una variables
    contenido=archivo.read()
    #Mostramos el archivo en pantalla
    print(contenido)
    
    