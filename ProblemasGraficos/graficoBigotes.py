import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el archivo con pandas
archivo=pd.read_csv("ProblemasGraficos\\bigotes.csv")

#Definimmos el tipo de grafico, además del valor del eje X e Y y la fuente de información con seaborn
#En este caso boxplot es llamado gráfico de bigotes
sns.boxplot(x="categoria",y="valor",data=archivo)

#Mostramos el grafico con matplotlib

plt.show()