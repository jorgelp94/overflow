

from memoria import *
from overflow import *


def ejecutaMaquina(directorio, cuadruplos):
	print("------------------")
	print("INICIA MV")
	print("------------------")
	print(directorio)
	print(cuadruplos)

	nombre_programa = directorio.keys()[0]

	stack_memoria = []

	cont_cuadruplos = 0

	memoria_global = Memoria(nombre_programa, directorio[nombre_programa]['Variables Globales']['Memoria'])
	print(memoria_global.name)
	print(memoria_global.ints)
	print(memoria_global.floats)
	print(memoria_global.chars)
	print(memoria_global.bools)

	memoria_activa = Memoria('main', directorio[nombre_programa]['Variables Locales']['Memoria'])
	print(memoria_activa.name)
	print(memoria_activa.ints)
	print(memoria_activa.floats)
	print(memoria_activa.chars)
	print(memoria_activa.bools)

