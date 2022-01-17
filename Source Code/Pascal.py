# An implementation of Dartmouth BASIC (1964)
#

import sys
sys.path.insert(0, "../..")

import PascalLex
import PascalParse
import PascalInterpreter

# If a filename has been specified, we try to run it.
# If a runtime error occurs, we bail out and enter
# interactive mode below
if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        data = f.read()
    prog = PascalParse.parse(data)
    if not prog:
        raise SystemExit
    b = PascalInterpreter.BasicInterpreter(prog)
    try:
        b.run()
        raise SystemExit
    except RuntimeError:
        pass

else:
    b = PascalInterpreter.PascalInterpreter({})

# Interactive mode.  This incrementally adds/deletes statements
# from the program stored in the BasicInterpreter object.  In
# addition, special commands 'NEW','LIST',and 'RUN' are added.
# Specifying a line number with no code deletes that line from
# the program.

while True:
    try:
        line = input("[PASCAL] ")
    except EOFError:
        raise SystemExit
    if not line:
        continue
    line += "\n"
    prog = PascalParse.parse(line)
    if not prog:
        continue

    keys = list(prog)
    if keys[0] > 0:
        b.add_statements(prog)
    else:
        stat = prog[keys[0]]
        if stat[0] == 'RUN':
            try:
                b.run()
            except RuntimeError:
                pass
        elif stat[0] == 'LIST':
            b.list()
        elif stat[0] == 'BLANK':
            b.del_line(stat[1])
        elif stat[0] == 'NEW':
            b.new()
