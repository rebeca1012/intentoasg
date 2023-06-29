import re
import sys
import ply.lex as lex
import ply.yacc as yacc
from lexer import *
from clases import Nodo

start = 'ENTRADA'

#Precedencia de operadores:
precedence = (
    ('right', 'TkAsignacion'),
    ('left', 'TkDisyuncion'),
    ('left', 'TkConjuncion'),
    ('left', 'TkIgual', 'TkDesigual'),
    ('nonassoc', 'TkMenor', 'TkMayor', 'TkMenorIgual', 'TkMayorIgual'),
    ('left', 'TkMas', 'TkMenos'),
    ('left', 'TkMult', 'TkDiv', 'TkMod'),
    ('right', 'TkNegacion'),
    ('left', 'UMENOS'),
    ('left', 'TkConcatHorizontal', 'TkConcatVertical'),
    ('right', 'TkRotacion'),
    ('left', 'TkTransposicion'),
    ('left', 'TkParAbre', 'TkParCierra')
)

#Gramatica:
#ENTRADA -> SECUENCIACION
#SECUENCIACION -> SENTENCIA_CONTROL 
#                     | ASIGNACION
#                     | EXPRESION_IO
#SENTENCIA_CONTROL -> SENTENCIA_IF 
#                     | SENTENCIA_FOR 
#                     | SENTENCIA_WHILE
#SENTENCIA_IF -> SENTENCIA_CONTROL 
#                     | ASIGNACION
#SENTENCIA_FOR -> SENTENCIA_CONTROL 
#                     | ASIGNACION
#SENTENCIA_WHILE -> SENTENCIA_CONTROL 
#                     | ASIGNACION
#ASIGNACION -> TkIdent TkIgual EXPRESION
#EXPRESION -> EXPRESION_NUM 
#                     | EXPRESION_BOOL
#                     | EXPRESION_CANVAS
#EXPRESION_NUM -> EXPRESION_NUM + EXPRESION_NUM
#                     | EXPRESION_NUM - EXPRESION_NUM
#                     | EXPRESION_NUM * EXPRESION_NUM
#                     | EXPRESION_NUM / EXPRESION_NUM
#                     | EXPRESION_NUM / EXPRESION_NUM
#                     | -EXPRESION_NUM
#                     | (EXPRESION_NUM)
#                     | TkIdent
#                     | TkNumLit
#EXPRESION_BOOL -> EXPRESION_BOOL /\ EXPRESION_BOOL
#                     | EXPRESION_BOOL \/ EXPRESION_BOOL
#                     | ^EXPRESION_BOOL
#                     | (EXPRESION_BOOL)
#                     | TkIdent
#                     | TkTrue
#                     | TkFalse
#EXPRESION_CANVAS -> EXPRESION_CANVAS : EXPRESION_CANVAS
#                     | <EXPRESION_CANVAS | EXPRESION_CANVAS>
#                     | $EXPRESION_CANVAS 
#                     | EXPRESION_CANVAS'
#                     | (EXPRESION_CANVAS)
#                     | TkCanvasLit


salida = ""

def p_empty(p):
    'empty :'
    pass


profundidad = 0

def p_ENTRADA(p):
    'ENTRADA : DECLARACIONES'
    p[0] = p[1]

def p_DECLARACIONES(p):
    '''DECLARACIONES : TkUsing SECUENCIA_DECLARACION TkBegin SECUENCIACION TkEnd'''
    if len(p) == 3:
        p[0] = Nodo('DECLARACIONES', [p[2], p[4]])
    

def p_SECUENCIA_DECLARACION(p):
    '''SECUENCIA_DECLARACION : DECLARACION TkPuntoYComa SECUENCIA_DECLARACION 
                   | DECLARACION'''
    if len(p) == 4:
        p[0] = Nodo('SECUENCIA_DECLARACION', [p[1], p[3]])
    else:
        p[0] = p[1]

def p_DECLARACION(p):
    'DECLARACION : VARIABLES TkOf TkType TIPO'
    p[0] = Nodo('DECLARACION', [p[1], p[4]])
    

def p_VARIABLES(p):
    '''VARIABLES : TkIdent TkComa VARIABLES
                 | TkIdent'''
    if len(p) == 4:
        p[0] = Nodo('VARIABLES', [p[1], p[3]])
    else:
        p[0] = Nodo('Variables', [p[1]])

