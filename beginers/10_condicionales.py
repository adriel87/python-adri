'''
los condicionales son estructuras de flujo que controlan por donde
se va a ir ejecutando nuestro codigo

podriamos decir que son como porteros de una discoteca discriminando quien
puede entrar
'''

'''
de forma general tenemos estas estructuras de flujo

if <condicion>

if <condicion> Else

if <condicion>
Elif <condicion>
Else

vamos a ver varios ejemplos
'''

# if

a = 3

if a > 1:
    print('hello world')

'''
con if declaramos el inicio del bloque

luego viene nuestra condicion, una condicion tiene que ser de algun modo verdadera o falsa

y por ultimo ejecutamos el codigo
es importante la indentacion, en python es la forma de discriminar que nos encontramos dentro de un
scope diferente

scope -- es el alcance de nuestro bloque de codigo, las variables a las que se tienen acceso 
y hasta donde va afectar lo que hagamos dentro de un bloque determinado 
'''

# if Else

if a > 4:
    print('hello world')
else:
    print('hola Ondux')

'''
si te fijas todo es igual hasta la parte del else
lo unico que hace el else es ejecutar el codigo
en caso de que no se cumpla la condicion
'''

# if elif else

if a > 4:
    print('hello world')
elif a == 3:
    print(f'exactly is {a}')
# podemos usar elif las veces que necesitemos despues del if y antes del else
else:
    print('hola Ondux')

'''
igual que el anterior pero ahora podemos incluir nuevas condiciones
'''


'''
Tambien tenemos una version corta de el if/else
primero ponemos el codigo que queremos ejecutar luego evaluamos con un if
luego usamos el else e indicamos que es lo que vamos ejecutar en caso 
de que no se cumpla
'''

print('awitaguisa') if a < 100 else print('pioa')


'''
anidamiento

el anidamiento no nada mas que ir metiendo bloques de condiciones dentro de otros bloques
'''

if a > 0:
    # aqui anidamos
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
    # aqui se acaba el primer anidamiento
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


'''
dentro de las condiciones podemos hacer uso de los operadores logicos
que vimos en el archivo de operadores
'''

if a > 1 and a <5 or a == 3:
    print('is between')


