with open('archivos\\texto.txt','a',encoding='UTF-8')as archivo:
    #Agregando texto al archivo
    archivo.writelines("\nAgregando línea con append")
    for i in range(5):
        archivo.writelines(f"\nAgreando linea {i+1} con Append")