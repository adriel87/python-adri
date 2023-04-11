# que es??
datetime es un modulo dentro de python para trabajar con fechas y tiempo

## importarlo

```python
from datetime import datetime
```

## utilidades

```python
from datetime import datetime

# get actual time

now = datetime.now()

# get day, month, year, min.....

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

# get actual timestamp

timestamp = now.timestamp

```

## formateando la fecha

```python
now = datetime.now()

# vamos a usar un metodo de formateo dentro de now
# strftime

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

```

Tambien podemos usar otro formatos de entrada para poder obtener una fecha

por el ejemplo `20 april, 2022` 

```python
from datetime import datetime

fecha_en_string = '20 april, 2022'

fecha = datetime.strptime(fecha_en_string, "%d %B, %Y")
print(fecha)

```

## una fecha en concreto

desde datetime podemos usar date, que con una serie de parametros nos devolvera la fecha

```python
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
```

## un tiempo concreto

por tiempo me refiero a un momento del dia en concreto

```python
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
```
# diferencia entre fechas y horas

podemos restar fechas sin complicacion con el operadore de resta

```python
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00


'''
tambien podemos usar el metodo timedelta 
'''
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

```

