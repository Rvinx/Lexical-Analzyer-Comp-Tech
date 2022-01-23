# Group 4
# 2301879671 - Aurelius Elvin#
# 2301856932 - Nicholas Enrico
# 2301871385 - Merlyn Febriany
# 2301867633 - I Made Yoga Mahendra
# 2301892704 - Jason
# 2301868812 - Jenifer Valen Lesmana
# 2301858282 - Ignacio Davin Haryadi

import sys
sys.path.insert(0, "../..")

import PascalParse
import PascalInterpreter

# Run menggunakan format Pascal.py filename.pas, sehingga len menjadi 2 (wajib dengan format ini karena 
# tidak menerapkan sistem interaktif)
# kalo ada error, system exit
    
with open(sys.argv[1]) as f:
    data = f.read()
prog = PascalParse.parse(data)
if not prog:
    raise SystemExit
b = PascalInterpreter.PascalInterpreter(prog)
try:
    b.run()
    raise SystemExit
except RuntimeError:
    pass

