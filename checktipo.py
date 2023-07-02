#!/usr/bin/python

import AST
from Symboltable import *


class RevisarNodos(object):
    def visit(self, nodo, tabla=None):
        metodo = 'visitar_' + nodo.__class__.__name__
        visitor = getattr(self, metodo, self.visita_generica)
        return visitor(nodo, tabla)


    def visita_generica(self, nodo, tabla): 
        if isinstance(nodo, list):
            for elem in nodo:
                self.visit(elem)
        else:
            for hijo in nodo.hijos:
                if isinstance(hijo, list):
                    for item in hijo:
                        if isinstance(item, AST.Nodo):
                            self.visit(item)
                elif isinstance(hijo, AST.Nodo):
                    self.visit(hijo)


class TypeChecker(RevisarNodos):
    def __init__(self):
        #Creación de diccionario
        self.ttype = {}

        #Diccionarios para cada operador de Asgard
        self.ttype['+'] = {}
        self.ttype['-'] = {}
        self.ttype['*'] = {}
        self.ttype['/'] = {}
        self.ttype['%'] = {}
        self.ttype['^'] = {}
        self.ttype['/\\'] = {}
        self.ttype['\\/'] = {}
        self.ttype['\^'] = {}
        self.ttype['='] = {}
        self.ttype['\/='] = {}
        self.ttype['>'] = {}
        self.ttype['<'] = {}
        self.ttype['<='] = {}
        self.ttype['>='] = {}
        self.ttype[':'] = {}
        self.ttype['\''] = {}
        self.ttype['\|'] = {}
        self.ttype['$'] = {}

        #Diccionario para cada operador entero
        self.ttype['+']['integer'] = {}
        self.ttype['-']['integer'] = {}
        self.ttype['*']['integer'] = {}
        self.ttype['/']['integer'] = {}
        self.ttype['%']['integer'] = {}
        self.ttype['>']['integer'] = {}
        self.ttype['<']['integer'] = {}
        self.ttype['<=']['integer'] = {}
        self.ttype['>=']['integer'] = {}
        self.ttype['=']['integer'] = {}
        self.ttype['\/=']['integer'] = {}

        #Diccionario para cada operador booleano
        self.ttype['/\\']["boolean"] = {}
        self.ttype['\\/']['boolean'] = {}
        self.ttype['\^']['boolean'] = {}
        self.ttype['=']['boolean'] = {}
        self.ttype['\/=']['boolean'] = {}
        self.ttype['=']['boolean'] = {}

        #Diccionario para cada operador canvas
        self.ttype[':']['canvas'] = {}
        self.ttype['\'']['canvas'] = {}
        self.ttype['$']['canvas'] = {}
        self.ttype['\|']['canvas'] = {}
        self.ttype['=']['canvas'] = {}
        self.ttype['\/=']['canvas'] = {}

        #Asignar el valor integer cuando se tiene operación integer con integer
        self.ttype['+']['integer']['integer'] = 'integer'
        self.ttype['-']['integer']['integer'] = 'integer'
        self.ttype['*']['integer']['integer'] = 'integer'
        self.ttype['/']['integer']['integer'] = 'integer'
        self.ttype['%']['integer']['integer'] = 'integer'


        #Asignar el valor boolean cuando se tiene comparación integer con integer
        self.ttype['=']['integer']['integer'] = 'boolean'
        self.ttype['\/=']['integer']['integer'] = 'boolean'
        self.ttype['>']['integer']['integer'] = 'boolean'
        self.ttype['<']['integer']['integer'] = 'boolean'
        self.ttype['<=']['integer']['integer'] = 'boolean'
        self.ttype['>=']['integer']['integer'] = 'boolean'

        #Asignar el valor boolean cuando se tiene operación boolean con boolean
        self.ttype['/\\']['boolean']['boolean'] = 'boolean'
        self.ttype['\\/']['boolean']['boolean'] = 'boolean'
        self.ttype['\^']['boolean']['boolean'] = 'boolean'
        self.ttype['=']['boolean']['boolean'] = 'boolean'
        self.ttype['\/=']['boolean']['boolean'] = 'boolean'
        

        #Asignar el valor canvas cuando se tiene operación canvas con canvas
        self.ttype[':']['canvas']['canvas'] = 'canvas'
        self.ttype['\'']['canvas']['canvas'] = 'canvas'
        self.ttype['$']['canvas']['canvas'] = 'canvas'
        self.ttype['\|']['canvas']['canvas'] = 'canvas'
        self.ttype['\/=']['canvas']['canvas'] = 'boolean'


    #Función que revisa si existe un diccionario con la operación, el tipo de la expresión 1 y la 2
    def check_new_type(self, expr1, op, expr2):
        try:
            return self.ttype[op][expr1][expr2]
        except:
            return 'undefined'

    #Función para visitar la Entrada, aquí se crea una nueva tabla de símbolos
    def visitar_Entrada(self, nodo, tabla):
        symbolTable = TablaSimbolos(None, 'global')
        self.visit(nodo.declaraciones, symbolTable)
    
    #Función para visitar Declaraciones 
    def visitar_Declaraciones(self, nodo, tabla):        
        self.visit(nodo.secuencia_declaracion, tabla)
        self.visit(nodo.secuenciacion, tabla)
    
    #Función para visitar Secuencia_Declaracion
    def visitar_Secuencia_Declaracion(self, nodo, tabla):
        self.visit(nodo.secuencia_declaracion, tabla)
        self.visit(nodo.declaracion, tabla)

    #Función para visitar Declaracion 
    def visitar_Declaracion(self, nodo, tabla):
        variables = []
        tmp = nodo.variables
        if type(tmp) == AST.Id:
            variables.append(tmp.id)
        else:
            if len(variables) > 1:
                while (tmp.variables):
                    tmp = tmp.variables
                    variables.append(tmp.id)
        variables.reverse()
        for variable in variables:
            if (not tabla.put(SimboloVariable(variable, nodo.tipo))):
                print ('Line '+str(variable.line)+': variable '+ variable+' already declared')

    #Función para visitar Variables
    def visitar_Variables(self, nodo, tabla):
        if ( nodo.variables ):
            self.visit(nodo.variables, tabla)
        self.visit(nodo.variable, tabla)

    #Función para visitar Secuenciación
    def visitar_Secuenciacion(self, nodo, tabla):
        if ( nodo.secuenciacion ):
            self.visit(nodo.secuenciacion, tabla)
        self.visit(nodo.instruccion, tabla)

    #Función para visitar Print
    def visitar_Print(self, nodo, tabla):
         return self.visit(nodo.expresion, tabla)

    #Función para visitar Asignación
    def visitar_Asignacion(self, nodo, tabla):
        #print nodo.id
        leftType = None
        leftSymbol = tabla.get(nodo.id)
        if leftSymbol:
            leftType = leftSymbol.type
        rightType = self.visit(nodo.der, tabla)

        if leftType == None:
            print ('Linea '+str(nodo.der.line)+': Variable '+ nodo.id+' no está declarada')
        elif rightType == 'undefined':
            return
    
    #Visitar While
    def visitar_While(self, nodo, tabla):
        self.visit(nodo.expresion, tabla)
        self.visit(nodo.secuenciacion, TablaSimbolos(tabla, 'while'))
        pass

    #Visitar From
    def visitar_From(self, nodo, tabla):
        #self.visit(nodo.cotainf, tabla)
        #self.visit(nodo.cotasup, tabla)
        self.visit(nodo.secuenciacion, TablaSimbolos(tabla, 'from'))

    def visitar_With(self, nodo, tabla):
        #nuevoscope
        nextTable = None
        if isinstance(tabla.name, SimboloScope):
            nextTable = tabla
        else:
            nextTable = TablaSimbolos(tabla, 'withInstr')

        self.visit(nodo.id, nextTable)
        self.visit(nodo.cotainf, nextTable)  
        self.visit(nodo.cotasup, nextTable)  
        self.visit(nodo.secuenciacion, nextTable)  
        
    def visitar_Declaraciones2(self, nodo, tabla):
        #neuevoscope
        nextTable = None
        if isinstance(tabla.name, SimboloScope):
            nextTable = tabla
        else:
            nextTable = TablaSimbolos(tabla, 'blockInstr')

        self.visit(nodo.secuencia_declaracion, nextTable)
        self.visit(nodo.secuenciacion, nextTable)        

    def visitar_If(self, nodo, tabla):
        self.visit(nodo.guardia, tabla)
        self.visit(nodo.secuenciacion, TablaSimbolos(tabla, 'if'))

    #Estas funciones retornan el tipo 
    def visitar_Integer(self, nodo, tabla):
        return 'integer'
    
    def visitar_Canvas(self, nodo, tabla):
        return 'canvas'

    def visitar_Boolean(self, nodo, tabla):
        return 'boolean'
        
    #Función para tratar con el ID
    def visitar_Id(self, nodo, tabla):
        symbol = tabla.get(nodo.id)
        if isinstance(symbol, SimboloVariable):
            return symbol.type
        elif isinstance(symbol, SimboloScope):
            return 'undefined'
        else:
            print ('Line '+str(nodo.line)+': '+nodo.id+' no está declarado ')
            return 'undefined'

    def visitar_Expresion(self, nodo, tabla):
        self.visit(nodo.tipo_expresion,tabla)

    def visitar_CI(self, nodo, tabla):
        self.visit(nodo.terminal, tabla)

    def visitar_CS(self, nodo, tabla):
        self.visit(nodo.terminal, tabla)

    def visitar_Expresion_Binaria(self, nodo, tabla):
        type1 = self.visit(nodo.izq, tabla)
        type2 = self.visit(nodo.der, tabla)

        if type1 == 'undefined' or type2 == 'undefined':
            return 'undefined'

        operator = nodo.opr

        result_type = self.check_new_type(type1,operator,type2)
        if result_type == 'undefined':
            print("Los tipos de variable no coinciden")
            return 'undefined'

        return result_type

    def visitar_UMenos(self, nodo, tabla):
        self.visit(nodo.expresion, tabla)

    def visitar_Tipo(self, nodo, tabla):
        self.visit(nodo.tipo, tabla)

    def visitar_Parentesis(self, nodo, tabla):
        return self.visit(nodo.expresion, tabla)

    def Read(self, nodo, tabla):
        self.visit(nodo.id, tabla)
        #Procedimiento similar a asignación

    def visitar_Empty(self, nodo, tabla):
        pass


