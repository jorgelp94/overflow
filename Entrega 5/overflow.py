import sys
import ply.lex as lex
import ply.yacc as yacc
from collections import deque

#############################################################################################
# Definicion del lexico del lenguaje
#############################################################################################

###########################
## Palabras reservadas   ##
###########################
reserved = {
  'program' : 'PROGRAM', 'print' : 'PRINT', 'end' : 'END', 'if' : 'IF',
  'else' : 'ELSE', 'var' : 'VAR', 'int' : 'INTTYPE', 'float' : 'FLOATTYPE',
  'char' : 'CHARTYPE', 'bool' : 'BOOLTYPE', 'void' : 'VOIDTYPE',
  'while' : 'WHILE', 'func' : 'FUNC', 'and' : 'AND', 'or'  : 'OR',
  'main' : 'MAIN', 'return' : 'RETURN', 'true' : 'TRUE', 'false' : 'FALSE'
}

###########################
## Tokens                ##
###########################
tokens = ['COMA', 'SEMICOLON', 'COLON', 'MULTIPLICATION', 'ADDITION',
          'SUBTRACTION', 'DIVISION', 'EQUAL', 'ASSIGN', 'LESS', 'GREATER',
          'NOTEQUAL', 'LESSEQUAL', 'GREATEREQUAL', 'LCURLY', 'RCURLY',
          'LBRACKET', 'RBRACKET', 'LPARENTHESIS', 'RPARENTHESIS', 'ID',
          'QUOTE', 'CTEINT', 'CTEFLOAT', 'CTECHAR', 'TRUE', 'FALSE', 'AND',
          'OR'
          ] + list(reserved.values())

###########################
## Expreg tokens         ##
###########################
t_COMA            = r','
t_SEMICOLON       = r';'
t_COLON           = r':'
t_MULTIPLICATION  = r'\*'
t_ADDITION        = r'\+'
t_SUBTRACTION     = r'-'
t_DIVISION        = r'/'
t_EQUAL           = r'=='
t_ASSIGN          = r'='
t_NOTEQUAL        = r'!='
t_LESS            = r'<'
t_GREATER         = r'>'
t_LESSEQUAL       = r'<='
t_GREATEREQUAL    = r'>='
t_LCURLY          = r'\{'
t_RCURLY          = r'\}'
t_LBRACKET        = r'\['
t_RBRACKET        = r'\]'
t_LPARENTHESIS    = r'\('
t_RPARENTHESIS    = r'\)'
t_QUOTE           = r'\"'
t_ignore          = ' \t'

def t_ID(t):
  r'[a-zA-Z]+(_?[a-zA-Z0-9])*'
  t.type = reserved.get(t.value, 'ID')    # Check for reserved words
  return t

def t_CTEFLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTEINT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CTECHAR(t):
    r'\"[^\n"]\"'
    return t

# Cuena el numero de lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#############################################################################################
# Tabla de variables y Dir de procedimientos
#############################################################################################

# Diccionario de variables globales
dirVarGlobales = {}
dirVarLocal = {}

# Variables globales y locales
varGlobales = []
varLocales = []

# Directorio de procedimientos
dirProc = {}

# Scope Global
scope = []

# Cuadruplos
cuadruplos = {}

###########################
## Pilas                 ##
###########################
pOperadores = []
pOperandos = []
pTipos = []
pSaltos = deque([])

###########################
## Contadores            ##
###########################
contCuadruplos = 0
contTemporales = 40001

###########################
## Dicrecciones          ##
###########################
localesDir = 10000
globalesDir = 20000
cteDir = 30000
tmpDir = 40000

###########################
## Tipos                 ##
###########################
INT = 1
FLOAT = 2
CHAR = 3
BOOL = 4

###########################
## Operaciones           ##
###########################
SUMA = 1
RESTA = 2
MULT = 3
DIV = 4
ASIG = 5
OR = 6
AND = 7
MAYOR = 8
MENOR = 9
MAYORIG = 10
MENORIG = 11
IGUAL = 12
DIF = 13
GOTO = 14
GOTOF = 15
GOTOV = 16
ERR = 17

###########################
## Cubo Semantico        ##
###########################

# Indices del arreglo de 3 dimensiones cuboSemantico[x][y][z] donde:
# x = opdoDer
# y = opdoIzq
# z = op

# El error se representara con = -1
# Resultado cuboSemantico[x][y][z] = tipo

#diccionario padre
cuboSemantico = {}

#diccionario donde INT es el primer operando
cuboSemantico[INT] = {}

#diccionario donde CHAR es el primer operando
cuboSemantico[CHAR] = {}

#diccionario donde FLOAT es el primer operando
cuboSemantico[FLOAT] = {}

#diccionario donde BOOL es el primer operando
cuboSemantico[BOOL] = {}

