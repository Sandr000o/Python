with open("archivos\\texto.txt","w" ,encoding="UTF-8") as archivo :
    #SobreEscribimos el archivo, con el permiso w, si no existe el archivoe, este lo crea
    # archivo.write("Uno Dos Tres Rational Software Architect")
    
    archivo.writelines(["\n-Hola maestro como andas","\n-bien po"])
    archivo.writelines(["\n-Que bueno maestrazo","\n-Vamos a comer"])
    for i in range(5):
        archivo.writelines(f"\nLinea {1+i}")
    