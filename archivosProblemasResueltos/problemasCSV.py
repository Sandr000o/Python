import pandas as pd
archivo=pd.read_csv("archivos\\datos.csv")
print(archivo)

#Cambiar tipo de dato de una columna
#Convirtiendo a str los datos de la columna edad
archivo['edad']=archivo['edad'].astype(str)

#Mostrar el tipo de dato del primer elemento de la columna edad
print(archivo['edad'][0])

#Reemplazar valores , reemplazamos dalto con 
archivo['apellido'].replace("dalto","NoMaestro",inplace=True)
print(archivo)

#Eliminar filas que tiene datos vacíos
archivo=archivo.dropna()
print(archivo)

#Eliminar filas repetidas
archivo=archivo.drop_duplicates()
print(archivo)

#Crear un CSV con el dataframe resultante(limpio)
archivo.to_csv("archivosProblemasResueltos\\datosLimpios.csv")
 