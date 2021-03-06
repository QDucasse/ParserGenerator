# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:35:45 2019

@author: Quentin Ducasse & Kevin Bedin
"""


import sys
import argparse
from mitos.core import Lexer, Parser

if __name__ == '__main__':
    testFileName = sys.argv[1]
    try:
      with open(testFileName, 'r') as testFile:
          testFileData = testFile.readlines()
    except FileNotFoundError:
      print('Error: test file {} does not exist'.format(testFileName))
      sys.exit()

    lexer = Lexer()
    lexems = lexer.lex(testFileData)

    verbose = True
    parser = Parser(verbose)
    grammar = parser.parse(lexems)
