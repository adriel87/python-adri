'''
vamos con los diccionarios o dictionaries
- los diccionarios son un tipo de datos que almacena cualquier cosa
- son mutables, por cierto mutable es que puede cambiar
- no tienen un orden definido

veamos un diccionario sencillito para entenderlo un poco
'''

diccionario_sencillo = {
    'name': 'trompaturtle',
    'age': 100
}

'''
si te fijas tiene una clave y un valor asociado a esa clave
en el ejemplo de arriba
las claves serian name y age
y sus valores respectivos son 
- para name, trompaturtle
- para age, 100
'''


'''
ahora veamos como se puede declarar un diccionario
'''

# o bien lo declaramos vacio

estoy_vacio = {}

# o bien lo incializamos, vamos como con el anterior

diccionario_sencillo = {
    'name': 'trompaturtle',
    'age': 100
}

# uno un poco mas complejo para que veas sus posibles usos
diccionario_sencillo = {
    'name': 'ondux',
    'age': 24,
    'games': ['Valorant', 'Diablo', 'El teto'],
    'is_vaca':True,
    'address':[
        {
            'street':'Space street',
            'zipcode':'02210'
        },
        {
            'street':'street of solitude',
            'zipcode':'060606'
        }
    ]
}

'''
Bueno veamos como en anteriores dias formas de trabajar con los diccionarios
'''

# len, nos devuelve la cantidad de claves que tiene el diccionario

print(len(diccionario_sencillo)) # 5

''' 
acceder a los valores de un diccionario
- podemos o bien usar la sintaxis de los corchetes indicando dentro la clave
  diccionario['clavesion']

en caso de que estemos completamente seguros de que existe esa clave en
ese diccionario no tendremos problemas, pero amigo si no existe la clave
tendras un error muy grande en el codigo

- o bien usar el metodo get de los diccionarios

  diccionario.get('clavesion') 

  si existe nos devolvera el valor
  y si no pues nos devolvera None

'''
# a corchete
diccionario_sencillo['name'] # ondux

diccionario_sencillo['address'][0]['street'] #Space street

# a metodo get

diccionario_sencillo.get('name') # ondux
diccionario_sencillo.get('trompa') # None

'''
incluir nuevos valores es relativamente facil 
entre corchetes indicamos la nueva clave y luego asignamos el valor

diccionario[nueva_clave] = valor

'''

diccionario_sencillo['is_pro_gamer'] = True


'''
modificar un valor de una clave en un diccionario tambien sigue el mismo patron

ya tenemos la clave name vamos a cambiarle el valor
'''

diccionario_sencillo['name'] = 'Onduxin'


'''
comprobar si existe una clave, esto es similar a usar el methodo get
pero en este caso nos devulve un valor booleano en caso de existir y no el valor

'estara_esto' in diccionario
'''

print('name' in diccionario_sencillo)
print('Trompa' in diccionario_sencillo)


'''
borrar claves de un diccionario, aunque no lo creas volvemos a usar pop y del, pero ademas incluimos
popItem
vamos a verlo en accion
'''

diccionario_sencillo.pop('name')
diccionario_sencillo.popitem() # elimina la ultima clave del diccionario
del diccionario_sencillo['is_pro_gamer']


'''
ahora veamos otro tipo de transformaciones que puede tener un diccionario
como:
    - pasarlo a lista
    - limpiarlo
    - borrarlo
    - copiarlo
    - obtener todas sus claves como una lista
    - obtener todos sus valores como una lista
'''

# pasarlo a lista
lista = diccionario_sencillo.items()

# obtener todas sus claves como lista
keys = diccionario_sencillo.keys()

# obtener todos sus valores como lista
values = diccionario_sencillo.values()

# copiarlo
la_copia = diccionario_sencillo.copy()

# limpiarlo
diccionario_sencillo.clear()

# eliminarlo
del diccionario_sencillo


