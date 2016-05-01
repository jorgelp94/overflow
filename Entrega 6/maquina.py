

from memoria import *
from overflow import *


def ejecutaMaquina(directorio, cuadruplos, constantes):
	print("------------------")
	print("INICIA MV")
	print("------------------")
	print(directorio)
	print(cuadruplos)
	print(len(cuadruplos))
	nombre_programa = directorio.keys()[0]
	cuadruplos[len(cuadruplos)] = ['ENDD', '', '', '']
	print(cuadruplos)
	stack_memoria = []

	cont_cuadruplos = 0

	memoria_global = Memoria(nombre_programa, directorio[nombre_programa]['Variables Globales']['Memoria'])
	memoria_activa = Memoria('main', directorio[nombre_programa]['Variables Locales']['Memoria'])

	while cuadruplos[cont_cuadruplos][0] != 'ENDD':
		cuadruplo = cuadruplos[cont_cuadruplos]

		if cuadruplo[0] == 'SUMA':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 + valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)

		elif cuadruplo[0] == 'RESTA':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 - valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)

		elif cuadruplo[0] == 'MULT':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 * valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'DIV':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 / valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'MENOR':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 < valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'MAYOR':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 > valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'IGUAL':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 == valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'MAYORIG':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 >= valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)

		elif cuadruplo[0] == 'MENORIG':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 <= valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)

		elif cuadruplo[0] == 'DIF':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 != valorOp2
			guarda =cuadruplo[3]
			
			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'AND':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			
			result = valorOp1 and valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)

		elif cuadruplo[0] == 'OR':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000:
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

			result = valorOp1 or valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'ASIG':
			op1 = cuadruplo[1]
			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			guarda = cuadruplo[3]
			if guarda >= 20000 and guarda < 30000:
				memoria_global.setValorDeDireccion(guarda, valorOp1)
			else:
				memoria_activa.setValorDeDireccion(guarda, valorOp1)




			
		cont_cuadruplos += 1
		#print(cont_cuadruplos)


	print(memoria_global.name)
	print(memoria_global.ints)
	print(memoria_global.floats)
	print(memoria_global.chars)
	print(memoria_global.bools)
	print(memoria_global.temp_int)
	print(memoria_global.temp_float)
	print(memoria_global.temp_char)
	print(memoria_global.temp_bool)
	print(memoria_activa.name)
	print(memoria_activa.ints)
	print(memoria_activa.floats)
	print(memoria_activa.chars)
	print(memoria_activa.bools)
	print(memoria_activa.temp_int)
	print(memoria_activa.temp_float)
	print(memoria_activa.temp_char)
	print(memoria_activa.temp_bool)


