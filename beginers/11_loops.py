'''
los loops o bucles son otra estructura de control dentro de los lenguages de programacion

un bucle se define por que va a ejecutar un numero determinado de veces un bloque de codigo

para determinar las veces que hace falta que actue ese bucle , nomalmente tendremos un condicional 
que sea el que maneje cuando se acaba el bucle
'''

'''
aqui vamos a ver los tipos de bucle que tiene python

- while, este bucle se ejecutara mientras su condicion sea verdadera

- for, este bucle se ejecutara un numero finito de veces, normalmente lo usaremos con listas
'''

# While

# su sintaxis

'''
while condition
    your code

ahora vamos a imprimir algo 5 veces
'''
i=0 #necesitamos una variable para poder modificarla
while i < 5:
    print(f'hello world {i}')
    i += 1



'''
tambiem podemos contar con que no se cumpla la condicion y en su lugar ejecutar otra cosa
por ejemplo si no se cumple la condicion nos despedimos
'''
while i < 5:
    print(f'hello world {i}')
    i += 1
else:
    print('Good bye')


'''
es posible que durante la ejecucion del codigo se den las circunstancias por las cuales
no necesitemos continuar dentro del bucle

para ello vamos a usar break

'''
i=0
while i < 5:
    print(f'hello world {i}')
    i += 1
    if i == 2:
        print('ok i will break the loop')
        break
else:
    print('Good bye')


'''
podemos hacer que nuestro codigo salte a la siguiente iteracion del bucle
con un continue

ten encuenta como modificas tu variables por que puedes provocar un bucle
infinito y no queremos eso
'''

i=0 #necesitamos una variable para poder modificarla
while i < 5:
    if i == 3 :
        i += 1
        continue
    print(f'hello world {i}')
    i += 1


'''
ahora vamos con los for

si recuerdas bien antes comentamos que como norma general los vamosa  usar con listas
y esto es por que las listas cuantan con una propiedad, y es que son iterables.

basicamente esto quiere decir que se puede recorrer de forma secuencial

la sintaxis basica

for element in elements:
    your code here

vamos a ver un par de ejemplos
'''

# creamos una lista para poder iterarla

mi_lista = [1,2,3,4,5]

# ahora vamos a usar un for

for numero in mi_lista:
    print(f'hello world {numero}')

'''
tenemos la misma salida que con el while 

pero con un estilo mas declarativo
'''

'''
ahora bien con que podemos usar un for

pues con todo aquello que pueda ser iterable

strings
listas
tuplas
sets
diccionarios, 

de los diccionarios solo obtenemos la clave pero veamos un ejemplito

'''

trompa = {
    'is_mad' : True,
    'name': 'Trompaturtle',
    'can_stay_calm_in_fps': False
}

# ahora vamos a iterarlo y ver el diccionario

for key in trompa:
    print(key, trompa[key], sep=' and the value is ')


'''
ademas con los for tambien puedes usar:
else, al final si quieres ejecutar algo cuando al final del for
break, para cortar el bucle
continue, para ir a la siguiente iteracion del bucle

'''

'''
podemos usar la funcion range() para que nos devuelva una lista sobre la que iterar
'''

for number in range(5):
    print(number)

'''
esta funcion puede recibir hasta tres parametros

# un solo parametro
range(numero_de_elementos_de_la_lista)

# 2 parametros
range(numero_donde_inicia, cantidad_de_numeros)

# 3 parametros
range(comienzo, final, pasos)

es bastante util asi que te recomiendo que la usar y aprendas a usarla
'''


'''
por ultimo recuerda que puedes anidar siempre que lo necesites
tanto los bucles while como los for
'''
