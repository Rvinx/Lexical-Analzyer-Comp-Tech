# Group 4
# 2301856932 - Nicholas Enrico
# 2301871385 - Merlyn Febriany
# 2301867633 - I Made Yoga Mahendra
# 2301892704 - Jason
# 2301879671 - Aurelius Elvin
# 2301868812 - Jenifer Valen Lesmana

from ply import *

# SIMPLE LOOPING WITH CONDITIONAL IF BLOCK WITH PLY

keywords =('BEGIN', 'END', 'PROGRAM', 'WRITELN', 'VAR', 'INTEGER', 'FLOAT', 'CHARACTER', 'DOUBLE', 'BOOLEAN', 'REAL', 'MOD','IF','ELSE' ,'THEN', 'FOR','DO', 'WRITE')

tokens =keywords +('COMMA', 'SEMI_COLON', 'ID', 'OPEN_PAREN', 'CLOSE_PAREN',
'STRING', 'SINGLE_QUOTE', 'NEWLINE', 'DOT', 'INTEGER', 'FLOAT',
'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'LOWER_THAN',
'LOWER_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'NOT_EQUAL', 'COLON', 'BLOCK')

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9]*'
    if t.value.upper() in keywords:
        t.type = t.value.upper()
    return t

def t_space(t):
    r'\ '
    pass

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER =r'\^'
t_DIVIDE = r'/'
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_LOWER_THAN = r'<'
t_LOWER_EQUAL = r'<='
t_GREATER_THAN = r'>'
t_GREATER_EQUAL = r'>='
t_NOT_EQUAL = r'<>'
t_COMMA = r'\,'
t_SEMI_COLON = r';'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\'.*?\''
t_SINGLE_QUOTE = r'\''
t_COLON = r':'
t_DOT = r'\.'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_BLOCK(t):
    r'\t+' 

    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = 'PROGRAM LISTODDNUMBER; \n'
data = data + 'VAR num,oddnum: integer; \n'
data = data + 'BEGIN\n'
data = data + "\t WRITELN('List of Odd Number 1-100:'); \n"
data = data + '\t WRITELN; \n'
data = data + '\t FOR num:=1 TO 100 DO  \n'
data = data + '\t\t BEGIN\n'
data = data + '\t\t\t IF (num MOD 2)<>0 THEN \n'
data = data + "\t\t\t\t Begin \n"
data = data + '\t\t\t\t\t oddnum := num; \n'
data = data + "\t\t\t\t\t WRITE(oddnum,' '); \n"
data = data + "\t\t\t\t End; \n"
data = data + '\t\t\t End; \n'
data = data + 'END.'

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    print(' ')