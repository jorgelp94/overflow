# Yacc example

import ply.yacc as yacc
import overflowLex

# Get the token map from the lexer.  This is required.
tokens = overflowLex.tokens

def p_programa(p):
    '''programa : PROGRAM ID SEMICOLON a b bloque END'''
    p[0] = "OK"

def p_a(p):
    '''a : variable
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
      | STRINGTYPE'''

def p_estatuto(p):
    '''estatuto : asignacion
      | condicion
      | escritura
      | ciclo'''

def p_variable(p):
    '''variable : VAR d'''

def p_d(p):
    '''d : e COLON tipo SEMICOLON f'''

def p_e(p):
    '''e : ID
      | ID LBRACKET RBRACKET COMA e
      | ID LBRACKET RBRACKET
      | ID COMA e'''

def p_f(p):
    '''f : d
      |'''

def p_asignacion(p):
    '''asignacion : ID g'''

def p_g(p):
    '''g : ASSIGN expresion
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
    '''expresion : exp o'''

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
    '''funcion : tipo FUNC ID LPARENTHESIS t RPARENTHESIS bloque'''

def p_t(p):
    '''t : argumentos
      |'''

def p_argumentos(p):
    '''argumentos : u'''

def p_u(p):
    '''u : ID tipo
      | ID tipo COMA u'''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error at %s!"%(p.lineno))

# Build the parser
parser = yacc.yacc(start='programa')

def archivo(file):
  fi = open(file, 'r')
  data = fi.read()
  fi.close()
  if parser.parse(data) == 'OK':
    print('Programa valido')