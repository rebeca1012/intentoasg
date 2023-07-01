import sys
import ply.yacc as yacc
from pparser import Pparser
#from TypeChecker import TypeChecker
from lexer import Lexer

archivo = open(input(), "r")
datos = archivo.read()
archivo.close()

lexer = Lexer()
lexer.build()
lexer.input(datos)
tok = lexer.token()

while True:
    tok = lexer.token()
    if not tok: 
        break

# #"Reseteamos" el lexer para imprimir los tokes si no se encontraron errores

lexer.input(datos)
lexer.lineno = 1
lexer.lexpos = 0

# #Imprimimos los tokens con su tipo, fila y columna

linecnt = 1

while lexer.cont == 0:
    tok = lexer.token()
    if not tok: 
        break
    if tok.type == 'Tk':
        if linecnt < tok.lineno:
            linecnt = tok.lineno
            print("")
            print(tok.type+tok.value.title(), end=" ")
        else:
            print(tok.type+tok.value.title(), end=" ")
    
    elif tok.type == 'TkIdent':
        if linecnt < tok.lineno:
            linecnt = tok.lineno
            print("")
            print(tok.type+'("'+tok.value+'")', end=" ")
        else:    
            print(tok.type+'("'+tok.value+'")', end=" ")
    
    elif tok.type == 'TkNumLit':
        if linecnt < tok.lineno:
            linecnt = tok.lineno
            print("")
            print(tok.type+'('+str(tok.value)+')', end=" ")
        else:
            print(tok.type+'('+str(tok.value)+')', end=" ")
    
    elif tok.type == 'TkCanvasLit':
        if linecnt < tok.lineno:
            linecnt = tok.lineno
            print("")
            print(tok.type+'("'+tok.value+'")', end=" ")
        else:
            print(tok.type+'("'+tok.value+'")', end=" ")
    else:

        if linecnt < tok.lineno:
            linecnt = tok.lineno
            print("")
            print(tok.type, end=" ")
        else:
            print(tok.type, end=" ")

print("", end="\n")


    
# Pparser = Pparser()
# parser = yacc.yacc(module=Pparser)
# text = file.read()
#ast = parser.parse(text, lexer=Pparser.scanner)
#typeChecker = TypeChecker()
#typeChecker.visit(ast, None)   # or alternatively ast.accept(typeChecker)