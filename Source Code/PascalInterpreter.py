# This file provides the runtime support for running a basic program
# Assumes the program has been parsed using basparse.py

import sys
import math
import random

class PascalInterpreter:
    # inisialisasi interpreter
    def __init_(self, prog):
        self.prog = prog

        self.functions = {
            # pusyang
        }

        self.data = []
        for lineno in self.stat:
            if self.prog[lineno][0] == 'DATA':
                self.data = self.data + self.prog[lineno][1]
        self.dc = 0