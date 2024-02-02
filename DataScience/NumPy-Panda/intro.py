import numpy as np


'''############################### NumPy ##############################'''

'''El array es el principal objeto de la librería. Representa datos de manera estructurada y se puede acceder a ellos a traves del indexado, a un dato específico o un grupo de muchos datos específicos.'''
'''yo creo una lista o una matriz y la paso a Numpy asi:'''
lista = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
print(lista)

arr = np.array(lista)
print(type(arr))


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(matriz)
print(matriz)

'''INDEXADO: nos permite acceder a los elementos de los array y matrices'''
print(arr[0])
print(matriz[0])
print(matriz[0,2])

'''SLICING: "Cortar una parte de ese array'''
print(arr[1:6])


'''TIPOS DE DATOS'''

'''NOTA:cada array tiene un solo tipo de dato'''
'''Cpomo saber que tipo de dato tengo'''
print(arr.dtype)

'''Puedo definir ese tipo de dato desde el inicio'''
arr=np.array([1,2,3,4],dtype='float64')
print(arr.dtype)
arr= arr.astype(np.float64)



'''DIMENSIONES'''
'''Hablamos de un escalar cuando es una dimension o un vector, tenemos matrices cuando son de dos (las tablas son matrices) y Tensores cuando tengo mas requiero por lo general una tercera dimension cuando hablo de tiempo'''

'''Puedo preguntar cuantas dimensiones tienen los datos con .ndim "numero de dimensiones": '''
arr.ndim

'''puedo expandir las dimensiones que tiene lo que estoy manejando'''
vectorexpandido=np.expand_dims(np.array([1,2,3]),axis=0)
print(vectorexpandido)
'''puedo reducir un vector a sus necesarias dimensiones'''
vectorreducido=np.squeeze(vectorexpandido)
print(vectorreducido)


'''Crear arrays segun periocidad'''
arr= np.arange(0,10) ## array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr= np.arange(0,20,2) ##array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
arr= np.zeros(3) #array([0., 0., 0.])
matriz= np.zeros((10,5))  #array([[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.],[0., 0., 0., 0., 0.]])
arr= np.linspace(0,10,15)# crea un array de 0 a 10 con 15 datos
matriz= np.eye(4)#crea una matriz con diagonal de 1 el resto en cero
num= np.random.rand() #genera numero random
arr= np.random.rand(4)#genera un vector de 4 numeros random 
matriz= np.random.rand(4,4) #genera un matriz de 4 numeros random por 4
numint= np.random.randint(1,15)# numero entero random entre 1 15
matrizint= np.random.randint(1,15,(3,3))#Matriz de numeros enteor random 


'''RESHAPE''' 
arr=np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
arr.shape #(3,4)

arrf= np.reshape(arr,(4,3),'F')# Lenguaje C: lo hace por columnas [[11 22 33],[21 32 14],[31 13 24], [12 23 34]]
arrc=np.reshape(arr,(4,3),'C')# Lenguale Fortran: lo hace por filas [[11 12 13],[14 21 22],[23 24 31],[32 33 34]]

'''FUNCIONES PRINCIPALES'''
arr = np.array([6,11,15,12,9,17,7,7,12,3])
matriz = arr.reshape(2,5) #array([[ 6, 11, 15, 12,  9],[17,  7,  7, 12,  3]])

#puedo sacar la transpuesta de una matriz 
print(matriz.T)

#MAX MIN
arr.max() #17
matriz.max() #17
matriz.max(1) #UNO indica el  max en las filas ---> array([15, 17])
matriz.max(0) #Cerp indica el max por fila ---> array([17, 11, 15, 12,  9])
arr.argmax() #nos regresa la posicion de ese valor max ---> 9
arr.ptp() # 17 - 3 ---> 14 #Podemos saber la distancia entre el valor más bajo con el más alto.

#Análisis estadístico
arr.sort()#ordena los elementos
np.percentile(arr, 50) #obtener un percentil ---> 10.0
np.median(arr) #Mediana ---> 10.0
np.std(arr) #Desviación estandar ---> 4.0853396431631
np.var(arr) #Varianza ---> 16.69
np.mean(arr) #Promedio ---> 9.9

#Concatenar
a=np.array([1,2,3])
b=np.array([1,2,3])
c=np.concatenate((a,b),axis=0)
#Nota: los array en este caso se pueden concatenar pues tienen la misma dimension



'''COPY'''
#Copy es necesario pues cuando yo edito un array creado a partir de otro este se va a editar tambien. 
#Si yo no quiero modificar el origianal debo crear una copia

arrnuevo = arr.copy()

'''Condiciones'''
#Me permite hacerconsultas especificas "Ej dentro de este array sacame los que son >5 y <9 asi:"
arr = np.linspace(1,10,10, dtype = 'int8') #array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int8)
arr[(arr > 5) & (arr < 9)] #array([6, 7, 8], dtype=int8)
# y modificar los valores que cumplan esa condicion
arr[arr > 5] = 99  #[ 1  2  3  4  5 99 99 99 99 99]
print(arr)
# Sacar solo los numeros pares:
pares = arr[(arr % 2 == 0)] #array([ 2,  4,  6,  8, 10], dtype=int8)
print(pares)

