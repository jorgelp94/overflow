
import ply.lex as lex

# List of token names.   This is always required

reserved = {
  'program' : 'PROGRAM',
  'print' : 'PRINT',
  'end' : 'END',
  'if' : 'IF',
  'else' : 'ELSE',
  'var' : 'VAR',
  'int' : 'INTTYPE',
  'float' : 'FLOATTYPE',
  'char'  : 'CHARTYPE',
  'bool'  : 'BOOLTYPE',
  'string'  : 'STRINGTYPE',
  'void'    : 'VOIDTYPE',
  'while' : 'WHILE',
  'func'  : 'FUNC',
  'and' : 'AND',
  'or'  : 'OR',
  'main' : 'MAIN',
  'return' : 'RETURN',
}

tokens = [
   'COMA',
   'SEMICOLON',
   'COLON',
   'MULTIPLICATION',
   'ADDITION',
   'SUBTRACTION',
   'DIVISION',
   'EQUAL',
   'ASSIGN',
   'LESS',
   'GREATER',
   'NOTEQUAL',
   'LESSEQUAL',
   'GREATEREQUAL',
   'LCURLY',
   'RCURLY',
   'LBRACKET',
   'RBRACKET',
   'LPARENTHESIS',
   'RPARENTHESIS',
   'CTESTRING',
   'INT',
   'FLOAT',
   'ID',
   'QUOTE',
   'BOOL',
   'CHAR',
   'STRING',
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

# Build the lexer
lexer = lex.lex()
