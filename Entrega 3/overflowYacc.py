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
    '''programa : PROGRAM createProcDir ID addProcDir SEMICOLON a b MAIN LPARENTHESIS RPARENTHESIS bloque END'''
    p[0] = "OK"

def p_createProcDir(p):
    '''createProcDir :'''
    dirProc = {}

def p_addProcDir(p):
    '''addProcDir :'''
    dirProc[p[-1]] = {'Variables' : varDir, 'Tipo' : p[-3]}

def p_a(p):
    '''a : variable
      | variable a
      |'''

def p_b(p):
    '''b : funcion b
      |'''

def p_bloque(p):
    '''bloque : LCURLY c RCURLY'''

def p_c(p):
    '''c : estatuto c
      |'''

def p_tipo(p):
    '''tipo : INTTYPE
          | FLOATTYPE
          | CHARTYPE
          | BOOLTYPE
          | STRINGTYPE
          | VOIDTYPE'''
    p[0] = p[1]

def p_estatuto(p):
    '''estatuto : asignacion
      | condicion
      | escritura
      | regreso
      | ciclo'''

def p_regreso(p):
    '''regreso : RETURN exp SEMICOLON'''

def p_variable(p):
    '''variable : VAR createVarDir d'''

def p_createVarDir(p):
    '''createVarDir :'''
    varDir = {}

def p_d(p):
    '''d : e COLON tipo addType SEMICOLON f'''

def p_addType(p):
    '''addType :'''
    scope = 'Global'
    while (len(varList) > 0):
        varDir[varList.pop()] = {'Tipo' : p[-1], 'Scope' : scope}
    #print(varDir)

def p_e(p):
    '''e : ID addVarDir
      | ID addVarDir LBRACKET RBRACKET COMA e
      | ID addVarDir LBRACKET RBRACKET
      | ID addVarDir COMA e'''

def p_addVarDir(p):
    '''addVarDir :'''
    varList.append(p[-1])
    #print(varList)

def p_f(p):
    '''f : d
      |'''

def p_asignacion(p):
    '''asignacion : ID g'''

def p_g(p):
    '''g : ASSIGN expresion SEMICOLON
      | LBRACKET RBRACKET ASSIGN LBRACKET h RBRACKET SEMICOLON'''

def p_h(p):
    '''h : expresion
    | expresion COMA h'''

def p_exp(p):
    '''exp : termino i'''

def p_i(p):
    '''i : j
      |'''

def p_j(p):
    '''j : ADDITION exp
      | SUBTRACTION exp'''

def p_termino(p):
    '''termino : factor k'''

def p_k(p):
    '''k : l
      |'''

def p_l(p):
    '''l : MULTIPLICATION termino
      | DIVISION termino'''

def p_factor(p):
    '''factor : m
      | n'''

def p_m(p):
    '''m : varcte'''

def p_n(p):
    '''n : LPARENTHESIS expresion RPARENTHESIS'''

def p_expresion(p):
    '''expresion : nuevaexp v'''

def p_v(p):
    '''v : w
        | w expresion
        |'''

def p_w(p):
    '''w : AND nuevaexp
        | OR nuevaexp'''

def p_nuevaexp(p):
    '''nuevaexp : exp o'''

def p_o(p):
    '''o : LESS exp
      | GREATER exp
      | LESSEQUAL exp
      | GREATEREQUAL exp
      | NOTEQUAL exp
      | EQUAL exp
      |'''

def p_varcte(p):
    '''varcte : p'''

def p_p(p):
    '''p : ID q
      | INT
      | FLOAT
      | CHAR
      | STRING
      | BOOL'''

def p_q(p):
    '''q : LBRACKET RBRACKET
      |'''

def p_condicion(p):
    '''condicion : IF LPARENTHESIS expresion RPARENTHESIS bloque r'''

def p_r(p):
    '''r : ELSE bloque
      |'''

def p_escritura(p):
    '''escritura : PRINT LPARENTHESIS s RPARENTHESIS SEMICOLON'''

def p_s(p):
    '''s : expresion
      | QUOTE CTESTRING QUOTE'''

def p_ciclo(p):
    '''ciclo : WHILE LPARENTHESIS expresion RPARENTHESIS bloque'''

def p_funcion(p):
    '''funcion : tipo FUNC ID addProcDirFunc LPARENTHESIS t RPARENTHESIS bloque'''

def p_addProcDirFunc(p):
    '''addProcDirFunc :'''
    dirProc[p[-1]] = {'Variables' : varDir2, 'Tipo' : p[-3]}

def p_t(p):
    '''t : argumentos
      |'''

def p_argumentos(p):
    '''argumentos : u'''

def p_u(p):
    '''u : ID addVarDirFunc COLON tipo addTypeFunc
      | ID addVarDirFunc COLON tipo addTypeFunc COMA u'''

def p_addVarDirFunc(p):
    '''addVarDirFunc :'''
    varList2.append(p[-1])

def p_addTypeFunc(p):
    '''addTypeFunc :'''
    scope = 'Local'
    while (len(varList2) > 0):
        varDir2[varList2.pop()] = {'Tipo' : p[-1], 'Scope' : scope}


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
