import sys
import argparse
from lexer import Lexer
from parser import Parser
#from visitor import Visitor
from prettyprinter import PrettyPrinter

if __name__ == '__main__':
    testFileName = 'grammars/ebnf_grammar.ebnf'

    try:
      with open(testFileName, 'r') as testFile:
          testFileData = testFile.readlines()
    except FileNotFoundError:
      print('Error: test file {} does not exist'.format(testFileName))
      sys.exit()

    lexer = Lexer()
    lexems = lexer.lex(testFileData)

    verbose = False
    parser = Parser(verbose)
    grammar = parser.parse(lexems)

    visitor = PrettyPrinter()
    visitor.visit(grammar)
