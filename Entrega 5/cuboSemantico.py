from collections import defaultdict
cuboSemantico = defaultdict(lambda :defaultdict(lambda :defaultdict(int)))

# Indices del arreglo de 3 dimensiones cuboSemantico[x][y][z] donde:
# x = opdoDer
# y = opdoIzq
# z = op

# Identificadores de los tipos de datos
# Int:    1
# Float:  2
# Char:   3
# String: 4

# Identificadores de los operadores
#	+,-      1
#	*,/      2
#	and,or   3
#	<,>    	 4
#	<=,>=    5
#	==,!=    6
#   =        7

# El error se representara con = -1
# Resultado cuboSemantico[x][y][z] = tipo

# Operadores + y -
cuboSemantico[1][1][1] = 1
cuboSemantico[1][2][1] = 1
cuboSemantico[2][1][1] = 1
cuboSemantico[2][2][1] = 2
cuboSemantico[3][1][1] = 1
cuboSemantico[1][3][1] = 1
cuboSemantico[3][2][1] = -1
cuboSemantico[2][3][1] = -1
cuboSemantico[3][3][1] = 1
cuboSemantico[1][4][1] = -1
cuboSemantico[4][1][1] = -1
cuboSemantico[2][4][1] = -1
cuboSemantico[4][2][1] = -1
cuboSemantico[3][4][1] = -1
cuboSemantico[4][3][1] = -1
cuboSemantico[4][4][1] = -1

# Operadores * y /
cuboSemantico[1][1][2] = 1
cuboSemantico[1][2][2] = 2
cuboSemantico[2][1][2] = 2
cuboSemantico[2][2][2] = 2
cuboSemantico[3][1][2] = -1
cuboSemantico[1][3][2] = -1
cuboSemantico[3][2][2] = -1
cuboSemantico[2][3][2] = -1
cuboSemantico[3][3][2] = -1
cuboSemantico[1][4][2] = -1
cuboSemantico[4][1][2] = -1
cuboSemantico[2][4][2] = -1
cuboSemantico[4][2][2] = -1
cuboSemantico[3][4][2] = -1
cuboSemantico[4][3][2] = -1
cuboSemantico[4][4][2] = -1

# Operadores and y or
cuboSemantico[1][1][3] = 1
cuboSemantico[1][2][3] = -1
cuboSemantico[2][1][3] = -1
cuboSemantico[2][2][3] = -1
cuboSemantico[3][1][3] = -1
cuboSemantico[1][3][3] = -1
cuboSemantico[3][2][3] = -1
cuboSemantico[2][3][3] = -1
cuboSemantico[3][3][3] = -1
cuboSemantico[1][4][3] = -1
cuboSemantico[4][1][3] = -1
cuboSemantico[2][4][3] = -1
cuboSemantico[4][2][3] = -1
cuboSemantico[3][4][3] = -1
cuboSemantico[4][3][3] = -1
cuboSemantico[4][4][3] = -1

# Operadores < y >
cuboSemantico[1][1][4] = 1
cuboSemantico[1][2][4] = 1
cuboSemantico[2][1][4] = 1
cuboSemantico[2][2][4] = 1
cuboSemantico[3][1][4] = -1
cuboSemantico[1][3][4] = -1
cuboSemantico[3][2][4] = -1
cuboSemantico[2][3][4] = -1
cuboSemantico[3][3][4] = -1
cuboSemantico[1][4][4] = -1
cuboSemantico[4][1][4] = -1
cuboSemantico[2][4][4] = -1
cuboSemantico[4][2][4] = -1
cuboSemantico[3][4][4] = -1
cuboSemantico[4][3][4] = -1
cuboSemantico[4][4][4] = -1

# Operadores <= y >=
cuboSemantico[1][1][5] = 1
cuboSemantico[1][2][5] = 1
cuboSemantico[2][1][5] = 1
cuboSemantico[2][2][5] = 1
cuboSemantico[3][1][5] = -1
cuboSemantico[1][3][5] = -1
cuboSemantico[3][2][5] = -1
cuboSemantico[2][3][5] = -1
cuboSemantico[3][3][5] = -1
cuboSemantico[1][5][5] = -1
cuboSemantico[5][1][5] = -1
cuboSemantico[2][5][5] = -1
cuboSemantico[5][2][5] = -1
cuboSemantico[3][5][5] = -1
cuboSemantico[5][3][5] = -1
cuboSemantico[5][5][5] = -1

# Operador == y !=
cuboSemantico[1][1][6] = 1
cuboSemantico[1][2][6] = 1
cuboSemantico[2][1][6] = 1
cuboSemantico[2][2][6] = 1
cuboSemantico[3][1][6] = 1
cuboSemantico[1][3][6] = 1
cuboSemantico[3][2][6] = 1
cuboSemantico[2][3][6] = 1
cuboSemantico[3][3][6] = 1
cuboSemantico[1][4][6] = -1
cuboSemantico[4][1][6] = -1
cuboSemantico[2][4][6] = -1
cuboSemantico[4][2][6] = -1
cuboSemantico[3][4][6] = -1
cuboSemantico[4][3][6] = -1
cuboSemantico[4][4][6] = 4

# Operador =
cuboSemantico[1][1][7] = 1
cuboSemantico[1][2][7] = 1
cuboSemantico[2][1][7] = 1
cuboSemantico[2][2][7] = 1
cuboSemantico[3][1][7] = 1
cuboSemantico[1][3][7] = 1
cuboSemantico[3][2][7] = -1
cuboSemantico[2][3][7] = -1
cuboSemantico[3][3][7] = 1
cuboSemantico[1][4][7] = -1
cuboSemantico[4][1][7] = -1
cuboSemantico[2][4][7] = -1
cuboSemantico[4][2][7] = -1
cuboSemantico[3][4][7] = -1
cuboSemantico[4][3][7] = -1
cuboSemantico[4][4][7] = 1

# Funcion de consulta del cubo para definir el resultado de una operacion
# Recibe como argumento los operandos y el operador
# Regresa la consulta al cubo
def getResultType(opdoDer, opdoIzq, op):
	return cuboSemantico[opdoDer][opdoIzq][op]