'''OPERACIONES MATEMÁTICAS'''
#Si yo le digo a python que a=array*2 el toma el array y lo reescribe haciendo que quede dos veces no se mete directamente con los valores de ese array
#en numpy toma cada valor de ese array y lo multiplica por dos. esto permite hacer operaciones matemáticas a multiples datos 
arr = np.linspace(1,10,10, dtype = 'int8') #[ 1  2  3  4  5  6  7  8  9 10]
arroperaciones = arr*2 #[ 2  4  6  8 10 12 14 16 18 20]

#Nota: si divido entre cero el campo me lo marca en el array como inf y me saca un problema pero no detiene la operacion 

'''Operaciones con Matrices'''
A = np.array([[2, 4], [-1, 2]])
B = np.array([[-1, 3], [-3, 6]])
np.matmul(A, B) #multiplicacion de matrices
Ainversa = np.linalg.inv(A) #Matriz inversa





'''############################### PANDA ##############################'''

'''Panda: maneja 
   - series que son como vectores, indexados 
   - Data frames que son como Matrices con indices'''
import pandas as pd

#Series
psg_players = pd.Series(['Navas','Mbappe','Neymar','Messi'], index=[1,7,10,30])
print(psg_players)
psg_players[7]
psg_players[0:3] # Slicing

#Data frames
dict = {'Jugador':['Navas','Mbappe','Neymar','Messi'],
'Altura':[183.0, 170.0, 170.0, 163.0],
'Goles':[2, 200, 150, 500]}

df_players = pd.DataFrame(dict, index=[1,7,10,30])
print(df_players)