#diccionarios vacios para cubo Semantico
cuboSemantico[INT][INT] = {}
cuboSemantico[INT][FLOAT] = {}
cuboSemantico[FLOAT][INT] = {}
cuboSemantico[INT][CHAR] = {}
cuboSemantico[CHAR][INT] = {}
cuboSemantico[INT][BOOL] = {}
cuboSemantico[BOOL][INT] = {}
cuboSemantico[CHAR][CHAR] = {}
cuboSemantico[CHAR][FLOAT] = {}
cuboSemantico[FLOAT][CHAR] = {}
cuboSemantico[CHAR][BOOL] = {}
cuboSemantico[BOOL][CHAR] = {}
cuboSemantico[FLOAT][FLOAT] = {}
cuboSemantico[FLOAT][BOOL] = {}
cuboSemantico[BOOL][FLOAT] = {}
cuboSemantico[BOOL][BOOL] = {}

# Operador +
cuboSemantico[INT][INT][SUMA] = INT
cuboSemantico[INT][FLOAT][SUMA] = INT
cuboSemantico[FLOAT][INT][SUMA] = INT
cuboSemantico[FLOAT][FLOAT][SUMA] = FLOAT
cuboSemantico[CHAR][INT][SUMA] = ERR
cuboSemantico[INT][CHAR][SUMA] = ERR
cuboSemantico[CHAR][FLOAT][SUMA] = ERR
cuboSemantico[FLOAT][CHAR][SUMA] = ERR
cuboSemantico[CHAR][CHAR][SUMA] = ERR
cuboSemantico[INT][BOOL][SUMA] = ERR
cuboSemantico[BOOL][INT][SUMA] = ERR
cuboSemantico[FLOAT][BOOL][SUMA] = ERR
cuboSemantico[BOOL][FLOAT][SUMA] = ERR
cuboSemantico[CHAR][BOOL][SUMA] = ERR
cuboSemantico[BOOL][CHAR][SUMA] = ERR
cuboSemantico[BOOL][BOOL][SUMA] = ERR

# Operador -
cuboSemantico[INT][INT][RESTA] = INT
cuboSemantico[INT][FLOAT][RESTA] = INT
cuboSemantico[FLOAT][INT][RESTA] = INT
cuboSemantico[FLOAT][FLOAT][RESTA] = FLOAT
cuboSemantico[CHAR][INT][RESTA] = ERR
cuboSemantico[INT][CHAR][RESTA] = ERR
cuboSemantico[CHAR][FLOAT][RESTA] = ERR
cuboSemantico[FLOAT][CHAR][RESTA] = ERR
cuboSemantico[CHAR][CHAR][RESTA] = ERR
cuboSemantico[INT][BOOL][RESTA] = ERR
cuboSemantico[BOOL][INT][RESTA] = ERR
cuboSemantico[FLOAT][BOOL][RESTA] = ERR
cuboSemantico[BOOL][FLOAT][RESTA] = ERR
cuboSemantico[CHAR][BOOL][RESTA] = ERR
cuboSemantico[BOOL][CHAR][RESTA] = ERR
cuboSemantico[BOOL][BOOL][RESTA] = ERR

# Operador *
cuboSemantico[INT][INT][MULT] = INT
cuboSemantico[INT][FLOAT][MULT] = FLOAT
cuboSemantico[FLOAT][INT][MULT] = FLOAT
cuboSemantico[FLOAT][FLOAT][MULT] = FLOAT
cuboSemantico[CHAR][INT][MULT] = ERR
cuboSemantico[INT][CHAR][MULT] = ERR
cuboSemantico[CHAR][FLOAT][MULT] = ERR
cuboSemantico[FLOAT][CHAR][MULT] = ERR
cuboSemantico[CHAR][CHAR][MULT] = ERR
cuboSemantico[INT][BOOL][MULT] = ERR
cuboSemantico[BOOL][INT][MULT] = ERR
cuboSemantico[FLOAT][BOOL][MULT] = ERR
cuboSemantico[BOOL][FLOAT][MULT] = ERR
cuboSemantico[CHAR][BOOL][MULT] = ERR
cuboSemantico[BOOL][CHAR][MULT] = ERR
cuboSemantico[BOOL][BOOL][MULT] = ERR

# Operador /
cuboSemantico[INT][INT][DIV] = INT
cuboSemantico[INT][FLOAT][DIV] = FLOAT
cuboSemantico[FLOAT][INT][DIV] = FLOAT
cuboSemantico[FLOAT][FLOAT][DIV] = FLOAT
cuboSemantico[CHAR][INT][DIV] = ERR
cuboSemantico[INT][CHAR][DIV] = ERR
cuboSemantico[CHAR][FLOAT][DIV] = ERR
cuboSemantico[FLOAT][CHAR][DIV] = ERR
cuboSemantico[CHAR][CHAR][DIV] = ERR
cuboSemantico[INT][BOOL][DIV] = ERR
cuboSemantico[BOOL][INT][DIV] = ERR
cuboSemantico[FLOAT][BOOL][DIV] = ERR
cuboSemantico[BOOL][FLOAT][DIV] = ERR
cuboSemantico[CHAR][BOOL][DIV] = ERR
cuboSemantico[BOOL][CHAR][DIV] = ERR
cuboSemantico[BOOL][BOOL][DIV] = ERR

