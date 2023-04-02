'''
vamos ver una serie de funciones utiles que precarga python

pero antes 
que es una funcion?

basicamente es un bloque de codigo que puedes ejecutar siempre que lo necesites
dentro de ese bloque codigo vas a tener una serie de instrucciones que se ejecutaran
siempre que se llame/invoque esa funcion

de todos modos veremos esto un poco mas tarde cuando aprendamos a definir nuestras propias
funciones
'''

# imprimir algo por pantalla

print('hola ', sep='soy el separador', end='y yo termino')
print('\n---------------------------------------------------')
print('hola ', ' el serparador solo sale si tenemos algo que separar', sep='soy el separador', end='y yo termino')
print('\n---------------------------------------------------')

# conocer la longitud de una cadena/array/set/diccionario
array_size = len([1,2,3])
cadena_size = len('ahora soy la cadena')
set_size = len({123,3,4})
dicccionario_size = len({'lala':1, 'lele':2})

print(array_size,' el array')
print(cadena_size, 'la cadena')
print(set_size,' el set')
print(dicccionario_size, 'diccionario')

# solicitar datos a un usuario en la terminal

tu_entrada = input('\n\nescribes algo para mi?  ')

print('voy a adivinar lo que acabas de escribir ==> ', tu_entrada, end='\n')


# conversores srt, float, int, bin ...

me_quiero_convertir = 7

ahora_soy_str = str(me_quiero_convertir)
ahora_soy_float= float(me_quiero_convertir)
ahora_soy_binario= bin(me_quiero_convertir)

print('este soy yo ', me_quiero_convertir, ' pero me quiero convertir')
print(ahora_soy_str, type(ahora_soy_str), sep=' ahora soy del tipo ==> ')
print(ahora_soy_float, type(ahora_soy_float), sep=' ahora soy del tipo ==> ')
print(ahora_soy_binario, type(ahora_soy_binario), sep=' ahora soy del tipo ==> ')

'''
si te fijas bien una vez que el numero se convierte cambia su tipo
pero con el numero dice qeu su tipo es str, esto es por que el retorno de la funcion determia el tipo

si quieres ver mas sobre las funciones del sistema En el readme tienes el enlace a la docu oficial
'''
