# Yacc example

import ply.yacc as yacc
import overflowLex
import sys

# Get the token map from the lexer.  This is required.
tokens = overflowLex.tokens
varDir = {}
varDir2 = {}
varList = []
varList2 = []
dirProc = {}
procList = []
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
    dirProc[p[-4]] = {'Variables' : varDir.copy(), 'Tipo' : p[-6]}
    varDir.clear()
    print("Pasa por addProcDir")
    print(dirProc)

def p_addMainProc(p):
    '''addMainProc :'''
    dirProc[p[-1]] = {'Variables' : varDir, 'Tipo' : 'void'}
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
    '''variable : VAR createVarDir variable_loop'''
    print("pasa por variable")

def p_createVarDir(p):
    '''createVarDir :'''
    varDir = {}
    print("pasa por createVarDir")

def p_variable_loop(p):
    '''variable_loop : variable_id_loop SEMICOLON variable_end_loop
                    | variable_arr_loop SEMICOLON variable_end_loop'''
    print("pasa por variable_loop")

def p_addType(p):
    '''addType :'''
    scope = 'Global'
    while (len(varList) > 0):
        varDir[varList.pop()] = {'Tipo' : p[-1], 'Scope' : scope}
    #print(varDir)
    print("pasa por addType")
    print(varDir)

def p_variable_id_loop(p):
    '''variable_id_loop : variable_id_loop_coma COLON tipo addType'''
    print("pasa por variable_id_loop")

def p_variable_id_loop_coma(p):
    '''variable_id_loop_coma : ID addVarDir
        | ID addVarDir COMA variable_id_loop_coma'''
    print("pasa por variable_id_loop_coma")

def p_variable_arr_loop(p):
    '''variable_arr_loop : variable_arr_coma COLON subtipo addType'''
    print("pasa por variable_arr_loop")

def p_variable_arr_coma(p):
    '''variable_arr_coma : ID addVarDir LBRACKET RBRACKET
        | ID addVarDir LBRACKET RBRACKET COMA variable_arr_coma'''
    print("pasa por variable_arr_coma")

def p_addVarDir(p):
    '''addVarDir :'''
    varList.append(p[-1])
    #print(varList)
    print("pasa por addVarDir")
    print(varList)

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
    dirProc[p[-4]] = {'Variables' : varDir2.copy(), 'Tipo' : p[-6]}
    varDir2.clear()
    print("pasa por addProcDirFunc")
    print(dirProc)

def p_funcion_option(p):
    '''funcion_option : argumentos
      |'''
    print("pasa por funcion_option")

def p_argumentos(p):
    '''argumentos : ID addVarDirFunc COLON tipo addTypeFunc argumentos_loop'''
    print("pasa por argumentos")

def p_argumentos_loop(p):
    '''argumentos_loop : COMA argumentos
      |'''
    print("pasa por argumentos_loop")

def p_addVarDirFunc(p):
    '''addVarDirFunc :'''
    varList2.append(p[-1])
    print("pasa por addVarDirFunc")
    print(varList2)

def p_addTypeFunc(p):
    '''addTypeFunc :'''
    scope = 'Local'
    while (len(varList2) > 0):
        varDir2[varList2.pop()] = {'Tipo' : p[-1], 'Scope' : scope}
    print("pasa por addTypeFunc")
    print(varDir2)


# Error rule for syntax errors
def p_error(p):
    print("Syntax error at %s, illegal token %s!"%(p.lineno, p.value))

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
