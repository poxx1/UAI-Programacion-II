#Excepciones...
def division(a, b):
        return a / b

def calcular():
    division(1, 0)

#calcular()

try:
    num = 33
except (NameError, ValueError): #NameError cuando una variable local o global no se encuentra, ValueError cuando un parámetro no es del tipo esperado...
    print ("Ocurrio un error")
else:
    print("Todo está bien")

try:
    z = 10 / 0
except ZeroDivisionError as d:
    print ("Division por cero", d)
finally:
    print("Limpiando")


class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return "Error " + str(self.valor)

try:
    if 40 > 20:
        raise MiError(33)
except MiError as e:
    print (e)


import modulo
modulo.mi_funcion()
clase = modulo.MiClase()


from modulo import *
a = MiClase()
mi_funcion()

from Paquete.BBDD import test
test()

import Paquete.DAO.dal as b
b.test_dao()






