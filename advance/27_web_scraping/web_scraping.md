# que es ?

El web scraping es una tecnica con la que podemos obtener informacion sobre una pagina web

basicamente consiste en ir recorriendo el documento HTML y coger los datos que nos interesan de esa web

desde imagenes a archivos o comentarios

## como hacer esto en python

para ello vamos a usar las siguientes 2 librerias
- request
- BuautifulSoup

```python
import requests
from bs4 import BeautifulSoup
```

una vez que la tengamos hace un get a la pagina que queramos scrapear

