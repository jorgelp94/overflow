import sys
import ply.lex as lex
import ply.yacc as yacc
import collections
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
  'while' : 'WHILE', 'and' : 'AND', 'or'  : 'OR', 'main' : 'MAIN',
  'return' : 'RETURN', 'true' : 'TRUE', 'false' : 'FALSE', 'func' : 'FUNC'
}

###########################
## Tokens                ##
###########################
tokens = ['COMA', 'SEMICOLON', 'COLON', 'MULTIPLICATION', 'ADDITION',
          'SUBTRACTION', 'DIVISION', 'EQUAL', 'ASSIGN', 'LESS', 'GREATER',
          'NOTEQUAL', 'LESSEQUAL', 'GREATEREQUAL', 'LCURLY', 'RCURLY',
          'LBRACKET', 'RBRACKET', 'LPARENTHESIS', 'RPARENTHESIS', 'ID',
          'QUOTE', 'CTEINT', 'CTEFLOAT', 'CTECHAR'
          #,'TRUE', 'FALSE', 'AND', 'OR'
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
    r'\'[^\n"]\''
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

# Directorio de variables globales
dir_var_globales = {}
dir_var_locales = {}

# Pila de variables globales y locales
pila_var_globales = []
pila_var_locales = []
pila_funciones = []
pila_var_funciones = []

# Directorio de funciones
dir_funciones = {}
dir_var_funciones = {}
dir_var_locales_funciones = {}

# Directorio de procedimientos
dir_proc = {}

# Directorio de cuadruplos
dir_cuadruplos = {}

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

# Cantidad de cuadruplos
contador_cuadruplos = 0

# Cantidad de variables por tipos
cantidad_int = 0
cantidad_float = 0
cantidad_char = 0
cantidad_bool = 0

# Cantidad de variables
cantidad_vars = {'INT' : cantidad_int, 'FLOAT' : cantidad_float, 'CHAR' : cantidad_char, 'BOOL' : cantidad_bool}

###########################
## Dicrecciones virtuales##
###########################

# Locales
int_dir_locales = 10000
float_dir_locales = 12500
char_dir_locales = 15000
bool_dir_locales = 17500

# Globales
int_dir_globales = 20000
float_dir_globales = 22500
char_dir_globales = 25000
bool_dir_globales = 27500

# Temporales
int_dir_temporales = 30000
float_dir_temporales = 32500
char_dir_temporales = 35000
bool_dir_temporales = 37500

# Params Funciones
int_dir_funciones = 40000
float_dir_funciones = 42500
char_dir_funciones = 45000
bool_dir_funciones = 47500

# Local Funciones
int_dir_funciones_locales = 50000
float_dir_funciones_locales = 52500
char_dir_funciones_locales = 55000
bool_dir_funciones_locales = 57500

# Funciones
id_funciones = 60000

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
ERR = -1

###########################
## Cubo Semantico        ##
###########################

# Indices del arreglo de 3 dimensiones cuboSemantico[x][y][z] donde:
# x = opdo_der
# y = opdo_izq
# z = operador

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
    '''programa : PROGRAM ID SEMICOLON variables_globales declaracion_funciones add_dir_proc MAIN LPARENTHESIS RPARENTHESIS bloque END'''
    p[0] = "OK"

    global cantidad_int
    global cantidad_float
    global cantidad_char
    global cantidad_bool
    global cantidad_vars

    print("Variables Globales")
    print(dir_var_globales)
    print("\n")

    print("Variables Locales")
    print(dir_var_locales)
    print("\n")

    print("Funciones")
    print(dir_funciones)
    print("\n")

    print("Params de Funciones")
    print(collections.OrderedDict(sorted(dir_var_funciones.items())))
    print("\n")

    print("Variables de Funciones")
    print(dir_var_locales_funciones)
    print("\n")

    print("Cuadruplos")
    print(dir_cuadruplos)
    print("\n")

    print("Contador de variables")
    print({'INT' : cantidad_int, 'FLOAT' : cantidad_float, 'CHAR' : cantidad_char, 'BOOL' : cantidad_bool})
    print("\n")

#############################
## Variables Globlaes      ##
#############################
def p_variables_globales(p):
    '''variables_globales : var_global variables_globales
      |'''

def p_var_global(p):
    '''var_global : VAR variable_global_id_loop SEMICOLON variable_global_end_loop'''

def p_variable_global_id_loop(p):
    '''variable_global_id_loop : variable_global_id_loop_coma COLON tipo global_addType'''

def p_variable_global_id_loop_coma(p):
    '''variable_global_id_loop_coma : ID add_pila_var_globales
        | ID add_pila_var_globales COMA variable_global_id_loop_coma'''

# Agrega las variabes de un solo tipo a la pila
def p_add_pila_var_globales(p):
    '''add_pila_var_globales :'''
    global pila_var_globales
    pila_var_globales.append(p[-1])

# En caso de querer seguir declarando variables de otro tipo
def p_variable_end_loop(p):
    '''variable_global_end_loop : var_global
      |'''

def p_global_addType(p):
    '''global_addType :'''
    global int_dir_globales
    global float_dir_globales
    global char_dir_globales
    global bool_dir_globales
    global cantidad_int
    global cantidad_float
    global cantidad_char
    global cantidad_bool

    scope = 'Global'

    while (len(pila_var_globales) > 0):
        tempPop = pila_var_globales.pop()

        # Checa si la variable se repite
        if dir_var_globales.has_key(tempPop) :
            print("Error: Ya existe otra variable con el ID %s" % tempPop)
            exit()
        else:
            if p[-1] == 'int' :
                dir_var_globales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : int_dir_globales}
                int_dir_globales += 1
                cantidad_int += 1
            elif p[-1] == 'float' :
                dir_var_globales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : float_dir_globales}
                float_dir_globales += 1
                cantidad_float += 1
            elif p[-1] == 'char' :
                dir_var_globales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : char_dir_globales}
                char_dir_globales += 1
                cantidad_char += 1
            elif p[-1] == 'bool' :
                dir_var_globales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : bool_dir_globales}
                bool_dir_globales += 1
                cantidad_bool += 1
            else :
                print("Error al agregar variable global")

