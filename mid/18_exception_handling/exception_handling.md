# que es??
las excepciones son otra forma para controlar el buen funcionamiento de nuestro programa

en terminos generales tenemos un bloque de prueba que es donde se intentara ejecutar el codigo

y un bloque donde se recoge el posible fallo

ademas en python podemos definir un bloque que se ejecutara si el bloque de prueba se ejecuta sin fallos
y el bloque que se ejecuta pase lo que pase

## sintaxis

```python

# bloque de prueba
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
# bloque de prueba
''''''
# bloque de fallo
'''
aqui podemos ademas definir el tipo de fallo que queremos recoger
y establecer mas de un bloque de fallo
'''
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
# bloque de fallo


# bloque si todo sale sin fallos
else:
    print('I usually run with the try block')
# bloque si todo sale sin fallos

# bloque que siempre se ejecuta
finally:
    print('I alway run.')
# bloque que siempre se ejecuta
```