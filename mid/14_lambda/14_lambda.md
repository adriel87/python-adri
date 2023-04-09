# que es 

una lambda es una funcion, 

***y que lo diferencia de una funcion normal ?***

pues su sintaxis, la forma en la que se escriben las lambdas puede hacer que tu codigo quede
mas limpio y compacto

```python
suma_2 = lambda a,b : a + b
```

## como usarla

pues tomemos de ejemplo la lambda que creamos arriba

```python
suma_2(1,1)
```

listo igual que una funcion.

Pero vamos a complicar un poco el asunto, usemos una lambda dentro de una funcion

```python
def print_name_multiplier(name):
    return lambda multiplier : multiplier * name

# ejecutemos la funcion
print_name_multiplier('adri')(10)
```