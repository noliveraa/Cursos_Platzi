#MODULOS DE PYTHON

import sys #informacion del sistema operativo
print(sys.path) #ruta en la que estoy ejecutando el archivo

import re #Expresiones regulares

import time #temas de timepo
print(time.asctime(time.localtime()))

import collections

import statistics
import random
import functools


'''-----------------------------------------------------------------------------------------------------------------------------'''
# VARIABLES
variable = "Hola" #str, se puede con comilla doble y sencila asi sea un numero si lo ponemos entre comillas queda como string
numero = 6 #entero
decimal = 10.2 
#Este ejemplo sirve para mostrar que python toma x como 3.3 con un solo decimal pero el resultado de la suma lo toma como 3.300000003 por eso al compararlos dice que no son iguales
x = 3.3
y = 1.1 + 2.2
print(x==y) #False 

age: int = 17 # asi puedo especificar que tipo de dato quiero que el tome que sea no el que el asuma
verdadero = True #boolean lo llama bool, la primera letra del true o false es mayuscula
falso = False
print(type(variable)) #me regresa el tipo de dato 

#CONCATENAR
name="Nathalia"
last_name = "Olivera"
full_name = name + " " +last_name
print(full_name)
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)
print(f"Hola esta es otra forma de insertar {name} y {last_name}")

# METODOS: función que viene incluida dentro de un objeto
texto = "Hola Mundo"
#indice  012345
print(texto)
print(texto.upper()) #lo pasa todo mayuscula
print(texto.lower()) #lo pasa todo minuscula
print(texto.find("M")) # regresa la M esta en la posicion 5 en la frase o string Hola Mundo
print(texto.replace("Mundo","Chanchito feliz"))
print(texto.count('a')) #cuenta el numero de a en el texto 
print(texto.swapcase) #lo que esta en may a min y al contrario
print(texto.startswith("Hola"))# me dice si incia con lo que le ponga en este caso true existe tambien endswith
nuevoTexto = texto.replace("Mundo","Chanchito feliz")
print(texto, nuevoTexto) 
print("Mundo" in texto) #buscar Mundo dentro de texto me saca un true o false si esta esto lo puedo usar por ejemplo en un in 

#OPERACIONES ARITMÉTICAS
print(5 + 14)
print(5 - 14)
print(5 * 14)
print(5 / 14)
print(5 ** 2) #Elevado
print(10 % 3) #modulo : o que resta de la division de dos numeros
numero -= 1 #Forma abreviada de decir numero = numero -14
print(numero)
vector = [3,4,5]
promedio = statistics.mean(vector)
print(promedio)

#OPERADORES DE COMPARACIÓN
n1 = 10
n2 = 15
print(n1 > n2)
print(n1 <= n2)
print(n1 == n2)
print(12 != 3) # 12 es diferente de 3 es True

#OBTENER DATOS DE USUARIO
edad = int(input('Ingresa tu edad:')) #int hace que el numero ingresado sea recibido como un entrero 
print(edad)
#convertir a otros tipos de datos
str(220)
float("22.3")
bool() #evalua lo que le ponemos como true o false por lo general sera true solo sera false si ponermos false, 0, "", none 

#OPERADORES LÓGICOS
print(edad>18 and edad<30) #evalua primero si es mayor de 18 y luego si es menor a 30 si es menor a 18 no mira si es 30 automaticamente es false con uno falso ambos son falsos
print(edad>18 or edad < 30) #uno o el otro es true
print(not(edad>18)) # al pasar por el not me manda la respuesta opuesta


'''-----------------------------------------------------------------------------------------------------------------------------'''
#LISTAS (list): el tipo de dato se llama list
lenguajes = ["python", "Ruby", "PHP", "js", "java","C","C++"]
print(lenguajes[1])
lenguajes[1]="Go" #reemplazo el segundo elemento 
print(lenguajes[-1]) # me da el ultimo elemento 
print(lenguajes[1:3])#Seleccionar un rango  desde el indice 1 y termine en el que va antes del 3 es decir en el 2 el 3 no lo incluye
print(lenguajes[:3])# asume que es desde el primer elemento si omito el 3 [1:] asume que es hasta el ultimo
print(lenguajes[::2]) #le digo parte del inicio hasta el final saltando de a dos pero el que muestra lo cuenta 

