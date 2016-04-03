import sys
import ply.lex as lex
import ply.yacc as yacc
import cuboSemantico

#############################################################################################
#Definicion del lexico del lenguaje
#############################################################################################

reserved = {
  'program' : 'PROGRAM', 'print' : 'PRINT', 'end' : 'END', 'if' : 'IF',
  'else' : 'ELSE', 'var' : 'VAR', 'int' : 'INTTYPE', 'float' : 'FLOATTYPE',
  'char'  : 'CHARTYPE', 'bool'  : 'BOOLTYPE', 'string'  : 'STRINGTYPE',
  'void'    : 'VOIDTYPE', 'while' : 'WHILE', 'func'  : 'FUNC', 'and' : 'AND',
  'or'  : 'OR', 'main' : 'MAIN', 'return' : 'RETURN',
}

tokens = ['COMA', 'SEMICOLON', 'COLON', 'MULTIPLICATION', 'ADDITION',
          'SUBTRACTION', 'DIVISION', 'EQUAL', 'ASSIGN', 'LESS', 'GREATER',
          'NOTEQUAL', 'LESSEQUAL', 'GREATEREQUAL', 'LCURLY', 'RCURLY',
          'LBRACKET', 'RBRACKET', 'LPARENTHESIS', 'RPARENTHESIS', 'CTESTRING',
          'INT', 'FLOAT', 'ID', 'QUOTE', 'BOOL', 'CHAR', 'STRING',
          ] + list(reserved.values())

# Regular expression rules for simple tokens
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
t_STRING          = r'\".*\"'
t_CHAR            = r'[a-zA-Z0-9]+'
t_BOOL            = r'(t | f)'
t_CTESTRING       = r'\".*\"'
t_FLOAT           = r'[0-9]+\.[0-9]+'
t_INT             = r'[0-9]+'
t_ignore  = ' \t'

def t_ID(t):
  r'[a-zA-Z]+(_?[a-zA-Z0-9])*'
  t.type = reserved.get(t.value, 'ID')    # Check for reserved words
  return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#############################################################################################
#Tabla de variables y Dir de procedimientos
#############################################################################################

#Diccionario de variables globales
dirVarGlobales = {}
dirVarLocal = {}
# Las variables que te encuentras por funcion
varGlobales = []
varLocales = []
# Directorio de procedimientos
dirProc = {}
#scope
scope = 'Global'

def p_programa(p):
    '''programa : PROGRAM createProcDir ID SEMICOLON programa_var_loop programa_func_loop addProcDir MAIN addMainProc LPARENTHESIS RPARENTHESIS bloque END'''
    p[0] = "OK"
    print("Pasa por programa")

def p_createProcDir(p):
    '''createProcDir :'''
    dirProc = {}
    print("Pasa por createProcessDir")

def p_addProcDir(p):
    '''addProcDir :'''
    dirProc[p[-4]] = {'Variables' : dirVarGlobales.copy(), 'Tipo' : p[-6]}
    dirVarGlobales.clear()
    print("Pasa por addProcDir")
    print(dirProc)

def p_addMainProc(p):
    '''addMainProc :'''
    dirProc[p[-1]] = {'Variables' : dirVarGlobales, 'Tipo' : 'void'}
    print("Pasa por addMainProcDir")
    print(dirProc)

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
          | STRINGTYPE
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
    '''variable : VAR createdirVarGlobales variable_loop'''
    print("pasa por variable")

def p_createdirVarGlobales(p):
    '''createdirVarGlobales :'''
    dirVarGlobales = {}
    print("pasa por createdirVarGlobales")

def p_variable_loop(p):
    '''variable_loop : variable_id_loop SEMICOLON variable_end_loop
                    | variable_arr_loop SEMICOLON variable_end_loop'''
    print("pasa por variable_loop")

def p_addType(p):
    '''addType :'''
    scope = 'Global'
    while (len(varGlobales) > 0):
        dirVarGlobales[varGlobales.pop()] = {'Tipo' : p[-1], 'Scope' : scope}
    #print(dirVarGlobales)
    print("pasa por addType")
    print(dirVarGlobales)

def p_variable_id_loop(p):
    '''variable_id_loop : variable_id_loop_coma COLON tipo addType'''
    print("pasa por variable_id_loop")