# Operador =
cuboSemantico[INT][INT][ASIG] = INT
cuboSemantico[INT][FLOAT][ASIG] = ERR
cuboSemantico[FLOAT][INT][ASIG] = ERR
cuboSemantico[FLOAT][FLOAT][ASIG] = FLOAT
cuboSemantico[CHAR][INT][ASIG] = ERR
cuboSemantico[INT][CHAR][ASIG] = ERR
cuboSemantico[CHAR][FLOAT][ASIG] = ERR
cuboSemantico[FLOAT][CHAR][ASIG] = ERR
cuboSemantico[CHAR][CHAR][ASIG] = CHAR
cuboSemantico[INT][BOOL][ASIG] = ERR
cuboSemantico[BOOL][INT][ASIG] = ERR
cuboSemantico[FLOAT][BOOL][ASIG] = ERR
cuboSemantico[BOOL][FLOAT][ASIG] = ERR
cuboSemantico[CHAR][BOOL][ASIG] = ERR
cuboSemantico[BOOL][CHAR][ASIG] = ERR
cuboSemantico[BOOL][BOOL][ASIG] = BOOL

# Operador and
cuboSemantico[INT][INT][AND] = ERR
cuboSemantico[INT][FLOAT][AND] = ERR
cuboSemantico[FLOAT][INT][AND] = ERR
cuboSemantico[FLOAT][FLOAT][AND] = ERR
cuboSemantico[CHAR][INT][AND] = ERR
cuboSemantico[INT][CHAR][AND] = ERR
cuboSemantico[CHAR][FLOAT][AND] = ERR
cuboSemantico[FLOAT][CHAR][AND] = ERR
cuboSemantico[CHAR][CHAR][AND] = ERR
cuboSemantico[INT][BOOL][AND] = ERR
cuboSemantico[BOOL][INT][AND] = ERR
cuboSemantico[FLOAT][BOOL][AND] = ERR
cuboSemantico[BOOL][FLOAT][AND] = ERR
cuboSemantico[CHAR][BOOL][AND] = ERR
cuboSemantico[BOOL][CHAR][AND] = ERR
cuboSemantico[BOOL][BOOL][AND] = BOOL

# Operador or
cuboSemantico[INT][INT][OR] = ERR
cuboSemantico[INT][FLOAT][OR] = ERR
cuboSemantico[FLOAT][INT][OR] = ERR
cuboSemantico[FLOAT][FLOAT][OR] = ERR
cuboSemantico[CHAR][INT][OR] = ERR
cuboSemantico[INT][CHAR][OR] = ERR
cuboSemantico[CHAR][FLOAT][OR] = ERR
cuboSemantico[FLOAT][CHAR][OR] = ERR
cuboSemantico[CHAR][CHAR][OR] = ERR
cuboSemantico[INT][BOOL][OR] = ERR
cuboSemantico[BOOL][INT][OR] = ERR
cuboSemantico[FLOAT][BOOL][OR] = ERR
cuboSemantico[BOOL][FLOAT][OR] = ERR
cuboSemantico[CHAR][BOOL][OR] = ERR
cuboSemantico[BOOL][CHAR][OR] = ERR
cuboSemantico[BOOL][BOOL][OR] = BOOL

# Operadores >
cuboSemantico[INT][INT][MAYOR] = BOOL
cuboSemantico[INT][FLOAT][MAYOR] = BOOL
cuboSemantico[FLOAT][INT][MAYOR] = BOOL
cuboSemantico[FLOAT][FLOAT][MAYOR] = BOOL
cuboSemantico[CHAR][INT][MAYOR] = ERR
cuboSemantico[INT][CHAR][MAYOR] = ERR
cuboSemantico[CHAR][FLOAT][MAYOR] = ERR
cuboSemantico[FLOAT][CHAR][MAYOR] = ERR
cuboSemantico[CHAR][CHAR][MAYOR] = ERR
cuboSemantico[INT][BOOL][MAYOR] = ERR
cuboSemantico[BOOL][INT][MAYOR] = ERR
cuboSemantico[FLOAT][BOOL][MAYOR] = ERR
cuboSemantico[BOOL][FLOAT][MAYOR] = ERR
cuboSemantico[CHAR][BOOL][MAYOR] = ERR
cuboSemantico[BOOL][CHAR][MAYOR] = ERR
cuboSemantico[BOOL][BOOL][MAYOR] = ERR

