
from overflow import *

class Memoria:

	def __init__(self, name, memoria, temporales):
		self.name  = name
		# inicializa la memoria por tipo de datos
		self.ints  = memoria['INT'] * [""]
		self.floats = memoria['FLOAT'] * [""]
		self.chars = memoria['CHAR'] * [""]
		self.bools = memoria['BOOL'] * [""]
		# inicializa los temporales por tipos
		self.temp_int = 20 * [""]
		self.temp_float = 20 * [""]
		self.temp_bool = 20 * [""]
		self.temp_char = 20 * [""]
		# self.temp_int = temporales['TEMP INT'] * [""]
		# self.temp_float = temporales['TEMP FLOAT'] * [""]
		# self.temp_bool = temporales['TEMP BOOL'] * [""]
		# self.temp_char = temporales['TEMP CHAR'] * [""]


	def offsetDireccion(self, direccion):
		# funcion que calcula el offset y tipo de una direccion recibida
		addressScope = self.scopeDireccion(direccion)[1]

		offset = direccion - addressScope
		if offset >= 0 and offset < 2500:
			return ['INT', 0]
		elif offset >= 2500 and offset < 5000:
			return ['FLOAT', 2500]
		elif offset >= 5000 and offset < 7500:
			 return ['CHAR', 5000]
		elif offset >= 7500 and offset < 10000:
			return ['BOOL', 7500]
		else:
			return "Error"

	def scopeDireccion(self, direccion):
		# funcion que regresa el scope y la direccion base de una direccion recibida
		if direccion >= 10000 and direccion < 20000:
			return ['Local', 10000]

		elif direccion >= 20000 and direccion < 30000:
			return ['Global', 20000]

		elif direccion >= 30000 and direccion < 40000:
			return ['Temporales', 30000]

		elif direccion >= 40000 and direccion < 50000:
			return ['CONSTANTE', 40000]

		elif direccion >= 50000 and direccion < 60000:
			return ['Funcion', 50000]
		else:
			return ['Error', 9999999]


	def memoriaActual(self, scope, tipo):
		# funcion que regresa la memoria requerida en base al scope
		if scope == 'Global' or scope == 'Funcion' or scope == 'Local':
			if tipo == 'INT':
				return self.ints
			elif tipo == 'FLOAT':
				return self.floats
			elif tipo == 'CHAR':
				return self.chars
			elif tipo == 'BOOL':
				return self.bools
		elif scope == 'Temporales':
			if tipo == 'INT':
				return self.temp_int
			elif tipo == 'FLOAT':
				return self.temp_float
			elif tipo == 'CHAR':
				return self.temp_char
			elif tipo == 'BOOL':
				return self.temp_bool


	def getValorDeDireccion(self, direccion, constantes):

		# funcion que regresa el valor almacenado en memoria al recibir una direccion
		scope = self.scopeDireccion(direccion)[0]
		tipo = self.offsetDireccion(direccion)[0]
		if scope != 'CONSTANTE': # si no es una constante, busca en la misma memoria
			dirBase = self.scopeDireccion(direccion)[1]
			offset = self.offsetDireccion(direccion)[1]
			real = direccion - dirBase - offset
			mem = self.memoriaActual(scope, tipo)
			return mem[real]
		else: # busca la constante en base a la direccion
			keys = constantes.keys()
			cons = constantes[keys[0]]
			cantidad = len(constantes.keys())
			i = 0
			while i < cantidad:
				if constantes[keys[i]]['Dir'] == direccion:
					return keys[i]
				i += 1


	def setValorDeDireccion(self, direccion, valor):
		scope = self.scopeDireccion(direccion)[0]
		tipo = self.offsetDireccion(direccion)[0]
		dirBase = self.scopeDireccion(direccion)[1]
		offset = self.offsetDireccion(direccion)[1]
		real = direccion - dirBase - offset
		mem = self.memoriaActual(scope, tipo)
		if real >= len(mem):
				print("Error: direccion no existente.")
				exit()
		mem[real] = valor