#############################
## Variables Locales       ##
#############################
def p_variables_locales(p):
    '''variables_locales : VAR variable_local_id_loop SEMICOLON variable_local_end_loop'''

def p_variable_local_id_loop(p):
    '''variable_local_id_loop : variable_local_id_loop_coma COLON tipo local_addType'''

def p_variable_local_id_loop_coma(p):
    '''variable_local_id_loop_coma : ID add_pila_var_locales
        | ID add_pila_var_locales COMA variable_local_id_loop_coma'''

# Agrega las variabes de un solo tipo a la pila
def p_add_pila_var_locales(p):
    '''add_pila_var_locales :'''
    pila_var_locales.append(p[-1])

# En caso de querer seguir declarando variables de otro tipo
def p_variable_local_end_loop(p):
    '''variable_local_end_loop : variables_locales
      |'''

def p_local_addType(p):
    '''local_addType :'''
    global int_dir_locales
    global float_dir_locales
    global char_dir_locales
    global bool_dir_locales
    global cantidad_int
    global cantidad_float
    global cantidad_char
    global cantidad_bool

    scope = 'Local'

    while (len(pila_var_locales) > 0):
        tempPop = pila_var_locales.pop()

        # Checa si la variable se repite
        if dir_var_locales.has_key(tempPop) :
            print("Error: Ya existe otra variable con el ID %s" % tempPop)
            exit()
        else:
            if p[-1] == 'int' :
                dir_var_locales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : int_dir_locales}
                int_dir_locales += 1
                cantidad_int += 1
            elif p[-1] == 'float' :
                dir_var_locales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : float_dir_locales}
                float_dir_locales += 1
                cantidad_float += 1
            elif p[-1] == 'char' :
                dir_var_locales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : char_dir_locales}
                char_dir_locales += 1
                cantidad_char += 1
            elif p[-1] == 'bool' :
                dir_var_locales[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : bool_dir_locales}
                bool_dir_locales += 1
                cantidad_bool += 1
            else :
                print("Error al agregar variable local")

#############################
## Funciones               ##
#############################
def p_declaracion_funciones(p):
    '''declaracion_funciones : funcion declaracion_funciones
    |'''

def p_funcion(p):
    '''funcion : tipo FUNC ID add_dir_funciones LPARENTHESIS params RPARENTHESIS vars_locales_funcion bloque'''

def p_add_dir_funciones(p):
    '''add_dir_funciones : '''

    scope = 'Funcion'

    #Checa si la funcion ya esta declarada
    if p[-1] not in dir_funciones :
        dir_funciones[p[-1]] = {'Tipo' : p[-3].upper(), 'Scope' : scope, 'ID' : id_funciones}
        pila_funciones.append([p[-1]])
    else :
        print("Ya existe una funcion con este nombre")
        exit()

def p_params(p):
    '''params : ID add_pila_funciones params_loop COLON tipo function_add_type semicolon_function_loop
    |'''

def p_params_loop(p):
    '''params_loop : COMA ID add_pila_funciones params_loop
    |'''

def p_add_pila_funciones(p):
    '''add_pila_funciones : '''
    # Cecha si el parametro no se repite
    if p[-1] not in pila_var_funciones :
        pila_var_funciones.append(p[-1])
    else :
        print("Ya existe una variable con ese nombre - funcion")
        exit()

def p_semicolon_function_loop(p):
    '''semicolon_function_loop : SEMICOLON params
    |'''

def p_vars_locales_funcion(p):
    '''vars_locales_funcion : VAR ID add_pila_funciones vars_locales_id_loop COLON tipo function_local_add_type semicolon_function_local_loop
    |'''

def p_vars_locales_id_loop(p):
    '''vars_locales_id_loop : COMA ID add_pila_funciones vars_locales_id_loop
    |'''

