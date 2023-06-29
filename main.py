import sys
import ply.yacc as yacc
from pparser import Pparser
#from TypeChecker import TypeChecker


archivo = open(input(), "r")
datos = archivo.read()
archivo.close()

    
Pparser = Pparser()
parser = yacc.yacc(module=Pparser)
text = file.read()
#ast = parser.parse(text, lexer=Pparser.scanner)
#typeChecker = TypeChecker()
#typeChecker.visit(ast, None)   # or alternatively ast.accept(typeChecker)