lenguajes.insert(0,"C") # adiciona C como lenguale al inicio antes de python 
lenguajes.remove("PHP") #quita PHP
print(len(lenguajes)) #muestra la longitud del array
lenguajes.append("SQL")#agrega un elemento al final de la lista
ubicacion = lenguajes.index("js") #pregunta en que posicion esta en el array
print(ubicacion)
lenguajes.pop() #quita por defecto el ultimo elemento si se cual posicion quiero quitar pongo dentro de los paentesis del pop la poscion
lenguajes.sort() #ordena los elementos del array alfabeticamente, acalaracion para hacerlo todos tienen que ser el mismo tipo de dato
print(lenguajes)

#list comprehention: busca resumir el codigo tomando el elemento que en el ejemplo es i*2 el ciclo por donde se extraen los elementos en este caso el ciclo for y la condicion opcional para filtrarlos que en este caso es el if
versionLarga=[]
for i in range (1,11):
    if i%2==0:
        versionLarga.append(i*2)

versionCorta= [i*2 for i in range (1,11)if i%2==0]

'''-----------------------------------------------------------------------------------------------------------------------------'''
#TUPLAS (tuple): Son listas inmutables una vez declarada no se puede modificar
nombres = ("Andrea", "Juana", "Juan", "Camila")
seleccion = random.choice(nombres)
print(seleccion)

'''-----------------------------------------------------------------------------------------------------------------------------'''
#DICCIONARIOS: son como los objetos en JS
objeto = {
    'tipo': 'carro',
    'color': 'rojo',
    'marca': 'Aveo',
    'motor':['1.6','1.8','2'],
    'anioFabricaccion': 2009
}


print(len(objeto)) #el tamanio del diccionario
print(objeto['marca']) #imprimiendo una llave 
print(objeto.get('marca'))
print('tipo' in objeto) #refresa True o False 
# otros métodos de los diccionarios https://www.w3schools.com/python/python_dictionaries_methods.asp
objeto['color']='Azul'
objeto['motor'].append('6.2')
del objeto["anioFabricaccion"]
objeto.pop('tipo')
print(objeto.items()) #Returns a list containing a tuple for each key value pair
print(objeto.keys()) #Returns a list containing the dictionary's keys
print(objeto.values()) #Returns a list containing the dictionary's values

#Dictionary comprehension: resumir la creacion del diccionario a partir de la iteración asi:

#{key:value for var in iterable}

#Ej1. 
diccionarioLargo = {}
for i in range (1,5):
    diccionarioLargo[i]=i*2

diccionarioCorto={i:i*2 for i in range(1,5)}

#Ej2.
names =['nico', 'zule','juan']
ages=[12,23,45]

uniondediccionario = {names[i]:ages[i] for i in range(len(names))}

print(uniondediccionario)

#{key:value for var in iterable if condition}
frase = 'Hola, soy Nathalia'
unique={i: i.upper() for i in frase if i in 'aeiou' }
print(unique)

'''-----------------------------------------------------------------------------------------------------------------------------'''
#LISTAS DE DICCIONARIOS

