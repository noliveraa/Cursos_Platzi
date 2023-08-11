import matplotlib.pyplot as plt
import numpy as np
'''
#GRAFICA DE BARRAS
labels = ['a','b','c']
values = [100,200,80]

fig, ax = plt.subplots()
ax.bar(labels,values)
plt.show()
'''

#PIE 
labels = ['a','b','c']
values = [100,200,80]

fig, ax = plt.subplots()
ax.pie(values, labels=labels)
ax.axis('equal')

#plt.show()
plt.savefig('/root/Cursos_Platzi/Python/pie.png')
plt.close()