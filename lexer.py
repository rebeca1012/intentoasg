import re
import ply.lex as lex
import sys

class Lexer(object):
    #contador de errores:

    cont = 0

    #Construccion:
    def build(self):
        self.lexer = lex.lex(object = self)

    def input(self,datos):
        self.datos = datos
        self.lexer.input(datos)

    def token(self):
        return self.lexer.token()

    #Palabras reservadas:

    reservado = {
        'if':'TkIf',
        'then':'TkThen',
        'otherwise':'TkOtherwise',
        'done':'TkDone',
        'while':'TkWhile',
        'repeat':'TkRepeat',
        'with':'TkWith',
        'from':'TkFrom',
        'to':'TkTo',
        'using':'TkUsing',
        'of':'TkOf',
        'type':'TkType',
        'integer':'TkInteger',
        'boolean':'TkBoolean',
        'canvas':'TkCanvas',
        'begin':'TkBegin',
        'end':'TkEnd',
        'print':'TkPrint',
        'read':'TkRead'
    }

    #Lista de tokens:

    tokens = ['TkComa', 'TkParAbre', 'TkParCierra', 'TkAsignacion', 'TkPuntoYComa', 'TkMas', 'TkMenos',
            'TkIdent', 'TkNumLit', 'TkMult', 'TkDiv', 'TkDisyuncion', 'TkConjuncion', 'TkNegacion', 'TkMenor',
            'TkMenorIgual', 'TkMayorIgual', 'TkMayor', 'TkIgual', 'TkDesigual',  'TkConcatHorizontal', 
            'TkConcatVertical', 'TkTrue', 'TkFalse', 'TkRotacion', 'TkTransposicion', 'TkMod', 'TkCanvasLit'] + list(reservado.values())

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

    def t_TkNumLit(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    #Identificadores de variables:

    def t_TkIdent(self, t):
        r'[a-zA-Z][a-zA-Z]*[0-9]*'
        t.type = Lexer.reservado.get(t.value, 'TkIdent')
        return t

    #Literales de lienzo:

    def t_TkCanvasLit(self, t):
        r'</>|<empty>|<\\>|<\|>|<_>|<\.>'
        return t 
        

    #Ignorar comentarios:

    def t_TkComment(self, t):
        r'{\-(.|\n)+?\-}'
        pass

    #Contar lineas:

    def t_lineas(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    #Ignorar espacios y tabuladores:

    t_ignore = ' \t'

    #Manejo de errores:

    def t_error(self,t):
        print('Error lexico:   Caracter inesperado "' + t.value[0] + '" en la fila ' + str(t.lineno) + ', columna ' + str(self.find_column(self.datos, t)))
        self.cont += 1
        t.lexer.skip(1)
    

    #Calculo de columna:

    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1


    #Tomamos el arhivo como string
    
        #archivo = open(input(), "r")
        #datos = archivo.read()
        #archivo.close()

    # #Introducimos la informacion al lexer

        #lexer.input(datos)

    # #Hacemos una corrida en busca de errores

    # while True:
    #     tok = lexer.token()
    #     if not tok: 
    #         break

    # # #"Reseteamos" el lexer para imprimir los tokes si no se encontraron errores

    # lexer.input(datos)
    # lexer.lineno = 1
    # lexer.lexpos = 0

    # # #Imprimimos los tokens con su tipo, fila y columna

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