def p_TIPO(p):
    '''TIPO : TkInteger 
            | TkBoolean 
            | TkCanvas'''
    p[0] = Nodo('TIPO', [p[1]])

def p_SECUENCIACION(p):
    '''SECUENCIACION : INSTRUCCION_IF
                     | INSTRUCCION_WITH
                     | INSTRUCCION_FROM
                     | INSTRUCCION_WHILE
                     | INSTRUCCION_ASIGNACION
                     | INSTRUCCION_IO
                     | empty'''
    p[0] = p[1]

def p_SECUENCIACION2(p):
    '''SECUENCIACION2 : INSTRUCCION_IF
                      | INSTRUCCION_WITH
                      | INSTRUCCION_FROM
                      | INSTRUCCION_WHILE
                      | INSTRUCCION_ASIGNACION
                      | INSTRUCCION_IO
                      | DECLARACIONES
                      | empty'''
    p[0] = p[1]

def p_INSTRUCCION_IF(p):
    '''INSTRUCCION_IF : TkIf EXPRESION TkThen SECUENCIACION2 TkOtherwise SECUENCIACION2 TkDone
                      | TkIf EXPRESION SECUENCIACION2 TkDone'''
    if len(p) == 7:
        if p(2):
            p[0] = Nodo('IF', [p[2], p[3]])
        else:
            p[0] = Nodo('IF', [-p[2], p[5]])
    elif len(p) == 5:
        if p[2]:
            p[0] = Nodo('IF', [p[2], p[3]])

def p_INSTRUCCION_WITH(p):
    '''INSTRUCCION_WITH : TkWith TkIdent TkFrom COTA_INF TkTo COTA_SUP TkRepeat SECUENCIACION2 TkDone TkPuntoYComa SECUENCIACION'''
    p[0] = Nodo('WITH', [p[2], p[4], p[6], p[8]])

def p_INSTRUCCION_FROM(p):
    '''INSTRUCCION_FROM : TkFrom COTA_INF TkTo COTA_SUP TkRepeat SECUENCIACION2 TkDone TkPuntoYComa SECUENCIACION'''
    p[0] = Nodo('FROM', [p[2], p[4], p[6]])

def p_INSTRUCCION_WHILE(p):
    '''INSTRUCCION_WHILE : TkWhile EXPRESION TkRepeat SECUENCIACION2 TkDone'''
    p[0] = Nodo('WHILE', [p[2], p[4]])

def p_INSTRUCCION_ASIGNACION(p):
    '''INSTRUCCION_ASIGNACION : TkIdent TkAsignacion EXPRESION TkPuntoYComa SECUENCIACION
                              | TkIdent TkAsignacion EXPRESION SECUENCIACION'''
    p[0] = Nodo('ASIGNACION', [p[1], p[3]])

def p_INSTRUCCION_IO(p):
    '''INSTRUCCION_IO : TkRead TkIdent TkPuntoYComa
                      | TkPrint EXPRESION'''
    if len(p) == 4:
        p[0] = Nodo('READ', [p[2]])
    elif len(p) == 3:
        p[0] = Nodo('PRINT', [p[2]])

def p_COTA_INF(p):
    '''COTA_INF : EXPRESION_TERMINAL'''
    p[0] = Nodo('COTA_INF', [p[1]])

def p_COTA_SUP(p):
    '''COTA_SUP : EXPRESION_TERMINAL'''
    p[0] = Nodo('COTA_SUP', [p[1]])

def p_EXPRESION(p):
    '''EXPRESION : EXPRESION_BINARIA
                 | EXPRESION_UNARIA
                 | EXPRESION_TERMINAL'''
    p[0] = p[1]

