# Group 4
# 2301856932 - Nicholas Enrico
# 2301871385 - Merlyn Febriany
# 2301867633 - I Made Yoga Mahendra
# 2301892704 - Jason
# 2301879671 - Aurelius Elvin
# 2301868812 - Jenifer Valen Lesmana

from ply import *

# SIMPLE ARITHMETIC PASCAL-LIKE USING PLY

keywords =('BEGIN', 'END', 'PROGRAM', 'WRITELN', 'VAR', 'INTEGER', 'FLOAT', 'CHARACTER', 'DOUBLE', 'BOOLEAN', 'REAL', 'MOD')

tokens =keywords +('COMMA', 'SEMI_COLON', 'ID', 'OPEN_PAREN', 'CLOSE_PAREN',
'STRING', 'SINGLE_QUOTE', 'NEWLINE', 'DOT', 'INTEGER', 'FLOAT',
'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'LOWER_THEN',
'LOWER_EQUAL', 'GREATER_THEN', 'GREATER_EQUAL', 'NOT_EQUAL', 'COLON')

t_ignore = '\t'

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9]*' #read up/lowcase

    if t.value.upper() in keywords: #dijadiin uppercase
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
t_LOWER_THEN = r'<'
t_LOWER_EQUAL = r'<='
t_GREATER_THEN = r'>'
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

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = 'PROGRAM SUMANDAVERAGE; \n'
data = data + 'VAR num1,num2,num3:integer; \n'
data = data + '\t sum:integer; \n'
data = data + '\t avg:real; \n'
data = data + 'BEGIN\n'
data = data + '\t num1:=10; \n'
data = data + '\t num2:=20; \n'
data = data + '\t num3:=30; \n'
data = data + '\t sum:=num1+num2+num3; \n'
data = data + '\t avg:=sum/3; \n'
data = data + "\t WRITELN('Num1 is ',num1); \n"
data = data + "\t WRITELN('Num2 is ',num2); \n"
data = data + "\t WRITELN('Num3 is ',num3); \n"
data = data + "\t WRITELN('Sum 3 numbers is ',sum); \n"
data = data + "\t WRITELN('Average is ',avg) \n"
data = data + 'END'

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    print(' ')