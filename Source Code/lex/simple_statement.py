# Group 4
# 2301856932 - Nicholas Enrico
# 2301871385 - Merlyn Febriany
# 2301867633 - I Made Yoga Mahendra
# 2301892704 - Jason
# 2301879671 - Aurelius Elvin
# 2301868812 - Jenifer Valen Lesmana

from ply import *

# SIMPLE STATEMENT PASCAL-LIKE USING PLY

keywords =('BEGIN', 'END', 'PROGRAM', 'WRITELN')

tokens =keywords +('COMMA', 'SEMI_COLON', 'ID', 'OPEN_PAREN', 'CLOSE_PAREN', 'STRING', 'SINGLE_QUOTE', 'NEWLINE', 'DOT')

t_ignore = '\t' #skip tab

def t_space(t): #skip space
    r'\ '
    pass

def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    if t.value.upper() in keywords:
        t.type = t.value.upper()
    return t

t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_COMMA = r'\,'
t_SEMI_COLON = r';'
t_STRING = r'\'.*?\''
t_SINGLE_QUOTE = r'\''
t_DOT = r'\.'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = 'PROGRAM HELLOWORLD ;\n'
data = data + 'BEGIN \n'
data = data + "\t WRITELN('Hello, World!'); \n"
data = data + 'END.' 
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    print(' ')