#Unificando funciones y objetos..
class Fruit:
    
    def check_ripeness(self):
        raise NotImplementedError("check_ripeness method not implemented!")

class Apple(Fruit):
    pass

try:
    a = Apple()
    a.check_ripeness() # Lanzo una excepción porque Apple no implementó el método check...
except Exception as e:
    print(e)


from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta): #Indico a la clase que es abstracta

    #Decoro los métodos abstractos
    @abstractmethod 
    def metodo_virtual_que_la_clase_hija_debe_implementar(self):
        pass

    def otro_metodo(self):
        print("Implementación...")

class SubClass(AbstractClass):
    def metodo_virtual_que_la_clase_hija_debe_implementar(self):
        return "Hello"

a = SubClass()
print(a.metodo_virtual_que_la_clase_hija_debe_implementar())       
a.otro_metodo() 

import sys 

if(len(sys.argv) > 1):
    print ("Abriendo " + sys.argv[1])
else: 
    print ("Debes indicar el nombre del archivo")

print ("Hola %s" % "mundo")
print ("%s %s" % ("Hola", "mundo"))

from math import pi
print ("%.4f" % pi)

print ("%.4s" % "hola mundo")
