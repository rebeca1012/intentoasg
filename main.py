import sys
import ply.yacc as yacc
from Cparser import Cparser
from TypeChecker import TypeChecker


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    Pparser = Pparser()
    parser = yacc.yacc(module=Pparser)
    text = file.read()
    ast = parser.parse(text, lexer=Pparser.scanner)
    typeChecker = TypeChecker()
    typeChecker.visit(ast, None)   # or alternatively ast.accept(typeChecker)