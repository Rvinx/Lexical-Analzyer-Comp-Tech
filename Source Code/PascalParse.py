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
    '''command : VAR variable EQUALS expr;'''
    p[0] = ('VAR', p[2], p[4])


def p_command_var_bad(p):
    '''command : VAR variable EQUALS error'''
    p[0] = "BAD EXPRESSION IN VAR"

# Statement untuk keyword write
def p_command_write(p):
    '''command : WRITE plist optend;'''
    p[0] = ('WRITE', p[2], p[3])


def p_command_write_bad(p):
    '''command : WRITE error'''
    p[0] = "MALFORMED PRINT STATEMENT"

# Stement untuk Nama Program