#Traer datos desde csv
tabla_csv=pd.read_csv('/root/Cursos_Platzi/Python/NumPy-Panda/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')
print(tabla_csv)
'''Puedo definir si la tabla tiene o no header poniendo 0 si esta en la primera fila o none si no tiene. tambien puedo definir el separador poniendo "sep= ',' en este caso no es necesario pues automaticamente lo toma como coma pero si usa otro se puede ajustar
tambien se puede ajustar como en este caso los titulos de la tabla asi:'''
pd.read_csv('/root/Cursos_Platzi/Python/NumPy-Panda/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv',header = 0, names = ['Namesss', 'Authhhhhor', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'])


#Traer datos desde json
tabla_json=pd.read_json('/root/Cursos_Platzi/Python/NumPy-Panda/hpcharacters.json')
print(tabla_json)

#Navegar un dataframe 

tabla_csv.head() #saca las primeras 5  lineas del dataFrame o las que uno poga entre parentesis
tabla_csv.tail(3) #saca las ultimas # lineas del dataFrame

#LOC
print(tabla_csv.loc[:])#muesta todos los datos 
print(tabla_csv.loc[0:4,['Name','Author']])#filtro fila 0 a 4, columna nombre y autor
print(tabla_csv.loc[:,['Reviews']]*-1)#multiplica todos los reviews por -1
print(tabla_csv.loc[:,['Author']]=='JJ Smith')#Muestra la columna con true o false segun sicumplen o no la igualdad
print(tabla_csv.loc[1,'Author'])

#ILOC filtramos segun los indices 
print(tabla_csv.iloc[:4,0:2])#muesta los datos de las filas a a 3 y las columnas 0 a 1 
print('Dato')
print(tabla_csv.iloc[1,3])#Muestra el dato en la fila 1 columna 3 sin contar el indice


#Borrar filas o columnas .drop
tabla_csv.drop('Genre', axis=1).head() #elimina la columna (1 es columnas 0 es filas) Genre de la salida pero no del dataFrame
tabla_csv.drop([0,1,2], axis=0).head() #elimina las filas 0,1 y 2 del data frame
tabla_csv.drop(range(0,10), axis=0) #elimina las primeras 10 filas del dataFrame
tabla_csv.drop_duplicates()# Elimina las filas que tengan duplicado
print(tabla_csv.shape[0] )#Muestra el numero de filas que posee el dataFrame
data= np.arange(0,tabla_csv.shape[0]) #Estoy creando un falso arreglo con los numeros del 1 al numero de filas de la tabla para luego poderlo agregar como una columna nueva

#Agregar nuevas filas o columnas
tabla_csv['Nueva_columna'] = np.nan #Crea una nueva columna con el nombre de Nueva_columna de valores Nan
tabla_csv['Rango'] = data #Crea una nueva columna llamada Rango con los valores del array 
#tabladuplicada = tabla_csv.append(tabla_csv, ignore_index=True)

#Manejo de valores nulos
#    Identificar los valores nulos
tabla_csv.isnull() #Me saca esta misma tabla donde el valor es nulo dice true donde no false
tabla_csv.isnull()*1 # asi el valor es nulo con 1 si no con 0
#     Sustituir valores nulos
tabla_csv.fillna('Missing value')#Sustituir los valores nulos por una cadena
tabla_csv.fillna(tabla_csv.mean)#Sustituir valores nulos por una medida estadística realizada con los valores de las columnas
tabla_csv.interpolate()#Sustituir valores nulos por valores de interpolación
#     Eliminar valores nulos
tabla_csv.dropna()

#Filtrar datos por condiciones
print(tabla_csv[tabla_csv['Year']>2016])
print(tabla_csv[tabla_csv['Genre']=='Fiction'])

#Informacion de la tabla
print(tabla_csv.info()) #muestra informacion general de la tabla
print(tabla_csv.describe) #muestra informacion específica sobre la tabla

#Uso de memoria
print(tabla_csv.memory_usage(deep=True))

#Contar numero de veces que se repite un valor en una columna organizado de menor a mayor
print(tabla_csv['Genre'].value_counts().sort_values())

#Ordenar el data frame
tabla_csv.sort_values(by='User Rating',ascending=False)#especifique que lo saque del valor más alto al más bajo
print(tabla_csv)

# GroupBy
print(tabla_csv.groupby('Author').count()) #Agrupa por autor te dice cuantos registros tiene por autor 
print(tabla_csv.groupby('Author').sum().loc['William Davis']) #tomamos los registros en que el autor sea William Davis y los sumamos
print(tabla_csv.groupby('Author').agg(['min','max'])) #agg permite evaluar dos funcionesen este caso min y max. para cada columna de cada autor.
print(tabla_csv.groupby('Author').agg({'Reviews':['min','max'], 'User Rating':'sum'})) #Agrupar por Author, obtener el mínimo y máximo de la columna ‘Reviews’ y sumar los valores de la columna ‘User Rating’
print(tabla_csv.groupby('Author').agg({'Year':lambda x: [i-2000 for i in x], 'Reviews':lambda x: sum([i**2 for i in x])})) #Se puede usar las funciones lambda en el método .agg(), para obtener funciones custom ya sea para modificar un valor o para filtrar valores.


# CONCAT
df1 = pd.DataFrame({'A':['A0', 'A1', 'A2','A3'],
        'B':['B0', 'B1', 'B2','B3'],
	'C':['C0', 'C1', 'C2','C3'],
	'D':['D0', 'D1', 'D2','D3']})


df2 = pd.DataFrame({'A':['A4', 'A5', 'A6','A7'],
	'B':['B4', 'B5', 'B6','B7'],
	'C':['C4', 'C5', 'C6','C7'],
	'D':['D4', 'D5', 'D6','D7']})

print(pd.concat([df1,df2])) #concatena las tablas por el axis 1 que es una debajo de la otra que esta por defecto
print(pd.concat([df1,df2], ignore_index= True)) #corregimos los indices para que continue contando no traiga los que ya tenia
print(pd.concat([df1,df2], axis = 1)) #concatenar una al lado de la otra (esto no es usual)


# MERGE 

izq = pd.DataFrame({'key' : ['k0', 'k1', 'k2','k3'],
 'A' : ['A0', 'A1', 'A2','A3'],
'B': ['B0', 'B1', 'B2','B3']})

der = pd.DataFrame({'key' : ['k0', 'k1', 'k2','k3'],
 'C' : ['C0', 'C1', 'C2','C3'],
'D': ['D0', 'D1', 'D2','D3']})

izq.merge(der, on='key')#Unir las tablas der e Izq


# JOIN

izq = pd.DataFrame({'A': ['A0','A1','A2'],
  'B':['B0','B1','B2']},
  index=['k0','k1','k2'])

der =pd.DataFrame({'C': ['C0','C1','C2'],
  'D':['D0','D1','D2']},
  index=['k0','k2','k3']) 

izq.join(der)

# PIVOT: Transforma los valores de determinadas columnas o filas en los índices de un nuevo DataFrame, y la intersección de estos es el valor resultante.

print(tabla_csv.pivot_table(index='Author',columns='Genre',values='User Rating'))
print(tabla_csv.pivot_table(index='Author',columns='Genre',values='User Rating', aggfunc='mean',fill_value="-"))

# MELT: es como un unpivot yo determino que columna se usará como index y que valores toman
#En el caso del ejemplo tengo una tabla con la informacion por local y por año pero yo necesito cada registro separado asi que hago una tabla que me diga que local que año y que vendio
data = {
    'Local': ['Local A', 'Local B', 'Local C'],
    #Ventas por año
    '2021': [100, 200, 300],
    '2022': [150, 250, 350],
    '2023': [200, 300, 400]
}
df = pd.DataFrame(data)

df.melt(id_vars=['Local'],
        var_name='Año',
        value_vars=['2021','2022','2023'],
        value_name='Ventas')

#Apply: Permite aplicar una funcion definida a una columna 

#    1. Defino la funcion
def two_times(value):
    return value * 2

#  2. la aplico en este caso a la columan user rating

tabla_csv['User Rating'].apply(two_times) # Se multiplica por 2 todos los valores de la columna

#Nota: esto se puede hacer con lambda functions
tabla_csv['User Rating2']=tabla_csv['User Rating'].apply(lambda x: x* 3)

#Aplicar la funcion si se cumple cierta condicion
tabla_csv.apply(lambda x: x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis = 1)





'''References:
https://pandas.pydata.org/docs/user_guide/10min.html
https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html

'''


