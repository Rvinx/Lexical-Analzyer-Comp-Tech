# Group 4
# 2301856932 - Nicholas Enrico
# 2301871385 - Merlyn Febriany
# 2301867633 - I Made Yoga Mahendra
# 2301892704 - Jason
# 2301879671 - Aurelius Elvin
# 2301868812 - Jenifer Valen Lesmana

from ply import *

# SIMPLE LOOPING WITH CONDITIONAL IF BLOCK WITH PLY

keywords =('BEGIN', 
    # 'End' ,
     'END', 'PROGRAM', 'WRITELN', 
     'VAR', 
    # 'IF','ELSE' ,'THEN', 'FOR','DO', 'WRITE', 
    'DATA',
    # 'BLANK'
    )

tokens =keywords +(
    'COMMA', 
    'SEMI', 
    'ID', 
    'LPAREN', 'RPAREN',
    'STRING', 'NEWLINE', 
    'DOT', 
    'INTEGER', 'FLOAT',
    # 'REAL',
    # 'EQUALS',
    # 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 
    # 'LT',
    # 'LE', 'GT', 'GE', 'NE', 'COLON'
    )

t_ignore = ' \t'

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9]*'
    if t.value.upper() in keywords:
        t.type = t.value
    return t

def t_PROGRAM(t):
    r'PROGRAM .*'
    return t

# def t_space(t):
#     r'\ '
#     pass

# t_EQUALS = r'='
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_POWER =r'\^'
# t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
# t_LT = r'<'
# t_LE = r'<='
# t_GT = r'>'
# t_GE = r'>='
# t_NE = r'<>'
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\'.*?\''
# t_COLON = r':'
t_DOT = r'.'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lex.lex(debug=0)