def p_semicolon_function_local_loop(p):
    '''semicolon_function_local_loop : SEMICOLON vars_locales_funcion
    |'''

def p_function_add_type(p):
    '''function_add_type : '''
    global int_dir_funciones
    global float_dir_funciones
    global char_dir_funciones
    global bool_dir_funciones
    global cantidad_int
    global cantidad_float
    global cantidad_char
    global cantidad_bool

    scope = pila_funciones[-1][0].upper()

    while (len(pila_var_funciones) > 0) :
        tempPop = pila_var_funciones.pop()

        # Checa si el tipo de las variables
        if p[-1] == 'int' :
            dir_var_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : int_dir_funciones}
            int_dir_funciones += 1
            cantidad_int += 1
        elif p[-1] == 'float' :
            dir_var_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : float_dir_funciones}
            float_dir_funciones += 1
            cantidad_float += 1
        elif p[-1] == 'char' :
            dir_var_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : char_dir_funciones}
            char_dir_funciones += 1
            cantidad_char += 1
        elif p[-1] == 'bool' :
            dir_var_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : bool_dir_funciones}
            bool_dir_funciones += 1
            cantidad_bool += 1
        else :
            print("Error al agregar variable local")

def p_function_local_add_type(p):
    '''function_local_add_type : '''
    global int_dir_funciones_locales
    global float_dir_funciones_locales
    global char_dir_funciones_locales
    global bool_dir_funciones_locales
    global cantidad_int
    global cantidad_float
    global cantidad_char
    global cantidad_bool

    scope = pila_funciones[-1][0].upper()

    while (len(pila_var_funciones) > 0) :
        tempPop = pila_var_funciones.pop()

        # Checa si el tipo de las variables
        if p[-1] == 'int' :
            dir_var_locales_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : int_dir_funciones_locales}
            int_dir_funciones_locales += 1
            cantidad_int += 1
        elif p[-1] == 'float' :
            dir_var_locales_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : float_dir_funciones_locales}
            float_dir_funciones_locales += 1
            cantidad_float += 1
        elif p[-1] == 'char' :
            dir_var_locales_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : char_dir_funciones_locales}
            char_dir_funciones_locales += 1
            cantidad_char += 1
        elif p[-1] == 'bool' :
            dir_var_locales_funciones[tempPop] = {'Tipo' : p[-1].upper(), 'Scope' : scope, 'Dir' : bool_dir_funciones_locales}
            bool_dir_funciones_locales += 1
            cantidad_bool += 1
        else :
            print("Error al agregar variable local")

#############################
## Proc Dir                ##
#############################
def p_add_dir_proc(p):
    '''add_dir_proc :'''
    dir_proc[p[-4]] = {
        'Variables Globales' : dir_var_globales,
        'Variables Locales' : dir_var_locales,
        'Funciones' : dir_funciones
    }

#############################
## Tipos                   ##
#############################
def p_tipo(p):
    '''tipo : INTTYPE
          | FLOATTYPE
          | CHARTYPE
          | BOOLTYPE
          | VOIDTYPE'''
    p[0] = p[1]

#############################
## Bloque                  ##
#############################
def p_bloque(p):
    '''bloque : LCURLY bloque_est_loop RCURLY'''

def p_bloque_est_loop(p):
    '''bloque_est_loop : estatuto bloque_est_loop
      |'''

#############################
## Estatuto                ##
#############################
def p_estatuto(p):
    '''estatuto : asignacion
      | condicion
      | escritura
      | regreso
      | ciclo
      | variables_locales'''

#############################
## Regreso                 ##
#############################
def p_regreso(p):
    '''regreso : RETURN exp SEMICOLON'''

#############################
## Escritura               ##
#############################
def p_escritura(p):
    '''escritura : PRINT LPARENTHESIS escritura_type RPARENTHESIS SEMICOLON'''

def p_escritura_type(p):
    '''escritura_type : expresion
      | QUOTE CTECHAR QUOTE'''

#############################
## Ciclo                   ##
#############################
def p_ciclo(p):
    '''ciclo : WHILE LPARENTHESIS nodo16 expresion RPARENTHESIS nodo13 bloque nodo17'''

#############################
## Nodo16                  ##
#############################
def p_nodo16(p):
    '''nodo16 : '''
    global contador_cuadruplos

    pSaltos.append(contador_cuadruplos)

#############################
## Nodo17                  ##
#############################
def p_nodo17(p):
    '''nodo17 : '''
    global contador_cuadruplos

    salto_en_falso = pSaltos.pop()
    dir_salto = pSaltos.pop()
    dir_cuadruplos[contador_cuadruplos] = ['GOTO', "", "", dir_salto]
    contador_cuadruplos += 1
    dir_cuadruplos[salto_en_falso][3] = contador_cuadruplos

#############################
## Condicion               ##
#############################
def p_condicion(p):
    '''condicion : IF LPARENTHESIS expresion RPARENTHESIS nodo13 bloque condicion_option nodo15'''

