import AST
from lexer import Lexer
from checktipo import TypeChecker


class Pparser(object):

    salida = ""

    def __init__(self):
        self.lexer = Lexer()
        self.lexer.build()

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

    def p_entrada(self, p):
        """entrada : declaraciones"""

        p[0] = AST.Entrada(p[1])


    def p_declaraciones(self, p):
        """declaraciones : TkUsing secuencia_declaracion TkBegin secuenciacion TkEnd"""      
        p[0] = AST.Declaraciones(p[2], p[4])

    def p_secuencia_declaracion(self, p):
        """secuencia_declaracion : declaracion TkPuntoYComa secuencia_declaracion 
                    | variables TkOf TkType tipo"""        
        if len(p) == 4:
            p[0] = AST.Secuencia_Declaracion(p[1], p[3])
        else:
            p[0] = AST.Declaracion(p[1], p[4])

    def p_declaracion(self, p):
        """declaracion : variables TkOf TkType tipo"""
        p[0] = AST.Declaracion(p[1], p[4])


    def p_variables(self, p):
        """variables : TkIdent TkComa variables
                    | TkIdent"""
        if len(p) == 4:
            p[0] = AST.Variables(p[1], p[3])
        else:
            p[0] = AST.Id(p[1])

    def p_tipo(self, p):
        """tipo : TkInteger 
                | TkBoolean 
                | TkCanvas"""
        p[0] = AST.Tipo(p[1])

    def p_secuenciacion(self, p):
        """secuenciacion : instruccion_if secuenciacion
                        | instruccion_with secuenciacion
                        | instruccion_from secuenciacion
                        | instruccion_while secuenciacion
                        | instruccion_asignacion secuenciacion
                        | instruccion_io secuenciacion
                        | declaraciones_2 secuenciacion"""
        p[0] = AST.Secuenciacion(p[1], p[2])

    def p_secuenciacion_1(self, p):
        """secuenciacion : """
        p[0] = AST.Empty()

    def p_declaraciones_2(self, p):
        """declaraciones_2 : TkUsing secuencia_declaracion TkBegin secuenciacion TkEnd"""
        
        p[0] = AST.Declaraciones2(p[2], p[4])

    def p_instruccion_if(self, p):
        """instruccion_if : TkIf expresion TkThen secuenciacion TkOtherwise secuenciacion TkDone
                        | TkIf expresion secuenciacion TkDone"""

        if len(p) == 7:
            if p(2):
                p[0] = AST.If(p[2], p[3])
            else:
                p[0] = AST.If(-p[2], p[5])
        elif len(p) == 5:
            if p[2]:
                p[0] = AST.If(p[2], p[3])

    def p_instruccion_with(self, p):
        """instruccion_with : TkWith TkIdent TkFrom cota_inf TkTo cota_sup TkRepeat secuenciacion TkDone TkPuntoYComa"""

        p[0] = AST.With(p[2], p[4], p[6], p[8])

    def p_instruccion_from(self, p):
        """instruccion_from : TkFrom cota_inf TkTo cota_sup TkRepeat secuenciacion TkDone TkPuntoYComa"""

        p[0] = AST.From(p[2], p[4], p[6])


    def p_instruccion_while(self, p):
        """instruccion_while : TkWhile expresion TkRepeat secuenciacion TkDone"""

        p[0] = AST.While(p[2], p[4])

    def p_instruccion_asignacion(self, p):
        """instruccion_asignacion : TkIdent TkAsignacion expresion TkPuntoYComa
                                | TkIdent TkAsignacion expresion"""
        p[0] = AST.Asignacion(p[1], p[3])

    def p_instruccion_io(self, p):
        """instruccion_io : TkRead TkIdent TkPuntoYComa
                        | TkPrint expresion"""
        if len(p) == 4:
            p[0] = AST.Read(p[2])
        elif len(p) == 3:
            p[0] = AST.Print(p[2])

    def p_cota_inf(self, p):
        """cota_inf : expresion""" 
        p[0] = AST.CI(p[1])


    def p_cota_sup(self, p):
        """cota_sup : expresion"""
 
        p[0] = AST.CS(p[1])



    def p_expresion_binaria(self, p):
        """expresion  :       expresion TkMas expresion
                            | expresion TkMenos expresion
                            | expresion TkMult expresion
                            | expresion TkDiv expresion
                            | expresion TkMod expresion
                            | expresion TkConjuncion expresion
                            | expresion TkDisyuncion expresion
                            | expresion TkMenor expresion
                            | expresion TkMayor expresion
                            | expresion TkMenorIgual expresion
                            | expresion TkMayorIgual expresion
                            | expresion TkIgual expresion
                            | expresion TkDesigual expresion
                            | expresion TkConcatHorizontal expresion
                            | expresion TkConcatVertical expresion"""                           
       
        p[0] = AST.Expresion_Binaria(p[1], p[2], p[3])

    def p_expresion_unaria(self, p):
        """expresion      : TkParAbre expresion TkParCierra
                            | TkMenos expresion %prec UMENOS
                            | expresion TkNegacion
                            | TkRotacion expresion
                            | expresion TkTransposicion"""
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
                

    def p_expresion_constante(self, p):
        """expresion : constante"""
        p[0] = p[1]
    
    def p_expresion_ident(self, p):
        """expresion : TkIdent"""
        p[0] = AST.Id(p[1])

    def p_constante_entero(self, p):
        """constante : TkNumLit"""
        p[0] = AST.Integer(p[1])

    def p_constante_boolean(self, p):
        """constante : TkTrue
                     | TkFalse """
        p[0] = AST.Boolean(p[1])
        
    def p_constante_canvas(self, p):
        """constante : TkCanvasLit"""

        p[0] = AST.Canvas(p[1])

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