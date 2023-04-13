# que es ??

aunque te suene de otros lenguajes, basicamente es para poder iterar sobre un objeto iterable
pero teniendo la capacidad de tener un indice

```python

for index, item in enumerate([20, 30, 40]):
    print(index, item)


for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')
```