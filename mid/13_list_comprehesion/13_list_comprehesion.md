# Que es
basicamente es otra sintaxis para trabajar con listas, nos permite crear las listas
de una forma rapida y sencilla

## sintaxis

```python
comprehesion = [i for i in interable <if expresion>]

# un ejemplo

numbers = [i for i in range(10)] # nos devuelve la isiguiente lista [0,1,2,3,4,5,6,7,8,9]

# usando el condicional

even_numbers = [i for i in range(10) if i % 2 == 0] #[0,2,4,6,8]

# usando un string como iterable

supe_name = 'aklfdhkjaehfkjhdaklfjalskjdhfkjsdhfkljsadhfjkahsdklfjhasd'
just_a = [i for i in supe_name if i == 'a']

```

un tip : lo que vasa  tener en la lista es lo que tienes a la izquierda del primer for

