import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("ProblemasGraficos\\pedos.csv")
sns.lineplot(x="fecha",y="pedos",data=df)
plt.plot("01-09",17,"o")
plt.show()