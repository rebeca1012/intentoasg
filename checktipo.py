#!/usr/bin/python

import AST
from Symboltable import *


class NodeVisitor(object):
    def visit(self, node, table=None):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node, table)


    def generic_visit(self, node, table):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)


class TypeChecker(NodeVisitor):
    def __init__(self):
        self.ttype = {}
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



        self.ttype['/\\']["boolean"] = {}
        self.ttype['\\/']['boolean'] = {}
        self.ttype['\^']['boolean'] = {}
        self.ttype['=']['boolean'] = {}
        self.ttype['\/=']['boolean'] = {}
        self.ttype['=']['boolean'] = {}


        self.ttype[':']['canvas'] = {}
        self.ttype['\'']['canvas'] = {}
        self.ttype['$']['canvas'] = {}
        self.ttype['\|']['canvas'] = {}
        self.ttype['=']['canvas'] = {}
        self.ttype['\/=']['canvas'] = {}

        #aritmética integer con integer
        self.ttype['+']['integer']['integer'] = 'integer'
        self.ttype['-']['integer']['integer'] = 'integer'
        self.ttype['*']['integer']['integer'] = 'integer'
        self.ttype['/']['integer']['integer'] = 'integer'
        self.ttype['%']['integer']['integer'] = 'integer'


        #comparar integer con integer
        self.ttype['=']['integer']['integer'] = 'boolean'
        self.ttype['\/=']['integer']['integer'] = 'boolean'
        self.ttype['>']['integer']['integer'] = 'boolean'
        self.ttype['<']['integer']['integer'] = 'boolean'
        self.ttype['<=']['integer']['integer'] = 'boolean'
        self.ttype['>=']['integer']['integer'] = 'boolean'

        #boolean con boolean
        self.ttype['/\\']['boolean']['boolean'] = 'boolean'
        self.ttype['\\/']['boolean']['boolean'] = 'boolean'
        self.ttype['\^']['boolean']['boolean'] = 'boolean'
        self.ttype['=']['boolean']['boolean'] = 'boolean'
        self.ttype['\/=']['boolean']['boolean'] = 'boolean'
        

        #canvas con canvas

        self.ttype[':']['canvas']['canvas'] = 'canvas'
        self.ttype['\'']['canvas']['canvas'] = 'canvas'
        self.ttype['$']['canvas']['canvas'] = 'canvas'
        self.ttype['\|']['canvas']['canvas'] = 'canvas'
        self.ttype['!=']['canvas']['canvas'] = 'boolean'
        self.ttype['\/=']['canvas']['canvas'] = 'boolean'


    def check_new_type(self, expr1, op, expr2):
        try:
            return self.ttype[op][expr1][expr2]
        except:
            return 'undefined'
        #return self.ttype[op][expr1][expr2]

    
    def visit_Entrada(self, node, table):
        symbolTable = SymbolTable(None, 'global')
        self.visit(node.declaraciones, symbolTable)
    
    #Esto era Programa
    def visit_Declaraciones(self, node, table):        
        self.visit(node.secuencia_declaracion, table)
        self.visit(node.secuenciacion, table)
    
    def visit_Secuencia_Declaracion(self, node, table):
        self.visit(node.secuencia_declaracion, table)
        self.visit(node.declaracion, table)

    def visit_Declaracion(self, node, table):
        variables = []
        tmp = node.variables
        variables.append(tmp.variable)
        while (tmp.variables):
            tmp = tmp.variables
            variables.append(tmp.variable)
        variables.reverse()
        for variable in variables:
            if (not table.put(VariableSymbol(variable.id, node.type))):
                print ('Line '+str(variable.line)+': variable '+ variable.id+' already declared')

    #esto era inits de el
    def visit_Variables(self, node, table):
        if ( node.variables ):
            self.visit(node.variables, table)
        self.visit(node.variable, table)

    # def visit_Init(self, node, table):
    #     #print node.ID
    #     return self.visit(node.expression, table)

    def visit_Secuenciacion(self, node, table):
        if ( node.secuenciacion ):
            self.visit(node.secuenciacion, table)
        self.visit(node.instruccion, table)

    # def visit_Instruction(self, node, table):
    #     return self.visit(node.instruction, table)

    def visit_Print(self, node, table):
        return self.visit(node.expresion, table)

    def visit_Asignacion(self, node, table):
        #print node.id
        leftType = None
        leftSymbol = table.get(node.id)
        if leftSymbol:
            leftType = leftSymbol.type
        rightType = self.visit(node.der, table)

        if leftType == None:
            print ('Line '+str(node.der.line)+': Variable '+ node.id+' is not declared')
        elif rightType == 'undefined':
            return
    
    #Visitar While
    def visit_While(self, node, table):
        self.visit(node.expresion, table)
        self.visit(node.secuenciacion, SymbolTable(table, 'while'))
        pass

    #Visitar From
    def visit_From(self, node, table):
        self.visit(node.expresion, table)
        self.visit(node.secuenciacion, SymbolTable(table, 'from'))


    def visit_Keyword(self, node, table):
        #print node.keyword
        pass

    # def visit_CompoundInstruction(self, node, table):
    #     #newSCOPe
    #     nextTable = None
    #     if isinstance(table.name, FunctionSymbol):
    #         nextTable = table
    #     else:
    #         nextTable = SymbolTable(table, 'blockInstr')

    #     self.visit(node.declarations, nextTable)
    #     self.visit(node.instructions, nextTable)

    #crear en symboltable una clase casi idéntica a FunctionSymbol para las declaraciones.
    #debe tener como atributos lo que sea que llevan las declaraciones. así como una función
    #tiene un nombre, argumentos y un tipo, una declaración debe tener sus propios atributos. (?
    #entiendo que esta función declara un nuevo scope
    def visit_Declaraciones2(self, node, table):
        #newSCOPe
        nextTable = None
        if isinstance(table.name, FunctionSymbol):
            nextTable = table
        else:
            nextTable = SymbolTable(table, 'blockInstr')

        self.visit(node.secuencia_declaracion, nextTable)
        self.visit(node.secuenciacion, nextTable)        

    def visit_If(self, node, table):
        self.visit(node.guardia, table)
        self.visit(node.secuenciacion, SymbolTable(table, 'if'))

    # def visit_Condition(self, node, table):
    #     return self.visit(node.expression, table)

    def visit_Integer(self, node, table):
        return 'integer'
    
    def visit_Canvas(self, node, table):
        return 'canvas'

    def visit_Boolean(self, node, table):
        return 'boolean'
        
    #esto era la Variable de el
    def visit_Id(self, node, table):
        symbol = table.get(node.id)
        if isinstance(symbol, VariableSymbol):
            return symbol.type
        elif isinstance(symbol, FunctionSymbol):
            print ('Line '+str(node.line)+': '+node.id+' is a function expected a variable ')
            return 'undefined'
        else:
            print ('Line '+str(node.line)+': '+node.id+' is not declared ')
            return 'undefined'

    def visit_Expresion_Binaria(self, node, table):
        #print node.operator
        type1 = self.visit(node.izq, table)
        type2 = self.visit(node.der, table)

        if type1 == 'undefined' or type2 == 'undefined':
            return 'undefined'

        operator = node.opr

        result_type = self.check_new_type(type1,operator,type2)
        if result_type == 'undefined':
            print ('Line '+str(node.line)+': Operator '+node.opr+' is not allowed here')
            return 'undefined'

        return result_type

    def visit_Parentesis(self, node, table):
        return self.visit(node.expresion, table)

    def visit_Empty(self, node, table):
        pass


