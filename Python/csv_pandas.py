#PANDAS: Es una herramienta para lectura de archivos tipo csv 

import pandas as pd
import matplotlib.pyplot as plt



df =pd.read_csv('/root/Cursos_Platzi/Python/data.csv') # df es data frame
df =df[df['Continent']=='South America']

countries =df['Country/Territory'].values
percentages = df['World Population Percentage'].values


#Grafico

fig, ax = plt.subplots()
ax.pie(percentages, labels=countries)
ax.axis('equal')

fontsize='3.5' 
label_distance = 0.7

plt.savefig('/root/Cursos_Platzi/Python/population_perc_SouthAmerica.png')
plt.close()
