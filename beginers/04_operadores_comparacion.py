'''
Los comparadores son operadores que nos devuelven un resultado booleano(true/false)

podemos comparar desde numeros, cadenas hasta otras expresiones

vamos a ver los comparadores mas tipicos

'''

# igual ==

print(1==1) # true
print(1==0) # false

mi_cadena = 'hola'

print(mi_cadena == 'hola') # true
print(mi_cadena == 2) # false

# distinto !=

print(1 != 1) # false
print(1 != 0) # true

# mayor >

print(1 > 1) # false
print(1 > 0) # true

# mayor o igual >=

print(1 >= 1) # true
print(1 >= 0) # true

# menor <
print(1 < 1) # false
print(1 < 0) # false

# menor o igual <=

print(1 <= 1) # true
print(1 <= 0) # false

'''
hasta aqui podemos definir si una condicion se cumple o no

pero seguramente necesites mirar mas de una comparacion a la vez

y par eso tenemos los operadores logicos
'''

# and --> que el resultado de 2 expresiones sea true
print(1==1 and 2<3) # true
print(1==1 and 1!=1) # false

# or --> que se cumpla al menos una de las expresiones
print(1==1 or 2<3) # true
print(1==1 or 1!=1) # true

# not --> una negacion, niega el resultado de la siguiente expresion
print(1==1 and not 2<3) # false
print(1==1 and not 1!=1) # true

'''
por ultimo podrias hacer varias comparaciones con cadenas y tenerlas tu en el codigo
'''




