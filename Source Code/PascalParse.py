from ply import *
import PascalLex

tokens = PascalLex.tokens

# precedence = (
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
#     ('left', 'POWER'),
#     # ('right', 'UMINUS')
# )

# PASCAL dictionary

def p_program(p):
    '''program : program statement
               | statement'''
    # print('asdfasfda')
    if len(p) == 2 and p[1]:
        p[0] = {}
        line, stat = p[1]
        p[0][line] = stat
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = {}
        if p[2]:
            line, stat = p[2]
            p[0][line] = stat

# catch error
def p_program_error(p):
    '''program : error'''
    # print('error')
    p[0] = None
    p.parser.error = 1

# Some Pascal Statement
def p_statement(p):
    '''statement : INTEGER command NEWLINE'''
    # print('asdfasdfa')
    if isinstance(p[2], str):
        print("%s %s %s" % (p[2], "AT LINE", p[1]))
        p[0] = None
        p.parser.error = 1
        # print('asdfasdf')
    else:
        # print('asdfasdf')
        lineno = int(p[1])
        p[0] = (lineno, p[2])


# error handling
def p_statement_bad(p):
    '''statement : INTEGER error NEWLINE'''
    print("MALFORMED STATEMENT AT %s" % p[1])
    p[0] = None
    p.parser.error = 1

# B line
def p_statement_newline(p):
    '''statement : NEWLINE'''
    p[0] = None

# nanti ke line 93
# def p_command_var(p):
#     '''command : VAR variable COLON'''

# DATA statement

# Blank line number
def p_statement_blank(p):
    '''statement : INTEGER NEWLINE'''
    p[0] = (0, ('BLANK', int(p[1])))

def p_command_data(p):
    '''command : DATA numlist'''
    p[0] = ('DATA', p[2])


def p_command_data_bad(p):
    '''command : DATA error'''
    p[0] = "MALFORMED NUMBER LIST IN DATA"

# ===================================================
# WRITELN STATEMENT
def p_command_writeln(p):
    '''command : WRITELN LPAREN wlist RPAREN ending'''
    p[0] = ('WRITELN', p[3], p[5])
    # print(p[3])

def p_command_writeln_bad(p):
    '''command : WRITELN error'''
    p[0] = "MALFORMED WRITELN STATEMENT"

def p_command_writeln_empty(p):
    '''command : WRITELN LPAREN RPAREN ending'''
    p[0] = ('WRITELN', [], None, p[4])

# WRITE STATEMENT
def p_command_write(p):
    '''command : WRITE LPAREN wlist RPAREN ending'''
    p[0] = ('WRITE', p[3], p[5])
    # print(p[3])

def p_command_write_bad(p):
    '''command : WRITE error'''
    p[0] = "MALFORMED WRITE STATEMENT"

def p_command_write_empty(p):
    '''command : WRITE LPAREN RPAREN ending'''
    p[0] = ('WRITE', [], None, p[4])

# SOME STATEMENT
def p_command_program(p):
    '''command : PROGRAM variable ending'''
    p[0] = ('PROGRAM', p[2], p[3])
    # print(p[0])
# ===================================================
# ===================================================
# Var statement

def p_command_var(p):
    '''command : VAR varlist COLON variable ending'''
    p[0] = ('VAR', p[2], p[4], p[5])
    # print(p[3])

def p_command_var_error(p):
    '''command : VAR error'''
    p[0] = "MALFORMED VARIABLE LIST IN VAR"

# Declare without var
def p_command_declare(p):
    '''command : variable COLON variable ending'''
    p[0] = ('DECLARE', p[1], p[3], p[4])
    # print(p[3])

def p_command_declare_error(p):
    '''command : variable error'''
    p[0] = "MALFORMED Declaration Variable"

# ASSIGN VALUE
def p_command_assign(p):
    '''command : variable COLON EQUALS expr SEMI'''
    p[0] = ('ASSIGN',p[1], p[4])
    # print(p[0])

def p_command_varlist(p):
    '''varlist : varlist COMMA variable
               | variable'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_command_value(p):
    '''expr : INTEGER
            | FLOAT'''
    p[0] = ('NUM', eval(p[1]))

def p_command_variable(p):
    '''expr : variable'''
    p[0] = ('VARIABLE', p[1])

def p_expr_binary(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr POWER expr'''

    p[0] = ('BINOP', p[2], p[1], p[3])
# ==========================================================

def p_variable(p):
    '''variable : ID'''
    p[0] = p[1]

def p_command_end(p):
    '''command : END DOT'''
    p[0] = ('END',)
    # print(p[0])

def p_command_begin(p):
    '''command : BEGIN'''
    p[0] = ('BEGIN',)
    # print(p[0])

# end of statement
def p_ending(p):
    '''ending : SEMI'''
    # print('asdfasd')
    p[0] = p[1]

# lanjut di line 172

def p_wlist(p):
    '''wlist   : wlist COMMA ID
               | witem'''
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        # print('asd')
        p[0] = [p[1]]

def p_item_string(p):
    '''witem : STRING'''
    # print('sadfasdfa')
    p[0] = (p[1][1:-1], None)
    # print(p[1][1:-1])

# diline 444
# def w_item_string_expr(p):

# Builds a list of numbers as a Python list

def p_numlist(p):
    '''numlist : numlist COMMA number
               | number'''

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

# A number. May be an integer or a float


def p_number(p):
    '''number  : INTEGER
               | FLOAT'''
    p[0] = eval(p[1])

# def p_empty(p):
#     '''empty : '''

def p_error(p):
    # print(p)
    if not p:
        print("SYNTAX ERROR NOT EOF")
        # None
    
pparser = yacc.yacc()

def parse(data, debug=0):
    # print()
    # data.split('\n')
    # print(data)
    # for i in data:
    #     print(i)
    # print("pass")
    pparser.error = 0
    p = pparser.parse(data, debug=debug)
    # print('sadf')
    if pparser.error:
        # print(pparser.error)
        return None
    print(p)
    return p
