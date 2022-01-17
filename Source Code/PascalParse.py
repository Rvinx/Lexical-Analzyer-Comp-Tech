# Syntax Analyzer

from ply import *
import PascalLex

tokens = PascalLex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
)

# Pascal Program merupakan kumpulan dari berbagai statement, oleh karena
# itu, saat menjalakannya perlu diread per baris.
# Dibawah ini merupakan function untuk merepresentasikan program
# sebagai kamus tuple yang ditandai dengan nomor baris

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

# Menangkap error. Jika error, maka akan mereturn null
def p_program_error(p):
    '''program : error'''
    p[0] = None
    p.parser.error = 1

# Formatting statement-statement yg ada pada Pascal
def p_statement(p):
    '''statement : INTEGER command NEWLINE'''
    if isinstance(p[2], str):
        print("%s %s %s" % (p[2], "AT LINE", p[1]))
        p[0] = None
        p.parser.error = 1
    else:
        lineno = int(p[1])
        p[0] = (lineno, p[2])

# Opsional, untuk menginput langsung di terminal
# def p_statement_interactive(p):
#     '''statement : RUN NEWLINE
#                  | LIST NEWLINE
#                  | NEW NEWLINE'''
#     p[0] = (0, (p[1], 0))

# Jika ada baris yang tidak punya nomor baris
def p_statement_blank(p):
    '''statement : INTEGER NEWLINE'''
    p[0] = (0, ('BLANK', int(p[1])))

# Jika ada error statement
def p_statement_bad(p):
    '''statement : INTEGER error NEWLINE'''
    print("MALFORMED STATEMENT AT LINE %s" % p[1])
    p[0] = None
    p.parser.error = 1

# Jika ada baris kosong
def p_statement_newline(p):
    '''statement : NEWLINE'''
    p[0] = None

# Statement untuk keyword Var
def p_command_var(p):
    '''command : VAR ID EQUALS expr;'''
    p[0] = ('VAR', p[2])


def p_command_var_bad(p):
    '''command : VAR ID EQUALS error'''
    p[0] = "BAD EXPRESSION IN VAR"

# Statement untuk keyword write
def p_command_write(p):
    '''command : WRITE OPEN_PARENT SINGLE_QUOTE expr SINGLE_QUOTE CLOSE_PAREN SEMI_COLON'''
    p[0] = ('WRITE', p[1], p[2], p[4], p[5], p[6])


def p_command_write_bad(p):
    '''command : WRITE OPEN_PARENT SINGLE_QUOTE error SINGLE_QUOTE CLOSE_PAREN SEMI_COLON'''
    p[0] = "MALFORMED WRITE STATEMENT"

# Statement untuk Nama Program
def p_command_program(p):
    '''command : PROGRAM ID SEMI_COLON'''
    p[0] = ('PROGRAM', p[2])


def p_command_program_bad(p):
    '''command : PROGRAM ID SEMI_COLON'''
    p[0] = "BAD EXPRESSION IN PROGRAM"

# Statement untuk Begin
def p_command_begin(p):
    '''command : BEGIN'''
    p[0] = ('BEGIN')


def p_command_begin_bad(p):
    '''command : BEGIN'''
    p[0] = "BAD EXPRESSION IN BEGIN"

# Statement untuk Begin
def p_command_end(p):
    '''command : END DOT'''
    p[0] = ('END', p[1])


def p_command_end_bad(p):
    '''command : END DOT'''
    p[0] = "BAD EXPRESSION IN END"

def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")

bparser = yacc.yacc()


def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p
