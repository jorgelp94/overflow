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
# Bool: 4

# Identificadores de los operadores
#	+     1
#   -	  2
#	*     3
#   /     4
#   =     5
#   or    6
#   and   7
#   >     8
#   <     9
#   >=    10
#   <=    11
#   ==    12
#   !=    13

# El error se representara con = -1
# Resultado cuboSemantico[x][y][z] = tipo

# Operador + 
cuboSemantico[1][1][1] = 1
cuboSemantico[1][2][1] = 1
cuboSemantico[2][1][1] = 1
cuboSemantico[2][2][1] = 2
cuboSemantico[3][1][1] = -1
cuboSemantico[1][3][1] = -1
cuboSemantico[3][2][1] = -1
cuboSemantico[2][3][1] = -1
cuboSemantico[3][3][1] = -1
cuboSemantico[1][4][1] = -1
cuboSemantico[4][1][1] = -1
cuboSemantico[2][4][1] = -1
cuboSemantico[4][2][1] = -1
cuboSemantico[3][4][1] = -1
cuboSemantico[4][3][1] = -1
cuboSemantico[4][4][1] = -1

# Operador - 
cuboSemantico[1][1][2] = 1
cuboSemantico[1][2][2] = 1
cuboSemantico[2][1][2] = 1
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

# Operador * 
cuboSemantico[1][1][3] = 1
cuboSemantico[1][2][3] = 2
cuboSemantico[2][1][3] = 2
cuboSemantico[2][2][3] = 2
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

# Operador / 
cuboSemantico[1][1][4] = 1
cuboSemantico[1][2][4] = 2
cuboSemantico[2][1][4] = 2
cuboSemantico[2][2][4] = 2
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

# Operador =
cuboSemantico[1][1][5] = 1
cuboSemantico[1][2][5] = -1
cuboSemantico[2][1][5] = -1
cuboSemantico[2][2][5] = 2
cuboSemantico[3][1][5] = -1
cuboSemantico[1][3][5] = -1
cuboSemantico[3][2][5] = -1
cuboSemantico[2][3][5] = -1
cuboSemantico[3][3][5] = 3
cuboSemantico[1][4][5] = -1
cuboSemantico[4][1][5] = -1
cuboSemantico[2][4][5] = -1
cuboSemantico[4][2][5] = -1
cuboSemantico[3][4][5] = -1
cuboSemantico[4][3][5] = -1
cuboSemantico[4][4][5] = 4

# Operador or
cuboSemantico[1][1][6] = -1
cuboSemantico[1][2][6] = -1
cuboSemantico[2][1][6] = -1
cuboSemantico[2][2][6] = -1
cuboSemantico[3][1][6] = -1
cuboSemantico[1][3][6] = -1
cuboSemantico[3][2][6] = -1
cuboSemantico[2][3][6] = -1
cuboSemantico[3][3][6] = -1
cuboSemantico[1][4][6] = -1
cuboSemantico[4][1][6] = -1
cuboSemantico[2][4][6] = -1
cuboSemantico[4][2][6] = -1
cuboSemantico[3][4][6] = -1
cuboSemantico[4][3][6] = -1
cuboSemantico[4][4][6] = 4

# Operador and
cuboSemantico[1][1][7] = -1
cuboSemantico[1][2][7] = -1
cuboSemantico[2][1][7] = -1
cuboSemantico[2][2][7] = -1
cuboSemantico[3][1][7] = -1
cuboSemantico[1][3][7] = -1
cuboSemantico[3][2][7] = -1
cuboSemantico[2][3][7] = -1
cuboSemantico[3][3][7] = -1
cuboSemantico[1][4][7] = -1
cuboSemantico[4][1][7] = -1
cuboSemantico[2][4][7] = -1
cuboSemantico[4][2][7] = -1
cuboSemantico[3][4][7] = -1
cuboSemantico[4][3][7] = -1
cuboSemantico[4][4][7] = 4

# Operador > 
cuboSemantico[1][1][8] = 4
cuboSemantico[1][2][8] = 4
cuboSemantico[2][1][8] = 4
cuboSemantico[2][2][8] = 4
cuboSemantico[3][1][8] = -1
cuboSemantico[1][3][8] = -1
cuboSemantico[3][2][8] = -1
cuboSemantico[2][3][8] = -1
cuboSemantico[3][3][8] = -1
cuboSemantico[1][4][8] = -1
cuboSemantico[4][1][8] = -1
cuboSemantico[2][4][8] = -1
cuboSemantico[4][2][8] = -1
cuboSemantico[3][4][8] = -1
cuboSemantico[4][3][8] = -1
cuboSemantico[4][4][8] = -1