def p_condicion_option(p):
    '''condicion_option : ELSE nodo14 bloque
      |'''

#############################
## Nodo15                  ##
#############################
def p_nodo15(p):
    '''nodo15 : '''
    global contador_cuadruplos

    salto_en_falso = pSaltos.pop()
    dir_cuadruplos[salto_en_falso][3] = contador_cuadruplos

#############################
## Nodo14                  ##
#############################
def p_nodo14(p):
    '''nodo14 : '''
    global contador_cuadruplos

    salto_en_falso = pSaltos.pop()
    dir_cuadruplos[contador_cuadruplos] = ['GOTO', "", "", ""]
    pSaltos.append(contador_cuadruplos)
    contador_cuadruplos += 1
    dir_cuadruplos[salto_en_falso][3] = contador_cuadruplos

#############################
## Nodo13                  ##
#############################
def p_nodo13(p):
    '''nodo13 : '''
    global contador_cuadruplos

    #Checa si el ultimo valor en la pila es booleano
    if pTipos[-1] == BOOL:
        opdo_izq = pOperandos.pop()
        pTipos.pop()
        dir_cuadruplos[contador_cuadruplos] = ['GOTOF', opdo_izq, "", ""]
        pSaltos.append(contador_cuadruplos)
        contador_cuadruplos += 1
    else:
        print ("Expresion no booleana")
        exit()

#############################
## Expresion               ##
#############################
def p_expresion(p):
    '''expresion : nuevaexp expresion_option nodo11 expresion_loop'''

def p_expresion_option(p):
    '''expresion_option : AND nodo12_and nuevaexp
        | OR nodo12_or nuevaexp
        |'''

