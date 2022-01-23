# Group 4
# 2301879671 - Aurelius Elvin#
# 2301856932 - Nicholas Enrico
# 2301871385 - Merlyn Febriany
# 2301867633 - I Made Yoga Mahendra
# 2301892704 - Jason
# 2301868812 - Jenifer Valen Lesmana
# 2301858282 - Ignacio Davin Haryadi

from genericpath import exists
import sys
from typing import final

class PascalInterpreter:
    def __init__(self, prog):
        self.prog = prog

    # collect all data statements
    def collect_data(self):
        self.data = []
        for lineno in self.stat:
            if self.prog[lineno][0] == 'DATA':
                self.data = self.data + self.prog[lineno][1]
        self.dc = 0

    # check for end statements
    def check_end(self):
        has_end = 0
        for lineno in self.stat:
            if self.prog[lineno][0] == 'END' and self.prog[lineno][1] == '.' and not has_end:
                has_end = lineno
        if not has_end:
            print("NO END INSTRUCTION")
            self.error = 1
            return
        if has_end != lineno:
            print("END IS NOT LAST")
            self.error = 1

    # Untuk arithmetical expression
    def eval(self, expr):
        etype = expr[0]
        if etype == 'NUM':
            return expr[1]
        elif etype == 'BINOP':
            if expr[1] == '+':
                return self.eval(expr[2]) + self.eval(expr[3])
            elif expr[1] == '-':
                return self.eval(expr[2]) - self.eval(expr[3])
            elif expr[1] == '*':
                return self.eval(expr[2]) * self.eval(expr[3])
            elif expr[1] == '/':
                return float(self.eval(expr[2])) / self.eval(expr[3])
            elif expr[1] == '^':
                return abs(self.eval(expr[2]))**self.eval(expr[3])
            elif expr[1] == 'MOD':
                return self.eval(expr[2]) % self.eval(expr[3])
        elif etype == 'VARIABLE':
            var = expr[1]
            if var in self.vars:
                    return self.vars[var]
            else:
                print("UNDEFINED VARIABLE %s AT LINE %s" %
                        (var, self.stat[self.pc]))
                raise RuntimeError

    # Untuk if expression
    def releval(self, expr):
        etype = expr[1]
        lhs = self.eval(expr[2])
        rhs = self.eval(expr[3])
        if etype == '<':
            if lhs < rhs:
                return 1
            else:
                return 0
        elif etype == '<=':
            if lhs <= rhs:
                return 1
            else:
                return 0

        elif etype == '>':
            if lhs > rhs:
                return 1
            else:
                return 0

        elif etype == '>=':
            if lhs >= rhs:
                return 1
            else:
                return 0

        elif etype == '=':
            if lhs == rhs:
                return 1
            else:
                return 0

        elif etype == '<>':
            if lhs != rhs:
                return 1
            else:
                return 0

    # Assignment variable
    def assign(self, target, value):
        var = target
        self.vars[var] = self.eval(value)


    # Change the current line number
    def goto(self, linenum):
        if not linenum in self.prog:
            print("UNDEFINED LINE NUMBER %d AT LINE %d" %
            (linenum, self.stat[self.pc]))
            raise RuntimeError
        self.pc = self.stat.index(linenum)

    # Run
    def run(self):
        self.vars = {} #all variables
        self.error = 0 #Indicates program error

        self.stat = list(self.prog) #ordered list of all line numbers
        self.stat.sort()
        self.pc = 0 #current program counter

        # Processing prior to running

        self.collect_data() #collect all of the data statements
        self.check_end()
        # self.check_loops()

        if self.error:
            raise RuntimeError
        
        # For flag, jika true, maka looping diulang
        # dan kembali ke baris FOR
        # deklarasi variabel
        flag = 0
        newval = 0
        # 0 jika variabel for blm dibuat untuk for
        # 1 jika variabel for sudah dibuat untuk for
        initial_flag = 0

        while 1:
            line = self.stat[self.pc]
            instr = self.prog[line]
            op = instr[0]
            # END statements
            if op == 'END':
                if len(instr) == 2:
                    # jika end mengandung titik, maka program selesai
                    if instr[1] == '.':
                        break

            # WRITELN statement
            elif op == 'WRITELN' or op == 'WRITE':
                plist = instr[1]
                out = ""
                for label, val in plist:
                    if out:
                        out += ' ' * (3 - (len(out) % 15))
                    out += label
                    if val:
                        if label:
                            out += " "
                        eval = self.eval(val)
                        out += str(eval)
                sys.stdout.write(out)
                end = instr[2]
                if not (end == ';'):
                    sys.stdout.write('\n')
                if end == ';':
                    sys.stdout.write(" " * (3 - (len(out) % 3)))
                    if(op == 'WRITELN'):
                        sys.stdout.write('\n')
            
            # ASSIGN STATEMENT
            elif op == 'ASSIGN':
                if op == 'ASSIGN':
                    target = instr[1]
                    value = instr[2]
                    self.assign(target, value)
            
            # VAR STATEMENT
            elif op == 'VAR':
                for target in instr[1]:
                    if self.dc < len(self.data):
                        value = ('NUM', self.data[self.dc])
                        self.assign(target, value)
                        self.dc += 1
                    else:
                        # No more data.  Program ends
                        # print('add')
                        break
                        # return

            # FOR STATEMENT
            elif op == 'FOR':
                # INISIALISASI VARIABEL FOR
                loopvar = instr[1]

                # VALUE AWAL
                initialval = instr[2]

                # VALUE AKHIR
                finalval = int(instr[3][1])

                # JIKA initial_flag 0 (tandanya loop baru)
                if initial_flag == 0:
                    self.assign(loopvar, initialval)

                    # Initial _flag jadi 1
                    newval += int(initialval[1])
                    initial_flag = 1
                    continue

                # JIKA initial_flag 1 menandakan looping kedua dan seterusnya
                elif initial_flag == 1:
                    # Next newval, misal dari 1 ke 2
                    if newval <= finalval:
                        newNUM = ('NUM', newval)
                        self.assign(loopvar, newNUM)
                        newline = instr[4]
                        self.goto(int(newline))
                        continue
                    else:
                        newline = instr[4]
                        flag = 1
                        self.goto(int(newline))
                        continue
            
            # ENDFOR
            elif op == 'ENDFOR':
                # Jika flag 0, akan looping
                if flag == 0:
                    # Line number FOR
                    newline = int(instr[2])
                    newval += 1
                    self.goto(newline)
                    continue

                # Jika flag 1, looping berhenti dan lompat ke baris end
                elif flag == 1:
                    newval = 0
                    initial_flag = 0
                    flag = 0
                    newline = int(instr[3])
                    self.goto(newline)
                    continue

            # IF STATEMENT
            elif op == 'IF':
                relop = instr[1]
                newline = instr[2]
                toelse = instr[3]
                if(self.releval(relop)):
                    self.goto(int(newline))
                    continue
                elif not(self.releval(relop)):
                    self.goto(int(toelse))
                    continue
            self.pc += 1

    # Create a program listing
    def list(self):
        stat = list(self.prog)      # Ordered list of all line numbers
        stat.sort()
        for line in stat:
            instr = self.prog[line]
            op = instr[0]
            if op in ['END']:
                print("%s %s" % (line, op))
                continue
            elif op == 'PROGRAM':
                print("%s %s" % (line, instr[1]))
            elif op == 'WRITELN':
                _out = "%s %s " % (line, op)
                first = 1
                for p in instr[1]:
                    if not first:
                        _out += ", "
                    if p[0] and p[1]:
                        _out += '"%s"%s' % (p[0], self.expr_str(p[1]))
                    elif p[1]:
                        _out += self.expr_str(p[1])
                    else:
                        _out += '"%s"' % (p[0],)
                    first = 0
                if instr[2]:
                    _out += instr[2]
                print(_out)
            elif op == 'IF':
                print("%s IF %s THEN %d" %
                      (line, self.relexpr_str(instr[1]), instr[2]))
            elif op == 'DATA':
                _out = "%s DATA " % line
                first = 1
                for v in instr[1]:
                    if not first:
                        _out += ","
                    first = 0
                    _out += v
                print(_out)

    # erase current program
    def new(self):
        self.prog = {}

    # insert statement
    def add_statement(self, prog):
        for line, stat in prog.items():
            self.prog[line] = stat
    
    # delete statement
    def del_line(self, lineno):
        try:
            del self.prog[lineno]
        except KeyError:
            pass
    