'''
Las funciones, podemos decir que esto es la magia de la programacion...
es coña, aunque tiene parte de verdad

las funciones no son mas que bloques de codigo que puedes llamar a demanda

y por que mola tanto hacer funciones?

pues igual a lo largo de el resto de archivos has visto que he repetido muchas veces
el mismo codigo, esto con el tiempo y en proyectos se hace mas evidente

las funciones tienen que cumplir con ciertos requisitos aunque el mas importante es

que con la misma entrada siempre tiene que devolver el mismo resultado
'''

# Sintaxis
'''
vamos a usar la palabra reservada def para indicar que vamos a usar una funcion,
luego le damos el nombre a nuestra funcion, 
abrimos y cerramos parentesis y ponemos 2 puntos,
declaramos el codigo que queremos ejecutar

def holita():
    print('hello world')
    
ya la tenemos declarada solo falta invocarla
holita()

veamos esto en accion
'''

def holita():
    print('hello world')

holita()

'''
acabamos de ver una funcion sin parametros de entrada
ahora vamos con una que reciba supongamos el nombre de alguien para
saludarlo
'''

def holita(nombre_amigo:str):
    print(f'hello {nombre_amigo}')

holita('Trompa')

'''
ahora bien aveces necesitamos que las funciones nos devuelvan valores 
para eso usamos return y devolvemos el valor
'''

def suma(num_a:int, num_b:int):
    return num_a + num_b

'''
podemos invocar la funcion y usar los los parametros en el orden que queramos
de la siguiente forma
'''

# con el orden definido en la funcion
suma(3,4)

suma(num_b = 100, num_a = 30)

'''
las funciones pueden tener tambien valores por defecto en caso de que no proporciones
un valor cuando la invoques
'''

def new_song(song = 'lalalala'):
    return 'The new ' + song

'''
una funcion puede tener un numero indeterminado de parametros
'''

def many_cosas(*cosas):
    return ' '.join(cosas)

'''
y podemos determinar parametros fijos y el resto indeterminado
'''

def make_a_sardina(papel,filtro,tabaco, *hierbas):
    return papel + filtro + tabaco + hierbas

'''
ademas de variables del tipo que sea podemos pasarle una funciona a las funciones como parametro
'''

def cooking(receta_function, chef):
    receta_function()
    return chef + ' well donde'

def recipe_of_paela():
    print('arroz_bomba mas garrofo con conejo y pollo')

cooking(recipe_of_paela, 'Trompa')
