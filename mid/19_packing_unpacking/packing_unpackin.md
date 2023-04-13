# que es ? 

desempaquetar o empaquetar, basicamente es una sintaxis que nos ayuda a guardar o coger variables de forma rapida de un objeto

## unpacking

veamos la sintaxis para desempaquetar

### sintaxis

```python
list = [a,b,c,d]

# vamos a usar el * para colocar los 3 ultimos valores aparte

first , *rest = list

# ahora el ejemplo de una funcion

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

```

podemos hacer esto mismo pero con listas

```python
# en este caso se usa **

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

```

## packing

podemos usar una sintaxis similar pero para una entrada de una funcion

### sintaxis

```python
# listas
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# diccionarios
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

