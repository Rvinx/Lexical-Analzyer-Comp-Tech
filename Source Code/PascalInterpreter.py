import sys
import math
import random

class PascalInterpreter:
    def __init__(self, prog):
        self.prog = prog

    # collect all data statements
    def collect_data(self):
        # print('hello')
        self.data = []
        for lineno in self.stat:
            if self.prog[lineno][0] == 'DATA':
                self.data = self.data + self.prog[lineno][1]
                # print('asdf')
        self.dc = 0

    # check for end statements
    def check_end(self):
        has_end = 0
        for lineno in self.stat:
            if self.prog[lineno][0] == 'END' and not has_end:
                has_end = lineno
                # print('END INSTRUCTION')
        if not has_end:
            print("NO END INSTRUCTION")
            self.error = 1
            return
        if has_end != lineno:
            print("END IS NOT LAST")
            self.error = 1
    
    # check loops line 51

    # Evaluate an expression line 69
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
        elif etype == 'VARIABLE':
            var = expr[1]
            if var in self.vars:
                    return self.vars[var]
            else:
                print("UNDEFINED VARIABLE %s AT LINE %s" %
                        (var, self.stat[self.pc]))
                raise RuntimeError

    # Evaluate a relational expression line 126

    # Assignment line 167
    def assign(self, target, value):
        # print(target, value)
        var = target
        # print(var)
        self.vars[var] = self.eval(value)
        print(self.vars[var])


    # Change the current line number
    # def goto(self, linenum):
    #     if not linenum in self.prog:
    #         print("UNDEFINED LINE NUMBER %d AT LINE %d" %
    #         (linenum, self.stat[self.pc]))
    #         raise RuntimeError
    #     self.pc = self.stat.index(linenum)

    # Run
    def run(self):
        self.vars = {} #all variables
        self.lists = {} #list variables
        # self.tables = {} #tables
        self.loops = [] #currently active loops
        self.loopend = {} #Mapping saying where loops end
        self.gosub = None #Gosub return point (if any)
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
        
        while 1:
            line = self.stat[self.pc]
            instr = self.prog[line]
            
            op = instr[0]
            # print(op)
            # END statements
            if op == 'END':
                # print('asdf')
                break

            # goto ga perlu

            # WRITELN statement
            elif op == 'WRITELN' or op == 'WRITE':
                # print('asdf')
                plist = instr[1]
                # print(plist[0])
                out = ""
                for label, val in plist:
                    if out:
                        out += ' ' * (15 - (len(out) % 15))
                        # print('halo')
                    out += label
                    if val:
                        # print('haloo')
                        if label:
                            out += " "
                        eval = self.eval(val)
                        out += str(eval)
                        # print('haloooo')
                sys.stdout.write(out)
                # print('haloooooooo')
                end = instr[2]
                if not (end == ';'):
                    sys.stdout.write('\n')
                if end == ';':
                    # print('asdddddddddddd')
                    sys.stdout.write(" " * (3 - (len(out) % 3)))
                    if(op == 'WRITELN'):
                        sys.stdout.write('\n')                        
                    # self.pc+= 1
                    # return 
            
            # ASSIGN STATEMENT
            elif op == 'ASSIGN':
                # print(op)
                target = instr[1]
                value = instr[2]
                self.assign(target, value)
                # print(target)
            
            # VAR STATEMENT
            elif op == 'VAR':
                # print('testing var')
                # print(instr)
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

            elif op == 'DECLARE':
                print('')
                
            self.pc += 1
            
            
            # var statement line 266

            # if statement line 282

            # for statement line 289

    # line 377 gatau buat apa

    # Utility function for program listing 377

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
            # elif op == 'LET':
            #     print("%s LET %s = %s" %
            #           (line, self.var_str(instr[1]), self.expr_str(instr[2])))
            # elif op == 'READ':
            #     _out = "%s READ " % line
            #     first = 1
            #     for r in instr[1]:
            #         if not first:
            #             _out += ","
            #         _out += self.var_str(r)
            #         first = 0
            #     print(_out)
            # elif op == 'IF':
            #     print("%s IF %s THEN %d" %
            #           (line, self.relexpr_str(instr[1]), instr[2]))
            # elif op == 'GOTO' or op == 'GOSUB':
            #     print("%s %s %s" % (line, op, instr[1]))
            # elif op == 'FOR':
            #     _out = "%s FOR %s = %s TO %s" % (
            #         line, instr[1], self.expr_str(instr[2]), self.expr_str(instr[3]))
            #     if instr[4]:
            #         _out += " STEP %s" % (self.expr_str(instr[4]))
            #     print(_out)
            # elif op == 'NEXT':
            #     print("%s NEXT %s" % (line, instr[1]))
            # elif op == 'FUNC':
            #     print("%s DEF %s(%s) = %s" %
            #           (line, instr[1], instr[2], self.expr_str(instr[3])))
            # elif op == 'DIM':
            #     _out = "%s DIM " % line
            #     first = 1
            #     for vname, x, y in instr[1]:
            #         if not first:
            #             _out += ","
            #         first = 0
            #         if y == 0:
            #             _out += "%s(%d)" % (vname, x)
            #         else:
            #             _out += "%s(%d,%d)" % (vname, x, y)

            #     print(_out)
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
    