def p_EXPRESION_BINARIA(p):
    '''EXPRESION_BINARIA : EXPRESION TkMas EXPRESION
                         | EXPRESION TkMenos EXPRESION
                         | EXPRESION TkMult EXPRESION
                         | EXPRESION TkDiv EXPRESION
                         | EXPRESION TkMod EXPRESION
                         | EXPRESION TkConjuncion EXPRESION
                         | EXPRESION TkDisyuncion EXPRESION
                         | EXPRESION TkMenor EXPRESION
                         | EXPRESION TkMayor EXPRESION
                         | EXPRESION TkMenorIgual EXPRESION
                         | EXPRESION TkMayorIgual EXPRESION
                         | EXPRESION TkIgual EXPRESION
                         | EXPRESION TkDesigual EXPRESION
                         | EXPRESION TkConcatHorizontal EXPRESION
                         | EXPRESION TkConcatVertical EXPRESION'''
    if p[2] == t_TkMas:
        p[0] = Nodo('MAS', [p[1], p[3]])
    elif p[2] == t_TkMenos:
        p[0] = Nodo('MENOS', [p[1], p[3]])
    elif p[2] == t_TkMult:
        p[0] = Nodo('MULT', [p[1], p[3]])
    elif p[2] == t_TkDiv:
        p[0] = Nodo('DIV', [p[1], p[3]])
    elif p[2] == t_TkMod:
        p[0] = Nodo('MOD', [p[1], p[3]])
    elif p[2] == t_TkConjuncion:
        p[0] = Nodo('CONJUNCION', [p[1], p[3]])
    elif p[2] == t_TkDisyuncion:
        p[0] = Nodo('DISYUNCION', [p[1], p[3]])
    elif p[2] == t_TkMenor:
        p[0] = Nodo('COMPARADOR_BOOLEANO', [p[1], p[3]])
    elif p[2] == t_TkMayor:
        p[0] = Nodo('COMPARADOR_BOOLEANO', [p[1], p[3]])
    elif p[2] == t_TkMenorIgual:
        p[0] = Nodo('COMPARADOR_BOOLEANO', [p[1], p[3]])
    elif p[2] == t_TkMayorIgual:
        p[0] = Nodo('COMPARADOR_BOOLEANO',[p[1], p[3]])
    elif p[2] == t_TkIgual:
        p[0] = Nodo('COMPARADOR_BOOLEANO', [p[1], p[3]])
    elif p[2] == t_TkDesigual:
        p[0] = Nodo('COMPARADOR_BOOLEANO', [p[1], p[3]])
    elif p[2] == t_TkConcatHorizontal:
        p[0] = Nodo('CONCAT_HORIZONTAL', [p[1], p[3]])
    elif p[2] == t_TkConcatVertical:
        p[0] = Nodo('CONCAT_VERTICAL', [p[1], p[3]])

def p_EXPRESION_UNARIA(p):
    '''EXPRESION_UNARIA : TkParAbre EXPRESION TkParCierra
                        | TkMenos EXPRESION %prec UMENOS
                        | EXPRESION TkNegacion
                        | TkRotacion EXPRESION
                        | EXPRESION TkTransposicion'''
    if len(p) == 4:    
        if p[1] == t_TkParAbre:
            p[0] = Nodo('PARENTESIS', [p[2]])
        elif p[1] == t_TkMenos:
            p[0] = Nodo('UMENOS', [p[2]])
    elif len(p) == 3:
        if p[2] == t_TkNegacion:
            p[0] = Nodo('NEGACION', [p[1]])
        elif p[1] == t_TkRotacion:
            p[0] = Nodo('ROTACION', [p[2]])
        elif p[2] == t_TkTransposicion:
            p[0] = Nodo('TRANSPOSICION', [p[1]])
            

def p_EXPRESION_TERMINAL(p):   
    '''EXPRESION_TERMINAL : TkIdent
                          | TkNumLit
                          | TkTrue
                          | TkFalse
                          | TkCanvasLit'''    
    if p[1] == t_TkIdent:
        p[0] = Nodo('ID', [p[1]])
    elif (p[1] == t_TkNumLit) | (p[1] == t_TkTrue) | (p[1] == t_TkFalse) | (p[1] == t_TkCanvasLit):
        p[0] = Nodo('TERMINAL', [p[1]])

def p_error(p):
    if p:
        print('Error sintactico:  Token inesperado "%s" en la linea %d, columna %d ' 
            % (p.type, p.lineno, find_column(p.lexer.lexdata, p)))
    else:
        print("EOF Inesperado")
    exit(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def main():
    lexer = lex.lex()
    parser = yacc.yacc()
    ast = parser.parse(datos, lexer)
    print(ast.__repr__)

main()