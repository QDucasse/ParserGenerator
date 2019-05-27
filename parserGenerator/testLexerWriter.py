import re
import sys
import argparse
from lexer import Lexer
from parser import Parser
#from visitor import Visitor
from lexerWriter import LexerWriter

if __name__ == '__main__':
    testFileName = 'test/pascal_grammar.ebnf'

    try:
      with open(testFileName, 'r') as testFile:
          testFileData = testFile.readlines()
    except FileNotFoundError:
      print('Error: test file {} does not exist'.format(testFileName))
      sys.exit()

    lexer = Lexer()
    tokens = lexer.lex(testFileData)

    verbose = False
    parser = Parser(verbose)
    grammar = parser.parse(tokens)

    writer = LexerWriter()
    writer.visit(grammar)
    print(writer.lexemList)
    writer.write(writer.lexemList)
