# Que es?

las funciones en python se tratan como ciudadanos de primer nivel, suena chulo pero
basicamente es :

- una funcion puede tener una o mas funciones como paramatro
- una funcion puede devolver como resultado una funcion
- una funcion puede ser modificada
- una funcion puede ser asignada a una variable

## funcion como parametro

si tuviera que compararlo con otro lenguaje en Javascript serian los callbacks.

estas funciones se terminaran ejecutando dentro de otras funciones

```python

def sum_numbers(nums):
    return sum(nums)

def high_order_function(function, list):
    summ = function(list)
    return summ

result = high_order_function(sum_numbers, [1,2,3,4])

```

## devolviendo una funcion como valor

imagina que tenemos un repositorio de cosas que podemos hacer

pero que para acceder a esos metodos tenemos invocar a otro

```python
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b

def high_order_component(type):
    if type == 'suma':
        return sumar
    else:
        return restar

mi_function = high_order_component('suma')


mi_funcion(1,2)

```

## closure

acceder a algo fuera del escope de la misma funcion dentro de otra funcion. Esto se conoce como closure

para crear un closure en python debemos anidar una funcion dentro de otra
el valor de retorno de la funcion que encapsula es la funcion interna, mindfuck

```python
def closure_func():
    variable = 10
    def add(value):
        return variable + value
    return add
        
# ahora la usamos
result = closure_func()

print(result(5), result(10))

```

## decoradores

los decoradores por lo general son un patron de dise;o que nos da mas funcionalidad a la ya existente.

normalmente los decoradores se llaman antes de declarar la funcion a la que se le quiere dar la
nueva funcionalidad

```python
# primero creamos la funcion decoradora
def upper_case_decorator(function):
    # necesitamos englobar la funcion que vamos a recibir
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@upper_case_decorator
def saludar():
    return 'Hi everyone'


print(saludar())
```

Se pueden aplicar mas de un decorador a la misma funcion

Ademas los decoradores pueden aceptar parametros ademas de la misma funcion

```python
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## funciones de python como HOF

- map, ejecuta sobre un elemento una funcion
- filter, filtra sobre una condicion si es true devuelve
- reduce, hace transformaciones con el elemento previo y el actual. devuelve un valor

estas funciones se prestan mucho a usar las lambdas, por que suelen ser procesos relativamente sencillos

estas funciones se pueden usar mientrar el segundo parametro que le pasemos se pueda iterar


```python
numbers = [1,2,3,4]

# map con funcion normal
def add_ten(number):
    return number + 10

new_numbers = map(add_ten, numbers)

# map con lambda

new_numbers = map(lambda n: n + 10, numbers)

# filter funcion normal
words = ['', 'asdfa', 'lala']

def not_empty_string(str):
    return True if len(str) > 0 else False

result = filter(not_empty_string, words)

# filter lambda

result = filter(lambda str: len(str)>10 , words)

# reduce funcion normal

numbers = [1,2,3,4]

def sum_all(a,b):
    return a + b

result = reduce(sum_all, numbers)

# reduce con lambda

result = reduce(lambda a,b: a+b, numbers)


```