poblacion_mundial = [
    {'Rank': '36', 'CCA3': 'AFG', 'Country/Territory': 'Afghanistan', 'Capital': 'Kabul', 'Continent': 'Asia', '2022 Population': '41128771', '2020 Population': '38972230', '2015 Population': '33753499', '2010 Population': '28189672', '2000 Population': '19542982', '1990 Population': '10694796', '1980 Population': '12486631', '1970 Population': '10752971', 'Area (km²)': '652230', 'Density (per km²)': '63.0587', 'Growth Rate': '1.0257', 'World Population Percentage': '0.52'},
    {'Rank': '138', 'CCA3': 'ALB', 'Country/Territory': 'Albania', 'Capital': 'Tirana', 'Continent': 'Europe', '2022 Population': '2842321', '2020 Population': '2866849', '2015 Population': '2882481', '2010 Population': '2913399', '2000 Population': '3182021', '1990 Population': '3295066', '1980 Population': '2941651', '1970 Population': '2324731', 'Area (km²)': '28748', 'Density (per km²)': '98.8702', 'Growth Rate': '0.9957', 'World Population Percentage': '0.04'},
    {'Rank': '34', 'CCA3': 'DZA', 'Country/Territory': 'Algeria', 'Capital': 'Algiers', 'Continent': 'Africa', '2022 Population': '44903225', '2020 Population': '43451666', '2015 Population': '39543154', '2010 Population': '35856344', '2000 Population': '30774621', '1990 Population': '25518074', '1980 Population': '18739378', '1970 Population': '13795915', 'Area (km²)': '2381741', 'Density (per km²)': '18.8531', 'Growth Rate': '1.0164', 'World Population Percentage': '0.56'},
    {'Rank': '213', 'CCA3': 'ASM', 'Country/Territory': 'American Samoa', 'Capital': 'Pago Pago', 'Continent': 'Oceania', '2022 Population': '44273', '2020 Population': '46189', '2015 Population': '51368', '2010 Population': '54849', '2000 Population': '58230', '1990 Population': '47818', '1980 Population': '32886', '1970 Population': '27075', 'Area (km²)': '199', 'Density (per km²)': '222.4774', 'Growth Rate': '0.9831', 'World Population Percentage': '0'},
    {'Rank': '203', 'CCA3': 'AND', 'Country/Territory': 'Andorra', 'Capital': 'Andorra la Vella', 'Continent': 'Europe', '2022 Population': '79824', '2020 Population': '77700', '2015 Population': '71746', '2010 Population': '71519', '2000 Population': '66097', '1990 Population': '53569', '1980 Population': '35611', '1970 Population': '19860', 'Area (km²)': '468', 'Density (per km²)': '170.5641', 'Growth Rate': '1.01', 'World Population Percentage': '0'}
]

# Acceder al 'Country/Territory' del primer elemento
print(poblacion_mundial[0]['Country/Territory'])

#Agregar un pais mas:
#1. Creo el nuevo pais (diccionario)
new_country = {'Rank': '99', 'CCA3': 'AUT', 'Country/Territory': 'Austria', 'Capital': 'Vienna', 'Continent': 'Europe', '2022 Population': '8939617', '2020 Population': '8907777', '2015 Population': '8642421', '2010 Population': '8362829', '2000 Population': '8010428', '1990 Population': '7678729', '1980 Population': '7547561', '1970 Population': '7465301', 'Area (kmÂ²)': '83871', 'Density (per kmÂ²)': '106.5877', 'Growth Rate': '1.002', 'World Population Percentage': '0.11'}
#2. Lo agrego
poblacion_mundial.append(new_country)

# Actualizar la población de 'Afghanistan' en 2022
for country_data in poblacion_mundial:
    if country_data['Country/Territory'] == 'Afghanistan':
        country_data['2022 Population'] = '50000000'  # Nuevo valor de la población
        break

'''-----------------------------------------------------------------------------------------------------------------------------'''
#CONJUNTOS (set): Se pueden modificar, tienen un orden y no permiten duplicados (si pongo algo repetido el programa lo quita al imprimir)
set_countries = {'col', 'mex', 'bol'}
print (set_countries)

size = len(set_countries) # conocer el tamaño del conjunto
print('col' in set_countries) # True
set_countries.add('per') # add
set_countries.update({'ar', 'ecua', 'pe'})# update, lo que hace es sumar elementos a los existentes  {'col', 'mex', 'bol', 'pe', 'ar', 'ecua'}
set_countries.remove('col') # remove si le doy remove a un elemento que no existe lanza un error. 
set_countries.discard('arg')# para eso usamos discard, si no existe, no falla.
set_countries.clear()# limpiar todo el conjunto, lo deja en vacío

numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers) # creamos un conjunto a partir de una lista, quita los duplicados
print (set_numbers) # {1, 2, 3, 4}

#operacion de conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Unión (|): de los elementos
set_c = set_a.union(set_b)
print(set_a | set_b)  # {'col', 'mex', 'bol', 'pe'}

# Intersección (&): obtener los elementos en común
set_c = set_a.intersection(set_b)
print(set_c) # {'bol'}
print(set_a & set_b)  # {'bol'}