# Operadores <
cuboSemantico[INT][INT][MENOR] = BOOL
cuboSemantico[INT][FLOAT][MENOR] = BOOL
cuboSemantico[FLOAT][INT][MENOR] = BOOL
cuboSemantico[FLOAT][FLOAT][MENOR] = BOOL
cuboSemantico[CHAR][INT][MENOR] = ERR
cuboSemantico[INT][CHAR][MENOR] = ERR
cuboSemantico[CHAR][FLOAT][MENOR] = ERR
cuboSemantico[FLOAT][CHAR][MENOR] = ERR
cuboSemantico[CHAR][CHAR][MENOR] = ERR
cuboSemantico[INT][BOOL][MENOR] = ERR
cuboSemantico[BOOL][INT][MENOR] = ERR
cuboSemantico[FLOAT][BOOL][MENOR] = ERR
cuboSemantico[BOOL][FLOAT][MENOR] = ERR
cuboSemantico[CHAR][BOOL][MENOR] = ERR
cuboSemantico[BOOL][CHAR][MENOR] = ERR
cuboSemantico[BOOL][BOOL][MENOR] = ERR

# Operadores >=
cuboSemantico[INT][INT][MAYORIG] = BOOL
cuboSemantico[INT][FLOAT][MAYORIG] = BOOL
cuboSemantico[FLOAT][INT][MAYORIG] = BOOL
cuboSemantico[FLOAT][FLOAT][MAYORIG] = BOOL
cuboSemantico[CHAR][INT][MAYORIG] = ERR
cuboSemantico[INT][CHAR][MAYORIG] = ERR
cuboSemantico[CHAR][FLOAT][MAYORIG] = ERR
cuboSemantico[FLOAT][CHAR][MAYORIG] = ERR
cuboSemantico[CHAR][CHAR][MAYORIG] = ERR
cuboSemantico[INT][BOOL][MAYORIG] = ERR
cuboSemantico[BOOL][INT][MAYORIG] = ERR
cuboSemantico[FLOAT][BOOL][MAYORIG] = ERR
cuboSemantico[BOOL][FLOAT][MAYORIG] = ERR
cuboSemantico[CHAR][BOOL][MAYORIG] = ERR
cuboSemantico[BOOL][CHAR][MAYORIG] = ERR
cuboSemantico[BOOL][BOOL][MAYORIG] = ERR

# Operadores <=
cuboSemantico[INT][INT][MENORIG] = BOOL
cuboSemantico[INT][FLOAT][MENORIG] = BOOL
cuboSemantico[FLOAT][INT][MENORIG] = BOOL
cuboSemantico[FLOAT][FLOAT][MENORIG] = BOOL
cuboSemantico[CHAR][INT][MENORIG] = ERR
cuboSemantico[INT][CHAR][MENORIG] = ERR
cuboSemantico[CHAR][FLOAT][MENORIG] = ERR
cuboSemantico[FLOAT][CHAR][MENORIG] = ERR
cuboSemantico[CHAR][CHAR][MENORIG] = ERR
cuboSemantico[INT][BOOL][MENORIG] = ERR
cuboSemantico[BOOL][INT][MENORIG] = ERR
cuboSemantico[FLOAT][BOOL][MENORIG] = ERR
cuboSemantico[BOOL][FLOAT][MENORIG] = ERR
cuboSemantico[CHAR][BOOL][MENORIG] = ERR
cuboSemantico[BOOL][CHAR][MENORIG] = ERR
cuboSemantico[BOOL][BOOL][MENORIG] = ERR

# Operadores ==
cuboSemantico[INT][INT][IGUAL] = BOOL
cuboSemantico[INT][FLOAT][IGUAL] = BOOL
cuboSemantico[FLOAT][INT][IGUAL] = BOOL
cuboSemantico[FLOAT][FLOAT][IGUAL] = BOOL
cuboSemantico[CHAR][INT][IGUAL] = ERR
cuboSemantico[INT][CHAR][IGUAL] = ERR
cuboSemantico[CHAR][FLOAT][IGUAL] = ERR
cuboSemantico[FLOAT][CHAR][IGUAL] = ERR
cuboSemantico[CHAR][CHAR][IGUAL] = BOOL
cuboSemantico[INT][BOOL][IGUAL] = ERR
cuboSemantico[BOOL][INT][IGUAL] = ERR
cuboSemantico[FLOAT][BOOL][IGUAL] = ERR
cuboSemantico[BOOL][FLOAT][IGUAL] = ERR
cuboSemantico[CHAR][BOOL][IGUAL] = ERR
cuboSemantico[BOOL][CHAR][IGUAL] = ERR
cuboSemantico[BOOL][BOOL][IGUAL] = BOOL

# Operadores !=
cuboSemantico[INT][INT][DIF] = BOOL
cuboSemantico[INT][FLOAT][DIF] = BOOL
cuboSemantico[FLOAT][INT][DIF] = BOOL
cuboSemantico[FLOAT][FLOAT][DIF] = BOOL
cuboSemantico[CHAR][INT][DIF] = ERR
cuboSemantico[INT][CHAR][DIF] = ERR
cuboSemantico[CHAR][FLOAT][DIF] = ERR
cuboSemantico[FLOAT][CHAR][DIF] = ERR
cuboSemantico[CHAR][CHAR][DIF] = BOOL
cuboSemantico[INT][BOOL][DIF] = ERR
cuboSemantico[BOOL][INT][DIF] = ERR
cuboSemantico[FLOAT][BOOL][DIF] = ERR
cuboSemantico[BOOL][FLOAT][DIF] = ERR
cuboSemantico[CHAR][BOOL][DIF] = ERR
cuboSemantico[BOOL][CHAR][DIF] = ERR
cuboSemantico[BOOL][BOOL][DIF] = BOOL