# Operador < 
cuboSemantico[1][1][9] = 4
cuboSemantico[1][2][9] = 4
cuboSemantico[2][1][9] = 4
cuboSemantico[2][2][9] = 4
cuboSemantico[3][1][9] = -1
cuboSemantico[1][3][9] = -1
cuboSemantico[3][2][9] = -1
cuboSemantico[2][3][9] = -1
cuboSemantico[3][3][9] = -1
cuboSemantico[1][4][9] = -1
cuboSemantico[4][1][9] = -1
cuboSemantico[2][4][9] = -1
cuboSemantico[4][2][9] = -1
cuboSemantico[3][4][9] = -1
cuboSemantico[4][3][9] = -1
cuboSemantico[4][4][9] = -1

# Operadores >=
cuboSemantico[1][1][10] = 4
cuboSemantico[1][2][10] = 4
cuboSemantico[2][1][10] = 4
cuboSemantico[2][2][10] = 4
cuboSemantico[3][1][10] = -1
cuboSemantico[1][3][10] = -1
cuboSemantico[3][2][10] = -1
cuboSemantico[2][3][10] = -1
cuboSemantico[3][3][10] = -1
cuboSemantico[1][5][10] = -1
cuboSemantico[5][1][10] = -1
cuboSemantico[2][5][10] = -1
cuboSemantico[5][2][10] = -1
cuboSemantico[3][5][10] = -1
cuboSemantico[5][3][10] = -1
cuboSemantico[5][5][10] = -1

# Operadores <=
cuboSemantico[1][1][11] = 4
cuboSemantico[1][2][11] = 4
cuboSemantico[2][1][11] = 4
cuboSemantico[2][2][11] = 4
cuboSemantico[3][1][11] = -1
cuboSemantico[1][3][11] = -1
cuboSemantico[3][2][11] = -1
cuboSemantico[2][3][11] = -1
cuboSemantico[3][3][11] = -1
cuboSemantico[1][5][11] = -1
cuboSemantico[5][1][11] = -1
cuboSemantico[2][5][11] = -1
cuboSemantico[5][2][11] = -1
cuboSemantico[3][5][11] = -1
cuboSemantico[5][3][11] = -1
cuboSemantico[5][5][11] = -1

# Operadores ==
cuboSemantico[1][1][12] = 4
cuboSemantico[1][2][12] = 4
cuboSemantico[2][1][12] = 4
cuboSemantico[2][2][12] = 4
cuboSemantico[3][1][12] = -1
cuboSemantico[1][3][12] = -1
cuboSemantico[3][2][12] = -1
cuboSemantico[2][3][12] = -1
cuboSemantico[3][3][12] = -1
cuboSemantico[1][5][12] = -1
cuboSemantico[5][1][12] = -1
cuboSemantico[2][5][12] = -1
cuboSemantico[5][2][12] = -1
cuboSemantico[3][5][12] = -1
cuboSemantico[5][3][12] = -1
cuboSemantico[5][5][12] = -1

# Operadores !=
cuboSemantico[1][1][13] = 4
cuboSemantico[1][2][13] = 4
cuboSemantico[2][1][13] = 4
cuboSemantico[2][2][13] = 4
cuboSemantico[3][1][13] = -1
cuboSemantico[1][3][13] = -1
cuboSemantico[3][2][13] = -1
cuboSemantico[2][3][13] = -1
cuboSemantico[3][3][13] = -1
cuboSemantico[1][5][13] = -1
cuboSemantico[5][1][13] = -1
cuboSemantico[2][5][13] = -1
cuboSemantico[5][2][13] = -1
cuboSemantico[3][5][13] = -1
cuboSemantico[5][3][13] = -1
cuboSemantico[5][5][13] = -1

# Funcion de consulta del cubo para definir el resultado de una operacion
# Recibe como argumento los operandos y el operador
# Regresa la consulta al cubo
def getResultType(opdoDer, opdoIzq, op):
	return cuboSemantico[opdoDer][opdoIzq][op]
