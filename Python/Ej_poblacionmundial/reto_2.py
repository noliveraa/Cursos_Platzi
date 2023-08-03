'''
RETO 2: tenemos en un CSV informacion sobre la poblacion mundial por pais.
Hay una columna que indica que porcentaje de la poblacion mundialrepresenta cada pais. 
Debemos graficar en forma de pie esta información
'''

import csv
import functools
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
 


#creo una lista que contenga [{'Country': 'Afghanistan', 'Percentage': '0.52'}, {'Country': 'Albania', 'Percentage': '0.04'}, {'Country': 'Algeria', 'Percentage': '0.56'}, {'Country': 'American Samoa', 'Percentage': '0'},
#Nota: esto no es necesario pero lo dejo aca para que no se me olvide como lo hice :)
percentage_country_data = []

for country_data in data:
    next_country = {
        'Country': country_data['Country/Territory'],
        'Percentage': float(country_data['World Population Percentage'])
        }
    percentage_country_data.append(next_country)


#2. crear un array solo de paises y otro solo de porcentajes, 

countries = []
percentages = []

for country_data in data:
    countries.append(country_data['Country/Territory'])
    percentages.append(float(country_data['World Population Percentage']))

'''
Lo anterior el profe lo hizo con lamda y map mucho mas reducido asi:

countries = list(map(lambda x:x['Country/Territory'], data))
percentages = list(map(lambda x:x['World Population Percentage'], data))
'''

# Organizar los datos de mayor a menor porcentaje utilizando la función sorted()
sorted_data = sorted(zip(countries, percentages), key=lambda x: x[1], reverse=True)

#hacer un array solo con los primeros 10 datos
first15=[]
for i in range (0,15):
    first15.append(sorted_data[i])


#separo de los ahora filtrados paises y porcentajes
first15_countries = [tupla[0] for tupla in first15]
first15_percentages = [tupla[1] for tupla in first15]


#sumo cuanto representa en porcentaje los otros paises que no estan en la lista de 10 

otros = 100-functools.reduce(lambda x,y: x+y, first15_percentages )

first15_countries.append('Otros')
first15_percentages.append(otros)


#3. grafico

fig, ax = plt.subplots()
ax.pie(first15_percentages, labels=first15_countries)
ax.axis('equal')



fontsize='3.5' 
label_distance = 0.7

plt.show()
