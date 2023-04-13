# que es ??

digamos que es algo asi como esparcir.

imagina que tienes 2 globos llenos de agua peque;os y un globo vacio

mediante el ***spread*** puedes rellenar el globo vacio

veamos un ejemplo en codigo

```python
globo_peque_1 = ["agua","agua","agua"]
globo_peque_2 = ["agua","agua"]

globo_vacio = [*globo_peque_1, *globo_peque_2]
# goblo_vacio ["agua","agua","agua","agua","agua"]
```

