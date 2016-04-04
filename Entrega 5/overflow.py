import sys
import ply.lex as lex
import ply.yacc as yacc

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
  'main' : 'MAIN', 'return' : 'RETURN'
}

###########################
## Tokens                ##
###########################
tokens = ['COMA', 'SEMICOLON', 'COLON', 'MULTIPLICATION', 'ADDITION',
          'SUBTRACTION', 'DIVISION', 'EQUAL', 'ASSIGN', 'LESS', 'GREATER',
          'NOTEQUAL', 'LESSEQUAL', 'GREATEREQUAL', 'LCURLY', 'RCURLY',
          'LBRACKET', 'RBRACKET', 'LPARENTHESIS', 'RPARENTHESIS', 'ID',
          'QUOTE', 'CTEINT', 'CTEFLOAT', 'CTECHAR', 'CTEBOOL'
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
t_NOTEQUAL        = r'<>'
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

def t_CTEBOOL(t):
    r'true| false'
    t.value = bool(t.value)
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
ERR = 6

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

def p_expresion(p):
    '''expresion : nuevaexp expresion_option expresion_loop'''
    print("pasa por expresion")

def p_expresion_option(p):
    '''expresion_option : AND nuevaexp
        | OR nuevaexp
        |'''
    print("pasa por expresion_option")

def p_expresion_loop(p):
    '''expresion_loop : expresion
        |'''
    print("pasa por expresion_loop")

def p_nuevaexp(p):
    '''nuevaexp : exp nuevaexp_type'''
    print("pasa por nuevaexp")

def p_nuevaexp_type(p):
    '''nuevaexp_type : LESS exp
      | GREATER exp
      | LESSEQUAL exp
      | GREATEREQUAL exp
      | NOTEQUAL exp
      | EQUAL exp
      |'''
    print("pasa por nuevaexp_type")

def p_condicion(p):
    '''condicion : IF LPARENTHESIS expresion RPARENTHESIS bloque condicion_option'''
    print("pasa por condicion")

def p_condicion_option(p):
    '''condicion_option : ELSE bloque
      |'''
    print("pasa por condicion_option")

def p_escritura(p):
    '''escritura : PRINT LPARENTHESIS escritura_type RPARENTHESIS SEMICOLON'''
    print("pasa por escritura")

def p_escritura_type(p):
    '''escritura_type : expresion
      | QUOTE CTECHAR QUOTE'''
    print("pasa por escritura_type")

def p_ciclo(p):
    '''ciclo : WHILE LPARENTHESIS expresion RPARENTHESIS bloque'''
    print("pasa por ciclo")

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
            print("Error en tipo de asignacion")
        pOperadores.append(ASIG)
    else:
        print "Variable invalida"
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
                cuadruplos[contCuadruplos] = [op, opdoIzq, opdoDer, opdoDer]
                contCuadruplos+=1
                print(cuadruplos)
            else:
                print("Error de tipos asignados")
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
                print("Error de Semantica")
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
                print("Error de Semantica")
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
    print("..........................")
    print(p[0])
    print("..........................")

def p_varcte_arr(p):
    '''varcte_arr : LBRACKET RBRACKET
      |'''
    print("pasa por varcte_arr")

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
    print("@@@@@@@@@@@@@@@@@@@@@@@@")

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
