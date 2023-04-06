'''
haciendolo facil un set es una lista donde sus valores no se pueden repetir
'''

'''
vamos a ver como definir un set
'''
mi_set_up = set()
mi_set_up = {}

# incluyendo valores al inicio
mi_set_up = {1,2,3,3}
print(mi_set_up, ' valor de mi set up, recuerda cuantos 3 inclui??') 


'''
para comprobar si tenemos algo dentro de un set lo vamos a hacer como con las listas
'''

print(1 in mi_set_up, ' estara el 1??')

'''
incluir dentro de un set un nuevo valor
'''

mi_set_up.add(77)

# y varios valores a la vez
mi_set_up.update([88,99])

print(mi_set_up, ' add and update')

'''
eliminar algo de un set
'''
mi_set_up.remove(99)

print(mi_set_up, ' sin el 99')
# y limpiarlo por completo

mi_set_up.clear()
print(mi_set_up, ' esta limpito')

'''
tambiem podemos borrar el set por completo
'''
del mi_set_up

'''
podemos convertirlo a una lista para poder trabajar de otra forma con los datos
que tiene el set
'''
mi_set_up = {1,2,4}

mi_set_up_to_list = list(mi_set_up)

mi_set_up_to_list.append(4)

print(mi_set_up_to_list, ' la lista')

# ahora volvamos a transformar la lista en un nuevo set

nuevo_set = set(mi_set_up_to_list)
print(nuevo_set, 'es un set nuevo')

'''
podemos unir los set, es similar a las listas pero no usamos el operador +
'''

nuevo_set.add(111) # incluyo un valor para que se vea el resultado de la union

sets_unidos = mi_set_up.union(nuevo_set)
print(sets_unidos, ' la union hace la fuerza')


'''
encontrar los elementos comunes entre 2 sets
'''

numeros_de_hielo = {1,3,5,6,7,8,4,3,2}
numeros_de_fuego = {2,34,4,6,7,4,3,2,6}

# ahora queremos saber que cuales estan en ambos sets

numeros_al_vapor = numeros_de_hielo.intersection(numeros_de_fuego)

print(numeros_al_vapor, ' comprobando si hay numeros de fuego dentro de hielo')

'''
comprobar si un set puede ser parte de otro o si un set contiene los valores de otro

podriamos buscar un simil del tipo
tenemos un vaso de agua y tambien tenemos un cubo con agua

subset
el vaso de agua esta contenido dentro cubo

superset
el cubo contiene lo que tenga el vaso

vamos a ver un ejemplo

'''

set_a = {1,2,3,4}
set_b = {2,3}

print(set_a.issubset(set_b), ' set_a es un subset de set_b ???')
print(set_a.issuperset(set_b), ' set_a es un superset de set_b ???')

'''
encontrar la diferencia simetrica entre 2 sets
'''

print(set_a.symmetric_difference(set_b), ' los elementos diferentes de forma simetrica')

'''
comprobar que 2 sets no tienen ningun item en comun
'''

set_c = {6,7,8}

print(set_a.isdisjoint(set_b), ' no tienen items en comun? set_a y set_b')
print(set_a.isdisjoint(set_c), ' no tienen items en comun? set_a y set_c')