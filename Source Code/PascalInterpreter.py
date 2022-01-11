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

    # def collect_data(self):
    #     self.data = []
    #     for lineno in self.stat:
    #         if self.prog[lineno][0] == 'DATA':
    #             self.data = self.data + self.prog[lineno][1]
    #     self.dc = 0

    def check_end(self):
        has_end = 0
        for lineno in self.stat:
            if self.prog[lineno][0] == 'END.' and not has_end:
                has_end = lineno
        if not has_end:
            print("NO END INSTRUCTION")
            self.error = 1
            return
        if has_end != lineno:
            print("END IS NOT LAST")
            self.error = 1
        
    # Check loops
    # nanti

    # Evaluate an expression
    # nanti

    # Evaluate a relational expression
    # nanti

    # Assignment
    # nanti

    # Change the current line number
    # nanti

    # Run
    def run(self):
        self
    