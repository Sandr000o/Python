import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leyendo el archivo con pandas
archivo=pd.read_csv("ProblemasGraficos\\coflaIngresos.csv")

#Asignadole los valores de X e Y y de donde extrae la info usando seaborn
sns.barplot(x="fuente",y="ingresos",data=archivo)

ingresosTotales=archivo["ingresos"].sum()

#Mostrando el total de ingresos
print("EL total de ingresos es ",ingresosTotales)
#Mostrando el gráfico usando matplotlib .pyploy
plt.show()
