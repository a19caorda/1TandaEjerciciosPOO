import copy

from Ej1 import Tiempo
from Ej2 import Fraccion
from Ej3 import Fecha


def createTime() -> Tiempo:
    horas = int(input("   Inserte horas: "))
    minutos = int(input(" Inserte minutos: "))
    segundos = int(input("Inserte segundos: "))

    return Tiempo(horas, minutos, segundos)


def createFraccion() -> Fraccion:
    numerador = int(input("  Inserte el numerador: "))
    denominador = int(input("Inserte el denominador: "))

    return Fraccion(numerador, denominador)


print("\n------------------Test de las clases------------------")

print()
print("Ejercicio 1. Clase Tiempo")
print()

print("Cree una instancia de la clase tiempo")
time = createTime()
print(f"Has introducido {time}")
print()

print("Cree otra instancia de la clase tiempo")
time2 = createTime()
print(f"Has introducido {time2}")
print()

time.SumarTiempo(time2)
print(f"La suma de los objetos es: { time }")
print(f"Ahora la primera instancia de Tiempo es {time}")

print()
print("Ejercicio 2. Clase Fracción")
print()

print("Cree una instancia de la clase fraccion")
frac = createFraccion()
print(f"Has introducido {frac}, cuyo resultado es {frac.resultado()}")
frac.Simplificar()
print(f"Has introducido {frac}")
print()

print("Cree otra instancia de la clase fraccion")
frac2 = createFraccion()
fracT = copy.copy(frac)
fracT.SumarFraccion(frac2)
print(f"La suma de las dos fracciones es { fracT }")

fracT = copy.copy(frac)
fracT.MulFraccion(frac2)
print(f"La multiplicacion de las dos fracciones es { fracT }")