def p_variable_id_loop_coma(p):
    '''variable_id_loop_coma : ID adddirVarGlobales
        | ID adddirVarGlobales COMA variable_id_loop_coma'''
    print("pasa por variable_id_loop_coma")

def p_variable_arr_loop(p):
    '''variable_arr_loop : variable_arr_coma COLON subtipo addType'''
    print("pasa por variable_arr_loop")

def p_variable_arr_coma(p):
    '''variable_arr_coma : ID adddirVarGlobales LBRACKET RBRACKET
        | ID adddirVarGlobales LBRACKET RBRACKET COMA variable_arr_coma'''
    print("pasa por variable_arr_coma")

def p_adddirVarGlobales(p):
    '''adddirVarGlobales :'''
    varGlobales.append(p[-1])
    #print(varGlobales)
    print("pasa por adddirVarGlobales")
    print(varGlobales)

def p_variable_end_loop(p):
    '''variable_end_loop : variable_loop
      |'''
    print("pasa por variable_end_loop")

def p_asignacion(p):
    '''asignacion : ID asignacion_option'''
    print("pasa por asignacion")

def p_asignacion_option(p):
    '''asignacion_option : ASSIGN expresion SEMICOLON
      | LBRACKET INT RBRACKET ASSIGN LBRACKET asignacion_type RBRACKET SEMICOLON'''
    print("pasa por asignacion_option")

def p_asignacion_type(p):
    '''asignacion_type : INT
    | FLOAT
    | INT COMA asignacion_type
    | FLOAT COMA asignacion_type'''
    print("pasa por asignacion_type")

def p_exp(p):
    '''exp : termino exp_loop'''
    print("pasa por exp")

def p_exp_loop(p):
    '''exp_loop : exp_type_loop
      |'''
    print("pasa por exp_loop")

def p_exp_type_loop(p):
    '''exp_type_loop : ADDITION exp
      | SUBTRACTION exp'''
    print("pasa por exp_type_loop")

def p_termino(p):
    '''termino : factor termino_loop'''
    print("pasa por termino")

def p_termino_loop(p):
    '''termino_loop : termino_type_loop
      |'''
    print("pasa por termino_loop")

def p_termino_type_loop(p):
    '''termino_type_loop : MULTIPLICATION termino
      | DIVISION termino'''
    print("pasa por termino_type_loop")

def p_factor(p):
    '''factor : factor_var
      | factor_exp'''
    print("pasa por factor")

def p_factor_var(p):
    '''factor_var : varcte'''
    print("pasa por factor_var")

def p_factor_exp(p):
    '''factor_exp : LPARENTHESIS expresion RPARENTHESIS'''
    print("pasa por factor_exp")

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

def p_varcte(p):
    '''varcte : varcte_type'''
    print("pasa por varcte")

def p_varcte_type(p):
    '''varcte_type : ID varcte_arr
      | INT
      | FLOAT
      | CHAR
      | STRING
      | BOOL'''
    print("pasa por varcte_type")

def p_varcte_arr(p):
    '''varcte_arr : LBRACKET RBRACKET
      |'''
    print("pasa por varcte_arr")

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
      | QUOTE CTESTRING QUOTE'''
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
    print(dirProc)

def p_funcion_option(p):
    '''funcion_option : argumentos
      |'''
    print("pasa por funcion_option")

def p_argumentos(p):
    '''argumentos : ID adddirVarGlobalesFunc COLON tipo addTypeFunc argumentos_loop'''
    print("pasa por argumentos")

def p_argumentos_loop(p):
    '''argumentos_loop : COMA argumentos
      |'''
    print("pasa por argumentos_loop")

def p_adddirVarGlobalesFunc(p):
    '''adddirVarGlobalesFunc :  '''
    varLocales.append(p[-1])
    print("pasa por adddirVarGlobalesFunc")
    print(varLocales)

def p_addTypeFunc(p):
    '''addTypeFunc :'''
    scope = 'Local'
    while (len(varLocales) > 0):
        dirVarLocal[varLocales.pop()] = {'Tipo' : p[-1], 'Scope' : scope}
    print("pasa por addTypeFunc")
    print(dirVarLocal)


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
