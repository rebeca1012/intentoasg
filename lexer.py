import re
import ply.lex as lex
import sys

#contador de errores:

cont = 0

#Lista de tokens:

tokens = ('TkComa', 'TkParAbre', 'TkParCierra', 'TkAsignacion', 'TkPuntoYComa', 'TkMas', 'TkMenos',
          'TkIdent', 'TkNumLit', 'TkMult', 'TkDiv', 'TkDisyuncion', 'TkConjuncion', 'TkNegacion', 'TkMenor',
          'TkMenorIgual', 'TkMayorIgual', 'TkMayor', 'TkIgual', 'TkDesigual',  'TkConcatHorizontal', 
          'TkConcatVertical', 'TkTrue', 'TkFalse', 'TkRotacion', 'TkTransposicion', 'TkMod', 'TkCanvasLit',
          'TkIf', 'TkThen', 'TkOtherwise', 'TkDone', 'TkWhile', 'TkRepeat', 'TkWith', 'TkFrom', 'TkTo', 'TkUsing',
          'TkOf', 'TkType', 'TkInteger', 'TkBoolean', 'TkCanvas', 'TkBegin', 'TkEnd', 'TkPrint', 'TkRead')


#Palabras reservadas:
"""
def t_Tk(t):
    r'if|then|otherwise|done|while|repeat|with|from|to|using|of|type|integer|boolean|canvas|begin|end|print|read'
    return t
"""

def t_TkIf(t):
   r'if'
   return t

def t_TkThen(t):
    r'then'
    return t 

def t_TkOtherwise(t):
    r'otherwise'
    return t

def t_TkDone(t):
    r'done'
    return t 

def t_TkWhile(t):
    r'while'
    return t 

def t_TkRepeat(t):
    r'repeat'
    return t 

def t_TkWith(t):
    r'with'
    return t 

def t_TkFrom(t):
    r'from'
    return t 

def t_TkTo(t):
    r'to'
    return t 

def t_TkUsing(t):
    r'using'
    return t 

def t_TkOf(t):
    r'of'
    return t 

def t_TkType(t):
    r'type'
    return t 

def t_TkInteger(t):
    r'integer'
    return t 

def t_TkBoolean(t):
    r'boolean'
    return t

def t_TkCanvas(t):
    r'canvas'
    return t 

def t_TkBegin(t):
    r'begin'
    return t 

def t_TkEnd(t):
    r'end'
    return t 

def t_TkPrint(t):
    r'print' 
    return t 

def t_TkRead(t):
    r'read'
    return t 


#Literales Booleanos:

t_TkTrue = 'true'
t_TkFalse = 'false'


#Separadores"


t_TkComa = r','
t_TkPuntoYComa = r';'
t_TkParAbre = r'\('
t_TkParCierra = r'\)'


#Operadores aritmeticos:

t_TkMas = r'\+'
t_TkMenos = r'-'
t_TkMult = r'\*'
t_TkDiv = r'/'
t_TkMod = r'%'
t_TkConjuncion = r'/\\'
t_TkDisyuncion = r'\\/'
t_TkNegacion = r'\^' 
t_TkMenor = r'<'
t_TkMenorIgual = r'<='
t_TkMayor = r'>'
t_TkMayorIgual = r'>='
t_TkIgual = r'='
t_TkDesigual = r'\/='
t_TkConcatHorizontal = r':'
t_TkConcatVertical = r'\|'
t_TkRotacion = r'\$'
t_TkTransposicion = r'\''
t_TkAsignacion = r':='

#Literales Numericos:

def t_TkNumLit(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Identificadores de variables:

def t_TkIdent(t):
    r'[a-zA-Z][a-zA-Z]*[0-9]*'
    return t

#Literales de lienzo:

def t_TkCanvasLit(t):
    r'</>|<empty>|<\\>|<\|>|<_>|<\.>'
    return t 
    

#Ignorar comentarios:

def t_TkComment(t):
    r'{\-(.|\n)+?\-}'
    pass

#Contar lineas:

def t_lineas(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Ignorar espacios y tabuladores:

t_ignore = ' \t'

#Manejo de errores:

def t_error(t):
    global cont
    global datos
    print('Error lexico:   Caracter inesperado "' + t.value[0] + '" en la fila ' + str(t.lineno) + ', columna ' + str(find_column(datos, t)))
    cont += 1
    t.lexer.skip(1)

#Calculo de columna:

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

#Construccion:

lexer = lex.lex()

#Tomamos el arhivo como string

archivo = open(input(), "r")
datos = archivo.read()
archivo.close()

# #Introducimos la informacion al lexer

# lexer.input(datos)

# #Hacemos una corrida en busca de errores

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break

# #"Reseteamos" el lexer para imprimir los tokes si no se encontraron errores

# lexer.input(datos)
# lexer.lineno = 1
# lexer.lexpos = 0

# #Imprimimos los tokens con su tipo, fila y columna

# linecnt = 1

# while cont == 0:
#     tok = lexer.token()
#     if not tok: 
#         break
#     if tok.type == 'Tk':
#         if linecnt < tok.lineno:
#             linecnt = tok.lineno
#             print("")
#             print(tok.type+tok.value.title(), end=" ")
#         else:
#             print(tok.type+tok.value.title(), end=" ")
    
#     elif tok.type == 'TkIdent':
#         if linecnt < tok.lineno:
#             linecnt = tok.lineno
#             print("")
#             print(tok.type+'("'+tok.value+'")', end=" ")
#         else:    
#             print(tok.type+'("'+tok.value+'")', end=" ")
    
#     elif tok.type == 'TkNumLit':
#         if linecnt < tok.lineno:
#             linecnt = tok.lineno
#             print("")
#             print(tok.type+'('+str(tok.value)+')', end=" ")
#         else:
#             print(tok.type+'('+str(tok.value)+')', end=" ")
    
#     elif tok.type == 'TkCanvasLit':
#         if linecnt < tok.lineno:
#             linecnt = tok.lineno
#             print("")
#             print(tok.type+'("'+tok.value+'")', end=" ")
#         else:
#             print(tok.type+'("'+tok.value+'")', end=" ")
#     else:

#         if linecnt < tok.lineno:
#             linecnt = tok.lineno
#             print("")
#             print(tok.type, end=" ")
#         else:
#             print(tok.type, end=" ")

# print("", end="\n")