# Diferencia (-): dejamos sólo los elementos de A
set_c = set_a.difference(set_b)
print(set_c)  # {'col', 'mex'}
print(set_a - set_b)  # {'col', 'mex'}

# Diferencia simétrica (^): es hacer una unión, sin los elementos en común
set_c = set_a.symmetric_difference(set_b)
print(set_c) # {'col', 'mex', 'pe'}
print(set_a ^ set_b) # {'col', 'mex', 'pe'}


'''-----------------------------------------------------------------------------------------------------------------------------'''
#IF
puntaje=97
if puntaje>=95:
    print("Aprobado con honores")
elif puntaje>=50:
    print("Alumno aprobado")
else:
    print("Reprobado")

#Ejercicio T en F a C
temperaturain = float(input('Ingresa la T a convertir :')) 
unidad = input("¿esta en F o C?")
if unidad == "F":
    temperaturaout= (temperaturain-32)*(5/9)
elif unidad == "C":
    temperaturaout= (temperaturain*9/5)+32
else:
    print("valor ingresado no valido")
print(temperaturaout)

#Programa para saber si el numero es par o impar
numero = 0
if (numero%2)==0:
    print("es par")
else:
    print("es impar ")


#WHILE
i=1
while i<=5:
    print(i* "hola ")
    i= i + 1
    if i == 4:
        break #Esto hace un pare al ciclo si alguna condicion especifica se cumple antes de que termine el ciclo

i=0
while i<20:
    i+=1
    if i<15:
        continue #la instruccion despues del continue solo se va a ejecutar dentro del ciclo luego de que se cumplea el if
    print(i)

i=0
while i<len(lenguajes):
    print(lenguajes[i])
    i=i+1
#cntr c para acabar un ciclo infinito


#FOR
for lenguaje in lenguajes: #asi puedo iterar en tuplas, listas o incluso diccionarios (keys in diccionario)
    print(lenguaje)

for element in range (1,21): #range me itera de 1 a 20, el 21 no lo ejecuta 
    print(element)

for key, value in objeto.items(): #iterando en un diccionerio 
    print(key, '=>', value)

#JSON: trabajando con un array de objetos
people =[
    {
        'name':'Juan',
        'age':55
    },
    {
        'name':'Pedro',
        'age':45
    },
    {
        'name':'Noa',
        'age':26
    },
    {
        'name':'Andres',
        'age':18
    }
]

for person in people:
    print ('name =>',person['name'])


# Ciclos anidados/MATRICES
matriz = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]

print(matriz[0])# Imprime la primera fila de la matriz
print(matriz[0][1])# Imprime el elemento 2 de la primera fila

for row in matriz: #Recorremos las filas de la matriz y por cada fila recorremos cada una de las columnas
  print(row)
  for column in row:
    print(column)

'''-----------------------------------------------------------------------------------------------------------------------------'''
# FUNCIONES
def suma(a,b):
    print(a+b)
suma(1,5)

#si yo necesito que la funcion me regrese ese resultado pongp return y lo asigno a una variable
def resta(a,b):
    return a-b
resultado = resta(6,1)
print(resultado)

#enviar valores por defecto por si al llamar la funcion el usuario no pone valores
def volumen (ancho=1, largo=1, fondo=1):
    return f"El volumen seria de {ancho*largo*fondo} cuendo el ancho es {ancho}"

print(volumen(5,3))

#regresar varios valores en una sola funcion
def varios(a,b,c):
    x=a+1 
    y=b-2
    c=c-x
    return x,y,c #6,4,4
valor1 , valor2, valor3 = varios (5,6,10)
print (valor1)

#Funciones lamda: es una forma de escribir las funciones de forma concisa, son funciones anónimas 
def incremento (x):
    return x+1
        
resultado1 = incremento(10)

incremento2 = lambda x : x+1
resultado2 = incremento2(10)

print(resultado1)
print(resultado2)

#High Order function: funciones que reciben como parámetro el return the otra función

base = lambda x:x+1
high_order_function = lambda x,func :x+2 #esta funcion recibe como parámetros x y func

valorresultante = high_order_function(2, base)
print(valorresultante)