def p_expresion_loop(p):
    '''expresion_loop : expresion
        |'''

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
    global contador_cuadruplos
    global bool_dir_temporales
    global cantidad_bool

    # Checa si hay algun operador relacional en la pila
    if pOperadores:
        # Checa si es operador es un AND o un OR
        if pOperadores[-1] == AND or pOperadores[-1] == OR:
            operador = pOperadores.pop()
            opdo_der = pOperandos.pop()
            tipo_der = pTipos.pop()
            opdo_izq = pOperandos.pop()
            tipo_izq = pTipos.pop()
            if cuboSemantico[tipo_der][tipo_izq][operador] != ERR :
                tipo_res = cuboSemantico[tipo_der][tipo_izq][operador]

                # Se inicializan en cero
                opdo_der_dir = 0
                opdo_izq_dir = 0

                # Checa si es operando derecho es una variable
                if opdo_der in dir_var_locales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Locales'][opdo_der]['Dir']
                elif opdo_der in dir_var_globales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Globales'][opdo_der]['Dir']

                # Checa si el operando izquierdo es una variable
                if opdo_izq in dir_var_locales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Locales'][opdo_izq]['Dir']
                elif opdo_izq in dir_var_globales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Globales'][opdo_izq]['Dir']

                # En caso de que ambos sean variables
                if opdo_izq_dir != 0 and opdo_der_dir != 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 6 :
                        dir_cuadruplos[contador_cuadruplos] = ['OR', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    elif operador == 7 :
                        dir_cuadruplos[contador_cuadruplos] = ['AND', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Expresion")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1

                # En caso que el opdo der sea variable
                elif opdo_izq_dir == 0 and opdo_der_dir != 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 6 :
                        dir_cuadruplos[contador_cuadruplos] = ['OR', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    elif operador == 7 :
                        dir_cuadruplos[contador_cuadruplos] = ['AND', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Expresion")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1

                # En caso que el opdo izq sea variable
                elif opdo_izq_dir != 0 and opdo_der_dir == 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 6 :
                        dir_cuadruplos[contador_cuadruplos] = ['OR', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    elif operador == 7 :
                        dir_cuadruplos[contador_cuadruplos] = ['AND', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Expresion")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1
                # En caso que amos sean constantes
                elif opdo_izq_dir == 0 and opdo_der_dir == 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 6 :
                        dir_cuadruplos[contador_cuadruplos] = ['OR', opdo_izq, opdo_der, bool_dir_temporales]
                    elif operador == 7 :
                        dir_cuadruplos[contador_cuadruplos] = ['AND', opdo_izq, opdo_der, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Expresion")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1
                else :
                    print("Error de asignacion - Expresion")
                    exit()

                pTipos.append(tipo_res)
                contador_cuadruplos += 1
            else:
                print("Error de condicion - valor no booleano")
                exit()

#############################
## NuevaExp                ##
#############################
def p_nuevaexp(p):
    '''nuevaexp : exp nuevaexp_type nodo10'''

def p_nuevaexp_type(p):
    '''nuevaexp_type : LESS nodo9_menor exp
      | GREATER nodo9_mayor exp
      | LESSEQUAL nodo9_menorig exp
      | GREATEREQUAL nodo9_mayorig exp
      | NOTEQUAL nodo9_dif exp
      | EQUAL nodo9_igual exp
      |'''

#############################
## Nodo10                  ##
#############################
def p_nodo10(p):
    '''nodo10 : '''
    global contador_cuadruplos
    global bool_dir_temporales
    global cantidad_bool

    # Nombre del programa
    program_name = dir_proc.keys()[0]

    # Checa si hay algun operador relacional en la pila
    if pOperadores:
        # Checa si es un operador relacional
        if pOperadores[-1] == MENOR or pOperadores[-1] == MAYOR or pOperadores[-1] == MENORIG or pOperadores[-1] == MAYORIG or pOperadores[-1] == IGUAL or pOperadores[-1] == DIF:
            operador = pOperadores.pop()
            opdo_der = pOperandos.pop()
            tipo_der = pTipos.pop()
            opdo_izq = pOperandos.pop()
            tipo_izq = pTipos.pop()
            if cuboSemantico[tipo_der][tipo_izq][operador] != ERR :
                tipo_res = cuboSemantico[tipo_der][tipo_izq][operador]

                # Se inicializan en cero
                opdo_der_dir = 0
                opdo_izq_dir = 0

                # Checa si es operando derecho es una variable
                if opdo_der in dir_var_locales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Locales'][opdo_der]['Dir']
                elif opdo_der in dir_var_globales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Globales'][opdo_der]['Dir']

                # Checa si el operando izquierdo es una variable
                if opdo_izq in dir_var_locales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Locales'][opdo_izq]['Dir']
                elif opdo_izq in dir_var_globales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Globales'][opdo_izq]['Dir']


                # En caso de que ambos sean variables
                if opdo_izq_dir != 0 and opdo_der_dir != 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 8 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYOR', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    elif operador == 9 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENOR', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    elif operador == 10 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYORIG', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    elif operador == 11 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENORIG', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    elif operador == 12 :
                        dir_cuadruplos[contador_cuadruplos] = ['IGUAL', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    elif operador == 13 :
                        dir_cuadruplos[contador_cuadruplos] = ['DIF', opdo_izq_dir, opdo_der_dir, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Nueva exp")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1

                # En caso que el opdo der sea variable
                elif opdo_izq_dir == 0 and opdo_der_dir != 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 8 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYOR', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    elif operador == 9 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENOR', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    elif operador == 10 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYORIG', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    elif operador == 11 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENORIG', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    elif operador == 12 :
                        dir_cuadruplos[contador_cuadruplos] = ['IGUAL', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    elif operador == 13 :
                        dir_cuadruplos[contador_cuadruplos] = ['DIF', opdo_izq, opdo_der_dir, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Nueva exp")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1

                # En caso que el opdo izq sea variable
                elif opdo_izq_dir != 0 and opdo_der_dir == 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 8 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYOR', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    elif operador == 9 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENOR', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    elif operador == 10 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYORIG', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    elif operador == 11 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENORIG', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    elif operador == 12 :
                        dir_cuadruplos[contador_cuadruplos] = ['IGUAL', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    elif operador == 13 :
                        dir_cuadruplos[contador_cuadruplos] = ['DIF', opdo_izq_dir, opdo_der, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Nueva exp")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1
                # En caso que amos sean constantes
                elif opdo_izq_dir == 0 and opdo_der_dir == 0 :
                    pOperandos.append(bool_dir_temporales)

                    if operador == 8 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYOR', opdo_izq, opdo_der, bool_dir_temporales]
                    elif operador == 9 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENOR', opdo_izq, opdo_der, bool_dir_temporales]
                    elif operador == 10 :
                        dir_cuadruplos[contador_cuadruplos] = ['MAYORIG', opdo_izq, opdo_der, bool_dir_temporales]
                    elif operador == 11 :
                        dir_cuadruplos[contador_cuadruplos] = ['MENORIG', opdo_izq, opdo_der, bool_dir_temporales]
                    elif operador == 12 :
                        dir_cuadruplos[contador_cuadruplos] = ['IGUAL', opdo_izq, opdo_der, bool_dir_temporales]
                    elif operador == 13 :
                        dir_cuadruplos[contador_cuadruplos] = ['DIF', opdo_izq, opdo_der, bool_dir_temporales]
                    else :
                        print("Error en el operador de asignaciones - Nueva exp")
                        exit()

                    bool_dir_temporales += 1
                    cantidad_bool += 1
                else :
                    print("Error de asignacion - Nueva exp")
                    exit()

                pTipos.append(tipo_res)
                contador_cuadruplos += 1
            else:
                print("Error arimetico - tipos no validos - Nueva exp")
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

def p_asignacion_option(p):
    '''asignacion_option : ASSIGN expresion nodo8 SEMICOLON
      | LBRACKET CTEINT RBRACKET ASSIGN nodo8 LBRACKET asignacion_type RBRACKET SEMICOLON'''

def p_asignacion_type(p):
    '''asignacion_type : CTEINT
    | CTEFLOAT
    | CTEINT COMA asignacion_type
    | CTEFLOAT COMA asignacion_type'''

#############################
## Nodo8                   ##
#############################
def p_nodo8(p):
    '''nodo8 : '''
    global contTemporales
    global contador_cuadruplos

    # Nombre del programa
    program_name = dir_proc.keys()[0]

    # Variables locales
    vars_locales = dir_proc[program_name]['Variables Locales'].keys()

    # Variables globales
    vars_globales = dir_proc[program_name]['Variables Globales'].keys()

    # Checa si el ID esta en la variables locales
    if p[-3] in vars_locales :
      pOperandos.append(p[-3])
      pOperadores.append(ASIG)
      if dir_proc[program_name]['Variables Locales'][p[-3]]['Tipo'] == 'INT' :
          pTipos.append(INT)
      elif dir_proc[program_name]['Variables Locales'][p[-3]]['Tipo'] == 'FLOAT' :
          pTipos.append(FLOAT)
      elif dir_proc[program_name]['Variables Locales'][p[-3]]['Tipo'] == 'CHAR' :
          pTipos.append(CHAR)
      elif dir_proc[program_name]['Variables Locales'][p[-3]]['Tipo'] == 'BOOL' :
          pTipos.append(BOOL)
      else :
          print("Error de asignacion - tipo no valido")
          exit()

    # Checa si el ID esta en las variables globales
    elif p[-3] in vars_globales :
        pOperandos.append(p[-3])
        pOperadores.append(ASIG)
        if dir_proc[program_name]['Variables Globales'][p[-3]]['Tipo'] == 'INT' :
            pTipos.append(INT)
        elif dir_proc[program_name]['Variables Globales'][p[-3]]['Tipo'] == 'FLOAT' :
            pTipos.append(FLOAT)
        elif dir_proc[program_name]['Variables Globales'][p[-3]]['Tipo'] == 'CHAR' :
            pTipos.append(CHAR)
        elif dir_proc[program_name]['Variables Globales'][p[-3]]['Tipo'] == 'BOOL' :
            pTipos.append(BOOL)
        else :
            print("Error de asignacion - tipo no valido")
            exit()
    else :
      print("Error de asignacion - variable no declarada")
      exit()

    # Checa si la pila de operadores contiene algo
    if pOperadores :
        # En caso de ser una asignacion
        if pOperadores[-1] == ASIG :
            operador = pOperadores.pop()
            opdo_der = pOperandos.pop()
            tipo_der = pTipos.pop()
            opdo_izq = pOperandos.pop()
            tipo_izq = pTipos.pop()

            # Se verifica que los tipos seran validos en el cubo semantico
            if cuboSemantico[tipo_der][tipo_izq][operador] != ERR :
                tipo_res = cuboSemantico[tipo_der][tipo_izq][operador]

                # Se inicializan en cero
                opdo_der_dir = 0
                opdo_izq_dir = 0

                # Checa si es operando derecho es una variable
                if opdo_der in vars_locales :
                    opdo_der_dir = dir_proc[program_name]['Variables Locales'][opdo_der]['Dir']
                elif opdo_der in vars_globales :
                    opdo_der_dir = dir_proc[program_name]['Variables Globales'][opdo_der]['Dir']

                # Checa si el operando izquierdo es una variable
                if opdo_izq in vars_locales :
                    opdo_izq_dir = dir_proc[program_name]['Variables Locales'][opdo_izq]['Dir']
                elif opdo_izq in vars_globales :
                    opdo_izq_dir = dir_proc[program_name]['Variables Globales'][opdo_izq]['Dir']

                # Si es != de cero es variable de lo contrario es constante
                if opdo_izq_dir != 0 and opdo_der_dir != 0 :
                    dir_cuadruplos[contador_cuadruplos] = ['ASIG', opdo_izq_dir, "", opdo_der_dir]
                elif opdo_izq_dir == 0 and opdo_der_dir != 0 :
                    dir_cuadruplos[contador_cuadruplos] = ['ASIG', opdo_izq, "", opdo_der_dir]
                elif opdo_izq_dir != 0 and opdo_der_dir == 0 :
                    dir_cuadruplos[contador_cuadruplos] = ['ASIG', opdo_izq_dir, "", opdo_der]
                else :
                    print("Error de asignacion")

                contador_cuadruplos+=1
            else :
                print("Error de asignacion - tipo de variable no es compatible con asignacion")
                exit()

#############################
## Exp                     ##
#############################
def p_exp(p):
    '''exp : termino nodo5 exp_loop'''

def p_exp_loop(p):
    '''exp_loop : exp_type_loop
      |'''

def p_exp_type_loop(p):
    '''exp_type_loop : ADDITION nodo3_suma exp
      | SUBTRACTION nodo3_resta exp'''

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
    global contador_cuadruplos
    global int_dir_temporales
    global float_dir_temporales
    global cantidad_int
    global cantidad_float

    # Nombre del programa
    program_name = dir_proc.keys()[0]

    # Checamos si existe existe aglun operador en la pila
    if pOperadores :
        # Checamos si el operador es Suma o Resta
        if pOperadores[-1] == SUMA or pOperadores[-1]== RESTA :
            operador = pOperadores.pop()
            opdo_der = pOperandos.pop()
            tipo_der = pTipos.pop()
            opdo_izq = pOperandos.pop()
            tipo_izq = pTipos.pop()

            # Checamos si los tipos son compatibles
            if cuboSemantico[tipo_der][tipo_izq][operador] != ERR and (cuboSemantico[tipo_der][tipo_izq][operador] == INT or cuboSemantico[tipo_der][tipo_izq][operador] == FLOAT) :
                tipo_res = cuboSemantico[tipo_der][tipo_izq][operador]

                # Se inicializan en cero
                opdo_der_dir = 0
                opdo_izq_dir = 0

                # Checa si es operando derecho es una variable
                if opdo_der in dir_var_locales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Locales'][opdo_der]['Dir']
                elif opdo_der in dir_var_globales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Globales'][opdo_der]['Dir']

                # Checa si el operando izquierdo es una variable
                if opdo_izq in dir_var_locales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Locales'][opdo_izq]['Dir']
                elif opdo_izq in dir_var_globales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Globales'][opdo_izq]['Dir']


                # En caso de que ambos sean variables
                if opdo_izq_dir != 0 and opdo_der_dir != 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq_dir, opdo_der_dir, int_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq_dir, opdo_der_dir, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq_dir, opdo_der_dir, float_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq_dir, opdo_der_dir, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - Exp")
                        exit()

                # En caso que el opdo der sea variable
                elif opdo_izq_dir == 0 and opdo_der_dir != 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq, opdo_der_dir, int_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq, opdo_der_dir, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq, opdo_der_dir, float_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq, opdo_der_dir, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - Exp")
                        exit()

                # En caso que el opdo izq sea variable
                elif opdo_izq_dir != 0 and opdo_der_dir == 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq_dir, opdo_der, int_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq_dir, opdo_der, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq_dir, opdo_der, float_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq_dir, opdo_der, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - Exp")
                        exit()

                # En caso que amos sean constantes
                elif opdo_izq_dir == 0 and opdo_der_dir == 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq, opdo_der, int_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq, opdo_der, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 1 :
                            dir_cuadruplos[contador_cuadruplos] = ['SUMA', opdo_izq, opdo_der, float_dir_temporales]
                        elif operador == 2 :
                            dir_cuadruplos[contador_cuadruplos] = ['RESTA', opdo_izq, opdo_der, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - Exp")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - Exp")
                        exit()
                else :
                    print("Error de asignacion - Exp")
                    exit()

                pTipos.append(tipo_res)
                contador_cuadruplos += 1
            else:
                print("Error arimetico - tipos no validos - Exp")
                exit()

#############################
## Termino                 ##
#############################
def p_termino(p):
    '''termino : factor nodo4 termino_loop'''

def p_termino_loop(p):
    '''termino_loop : termino_type_loop
      |'''

def p_termino_type_loop(p):
    '''termino_type_loop : MULTIPLICATION nodo2_mult termino
      | DIVISION nodo2_div termino'''

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
    global contador_cuadruplos
    global int_dir_temporales
    global float_dir_temporales
    global cantidad_int
    global cantidad_float

    # Nombre del programa
    program_name = dir_proc.keys()[0]

    # Checamos si existe existe aglun operador en la pila
    if pOperadores :
        # Checamos si el operador es Multiplicacion o Division
        if pOperadores[-1] == MULT or pOperadores[-1]== DIV :
            operador = pOperadores.pop()
            opdo_der = pOperandos.pop()
            tipo_der = pTipos.pop()
            opdo_izq = pOperandos.pop()
            tipo_izq = pTipos.pop()

            # Checamos si los tipos son compatibles
            if cuboSemantico[tipo_der][tipo_izq][operador] != ERR and (cuboSemantico[tipo_der][tipo_izq][operador] == INT or cuboSemantico[tipo_der][tipo_izq][operador] == FLOAT) :
                tipo_res = cuboSemantico[tipo_der][tipo_izq][operador]

                # Se inicializan en cero
                opdo_der_dir = 0
                opdo_izq_dir = 0

                # Checa si es operando derecho es una variable
                if opdo_der in dir_var_locales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Locales'][opdo_der]['Dir']
                elif opdo_der in dir_var_globales.keys() :
                    opdo_der_dir = dir_proc[program_name]['Variables Globales'][opdo_der]['Dir']

                # Checa si el operando izquierdo es una variable
                if opdo_izq in dir_var_locales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Locales'][opdo_izq]['Dir']
                elif opdo_izq in dir_var_globales.keys() :
                    opdo_izq_dir = dir_proc[program_name]['Variables Globales'][opdo_izq]['Dir']


                # En caso de que ambos sean variables
                if opdo_izq_dir != 0 and opdo_der_dir != 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq_dir, opdo_der_dir, int_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq_dir, opdo_der_dir, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq_dir, opdo_der_dir, float_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq_dir, opdo_der_dir, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - termino")
                        exit()

                # En caso que el opdo der sea variable
                elif opdo_izq_dir == 0 and opdo_der_dir != 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq, opdo_der_dir, int_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq, opdo_der_dir, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq, opdo_der_dir, float_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq, opdo_der_dir, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - termino")
                        exit()

                # En caso que el opdo izq sea variable
                elif opdo_izq_dir != 0 and opdo_der_dir == 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq_dir, opdo_der, int_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq_dir, opdo_der, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq_dir, opdo_der, float_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq_dir, opdo_der, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - termino")
                        exit()

                # En caso que amos sean constantes
                elif opdo_izq_dir == 0 and opdo_der_dir == 0 :
                    if tipo_res == INT :
                        pOperandos.append(int_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq, opdo_der, int_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq, opdo_der, int_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        int_dir_temporales += 1
                        cantidad_int += 1
                    elif tipo_res == FLOAT :
                        pOperandos.append(float_dir_temporales)

                        if operador == 3 :
                            dir_cuadruplos[contador_cuadruplos] = ['MULT', opdo_izq, opdo_der, float_dir_temporales]
                        elif operador == 4 :
                            dir_cuadruplos[contador_cuadruplos] = ['DIV', opdo_izq, opdo_der, float_dir_temporales]
                        else :
                            print("Error en el operador de asignaciones - termino")
                            exit()

                        float_dir_temporales += 1
                        cantidad_float += 1
                    else :
                        print("Error en tipo de respuesta - termino")
                        exit()
                else :
                    print("Error de asignacion - termino")
                    exit()

                pTipos.append(tipo_res)
                contador_cuadruplos+=1
            else:
                print("Error arimetico - tipos no validos - termino")
                exit()

#############################
## Factor                  ##
#############################
def p_factor(p):
    '''factor : factor_var
      | factor_exp'''

def p_factor_var(p):
    '''factor_var : varcte nodo1'''

def p_factor_exp(p):
    '''factor_exp : LPARENTHESIS nodo6 expresion RPARENTHESIS nodo7'''

#############################
## Nodo1                   ##
#############################
def p_nodo1(p):
    '''nodo1 : '''
    # Checa que no sea una variable ya declarada previamente
    if p[-1] not in dir_var_locales.keys() and p[-1] not in dir_var_globales.keys() :
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

    # Checa que esta el parentesis que abre
    if pOperadores[-1] == "(" :
        pOperadores.pop()
    else:
        print("Falta parentesis izquierdo")

#############################
## Varcte                  ##
#############################
def p_varcte(p):
    '''varcte : ID varcte_arr nodoCteV
      | CTEINT nodoCteE
      | CTEFLOAT nodoCteF
      | CTEBOOL nodoCteB
      | CTECHAR nodoCteC'''
    p[0] = p[1]

# Verifica si es valor es booleano
def p_CTEBOOL(p):
    '''CTEBOOL : TRUE
        | FALSE'''
    p[0] = p[1]

# Verifica si es un arreglo
def p_varcte_arr(p):
    '''varcte_arr : LBRACKET RBRACKET
      |'''

#############################
## Nodo cteV               ##
#############################
def p_nodoCteV(p):
    '''nodoCteV : '''
    # Checa si el ID esta en las variables locales
    if p[-2] in dir_var_locales.keys() :
        pOperandos.append(dir_var_locales[p[-2]]['Dir'])
        if dir_var_locales[p[-2]]['Tipo'] == 'INT' :
            pTipos.append(1)
        elif dir_var_locales[p[-2]]['Tipo'] == 'FLOAT' :
            pTipos.append(2)
        elif dir_var_locales[p[-2]]['Tipo'] == 'CHAR' :
            pTipos.append(3)
        elif dir_var_locales[p[-2]]['Tipo'] == 'BOOL' :
            pTipos.append(4)
        else :
            print("Error en asignacion de tipo de variable")
            exit()

    # Checa si el ID esta en las variables globales
    elif p[-2] in dir_var_globales.keys() :
        pOperandos.append(dir_var_globales[p[-2]]['Dir'])
        if dir_var_globales[p[-2]]['Tipo'] ==  'INT' :
            pTipos.append(1)
        elif dir_var_globales[p[-2]]['Tipo'] == 'FLOAT' :
            pTipos.append(2)
        elif dir_var_globales[p[-2]]['Tipo'] == 'CHAR' :
            pTipos.append(3)
        elif dir_var_globales[p[-2]]['Tipo'] == 'BOOL' :
            pTipos.append(4)
        else :
            print("Error en asignacion de tipo de variable")
            exit()
    else :
        print("Variable no declarada")
        exit()

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
    exit()

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
				print ("FINAL");

		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')
