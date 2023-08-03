'''
RETO: tenemos en un CSV informacion sobre la poblacion mundial por pais. lo pasamos a un diccionario. 
a partir de ese diccionario debemos hacer otro que solo contenga nombre de pais y poblacion por año.
Esta es la informacion que queremos graficar
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

#1. traigo el csv y lo convierto en una lista de diccionarios llamada "data"
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') #indico que los datos estan separados por comas
    header = next(reader) #esto me saca un array con solo los titulos de cada columna
    data = []
    for row in reader:
      iterable = zip(header, row) #uno el header con su row en tuplas es decir [(titulo de la columna , valor correspondiente), (titulo columna 2, valor correspondiente)...][(titulocolumna, valor),(titulo columna, valor)...][..datos de la siguiente fial.][.datos de otra fila..] 
      country_dict = {key: value for key, value in iterable} #genero un diccionario "country dict"
      data.append(country_dict)
    return data
if __name__ == '__main__':
  data = read_csv('./Python/data.csv')
 
#2. Selecciono que pais quiero graficar 
study_country = 'China'

#3. traigo de data el diccionario correspondiente solo al pais seleccionado 
#Nota: los datos los multiplico por 0.000001 para dejarlos en terminos de millones para que la grafica quede más clara
study_country_data = {}

for country_data in data:
    if country_data['Country/Territory'] == study_country:
        study_country_data = {
            '1970': (int(country_data['1970 Population'])*1e-6),
            '1980': (int(country_data['1980 Population'])*1e-6),
            '1990': (int(country_data['1990 Population'])*1e-6),
            '2000': (int(country_data['2000 Population'])*1e-6),
            '2010': (int(country_data['2010 Population'])*1e-6),
            '2015': (int(country_data['2015 Population'])*1e-6),
            '2020': (int(country_data['2020 Population'])*1e-6),
            '2022': (int(country_data['2022 Population'])*1e-6),
        }



#4. usando los métodos keys and values hago una lista o array con solo los datos de los años para que esten en mi eje x y la poblacion para que este en y
labels = study_country_data.keys()
values = study_country_data.values()

#5. grafico
fig, ax = plt.subplots()
ax.bar(labels,values,color='#FFC6AC') #color de las barras
#quitar bordes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

plt.tick_params(left = False, bottom = False) #quitar los palitos que salen con los labels
plt.xticks(fontsize='8.5', weight='bold', color='#7e807e') #indicar caracteristicas para los labels
plt.yticks(fontsize='8.5', weight='bold', color='#7e807e')
ax.set_xlabel("Año", labelpad=18, size=10, fontfamily="sans", color='#7e807e') #pone los labels en los ejes 
ax.set_ylabel("Población (Millones)", labelpad=18, size=10, fontfamily="sans", color='#7e807e')
plt.title("Crecimiento poblacional de " + study_country , size=17, weight='bold', fontfamily="serif", color='#9E9FA5', horizontalalignment = 'center') #el titulo del gráfico

plt.show()


