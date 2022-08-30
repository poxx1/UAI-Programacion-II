# Módulos
import pygame, sys
from pygame.locals import * #Para tener QUIT
 
# Constantes
WIDTH = 640
HEIGHT = 480

# Clases
# --------------------------------------------------------------------- 
# ---------------------------------------------------------------------
 
# Funciones
# --------------------------------------------------------------------- 
# ---------------------------------------------------------------------

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Test Pygame")
    
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0
 
if __name__ == '__main__':
    pygame.init()
    #main()


#Collections
#ChainMap
from collections import ChainMap
 
dict_a = {'a': 1, 'b': 10}
dict_b = {'b': 100, 'c': 1000}
 
cm = ChainMap(dict_a, dict_b)
for key, value in cm.items():
    print(key, value)    

print(cm.maps)

#Counter

from io import StringIO
from collections import Counter
 
virtual_file = StringIO("""2010/01/01 2.7
2010/01/02 2.2
2010/01/03 2.1
2010/01/04 2.3
2010/01/05 2.4
2010/01/06 2.2
2010/01/02 2.2
2010/01/03 2.1
2010/01/04 2.3
""")

print(Counter(virtual_file.readlines()).most_common(1))

#namedtuple

import numpy as np
import datetime as dt
from pprint import pprint

datos = {
    'valores': np.random.randn(100),
    'frecuencia': dt.timedelta(minutes = 10),
    'fecha_inicial': dt.datetime(2016, 1, 1),
    'parametro': 'wind_speed',
    'unidades': 'm/s'
}

pprint(datos)


from collections import namedtuple
 
Datos = namedtuple('Datos', 'valores frecuencia fecha_inicial parametro unidades')
 
datos = Datos(np.random.randn(100), 
              dt.timedelta(minutes = 10),
              dt.datetime(2016, 1, 1),
              'wind_speed',
              'm/s')
print(datos)
print(datos.valores)


class DatosExtendidos(Datos):
    def media(self): 
        "Calcula la media de los valores." 
        return self.valores.mean()

datos_ext = DatosExtendidos(**datos._asdict())
#** Desempaqueta un diccionario como parámetros de una función

print(datos_ext.media())


#deque
from collections import deque
 
dq = deque(range(10), maxlen = 10)
lst = list(range(10))
print(dq)
print(lst)

# los tres últimos elementos los anexa nuevamente al principio de la secuencia.
dq.rotate(3)
print(dq)
lst = lst[-3:] + lst[:-3] #Podría hacer lo mismo con listas y slicing
print(lst)

dq.append(100)
print(dq)
dq.appendleft(10000)
print(dq)

dq.extend(range(11))
print(dq)
dq.extendleft([10, 100])
print(dq)

#numPy y matplotlib

import numpy
from matplotlib import pyplot
x = numpy.linspace(0, 2 * numpy.pi, 100)
y = numpy.sin(x)
pyplot.plot(x, y)
pyplot.show()

#SQLAlchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.sql import select
from sqlalchemy import Table, Column, Integer, String, MetaData

import urllib
params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=.\SQLEXPRESS;"
                                 "DATABASE=Security;"
                                 "UID=test;"
                                 "PWD=qwerty")

engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

conn = engine.connect()

metadata = MetaData()
Usuario = Table('Usuario', metadata,
            Column('idUsuario', String, primary_key=True),
            Column('Nombre', String))

s = select([Usuario])

result = conn.execute(s)

for row in result:
    print(row)


#Requests

import requests
r = requests.get('https://api.github.com/repos/psf/requests')
print(r.json()["description"])


#PIL

from PIL import Image
from PIL import ImageFont 
from PIL import ImageDraw 

img = Image.new('RGB', (800, 400), "white") 
draw = ImageDraw.Draw(img) 
font = ImageFont.truetype("LiberationSerif-Regular.ttf", 36) 
draw.text((20, 20),"UAI-PROGRAMACIÓN II",(0,2,27),font=font) 
img.save('image.png')