#############################################################################################
# Gramatica
#############################################################################################
def p_programa(p):
    '''programa : PROGRAM ID SEMICOLON programa_var_loop programa_func_loop addProcDir MAIN addMainProc LPARENTHESIS RPARENTHESIS bloque END'''
    p[0] = "OK"
    print("Pasa por programa")

def p_addProcDir(p):
    '''addProcDir :'''
    dirProc[p[-4]] = {'Variables' : dirVarGlobales.copy(), 'Tipo' : p[-5]}
    dirVarGlobales.clear()
    print("Pasa por addProcDir")
    print("..........................")
    print(dirProc)
    print("..........................")

def p_addMainProc(p):
    '''addMainProc :'''
    dirProc[p[-1]] = {'Variables' : dirVarGlobales, 'Tipo' : 'VOID'}
    print("Pasa por addMainProcDir")
    print("..........................")
    print(dirProc)
    print("..........................")

def p_programa_var_loop(p):
    '''programa_var_loop : variable programa_var_loop
      |'''
    print("Pasa por programa_var_loop")

def p_programa_func_loop(p):
    '''programa_func_loop : funcion programa_func_loop
      |'''
    print("Pasa por programa_func_loop")

def p_bloque(p):
    '''bloque : LCURLY bloque_est_loop RCURLY'''
    print("pasa por bloque")

def p_bloque_est_loop(p):
    '''bloque_est_loop : estatuto bloque_est_loop
      |'''
    print("pasa por bloque_est_loop")

def p_tipo(p):
    '''tipo : INTTYPE
          | FLOATTYPE
          | CHARTYPE
          | BOOLTYPE
          | VOIDTYPE'''
    p[0] = p[1]
    print("pasa por tipo")

def p_subtipo(p):
    '''subtipo : INTTYPE
        | FLOATTYPE'''
    p[0] = p[1]
    print("pasa por subtipo")

def p_estatuto(p):
    '''estatuto : asignacion
      | condicion
      | escritura
      | regreso
      | ciclo'''
    print("pasa por estatuto")

def p_regreso(p):
    '''regreso : RETURN exp SEMICOLON'''
    print("pasa por regreso")

def p_variable(p):
    '''variable : VAR variable_loop'''
    print("pasa por variable")

def p_variable_loop(p):
    '''variable_loop : variable_id_loop SEMICOLON variable_end_loop
                    | variable_arr_loop SEMICOLON variable_end_loop'''
    print("pasa por variable_loop")

def p_addType(p):
    '''addType :'''
    scope.append('Global')
    while (len(varGlobales) > 0):
        dirVarGlobales[varGlobales.pop()] = {'Tipo' : p[-1].upper(), 'Scope' : scope[-1]}
    print("pasa por addType")
    print("..........................")
    print(dirVarGlobales)
    print("..........................")

def p_variable_id_loop(p):
    '''variable_id_loop : variable_id_loop_coma COLON tipo addType'''
    print("pasa por variable_id_loop")

def p_variable_id_loop_coma(p):
    '''variable_id_loop_coma : ID addDirVarGlobales
        | ID addDirVarGlobales COMA variable_id_loop_coma'''
    print("pasa por variable_id_loop_coma")

def p_variable_arr_loop(p):
    '''variable_arr_loop : variable_arr_coma COLON subtipo addType'''
    print("pasa por variable_arr_loop")

def p_variable_arr_coma(p):
    '''variable_arr_coma : ID addDirVarGlobales LBRACKET RBRACKET
        | ID addDirVarGlobales LBRACKET RBRACKET COMA variable_arr_coma'''
    print("pasa por variable_arr_coma")

def p_addDirVarGlobales(p):
    '''addDirVarGlobales :'''
    varGlobales.append(p[-1])
    print("pasa por addDirVarGlobales")
    print("..........................")
    print(varGlobales)
    print("..........................")

def p_variable_end_loop(p):
    '''variable_end_loop : variable_loop
      |'''
    print("pasa por variable_end_loop")

def p_escritura(p):
    '''escritura : PRINT LPARENTHESIS escritura_type RPARENTHESIS SEMICOLON'''
    print("pasa por escritura")

def p_escritura_type(p):
    '''escritura_type : expresion
      | QUOTE CTECHAR QUOTE'''
    print("pasa por escritura_type")

def p_funcion(p):
    '''funcion : tipo FUNC ID LPARENTHESIS funcion_option RPARENTHESIS addProcDirFunc bloque'''
    print("pasa por funcion")

