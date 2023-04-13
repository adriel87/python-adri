# que es ??
en este caso vamos a ver como es el modulo de regex que tenemos en python

regex es la forma corta de hacer referencia al termino de expresiones regulares

las expresiones regulares se utilizan para encontrar de forma relativamente sencilla patrones definidos en mediante la expresion dentro de una cadena.

## El modulo

para usar regex necesitamos importar el modulo correspondiente

```python
import re
```

## metodos

vamos a ver algunos de los metodos que tiene el modulo

```python
re.match() # busca dentro de la primera linea de la cadena y devuelve el objeto si lo encuentra en caso contrario no

re.search # devuelve el objeto si lo encuentra incluso en cadenas multilinea

re.findall # devuelve una lista con todos los matches

re.split # coge una cadena y la parte en donde coincida con la expresion

re.sub #reemplaza una o mas matches con la string de reemplazo
```

## sintanxis

junto a la sintaxis vamos a ver algunos ejemplos de los metodos vistos arriba

- match

```python
re.match(substring, string, re.I)

import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach


```

- seach

```python
re.match(substring, string, re.I)


import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

- findall

```python
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']


'''
si no incluimos el ultimo parametro a la funcion Re.I
podemos identificar de varias formas que buscar
'''

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
```

- sub

```python
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

- split

```python
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol
```

## como hacer patrones RegEx

podemos definir un patron de la siguiente forma

```python
patron_regex = r'ondux'
# y luego usarlo en cualquiera de los metodos anteriores
matches = re.findall(regex_pattern, txt)
```

los patrones regex pueden seguir una serie de normas, miralas [aqui](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md)

### square bracket
