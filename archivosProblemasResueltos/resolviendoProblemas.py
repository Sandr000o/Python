#2 Listas una con nombres y una con apellidos

nombres=["Lucas","Matías","Camila","Pedro","Roberto"]
apellido=["Dalto","Zing","Dalto","Robetix","TARADO"]

#Registrar esta información en un txt
with open("archivosProblemasResueltos\\nombresyapellidos.txt","w",encoding="UTF-8") as archivo:
    archivo.writelines("Los datos son : \n")
    for n,a in zip(nombres,apellido):
        archivo.writelines(f"Nombre : {n}\nApellidos : {a}\n--------------------\n")
        