def p_addProcDirFunc(p):
    '''addProcDirFunc :'''
    dirProc[p[-4]] = {'Variables' : dirVarLocal.copy(), 'Tipo' : p[-6]}
    dirVarLocal.clear()
    print("pasa por addProcDirFunc")
    print("..........................")
    print(dirProc)
    print("..........................")

def p_funcion_option(p):
    '''funcion_option : argumentos
      |'''
    print("pasa por funcion_option")

def p_argumentos(p):
    '''argumentos : ID addDirVarGlobalesFunc COLON tipo addTypeFunc argumentos_loop'''
    print("pasa por argumentos")

def p_argumentos_loop(p):
    '''argumentos_loop : COMA argumentos
      |'''
    print("pasa por argumentos_loop")

def p_addDirVarGlobalesFunc(p):
    '''addDirVarGlobalesFunc :  '''
    varLocales.append(p[-1])
    print("pasa por addDirVarGlobalesFunc")
    print("..........................")
    print(varLocales)
    print("..........................")

def p_addTypeFunc(p):
    '''addTypeFunc :'''
    scope.append('Local')
    while (len(varLocales) > 0):
        dirVarLocal[varLocales.pop()] = {'Tipo' : p[-1], 'Scope' : scope[-1]}
    print("pasa por addTypeFunc")
    print("..........................")
    print(dirVarLocal)
    print("..........................")

#############################
## Ciclo                   ##
#############################
def p_ciclo(p):
    '''ciclo : WHILE LPARENTHESIS nodo16 expresion RPARENTHESIS nodo13 bloque nodo17'''
    print("pasa por ciclo")

#############################
## Nodo16                  ##
#############################
def p_nodo16(p):
    '''nodo16 : '''
    global contCuadruplos
    pSaltos.append(contCuadruplos)

#############################
## Nodo17                  ##
#############################
def p_nodo17(p):
    '''nodo17 : '''
    global contCuadruplos
    op = GOTO
    saltoEnFalso = pSaltos.pop()
    dirCuadruplo = pSaltos.pop()
    cuadruplos[contCuadruplos] = [op, "", "", dirCuadruplo]
    contCuadruplos+=1
    cuadruplos[saltoEnFalso][3] = contCuadruplos
    print(cuadruplos)

#############################
## Condicion               ##
#############################
def p_condicion(p):
    '''condicion : IF LPARENTHESIS expresion RPARENTHESIS nodo13 bloque condicion_option nodo15'''
    print("pasa por condicion")

def p_condicion_option(p):
    '''condicion_option : ELSE nodo14 bloque
      |'''
    print("pasa por condicion_option")

#############################
## Nodo15                  ##
#############################
def p_nodo15(p):
    '''nodo15 : '''
    global contCuadruplos
    saltoEnFalso = pSaltos.pop()
    cuadruplos[saltoEnFalso][3] = contCuadruplos
    print(cuadruplos)

#############################
## Nodo14                  ##
#############################
def p_nodo14(p):
    '''nodo14 : '''
    global contCuadruplos
    op = GOTO
    saltoEnFalso = pSaltos.pop()
    cuadruplos[contCuadruplos] = [op, "", "", ""]
    pSaltos.append(contCuadruplos)
    contCuadruplos+=1
    cuadruplos[saltoEnFalso][3] = contCuadruplos
    print(cuadruplos)

#############################
## Nodo13                  ##
#############################
def p_nodo13(p):
    '''nodo13 : '''    
    global contCuadruplos
    if pTipos[-1] == BOOL:
        op = GOTOF
        opdoIzq = pOperandos.pop()
        pTipos.pop()
        cuadruplos[contCuadruplos] = [op, opdoIzq, "", ""]
        pSaltos.append(contCuadruplos)
        contCuadruplos+=1
        print(cuadruplos)
    else:
        print ("Expresion no booleana")
        exit()

#############################
## Expresion               ##
#############################
def p_expresion(p):
    '''expresion : nuevaexp expresion_option nodo11 expresion_loop'''
    print("pasa por expresion")

def p_expresion_option(p):
    '''expresion_option : AND nodo12_and nuevaexp
        | OR nodo12_or nuevaexp
        |'''
    print("pasa por expresion_option")

def p_expresion_loop(p):
    '''expresion_loop : expresion
        |'''
    print("pasa por expresion_loop")

#############################
## Nodo12                  ##
#############################
def p_nodo12_and(p):
    '''nodo12_and : '''
    pOperadores.append(AND)

def p_nodo12_or(p):
    '''nodo12_or : '''
    pOperadores.append(OR)

#############################
## Nodo11                  ##
#############################
def p_nodo11(p):
    '''nodo11 : '''
    global contTemporales
    global contCuadruplos
    if pOperadores:
        if pOperadores[-1] == AND or pOperadores[-1] == OR:
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cuboSemantico[tipoDer][tipoIzq][op] != ERR :
                tipoRes = cuboSemantico[tipoDer][tipoIzq][op]
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error de condicion - valor no booleano")
                exit()

