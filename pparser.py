import AST
from lexer import Lexer
from checktipo import TypeChecker


class Pparser(object):

    salida = ""

    def __init__(self):
        self.scanner = Lexer()
        self.scanner.build()

    tokens = Lexer.tokens
    
    #Precedencia de operadores:
    precedence = (
        ('nonassoc', 'TkIf'),
        ('nonassoc', 'TkOtherwise'),
        ('right', 'TkAsignacion'),
        ('left', 'TkDisyuncion'),
        ('left', 'TkConjuncion'),
        ('nonassoc', 'TkMenor', 'TkMayor', 'TkMenorIgual', 'TkMayorIgual', 'TkIgual', 'TkDesigual'),
        ('left', 'TkMas', 'TkMenos'),
        ('left', 'TkMult', 'TkDiv', 'TkMod'),
        ('right', 'TkNegacion'),
        ('left', 'UMENOS'),
        ('left', 'TkConcatHorizontal', 'TkConcatVertical'),
        ('right', 'TkRotacion'),
        ('left', 'TkTransposicion'),
        ('left', 'TkParAbre', 'TkParCierra')
    )

    error = 0

    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
    
    def p_error(self, p):
        if p:
            print('Error sintactico:  Token inesperado "%s" en la linea %d, columna %d ' 
                % (p.type, p.lineno, Pparser.find_column(p.lexer.lexdata, p)))
        else:
            print("EOF Inesperado")
        exit(1)

    def p_ENTRADA(self, p):
        'ENTRADA : DECLARACIONES'
        p[0] = AST.Entrada(p[1])

    def p_DECLARACIONES(self, p):
        '''DECLARACIONES : TkUsing SECUENCIA_DECLARACION TkBegin SECUENCIACION TkEnd'''
        if len(p) == 3:
            p[0] = AST.Declaraciones(p[2], p[4])
        

    def p_SECUENCIA_DECLARACION(self, p):
        '''SECUENCIA_DECLARACION : DECLARACION TkPuntoYComa SECUENCIA_DECLARACION 
                    | DECLARACION'''
        if len(p) == 4:
            p[0] = AST.Secuencia_Declaracion(p[1], p[3])
        else:
            p[0] = AST.Secuencia_Declaracion(p[1])

    def p_DECLARACION(self, p):
        'DECLARACION : VARIABLES TkOf TkType TIPO'
        p[0] = AST.Declaracion(p[1], p[4])
        

    def p_VARIABLES(self, p):
        '''VARIABLES : TkIdent TkComa VARIABLES
                    | TkIdent'''
        if len(p) == 4:
            p[0] = AST.Variables(p[1], p[3])
        else:
            p[0] = AST.Id(p[1])

    def p_TIPO(self, p):
        '''TIPO : TkInteger 
                | TkBoolean 
                | TkCanvas'''
        p[0] = AST.Tipo(p[1])

    def p_SECUENCIACION(self, p):
        '''SECUENCIACION : INSTRUCCION_IF SECUENCIACION
                        | INSTRUCCION_WITH SECUENCIACION
                        | INSTRUCCION_FROM SECUENCIACION
                        | INSTRUCCION_WHILE SECUENCIACION
                        | INSTRUCCION_ASIGNACION SECUENCIACION
                        | INSTRUCCION_IO SECUENCIACION
                        | DECLARACIONES2 SECUENCIACION'''
        p[0] = AST.Secuenciacion(p[1])

    def p_SECUENCIACION_1(self, p):
        '''SECUENCIACION : '''
        p[0] = AST.Empty()

    def p_DECLARACIONES2(self, p):
        '''DECLARACIONES2 : TkUsing SECUENCIA_DECLARACION TkBegin SECUENCIACION TkEnd'''
        if len(p) == 3:
            p[0] = AST.Declaraciones2(p[2], p[4])

    def p_INSTRUCCION_IF(self, p):
        '''INSTRUCCION_IF : TkIf EXPRESION TkThen SECUENCIACION TkOtherwise SECUENCIACION TkDone
                        | TkIf EXPRESION SECUENCIACION TkDone'''
        if len(p) == 7:
            if p(2):
                p[0] = AST.If(p[2], p[3])
            else:
                p[0] = AST.If(-p[2], p[5])
        elif len(p) == 5:
            if p[2]:
                p[0] = AST.If(p[2], p[3])

    def p_INSTRUCCION_WITH(self, p):
        '''INSTRUCCION_WITH : TkWith TkIdent TkFrom COTA_INF TkTo COTA_SUP TkRepeat SECUENCIACION TkDone TkPuntoYComa'''
        p[0] = AST.With(p[2], p[4], p[6], p[8])

    def p_INSTRUCCION_FROM(self, p):
        '''INSTRUCCION_FROM : TkFrom COTA_INF TkTo COTA_SUP TkRepeat SECUENCIACION TkDone TkPuntoYComa'''
        p[0] = AST.From(p[2], p[4], p[6])

    def p_INSTRUCCION_WHILE(self, p):
        '''INSTRUCCION_WHILE : TkWhile EXPRESION TkRepeat SECUENCIACION TkDone'''
        p[0] = AST.While(p[2], p[4])

    def p_INSTRUCCION_ASIGNACION(self, p):
        '''INSTRUCCION_ASIGNACION : TkIdent TkAsignacion EXPRESION TkPuntoYComa
                                | TkIdent TkAsignacion EXPRESION'''
        p[0] = AST.Asignacion(p[1], p[3])

    def p_INSTRUCCION_IO(self, p):
        '''INSTRUCCION_IO : TkRead TkIdent TkPuntoYComa
                        | TkPrint EXPRESION'''
        if len(p) == 4:
            p[0] = AST.Read(p[2])
        elif len(p) == 3:
            p[0] = AST.Print(p[2])

    def p_COTA_INF(self, p):
        '''COTA_INF : EXPRESION_TERMINAL'''
        p[0] = AST.CI(p[1])

    def p_COTA_SUP(self, p):
        '''COTA_SUP : EXPRESION_TERMINAL'''
        p[0] = AST.CS(p[1])

    def p_EXPRESION(self, p):
        '''EXPRESION : EXPRESION_BINARIA
                    | EXPRESION_UNARIA
                    | EXPRESION_TERMINAL'''
        p[0] = AST.Expresion(p[1])

    def p_EXPRESION_BINARIA(self, p):
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
        if p[2] == Lexer.t_TkMas:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkMenos:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkMult:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkDiv:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkMod:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkConjuncion:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkDisyuncion:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkMenor:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkMayor:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkMenorIgual:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkMayorIgual:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkIgual:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkDesigual:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkConcatHorizontal:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])
        elif p[2] == Lexer.t_TkConcatVertical:
            p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])

    def p_EXPRESION_UNARIA(self, p):
        '''EXPRESION_UNARIA : TkParAbre EXPRESION TkParCierra
                            | TkMenos EXPRESION %prec UMENOS
                            | EXPRESION TkNegacion
                            | TkRotacion EXPRESION
                            | EXPRESION TkTransposicion'''
        if len(p) == 4:    
            if p[1] == Lexer.t_TkParAbre:
                p[0] = AST.Parentesis(p[2])
            elif p[1] == Lexer.t_TkMenos:
                p[0] = AST.UMenos(p[2])
        elif len(p) == 3:
            if p[2] == Lexer.t_TkNegacion:
                p[0] = AST.Negacion(p[2], p[1])
            elif p[1] == Lexer.t_TkRotacion:
                p[0] = AST.Rotacion(p[1], p[2])
            elif p[2] == Lexer.t_TkTransposicion:
                p[0] = AST.Transposicion(p[1], p[2])
                

    def p_EXPRESION_TERMINAL(self, p):   
        '''EXPRESION_TERMINAL : TkIdent
                            | TkNumLit
                            | TkTrue
                            | TkFalse
                            | TkCanvasLit'''    
        if p[1] == Lexer.t_TkIdent:
            p[0] = AST.Id(p[1])
        elif p[1] == Lexer.t_TkNumLit:
            p[0] = AST.Integer(p[1])
        elif (p[1] == Lexer.t_TkTrue) | (p[1] == Lexer.t_TkFalse):
            p[0] = AST.Boolean(p[1])
        elif p[1] == Lexer.t_TkCanvasLit:
            p[0] = AST.Canvas(p[1])