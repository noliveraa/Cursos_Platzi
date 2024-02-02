import mi_modulo #traigo lo que se hizo en el otro archivo

data = [{
	'Country': 'Colombia',
	'Population': 500
},
{
	'Country': 'Bolivia',
	'Population': 300
}
]

'''
si yo me llevo el archivo main como modulo a otro documento al importar main este se va a ejecutar 
por lo que se recomienda encapsular todo lo que es "ejecutable" dentro de una funcion 
de tal forma que cuando yo importe main tenga que indicar que corra para que corra. 
sin embargo si yo ahora quiero ejecutar main desde la terminal como un scrip no lo puedo hacer pues no puedo ejecutar la funcion
por lo que recomienda poner ese if que se pone en este archivo al final "if __name__ == '__main__':run()
'''

def run(): #todo lo que se ejecute cuando voy 

    print(mi_modulo.a) #imprimo variable que le di a a en mi modulo desde este archivo

    keys,values = mi_modulo.get_population()
    print(keys,values) # ['col','bol'] [300,400]



    country = input('Type Country => ')

    result = mi_modulo.population_by_country(data, country)
    print(result)  # [{'Country': 'Colombia','Population': 500}]


if __name__ == '__main__':
    run()
#Este if dice que si es ejecutado desde la terminal, entre al run y si es ejecutado desde otro archivo, no se ejecuta.