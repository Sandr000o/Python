
import pandas as pd

#Usando la función read_csv para leer el archivo csv
archivo=pd.read_csv("archivos\\UTP-RNA_EPI.csv")
print(archivo)

archivo2=pd.read_csv("archivos\\datos.csv")

#Mostramos solo la columna que queremos
df=pd.read_csv("archivos\\UTP-RNA_EPI.csv")
print(df["EMAIL"])

#Asignando nombres a los encabezados de las columnas
asig=pd.read_csv("archivos\\UTP-RNA_EPI.csv",names=["APELLIDOS","NOMBRES","EMAIL","TELEFONO","DISTRITO","GRUPO"])
print(asig)

#Definimos del punto de inicio y final de lo que queremos mostrar
cadena="abcdefghijklmnopqrstuvwxyz".upper()
print(cadena[0:4])

#Ordenando el dataframe por los grupos
#ascending nos sirve para establecer si se hace de forma ascendente o descendente de acuerdo al valor que le coloquemos
dfOrdenado=df.sort_values("GRUPO",ascending=True)
print(dfOrdenado)

#Concatenamos 2 dataframes
dfConcatenado=pd.concat([archivo,archivo2])
print(dfConcatenado)

#Accediendo a las filas empezando por el inicio
primerasFilas=archivo.head(1)
print(primerasFilas)

#Accediendo a las filas empezando por el final
ultimasFilas=archivo.tail(1)
print(ultimasFilas)

#Accediento a la cantidad de filas y columnas que tiene el dataFrame
filasColumnas=archivo.shape
filas,columnas=filasColumnas
print(f"Cantidad de filas : {filas}\nCantidad de columnas : {columnas}")

#Obtener datos estadísticos del dataframe
dfInfo=archivo.describe()
print(dfInfo)

#Accediendo a un elemento especifíco del dataframe con loc
elementoEspecificoLoc=archivo.loc[:,"NOMBRES"]
print(elementoEspecificoLoc)

#Accediendo a un elemento específico del dataframe con iloc
elementoEspecificoILoc=archivo.iloc[2,3]
print(elementoEspecificoILoc)

#Accediendo a todos los apellidos con loc
apellidos=archivo.loc[:,"APELLIDOS"]
print(apellidos)

#Accediendo a todos los nombres con iloc
nombres=archivo.iloc[:,1]
print(nombres)

#Accediendo a las filas con el número de grupo mayor a 4
grupos=archivo.loc[archivo["GRUPO"]>4,:]
print(grupos)

