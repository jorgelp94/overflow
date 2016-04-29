
class Memoria:

	def __init__(self, name, memoria):
		self.name  = name
		self.ints  = memoria['INT'] * [""]
		self.floats = memoria['FLOAT'] * [""]
		self.chars = memoria['CHAR'] * [""]
		self.bools = memoria['BOOL'] * [""]


	def offsetDireccion(self, direccion):
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
		if direccion >= 10000 and direccion < 20000:
			return ['Local', 10000]

		if direccion >= 20000 and direccion < 30000:
			return ['Global', 20000]

		if direccion >= 30000 and direccion < 40000:
			return ['Temporales', 30000]

		if direccion >= 40000 and direccion < 50000:
			return ['CONSTANTE', 40000]

		if direccion >= 50000 and direccion < 60000:
			return ['Funcion', 50000]

		if direccion >= 60000 and direccion < 70000:
			return ['FuncionL', 60000]


	def memoriaActual(self, scope, tipo):
		if scope == 'Global' or scope == 'Funcion' or scope == 'Local':
			if tipo == 'INT':
				return self.ints
			elif tipo == 'FLOAT':
				return self.floats
			elif tipo == 'CHAR':
				return self.chars
			elif tipo == 'BOOL':
				return self.bools

	def getValorDeDireccion(self, direccion):
		scope = self.scopeDireccion(direccion)[0]
		tipo = self.offsetDireccion(direccion)[0]
		if scope != 'CONSTANTE':
			dirBase = self.scopeDireccion(direccion)[1]
			offset = self.offsetDireccion(direccion)[1]
			real = direccion - dirBase - offset
			mem = self.memoriaActual(scope, tipo)
			return mem[real]

	def setValorDeDireccion(self, direccion, valor):
		scope = self.scopeDireccion(direccion)[0]
		tipo = self.offsetDireccion(direccion)[0]
		dirBase = self.scopeDireccion(direccion)[1]
		offset = self.offsetDireccion(direccion)[1]
		real = direccion - dirBase - offset
		mem = self.memoriaActual(scope, tipo)
		mem[real] = valor



