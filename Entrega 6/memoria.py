
class Memoria:

	def __init__(self, name, memoria):
		self.name  = name
		self.ints  = memoria['INT']
		self.floats = memoria['FLOAT']
		self.chars = memoria['CHAR']
		self.bools = memoria['BOOL']


	def realValue(self, direccion):