#lo anterior lo puedo simplificar asi:
valorresultante = high_order_function(2, lambda x:x+1) #de esta forma no tengo que definir aparte la funcion "base"

'''-----------------------------------------------------------------------------------------------------------------------------'''
#MAP: ejecuta una función especifica para cada elemento en un iterable y el elemento se envía a la función como un parámetro.Se plantea asi map(funcion, iterable)

numbers =[1,2,3,4]

# sin map seria asi
numbers_v2 =[]

for i in numbers:
    numbers_v2.append(i*2)

#lo anterior con map seria asi
number_v3 = list(map (lambda i:i*2,numbers))

#Map en diccionarios

items = [
    {'product':'camisa',
     'price' :100},
     
    {'product':'pantalones',
     'price' :300},
     
    {'product':'chaqueta',
     'price' :400}
]

prices = list(map(lambda item: item['price'],items))
print(prices)

#quiero agreagar el atributo taxes a cada item
def add_taxes (item):
    item['taxes'] = item['price']*.19
    return item

new_items = list(map(add_taxes,items)) 

'''-----------------------------------------------------------------------------------------------------------------------------'''
#FILTER

letras = ['a','b','c','d','e','f','g']
vocales = list(filter(lambda x: x in ['a','e','i','o','u'], letras))
print(vocales)

words = ['amor', 'sol', 'piedra', 'día']
print(len(words[1]))

'''-----------------------------------------------------------------------------------------------------------------------------'''
#REDUCE
#Nota para usar esto debo importar "import functools"

otralista = [ 1, 5,6,7]
result = functools.reduce(lambda counter , item : counter +item , otralista)

letters =['H','E','L','L','O']
word = functools.reduce (lambda x,y: x+y, letters) #este lambda debe recibir dos parámetros en este caso x y y que son los dos primeros elementos de la palabra que va a juntar en este caso H y E en la siguiente iteracion X sera igual a HE y y sera L se sumaran y asi sucesivamente 

'''-----------------------------------------------------------------------------------------------------------------------------'''
#ITERABLES: Tipo de objeto que contiene un numero de valores que son iterable
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

'''-----------------------------------------------------------------------------------------------------------------------------'''
#PRUEBA ERRORES
#assert: permite evaluar que el resultado esperado sea realmente lo que da como resultdado asi:
suma = lambda x,y: x+y
assert  suma(2,2)==5  #me marca una alerta pues 2 + 2 no es 5 y para la ejecucion  

assert 1!=1, 'Uno no es igual'

#Exception: yo le pongo una regla a python si no se cumple el programa saca un error
age = 10
if age < 18:
    raise Exception ('no se aceptan menores de edad') #no se ejecutan lineas posteriores a esta si no se cumple

#Try: Permite probar un bloque de código en busqueda del error, sin detener la ejecucion 

def my_divide(a, b):
   # Escribe tu solución 👇
   try:
      result = a / b
   except ZeroDivisionError:
         result = 'No se puede dividir por 0'
   return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0

'''-----------------------------------------------------------------------------------------------------------------------------'''
#Abrir desde python archivos de texto:

'''
file = open('./Python/text.txt','w+')
print(file.read()) #lee todo el texto, no estan liviano 
print(file.readline()) #Lee línea a línea, es liviano  
for line in file:
  print(line)
file.close() # Cierra el archivo
'''

# Version que cierra archivos automáticamente 
with open('./Python/text.txt','r+') as file: #r+ -> abre un archivo para escritura y lectura. , w+ reescribe todo el archivo 
    for line in file:
        print(line)
# sobreescribir sobre el contenido existente
    file.write('\n')  # salto de linea
    file.write('una nueva linea\n')

'''-----------------------------------------------------------------------------------------------------------------------------'''
#Abrir desde python archivos de CSV: requiero transformar estos datos a formato de diccionario
import csv

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
  

#para poder ejecutar esto como un script 
if __name__ == '__main__':
  data = read_csv('./Python/data.csv')
  print(data)


import csv

def read_csv(path):
  total=0
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') #indico que los datos estan separados por comas
    for row in reader:
        print('******')
        total += int(row[1])
        print(total)
    return total

read_csv('./Python/data2.csv')
