# Group 4
# 2301879671 - Aurelius Elvin#
# 2301856932 - Nicholas Enrico
# 2301871385 - Merlyn Febriany
# 2301867633 - I Made Yoga Mahendra
# 2301892704 - Jason
# 2301868812 - Jenifer Valen Lesmana
# 2301858282 - Ignacio Davin Haryadi

from ply import *
import PascalLex

tokens = PascalLex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
)

# PASCAL dictionary

def p_program(p):
    '''program : program statement
               | statement'''
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
    p[0] = None
    p.parser.error = 1

# Some Pascal Statement, penerjemahan syntax dibantu oleh linenumber berupa integer di awal
def p_statement(p):
    '''statement : INTEGER command NEWLINE'''
    if isinstance(p[2], str):
        print("%s %s %s" % (p[2], "AT LINE", p[1]))
        p[0] = None
        p.parser.error = 1
    else:
        lineno = int(p[1])
        p[0] = (lineno, p[2])


# error handling
def p_statement_bad(p):
    '''statement : INTEGER error NEWLINE'''
    print("MALFORMED STATEMENT AT %s" % p[1])
    p[0] = None
    p.parser.error = 1

# Blank line
def p_statement_newline(p):
    '''statement : NEWLINE'''
    p[0] = None

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

# ======================================================
# WRITELN STATEMENT
def p_command_writeln(p):
    '''command : WRITELN LPAREN wlist RPAREN ending'''
    p[0] = ('WRITELN', p[3], p[5])

def p_command_writeln_bad(p):
    '''command : WRITELN error'''
    p[0] = "MALFORMED WRITELN STATEMENT"

def p_command_writeln_empty(p):
    '''command : WRITELN ending'''
    p[0] = ('WRITELN', [], None, p[2])

# WRITE STATEMENT
def p_command_write(p):
    '''command : WRITE LPAREN wlist RPAREN ending'''
    p[0] = ('WRITE', p[3], p[5])

def p_command_write_bad(p):
    '''command : WRITE error'''
    p[0] = "MALFORMED WRITE STATEMENT"

def p_command_write_empty(p):
    '''command : WRITE LPAREN RPAREN ending'''
    p[0] = ('WRITE', [], None, p[4])
# ======================================================


# ======================================================
# PROGRAM STATEMENT
def p_command_program(p):
    '''command : PROGRAM variable ending'''
    p[0] = ('PROGRAM', p[2], p[3])
# ======================================================

# ======================================================
# Var statement

def p_command_var(p):
    '''command : VAR varlist COLON variable ending'''
    p[0] = ('VAR', p[2], p[4], p[5])

def p_command_var_error(p):
    '''command : VAR error'''
    p[0] = "MALFORMED VARIABLE LIST IN VAR"

# Declare without var
def p_command_declare(p):
    '''command : variable COLON variable ending'''
    p[0] = ('', p[1], p[3], p[4])

def p_command_declare_error(p):
    '''command : variable error'''
    p[0] = "MALFORMED Declaration Variable"

# ASSIGN VALUE
def p_command_assign(p):
    '''command : variable COLON EQUALS expr SEMI'''
    p[0] = ('ASSIGN',p[1], p[4])

def p_command_varlist(p):
    '''varlist : varlist COMMA variable
               | variable'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

# Expr grammar
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
            | expr POWER expr
            | expr MOD expr '''

    p[0] = ('BINOP', p[2], p[1], p[3])
# ======================================================

# ======================================================
# Common Statement
def p_variable(p):
    '''variable : ID'''
    p[0] = p[1]

# END PROGRAM
def p_command_end(p):
    '''command : END DOT'''
    p[0] = ('END', p[2])

def p_command_begin(p):
    '''command : BEGIN'''
    p[0] = ('BEGIN',)

# end of statement
def p_ending(p):
    '''ending : SEMI'''
    p[0] = p[1]

# ======================================================
# IF Statement

def p_command_if(p):
    '''command : IF LPAREN relexpr RPAREN THEN INTEGER INTEGER'''
    p[0] = ('IF', p[3], p[6], p[7])

def p_command_if_bad(p):
    '''command : IF LPAREN error RPAREN THEN INTEGER INTEGER'''
    p[0] = "BAD RELATIONAL EXPRESSION"

def p_command_if_bad2(p):
    '''command : IF LPAREN relexpr RPAREN THEN error'''
    p[0] = "INVALID IF Statement"

def p_command_else(p):
    '''command : ELSE'''
    p[0] = ('ELSE',)

def p_command_endelseif(p):
    '''command : END ending'''
    p[0] = ('END', p[2])

def p_command_endfor(p):
    '''command : END ending INTEGER INTEGER'''
    p[0] = ('ENDFOR', p[2], p[3], p[4])

def p_command_endif(p):
    '''command : END INTEGER'''
    p[0] = ('END', p[2])
    # print(p[0])

def p_relexpr(p):
    '''relexpr : expr LT expr
               | expr LE expr
               | expr GT expr
               | expr GE expr
               | expr EQUALS expr
               | expr NE expr'''
    p[0] = ('RELOP', p[2], p[1], p[3])
# ======================================================

# ======================================================
# FOR statement
# Dengan bantuan line number untuk berpindah
def p_command_for(p):
    '''command : FOR variable COLON EQUALS expr TO expr DO INTEGER INTEGER'''
    p[0] = ('FOR', p[2], p[5], p[7], p[9], p[10])

# ======================================================

def p_wlist(p):
    '''wlist   : wlist COMMA witem
               | witem'''
    if len(p) > 3:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

def p_item_string(p):
    '''witem : STRING'''
    p[0] = (p[1][1:-1], None)

def p_item_expr(p):
    '''witem : expr'''
    p[0] = ("", p[1])

# Array of number

def p_numlist(p):
    '''numlist : numlist COMMA number
               | number'''

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]

# Number berupa tipe data integer dan float
def p_number(p):
    '''number  : INTEGER
               | FLOAT'''
    p[0] = eval(p[1])

def p_error(p):
    if not p:
        print("SYNTAX ERROR NOT EOF")
    
pparser = yacc.yacc()

def parse(data, debug=0):
    pparser.error = 0
    p = pparser.parse(data, debug=debug)
    if pparser.error:
        return None
    return p
