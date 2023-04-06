'''
Las listas son un tipo de datos que te permite almacenar datos de forma ordenada
ademas en las listas se permite la duplicidad de los valores

no tienes ningun tipo de limitacio al tipo de dato a insertar, eso quiere decir
que dentro de una misma lista puedes tener desde str a number u otro tipo de dato
como otra lista.

bueno vamos a ver un ejemplo de como se declara una lista
'''

my_list = list()

print("la lista que acabamos de declarar --> ",my_list, type(my_list))

# conseguimo el mismo resultado asi

my_list2 = []

print("la lista 2 que acabamos de declarar --> ",my_list2)

# tambiem podemos definir las variables al incializar la lista

fps_games = ['CSGO','valorant','apex legend']

print(fps_games, ' lista de juegos')

'''
recuerdas como obtener el tamaño de una cadena
descomenta la linea de abajo y añade lo necesario para
indicar el tamaño de esa lista
'''

# print('the length of my list of fps games is --> ', aqui debes colocar tu codigo)


'''
vamos a ver como acceder a los valores que hay dentro de una lista

igual te suena de las cadenas
'''

# acceder al primer elemento de fps_games
print(fps_games[0], 'e valor del primer elementos de fps games')

# ahora al ultimo
print(fps_games[-1])


'''
asignar valores desenpaquetando/unpacking

veamos el unpacking como una forma rapida de inicializar variables desde una lista
que tenga ya datos
'''

mis_cosas = ['tenedor', 'papel', 'pc gaming', 'te caducado']

cosa1, cosa2, cosa3, cosa4 = mis_cosas

print(cosa1, ' cosa 1')
print(cosa2, ' cosa 2')
print(cosa3, ' cosa 3')
print(cosa4, ' cosa 4')

# de esta forma obtenemos en orden los valores de la lista
# pero si solo ponemos 2 variables o menos variables que los valores que posee la lista?

cosa5, *cosa6 = mis_cosas

print(cosa5, ' cosa 5')
print(cosa6, ' cosa 6')


'''
si te fijas obtenemo el primer valor en cosa5 y en cosa6 colocamos el resto, de primeras parece
util. Pero y si queremos tener el primer valor y el ultimo por separado y el resto en otra variable
'''

primera_cosa ,*resto_de_cosas, la_ultima_cosa= mis_cosas

print(primera_cosa, ' primera_cosa')
print(resto_de_cosas, ' resto_de_cosas')
print(la_ultima_cosa, ' la_ultima_cosa')



'''
recortando nuestra lista

esto es muy similar tambien,por no decir identico al apartado de las cadenas
'''

locos = ['trompa', 'ondux', 'diiimeeenn', 'awitaguisa', 'poia']

todos_los_locos = locos[0:5]
print(todos_los_locos, ' todos los locos')

# tambien podemos obtener a todos los locos indicando el inicio y no el fin
todos_los_locos = locos[0:]
print(todos_los_locos, ' todos los locos again')

# solo algunos locos
solo_algunos = locos[1:3]
print(solo_algunos, ' solo algunos locos')

'''
si te has fijado a veces usamos esta sintaxis con las listas o las cadenas
[indice : hasta_donde_quieres_llegar] 

y en ocasiones usamos la siguiente
[indice : limite : pasos]

los pasos son basicamente los valores que vas a ir saltando entre el indice y el limite vamos a verlo
'''
solo_algunos = locos[0::2]
print(solo_algunos,' saltando locos')

'''
el paso o step lo da desde la posicion donde se encuntra y empieza a contar desde hay
puedes ir modificando el script para que vayas entendiendo el funcionamiento
'''


'''
modificar elementos de una lista
'''

cuentas = [1,2,3,4,5]

# modifiquemos el primer valor
cuentas[0] = 1000

# ahora intenta modificar el penultimo valor



'''
comprobar si exite algo dentro de una lista

para eso vamos a usar la siguiente sintaxis

valor in your_list

donde
 valor      --> es lo que quieres buscar
 in         --> es una palabra reservada que nos provee esa funcionalidad para las listas
 your_list  --> es la lista donde quieras buscar

vamos a ver si nuestro amigo negrita esta dentro de la lista de locos
'''
print('negrita' in locos, ' estara el negrita') # recuerda que puedes invertir el resultado de esa expresion con un not para buscar lo contrario


