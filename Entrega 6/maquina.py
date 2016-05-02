

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
	stack_memoria = []
	saltos = []
	cont_cuadruplos = 0
	retunValue = None

	memoria_global = Memoria(nombre_programa, directorio[nombre_programa]['Variables Globales']['Memoria'])
	memoria_activa = Memoria('main', directorio[nombre_programa]['Variables Locales']['Memoria'])
	memoria_nueva = ""

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
	print("------------------------------------------------------------------------------------")

	while cuadruplos[cont_cuadruplos][0] != 'ENDPROGRAM':
		cuadruplo = cuadruplos[cont_cuadruplos]
		print(cuadruplo)
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

			print(valorOp2)
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
			
			if len(cuadruplo) == 5:
				if retunValue != None:
					valorOp1 = retunValue
					retunValue = None
				else:
					if op1 >= 20000 and op1 < 30000:
						valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
					else:
						print(op1)
						valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)
				
				valorAgregado = cuadruplo[4]
				
				# quita los ( ) de la direccion relativa
				otro = valorAgregado.replace("(", "")
				otro2 = otro.replace(")", "")
				valorAgregado = int(otro2)


				if valorAgregado >= 20000 and valorAgregado < 30000:
					sumale = memoria_global.getValorDeDireccion(valorAgregado, constantes)
				else:
					sumale = memoria_activa.getValorDeDireccion(valorAgregado, constantes)

				
				guarda = cuadruplo[3] + sumale
				guarda = int(guarda)

			else:
				if retunValue != None:
					valorOp1 = retunValue
					retunValue = None
				else:
					if op1 >= 20000 and op1 < 30000:
						valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
					else:
						valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)
			
				guarda = cuadruplo[3]
			

			if guarda >= 20000 and guarda < 30000:
				memoria_global.setValorDeDireccion(guarda, valorOp1)
			else:
				memoria_activa.setValorDeDireccion(guarda, valorOp1)


		elif cuadruplo[0] == 'GOTO':
			nuevaPosicion = cuadruplo[3]
			cont_cuadruplos = nuevaPosicion - 1


		elif cuadruplo[0] == 'ERA':
			nombre = cuadruplo[1].lower()
			memoria = directorio[nombre_programa]['Funciones'][nombre]['Memoria']
			memoria_nueva = Memoria(nombre, memoria)

		elif cuadruplo[0] == 'GOSUB':
			saltos.append(cont_cuadruplos)
			nombre = cuadruplo[1].lower()
			salto = directorio[nombre_programa]['Funciones'][nombre]['Start']
			cont_cuadruplos = salto - 1
			stack_memoria.append(memoria_activa)
			memoria_activa = memoria_nueva

		elif cuadruplo[0] == 'RETURN':
			valor = cuadruplo[1]
			if valor >= 20000 and valor < 30000:
				retorno = memoria_global.getValorDeDireccion(valor, constantes)
			else:
				retorno = memoria_activa.getValorDeDireccion(valor, constantes)

			retunValue = retorno


		elif cuadruplo[0] == 'RET':
			memoria_activa = stack_memoria.pop()
			cont_cuadruplos = saltos.pop()
			print(memoria_activa.name)
			print(memoria_activa.ints)
			print(memoria_activa.floats)
			print(memoria_activa.chars)
			print(memoria_activa.bools)
			print(memoria_activa.temp_int)
			print(memoria_activa.temp_float)
			print(memoria_activa.temp_char)
			print(memoria_activa.temp_bool)

		elif cuadruplo[0] == 'PARAM':
			op1 = cuadruplo[1]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			guarda = cuadruplo[3]

			memoria_nueva.setValorDeDireccion(guarda, valorOp1)

		elif cuadruplo[0] == 'GOTOF':
			salto = cuadruplo[3]
			verifica = cuadruplo[1]
			res = memoria_activa.getValorDeDireccion(verifica, constantes)
			if res == False:
				cont_cuadruplos = salto-1

		elif cuadruplo[0] == 'PRINT':
			valor = cuadruplo[1]

			if valor >= 20000 and valor < 30000:
				retorno = memoria_global.getValorDeDireccion(valor, constantes)
			else:
				retorno = memoria_activa.getValorDeDireccion(valor, constantes)

			print(retorno)



		cont_cuadruplos += 1
		#print("Contador cuadruplos: %s" % cont_cuadruplos)
		


		# print(memoria_global.name)
		# print(memoria_global.ints)
		# print(memoria_global.floats)
		# print(memoria_global.chars)
		# print(memoria_global.bools)
		# print(memoria_global.temp_int)
		# print(memoria_global.temp_float)
		# print(memoria_global.temp_char)
		# print(memoria_global.temp_bool)
		# print(memoria_activa.name)
		# print(memoria_activa.ints)
		# print(memoria_activa.floats)
		# print(memoria_activa.chars)
		# print(memoria_activa.bools)
		# print(memoria_activa.temp_int)
		# print(memoria_activa.temp_float)
		# print(memoria_activa.temp_char)
		# print(memoria_activa.temp_bool)
		# print("------------------------------------------------------------------------------------")
		


	



