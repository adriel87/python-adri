# que es un modulo
un modulo o libreria es un conjunto de codigo que contiene una serie de funciones, variables
o codigo en general

## como crear un modulo

para ello necesitamos crear un archivo con extension de python y escribir el codigo en el
supongamos que queremos un modulo que entre sus funciones nos devuelva la suma entre 2 numeros

```python
# basic_calc.py
def sum_two_numbers(num_a, num_b):
    return num_a + num_b
```

ya tenemos el modulo creado, pero como lo usamos ahora

## usando el modulo

para ello nos vamos a otro archivo, en nuestro ejemplo lo vamos a ver con el archivo `main.py`

```python
import basic_calc

basic_calc.sum_two_numbers(1,2)

```
ahora bien no queremos importar la totalida de un modulo solo una parte

```python

from basic_calc import sum_two_numbers

sum_two_numbers(1,2)

```

### renombrando

no nos gusta como se llama la funcion por varios motivos
1. el nombre choca con otro nombre de otro modulo
2. es muy feo
3. y nos da la gana

```python

from basic_calc import sum_two_numbers as cute_sum

sum_two_numbers(1,2)

```

## modulos incluidos por Python

### OS

operaciones relacionadas con el sistema de carpetas del SO como:
- crear un directiorio
- obtener el directorio donde estamos
- elminarlo

```python
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

### SYS

nos da inforamcion relativa al sistema y funciones que tienen que ver con el mismo
tambien nos da accesos a las variables que podamos pasarle al ejecutar el script

```python
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

## STATISTICS

este modulo nos da una serie de funciones y variables para poder trabajar de forma comoda con 
estadisticas

```python
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Other modules

- math
- String
- random