#############################
## NuevaExp                ##
#############################
def p_nuevaexp(p):
    '''nuevaexp : exp nuevaexp_type nodo10'''
    print("pasa por nuevaexp")

def p_nuevaexp_type(p):
    '''nuevaexp_type : LESS nodo9_menor exp
      | GREATER nodo9_mayor exp
      | LESSEQUAL nodo9_menorig exp
      | GREATEREQUAL nodo9_mayorig exp
      | NOTEQUAL nodo9_dif exp
      | EQUAL nodo9_igual exp
      |'''
    print("pasa por nuevaexp_type")

#############################
## Nodo10                  ##
#############################
def p_nodo10(p):
    '''nodo10 : '''
    global contTemporales
    global contCuadruplos
    if pOperadores:
        print(pOperadores)
        if pOperadores[-1] == MENOR or pOperadores[-1] == MAYOR or pOperadores[-1] == MENORIG or pOperadores[-1] == MAYORIG or pOperadores[-1] == IGUAL or pOperadores[-1] == DIF:
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cuboSemantico[tipoDer][tipoIzq][op] != ERR :
                tipoRes = cuboSemantico[tipoDer][tipoIzq][op]
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contCuadruplos+=1
                contTemporales+=1
                print(cuadruplos)
            else:
                print("Error de comparacion - Los valores comparados no son validos")
                exit()

#############################
## Nodo9                   ##
#############################
def p_nodo9_menor(p):
    '''nodo9_menor : '''
    pOperadores.append(MENOR)

def p_nodo9_mayor(p):
    '''nodo9_mayor : '''
    pOperadores.append(MAYOR)

def p_nodo9_menorig(p):
    '''nodo9_menorig : '''
    pOperadores.append(MENORIG)

def p_nodo9_mayorig(p):
    '''nodo9_mayorig : '''
    pOperadores.append(MAYORIG)

def p_nodo9_dif(p):
    '''nodo9_dif : '''
    pOperadores.append(DIF)

def p_nodo9_igual(p):
    '''nodo9_igual : '''
    pOperadores.append(IGUAL)

#############################
## Asignacion              ##
#############################
def p_asignacion(p):
    '''asignacion : ID asignacion_option'''
    print("pasa por asignacion")

def p_asignacion_option(p):
    '''asignacion_option : ASSIGN expresion nodo8 SEMICOLON
      | LBRACKET CTEINT RBRACKET ASSIGN nodo8 LBRACKET asignacion_type RBRACKET SEMICOLON'''
    print("pasa por asignacion_option")

def p_asignacion_type(p):
    '''asignacion_type : CTEINT
    | CTEFLOAT
    | CTEINT COMA asignacion_type
    | CTEFLOAT COMA asignacion_type'''
    print("pasa por asignacion_type")

#############################
## Nodo8                   ##
#############################
def p_nodo8(p):
    '''nodo8 : '''
    global contTemporales
    global contCuadruplos
    varsDic = dirProc['overflow']['Variables'].keys()
    if p[-3] in varsDic :
        pOperandos.append(p[-3])
        if dirProc['overflow']['Variables'][p[-3]]['Tipo'] == 'INT' :
            pTipos.append(INT)
        elif dirProc['overflow']['Variables'][p[-3]]['Tipo'] == 'FLOAT' :
            pTipos.append(FLOAT)
        elif dirProc['overflow']['Variables'][p[-3]]['Tipo'] == 'CHAR' :
            pTipos.append(CHAR)
        elif dirProc['overflow']['Variables'][p[-3]]['Tipo'] == 'BOOL' :
            pTipos.append(BOOL)
        else:
            print("Error de asignacion - tipo no valido")
        pOperadores.append(ASIG)
    else:
        print("Error de asignacion - variable no declarada")
        exit()

    if pOperadores :
        if pOperadores[-1] == ASIG :
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cuboSemantico[tipoDer][tipoIzq][op] != ERR :
                tipoRes = cuboSemantico[tipoDer][tipoIzq][op]
                cuadruplos[contCuadruplos] = [op, opdoIzq, "", opdoDer]
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error de asignacion - tipo de variable no es compatible con asignacion")
                exit()

#############################
## Exp                     ##
#############################
def p_exp(p):
    '''exp : termino nodo5 exp_loop'''
    print("pasa por exp")

def p_exp_loop(p):
    '''exp_loop : exp_type_loop
      |'''
    print("pasa por exp_loop")

def p_exp_type_loop(p):
    '''exp_type_loop : ADDITION nodo3_suma exp
      | SUBTRACTION nodo3_resta exp'''
    print("pasa por exp_type_loop")

#############################
## Nodo3                   ##
#############################
def p_nodo3_suma(p):
    '''nodo3_suma : '''
    pOperadores.append(SUMA)

def p_nodo3_resta(p):
    '''nodo3_resta : '''
    pOperadores.append(RESTA)

