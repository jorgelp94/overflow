

from memoria import *
from overflow import *


def ejecutaMaquina(directorio, cuadruplos, constantes):
	print("------------------")
	print("INICIA MV")
	print("------------------")
	
	nombre_programa = directorio.keys()[0]
	stack_memoria = []
	saltos = []
	cont_cuadruplos = 0
	retunValue = None

	# Se inicializa la memoria global y local
	memoria_global = Memoria(nombre_programa, directorio[nombre_programa]['Variables Globales']['Memoria'], directorio[nombre_programa]['Temporales']['Memoria'])
	memoria_activa = Memoria('main', directorio[nombre_programa]['Variables Locales']['Memoria'], directorio[nombre_programa]['Temporales']['Memoria'])
	memoria_nueva = ""

	# Funcion que resuelve todos los cuadruplos que se generaron en compilacion
	while cuadruplos[cont_cuadruplos][0] != 'ENDPROGRAM':
		cuadruplo = cuadruplos[cont_cuadruplos]
		#print(cuadruplo)

		if cuadruplo[0] == 'SUMA':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]
			guarda =cuadruplo[3]

			op1 = str(op1)
			if op1.find('(') != -1: # si encuentra ( ) tiene una direccion relativa

				otro = op1.replace("(", "") # quita los ( ) de la direccion relativa
				otro2 = otro.replace(")", "")
				op1 = int(otro2) # convertir a entera la direccion

				if op1 >= 20000 and op1 < 30000:
					valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
				else:
					valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)
				if valorOp1 < 0:
					print("Error: indice de arreglo no puede ser negativo.")
					exit()
				sumale = valorOp1 + op2 # suma el valor de la direccion relativa a la direccion base
				sumale = int(sumale) # genera una nueva direccion para accesar el arreglo

				if sumale >= 20000 and sumale < 30000:
					valorOp2 = memoria_global.getValorDeDireccion(sumale, constantes)
				else:
					valorOp2 = memoria_activa.getValorDeDireccion(sumale, constantes)

				result = valorOp2 # obtiene el valor de la direccion del arreglo


			else:
				# es una suma normal
				op1 = int(op1)

				if op1 >= 20000 and op1 < 30000: # verifica si es global
					valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
				else:
					valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

				if op2 >= 20000 and op2 < 30000: # verifica si es global
					valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
				else:
					valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)

				result = valorOp1 + valorOp2  # se realiza la suma de los valores

			memoria_activa.setValorDeDireccion(guarda, result) # guarda el resultado en la direccion que recibe

		elif cuadruplo[0] == 'RESTA':
			op1 = cuadruplo[1]
			op2 = cuadruplo[2]

			if op1 >= 20000 and op1 < 30000: # verifica si es global
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			if op2 >= 20000 and op2 < 30000: # verifica si es global
				valorOp2 = memoria_global.getValorDeDireccion(op2, constantes)
			else:
				valorOp2 = memoria_activa.getValorDeDireccion(op2, constantes)


			result = valorOp1 - valorOp2 # se realiza la resta de los valores
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


			result = valorOp1 * valorOp2 # se realiza la multiplicacion de los valores
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


			result = valorOp1 / valorOp2 # se realiza la division de los valores
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


			result = valorOp1 < valorOp2 # se realiza la comparacion de los valores
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


			result = valorOp1 > valorOp2 # se realiza la comparación de los valores
			guarda =cuadruplo[3] # direccion donde se guardara el resultado
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

			# convierte el valor del string 'true' o 'false' a True o False y despues compara
			if valorOp1 == 'true':
				valorOp1 = True
			elif valorOp1 == 'false':
				valorOp1 = False
			
			if valorOp2 == 'true':
				valorOp2 = True
			elif valorOp2 == 'false':
				valorOp2 = False

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

			# convierte el valor del string 'true' o 'false' a True o False y despues compara
			if valorOp1 == 'true':
				valorOp1 = True
			elif valorOp1 == 'false':
				valorOp1 = False
			
			if valorOp2 == 'true':
				valorOp2 = True
			elif valorOp2 == 'false':
				valorOp2 = False

			result = valorOp1 or valorOp2
			guarda =cuadruplo[3]

			memoria_activa.setValorDeDireccion(guarda, result)


		elif cuadruplo[0] == 'ASIG':
			op1 = cuadruplo[1]

			if len(cuadruplo) == 5: # si viene un quintuplo, es una asignacion para un arreglo
				if retunValue != None:
					valorOp1 = retunValue
					retunValue = None
				else:
					if op1 >= 20000 and op1 < 30000:
						valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
					else:
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


				guarda = cuadruplo[3] + sumale # suma el calor de la direccion relativa a la direccion base para obtener la posicion del arreglo
				guarda = int(guarda)

			else: # asignacion normal
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
			cont_cuadruplos = nuevaPosicion - 1 # salta a una nueva direccion de cuadruplo


		elif cuadruplo[0] == 'ERA':
			nombre = cuadruplo[1].lower()
			# inicializa la memoria nueva de la funcion que se manda llamar
			memoria = directorio[nombre_programa]['Funciones'][nombre]['Memoria']
			temps = directorio[nombre_programa]['Temporales']['Memoria']
			memoria_nueva = Memoria(nombre, memoria, temps)

		elif cuadruplo[0] == 'GOSUB':
			saltos.append(cont_cuadruplos)
			nombre = cuadruplo[1].lower()
			# almacena a cual cuadruplo va regresar cuando terine la funcion
			salto = directorio[nombre_programa]['Funciones'][nombre]['Start']
			cont_cuadruplos = salto - 1
			# se guarda la memoria actual en un stack y se asgigna la nueva memoria a la actual
			stack_memoria.append(memoria_activa)
			memoria_activa = memoria_nueva

		elif cuadruplo[0] == 'RETURN':
			valor = cuadruplo[1]
			if valor >= 20000 and valor < 30000:
				retorno = memoria_global.getValorDeDireccion(valor, constantes)
			else:
				retorno = memoria_activa.getValorDeDireccion(valor, constantes)

			# guarda el valor de retorno en una variable global
			retunValue = retorno


		elif cuadruplo[0] == 'RET':
			# hace el cambio de memoria y regresa la memoria del main
			memoria_activa = stack_memoria.pop()
			cont_cuadruplos = saltos.pop()
			

		elif cuadruplo[0] == 'PARAM':
			op1 = cuadruplo[1]

			if op1 >= 20000 and op1 < 30000:
				valorOp1 = memoria_global.getValorDeDireccion(op1, constantes)
			else:
				valorOp1 = memoria_activa.getValorDeDireccion(op1, constantes)

			guarda = cuadruplo[3]

			# le asigna el valor que se envia como parametro a la nueva memoria y lo almacena

			memoria_nueva.setValorDeDireccion(guarda, valorOp1)

		elif cuadruplo[0] == 'GOTOF':
			salto = cuadruplo[3]
			verifica = cuadruplo[1]

			# salta entre cuadruplos si el resultado de la expresion es falsa

			res = memoria_activa.getValorDeDireccion(verifica, constantes)
			if res == False:
				cont_cuadruplos = salto-1



		elif cuadruplo[0] == 'PRINT':
			valor = cuadruplo[1]

			if valor >= 20000 and valor < 30000:
				retorno = memoria_global.getValorDeDireccion(valor, constantes)
			else:
				retorno = memoria_activa.getValorDeDireccion(valor, constantes)

			# imprime el valor de la direccion que recibe una vez que lo obtiene

			print(retorno)



		cont_cuadruplos += 1
		

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
