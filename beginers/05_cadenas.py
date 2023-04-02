'''
veamos un poquito como trabajar con cadenas dentro de python
'''

# veamos una cadena simple

'hello world'

'''
En python podemos tanto usar comillas simples como dobles

imagina que en la cadena de 'hello world' quieres poner el world entre comillas
'''

# usando una combinacion de ambas comillas
# si empiezas con simples lo que tengas dentro lo puedes hacer con dobles

'hola "mundo"'
# o al reves
"hola 'mundo'"

# solo usando un tipo de comillas, es necesario escapar el caracter

'hola \'mundo\''

# incluso podrias concatenar una variable que contenga la comilla escapada, todo depende de lo que te haga falta

r'''
en las cadenas los caracteres de escape se usan para muchas cosas 
desde incluir comillas como vimos arriba
a formatear un poco nuestra cadena
la forma mas tipica de escapar caracteres es usando la barra invertida \

fijate que este bloque de comentario empieza por r
esto permite evitar el compartamiento que hace que usando la barra invertida se escapen los caracteres
puede que te resulte util, por ejemplo en alguna ruta relativa

veamos un ejemplito
'''

url_whit_format = 'C:\ondux\name'
url_whitout_formar = r'C:\ondux\name'
print(url_whit_format)
print(url_whitout_formar)


'''
tambiem podemos escribir bloques de cadenas de caracters
'''

mi_bloque = '''
hola soy nuevo en esto
y me gusta el chocolate
el cafe y befunge
'''

print(mi_bloque)

# podemos evitar el salto de linea inicial si usamos una barra invertida al comienzo

mi_bloque = '''\
hola soy nuevo en esto
y me gusta el chocolate
el cafe y befunge
'''
print(mi_bloque)

'''
fijate que ahora tienes el segundo bloque pegado al anterior
y no tienes un salto de linea
'''

'''
ahora veamos como podemos acceder a las pocisiones de una cadena
por ejemplo acceder al tercer caracter de una cadena
'''

print('cual sera el tercer caracter de esta cadena ondux?'[2])

'''
solo ha impreso un caracter no??
y es que las cadenas son un tipo de dato que contiene un indice

que quiere decir que tenga un indice, pues igual que en un documento convecional
tenemos una especie de referencia que nos indica a donde tenemos quie ir si queremos
consumir o leer esa parte del documento

en este caso el indice de una cadena se representa de forma numeral,
siempre empieza en 0 y el final es el tamaño menos 1
con un ejemplito se ve mejor
'''

mi_cadena = 'vaquita'
# que caracter esperas ver en vaquita[0], escribe tu el codigo para mostrarlo

# y en la ultima posicion de mi_cadena

# te voy a complicar un poco, ahora muestrame la ultima posicion de mi cadena
# no modifiques la cadena y escribe debajo
mi_cadena = 'sdkjl;alskdjfklasjdfkljasldkfjalskdjfklasjdflkjsdlkfjkjkhgjhsdz'

'''
un tip recuerda que hay funciones de sistema que te pueden ayudar con este ejercicio
o incluso la misma documentacion
'''


'''
tambien podemos hacer trozos de nuestras cadenas veamos la siguiente sintaxis

mi_cadena[0:2]

el 0 seria el primer indice, vamos desde donde quieres trocear la cadena
y el 2 seria el indice hasta donde quieres trocear

'''

mi_cadena= 'como me cortes te reviento'
# es muy agresivo vamos a coger hasta el 'cortes'

print(mi_cadena[0:17])

'''
podriamos poner lo que queremos en una variable nueva
'''
la_intencio = mi_cadena[-11:]

print(la_intencio)

'''
invertir una cadena, peculiaridad del lenguaje
hay muchas mas pero te dejo el resto a ti y a la docu
'''
sentido = 'hola mundo'
sentido_inverso = sentido[::-1]
print(sentido, sentido_inverso, sep=' y le damos la vuelta ')

'''
acabas de ver que se pueden usar numeros negativos en los indices.
En python podemos usar valores negativos para indicar que vamos a empezar en orden inverso,
algo asi como de atras a adelante, te dejo un enlace a la docu oficial en el README
'''

'''
vamos a ver algunas funciones destinadas solo a las cadenas
'''
# definimos nuestra variable para trabajar con los metodos de las cadenas
el_util = 'hola mundo'

print(el_util.capitalize())
print(el_util.count('o'))
print(el_util.index('a'))
print(el_util.find('z'))
print(el_util.title())
que_tenemos = el_util.split(' ')
print(que_tenemos)
print(el_util.replace('o', '8===D'))





'''
format string y literales formateados
'''

# format string
my_number,my_name  = 2, 'adri'
print('mi edad es {} y mi nombre es {}'.format(my_number,my_name))

formated_str = 'mi edad es %d y mi nombre es %s' %(my_number,my_name)

print(formated_str)

# literales formateados
my_name = 'adriel'

print(f'mi nombre es {my_name}')