#############################
## Nodo5                   ##
#############################
def p_nodo5(p):
    '''nodo5 : '''
    global pOperadores
    global contTemporales
    global contCuadruplos
    if pOperadores :
        if pOperadores[-1] == SUMA or pOperadores[-1]== RESTA :
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cuboSemantico[tipoDer][tipoIzq][op] != ERR and (cuboSemantico[tipoDer][tipoIzq][op] == INT or cuboSemantico[tipoDer][tipoIzq][op] == FLOAT) :
                tipoRes = cuboSemantico[tipoDer][tipoIzq][op]
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error arimetico - tipos no validos")
                exit()

#############################
## Termino                 ##
#############################
def p_termino(p):
    '''termino : factor nodo4 termino_loop'''
    print("pasa por termino")

def p_termino_loop(p):
    '''termino_loop : termino_type_loop
      |'''
    print("pasa por termino_loop")

def p_termino_type_loop(p):
    '''termino_type_loop : MULTIPLICATION nodo2_mult termino
      | DIVISION nodo2_div termino'''
    print("pasa por termino_type_loop")

#############################
## Nodo2                   ##
#############################
def p_nodo2_mult(p):
    '''nodo2_mult : '''
    pOperadores.append(MULT)

def p_nodo2_div(p):
    '''nodo2_div : '''
    pOperadores.append(DIV)

#############################
## Nodo4                   ##
#############################
def p_nodo4(p):
    '''nodo4 : '''
    global pOperadores
    global contTemporales
    global contCuadruplos
    if pOperadores :
        if pOperadores[-1] == MULT or pOperadores[-1]== DIV :
            op = pOperadores.pop()
            opdoDer = pOperandos.pop()
            tipoDer = pTipos.pop()
            opdoIzq = pOperandos.pop()
            tipoIzq = pTipos.pop()
            if cuboSemantico[tipoDer][tipoIzq][op] != ERR and (cuboSemantico[tipoDer][tipoIzq][op] == INT or cuboSemantico[tipoDer][tipoIzq][op] == FLOAT) :
                tipoRes = cuboSemantico[tipoDer][tipoIzq][op]
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, contTemporales]
                pOperandos.append(contTemporales)
                pTipos.append(tipoRes)
                contTemporales+=1
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error arimetico - tipos no validos")
                exit()

#############################
## Factor                  ##
#############################
def p_factor(p):
    '''factor : factor_var
      | factor_exp'''
    print("pasa por factor")

def p_factor_var(p):
    '''factor_var : varcte nodo1'''
    print("pasa por factor_var")

def p_factor_exp(p):
    '''factor_exp : LPARENTHESIS nodo6 expresion RPARENTHESIS nodo7'''
    print("pasa por factor_exp")

#############################
## Nodo1                   ##
#############################
def p_nodo1(p):
    '''nodo1 : '''
    pOperandos.append(p[-1])

#############################
## Nodo6                   ##
#############################
def p_nodo6(p):
    '''nodo6 : '''
    pOperadores.append("(")

#############################
## Nodo7                   ##
#############################
def p_nodo7(p):
    '''nodo7 : '''
    if pOperadores[-1] == "(" :
        pOperadores.pop()
    else:
        print("Falta parentesis izquierdo")

#############################
## Varcte                  ##
#############################
def p_varcte(p):
    '''varcte : ID varcte_arr
      | CTEINT nodoCteE
      | CTEFLOAT nodoCteF
      | CTEBOOL nodoCteB
      | CTECHAR nodoCteC'''
    print("pasa por varcte")
    p[0] = p[1]
    print("..........................")
    print(pTipos)
    print("..........................*")
    print(p[0])
    print("..........................")

def p_varcte_arr(p):
    '''varcte_arr : LBRACKET RBRACKET
      |'''
    print("pasa por varcte_arr")

def p_CTEBOOL(p):
    '''CTEBOOL : TRUE
        | FALSE'''
    p[0] = p[1]

#############################
## Nodo cteE               ##
#############################
def p_nodoCteE(p):
    '''nodoCteE : '''
    pTipos.append(INT)

#############################
## Nodo cteF               ##
#############################
def p_nodoCteF(p):
    '''nodoCteF : '''
    pTipos.append(FLOAT)

#############################
## Nodo cteB               ##
#############################
def p_nodoCteB(p):
    '''nodoCteB : '''
    pTipos.append(BOOL)

#############################
## Nodo cteC               ##
#############################
def p_nodoCteC(p):
    '''nodoCteC : '''
    pTipos.append(CHAR)

# Error rule for syntax errors
def p_error(p):
    print("Syntax error at %s, illegal token %s!"%(p.lineno, p.value))

# Build the lexer
lex.lex()

# Build the parser
parser = yacc.yacc(start='programa')

# Main
if __name__ == '__main__':
	# Revisa si el archivo se dio como input
	if (len(sys.argv) > 1):
		file = sys.argv[1]
		# Abre el archivo, almacena su informacion y lo cierra
		try:
			f = open(file,'r')
			data = f.read()
			f.close()
			# Parse the data
			if (parser.parse(data, tracking=True) == 'OK'):
				print (dirProc);

		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')
