from abc import ABCMeta, abstractmethod

class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)
print(c)

# Salida -> Color azul, 4 ruedas, 150 km/h, 1200 cc


class A:
    def __init__(self):
        print("Soy de clase A")

    def a(self):
        print("Este método es de A")


class B:
    def __init__(self):
        print("Soy de clase B")

    def a(self):
        print("Este método es de B")


class C(B, A):
    def c(self):
        print("Este método es de C")


def ejecutar(obj1, obj2, obj3):
    lst = [obj1, obj2, obj3]
    for obj in lst:
        obj.a()


objetos = {"obj1": A(),
           "obj2": B(),
           "obj3": C()}

ejecutar(**objetos)


def bitacora(funcion):
    def escribo(*args):
        print ("Escribo en bitácora que el alumno rinde la materia:" , args[1])
        retorno = funcion(*args)
        return retorno
    return escribo

from abc import ABCMeta, abstractmethod
class Estudiante(metaclass=ABCMeta):

    @abstractmethod
    def rendir(self, materia):
        pass

    def ingresar(self):
        print("Ingresando al establecimiento...")

class EstudianteUniversitario(Estudiante):
    @bitacora
    def rendir(self, materia):
        return "Rindiendo materia " + materia

estudiante_universitario = EstudianteUniversitario()
estudiante_universitario.ingresar()
print(estudiante_universitario.rendir("Geografía"))

try:
    estudiante = Estudiante() #Verificar la Exception
    estudiante.ingresar()
except Exception as exp:
    print(exp)
