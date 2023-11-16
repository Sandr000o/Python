import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el archivo con pandas
archivo=pd.read_csv("ProblemasGraficos\\dispersion.csv")

#Definimmos el tipo de grafico, además del valor del eje X e Y y la fuente de información con seaborn
#En este caso scatterplot es un gráfico de dispersión
sns.scatterplot(x="tiempo",y="dinero",data=archivo)

#Mostramos el grafico con matplotlib

plt.show()