'''
bueno ahora vamos ir incluyendo datos en nuestras listas
ten encuenta que la mayoria de los lenguajes de programacion estan escritos en
y si te has fijado python es basicamente hablar en ingles
pues bien vamos al lio

'''

locos.append('negrita')

# acabamos de incluir a negrita podrias comprobar si de verdad esta en locos ??

'''
con append si te fijas icluimos un valor al final de nuestra lista
pero puede que quieras colocar alguien en un lugar concreto de la lista
probemos con el mojoyoyo que queremos colocarlo entre el trompa y el ondux
'''

# primero tenemos que ver donde esta el trompa y el ondux
print(locos, ' buscando al trompa y al ondux')

# en la primera y la segunda posicion
# es decir que ahora el mojo estaria en la segunda posicion

locos.insert(1,'mojoyoyo')
print(locos, ' el mojo entro en la ecuacion')

'''
vale sabemos incluir valores a nuestra lista

pero ahora tenemos un problema con el poia y queremos elimiarlo de los locos
vamos a removerlo
'''

locos.remove('poia')
print('poia' in locos, ' a ver si se fue el poia')

'''
pero la cosa no acaba bien y el trompa se calienta por que hemos eliminado de los locos
al poia y que vamos a hacer con el trompa

pues sacarlo
'''
# si recuerdas el trompa esta en la primera pocision de esta lista es decir la 0

locos.pop(0)

print(locos, ' el trompa fue a hablar con la pili')

# ya esta el grupo para jugar completo

'''
una vez que la partida termino se nos van el mojo y el ondux que curran ma;ana temprano

hay que eliminarlos para dejar hueco
'''

del locos[0:2]
print(locos, ' hay que trabajar adios')
# de esta forma podemos eliminar con la misma sintaxis que usamos para trocear nuestras listas

'''
al final no viene nadie y todo el mundo se va a la cama, pues ya no hay locos
vamos a limpiar la lista
'''
locos.clear()

# veamos ahora cuantos locos quedaron en la lista

print(len(locos), ' el grupo se fue a mimi')


'''
bueno ya no tenemos a los locos asi qeu volvamos a las listas

imagina que tu madre te dice que si puedes ir a comprar
papas, leche y huevo

pero de camino tu abuelo tambien te dice que si puedes comprarle lo mismo que le vas 
a comprar a tu madre

parece sencillo ya tienes la lista de mama y el abuelo solo queria la mismo
vamos a simularlo

'''

lista_mama = ['papas','leche','huevo']

print(lista_mama, 'la lista de mama')

lista_abuelo = lista_mama

print(lista_abuelo, 'la lista del abuelo')

# solucionado no?
'''
ahora te llama el abuelo y quiere incluir a la lista queso
pues vamos a hacerle un append
'''
lista_abuelo.append('queso')

print(lista_abuelo, 'lista del abuelo con queso')

# volvamos a revisar la lista de mama

print(lista_mama, ' revisando la lista de mama')

'''
si te fijas ahora la lista de mama tiene el queso

esto pasa por que literalmente indicamos que una lista es igual a la otra,
basicamente va a buscar la informacion al mismo punto

vamos a solucionarlo
'''
lista_mama = ['papas','leche','huevo']

print(lista_mama, 'la lista de mama v2')

lista_abuelo = lista_mama.copy() # copiamos la lista y devolvemos su valor

print(lista_abuelo, 'la lista del abuelo v2')

# hasta aqui solo cambiamos el copy
# ahora modifiquemos la lista del abuelo

lista_abuelo.append('queso')


print(lista_abuelo, 'lista del abuelo con queso v2')

# volvamos a revisar la lista de mama

print(lista_mama, ' revisando la lista de mama v2')

'''
ahora las referencias de las listas son distintas y no vamos a tener ningun problema
'''

'''
por ultimo vamos a ver como juntar 2 listas podemos usar las listas anteriores
y ver el resultado
'''
# usamos el operador +
bloc_de_listas = lista_mama + lista_abuelo

print(bloc_de_listas, ' las listas esta unidas')

'''
pues esto es bastante basico de las listas pero hay algo que me gustaria
que investigaras

quiero saber lo siguiente :
1. cuantas papas hay en la lista
2. el indice del queso
3. imprimir la lista de forma ordenada
'''


