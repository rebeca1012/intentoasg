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
        #self.ttype['|'] = {}
        #self.ttype['&'] = {}
        #self.ttype['AND'] = {}
        #self.ttype['OR'] = {}
        #self.ttype['SHL'] = {}
        #self.ttype['SHR'] = {}
        #self.ttype['=='] = {}
        #self.ttype['!='] = {}
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
        #self.ttype['^']['integer'] = {}
        
        #self.ttype['&']['integer'] = {}
        #self.ttype['AND']['integer'] = {}
        #self.ttype['OR']['integer'] = {}
        #self.ttype['SHL']['integer'] = {}
        #self.ttype['SHR']['integer'] = {}

        # self.ttype['==']['integer'] = {}
        # self.ttype['!=']['integer'] = {}
        # self.ttype['>']['integer'] = {}
        # self.ttype['<']['integer'] = {}
        # self.ttype['<=']['integer'] = {}
        # self.ttype['>=']['integer'] = {}



        self.ttype['/\\']["boolean"] = {}
        self.ttype['\\/']['boolean'] = {}
        self.ttype['\^']['boolean'] = {}
        self.ttype['=']['boolean'] = {}
        self.ttype['\/=']['boolean'] = {}
        self.ttype['>']['boolean'] = {}
        self.ttype['<']['boolean'] = {}
        self.ttype['<=']['boolean'] = {}
        self.ttype['>=']['boolean'] = {}
        self.ttype['=']['boolean'] = {}
        self.ttype['\/=']['boolean'] = {}

        self.ttype[':']['canvas'] = {}
        self.ttype['\'']['canvas'] = {}
        self.ttype['$']['canvas'] = {}
        self.ttype['\|']['canvas'] = {}

        # self.ttype['+']['float'] = {}
        # self.ttype['-']['float'] = {}
        # self.ttype['*']['float'] = {}
        # self.ttype['/']['float'] = {}
        # self.ttype['%']['float'] = {}
        # self.ttype['==']['float'] = {}
        # self.ttype['!=']['float'] = {}
        # self.ttype['>']['float'] = {}
        # self.ttype['<']['float'] = {}
        # self.ttype['<=']['float'] = {}
        # self.ttype['>=']['float'] = {}

        # self.ttype['+']['string'] = {}
        # self.ttype['*']['string'] = {}
        # self.ttype['==']['string'] = {}
        # self.ttype['!=']['string'] = {}
        # self.ttype['>']['string'] = {}
        # self.ttype['<']['string'] = {}
        # self.ttype['<=']['string'] = {}
        # self.ttype['>=']['string'] = {}

        #aritmética integer con integer
        self.ttype['+']['integer']['integer'] = 'integer'
        self.ttype['-']['integer']['integer'] = 'integer'
        self.ttype['*']['integer']['integer'] = 'integer'
        self.ttype['/']['integer']['integer'] = 'integer'
        self.ttype['%']['integer']['integer'] = 'integer'
        #self.ttype['^']['integer']['integer'] = 'integer'
        #self.ttype['|']['integer']['integer'] = 'integer'
        #self.ttype['&']['integer']['integer'] = 'integer'
        #self.ttype['AND']['integer']['integer'] = 'integer'
        #self.ttype['OR']['integer']['integer'] = 'integer'
        #self.ttype['SHL']['integer']['integer'] = 'integer'
        #self.ttype['SHR']['integer']['integer'] = 'integer'
        #si comparas un numero con un numero da un boolean
        # self.ttype['==']['integer']['integer'] = 'integer'
        # self.ttype['!=']['integer']['integer'] = 'integer'
        # self.ttype['>']['integer']['integer'] = 'integer'
        # self.ttype['<']['integer']['integer'] = 'integer'
        # self.ttype['<=']['integer']['integer'] = 'integer'
        # self.ttype['>=']['integer']['integer'] = 'integer'

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
        self.ttype['!=']['boolean']['boolean'] = 'boolean'
        self.ttype['\/=']['boolean']['boolean'] = 'boolean'
        

        #canvas con canvas

        self.ttype[':']['canvas']['canvas'] = 'canvas'
        self.ttype['\'']['canvas']['canvas'] = 'canvas'
        self.ttype['$']['canvas']['canvas'] = 'canvas'
        self.ttype['\|']['canvas']['canvas'] = 'canvas'

        # self.ttype['+']['int']['float'] = 'float'
        # self.ttype['-']['int']['float'] = 'float'
        # self.ttype['*']['int']['float'] = 'float'
        # self.ttype['/']['int']['float'] = 'float'
        # self.ttype['==']['int']['float'] = 'int'
        # self.ttype['!=']['int']['float'] = 'int'
        # self.ttype['>']['int']['float'] = 'int'
        # self.ttype['<']['int']['float'] = 'int'
        # self.ttype['<=']['int']['float'] = 'int'
        # self.ttype['>=']['int']['float'] = 'int'

        # self.ttype['+']['float']['float'] = 'float'
        # self.ttype['-']['float']['float'] = 'float'
        # self.ttype['*']['float']['float'] = 'float'
        # self.ttype['/']['float']['float'] = 'float'
        # self.ttype['==']['float']['float'] = 'int'
        # self.ttype['!=']['float']['float'] = 'int'
        # self.ttype['>']['float']['float'] = 'int'
        # self.ttype['<']['float']['float'] = 'int'
        # self.ttype['<=']['float']['float'] = 'int'
        # self.ttype['>=']['float']['float'] = 'int'

        # self.ttype['+']['float']['int'] = 'float'
        # self.ttype['-']['float']['int'] = 'float'
        # self.ttype['*']['float']['int'] = 'float'
        # self.ttype['/']['float']['int'] = 'float'
        # self.ttype['==']['float']['int'] = 'int'
        # self.ttype['!=']['float']['int'] = 'int'
        # self.ttype['>']['float']['int'] = 'int'
        # self.ttype['<']['float']['int'] = 'int'
        # self.ttype['<=']['float']['int'] = 'int'
        # self.ttype['>=']['float']['int'] = 'int'

        # self.ttype['+']['string']['string'] = 'string'
        # self.ttype['*']['string']['int'] = 'string'
        # self.ttype['==']['string']['string'] = 'int'
        # self.ttype['!=']['string']['string'] = 'int'
        # self.ttype['>']['string']['string'] = 'int'
        # self.ttype['<']['string']['string'] = 'int'
        # self.ttype['<=']['string']['string'] = 'int'
        # self.ttype['>=']['string']['string'] = 'int'

    def check_new_type(self, expr1, op, expr2):
        try:
            return self.ttype[op][expr1][expr2]
        except:
            return 'undefined'
        #return self.ttype[op][expr1][expr2]

    #Esto sería entrada
    def visit_Program(self, node, table):
        symbolTable = SymbolTable(None, 'global')
        self.visit(node.declarations, symbolTable)
        self.visit(node.fundefs, symbolTable)
        self.visit(node.instructions, symbolTable)
    
    def visit_Declarations(self, node, table):
        self.visit(node.declarations, table)
        self.visit(node.declaration, table)

    def visit_Declaration(self, node, table):
        inits = []
        tmp = node.inits
        inits.append(tmp.init)
        while (tmp.inits):
            tmp = tmp.inits
            inits.append(tmp.init)
        inits.reverse()
        for init in inits:
            if (not table.put(VariableSymbol(init.id, node.type))):
                print ('Line '+str(init.line)+': variable '+ init.id+' alreday declared')

    def visit_Inits(self, node, table):
        if ( node.inits ):
            self.visit(node.inits, table)
        self.visit(node.init, table)

    def visit_Init(self, node, table):
        #print node.ID
        return self.visit(node.expression, table)

    def visit_Instructions(self, node, table):
        if ( node.instructions ):
            self.visit(node.instructions, table)
        self.visit(node.instruction, table)

    def visit_Instruction(self, node, table):
        return self.visit(node.instruction, table)

    def visit_Print(self, node, table):
        return self.visit(node.expression, table)

    def visit_Labeled(self, node, table):
        #print node.id
        return self.visit(node.instruction, table)

    def visit_Assignment(self, node, table):
        #print node.id
        leftType = None
        leftSymbol = table.get(node.id)
        if leftSymbol:
            leftType = leftSymbol.type
        rightType = self.visit(node.expression, table)

        if leftType == None:
            print ('Line '+str(node.expression.line)+': Variable '+ node.id+' is not declared')
        elif rightType == 'undefined':
            return
        elif not (leftType == rightType or (leftType == 'float' and rightType == 'integer')):
            print ('Line '+str(node.expression.line)+': Incorrect assignment - '+rightType+' to '+leftType)

    def visit_Choice(self, node, table):
        self.visit(node.condition, table)
        self.visit(node.instruction1, SymbolTable(table, 'choice_instr1'))
        if (node.instruction2):
            self.visit(node.instruction2, SymbolTable(table, 'choice_instr2'))


    # def visit_While(self, node, table):
    #     self.visit(node.condition, table)
    #     self.visit(node.instruction, SymbolTable(table, 'while'))
    #     pass

    # def visit_Repeat(self, node, table):
    #     self.visit(node.condition, table)
    #     self.visit(node.instruction, SymbolTable(table, 'repeat'))
    
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

    def visit_CompoundInstruction(self, node, table):
        #newSCOPe
        nextTable = None
        if isinstance(table.name, FunctionSymbol):
            nextTable = table
        else:
            nextTable = SymbolTable(table, 'blockInstr')

        self.visit(node.declarations, nextTable)
        self.visit(node.instructions, nextTable)

    def visit_Condition(self, node, table):
        return self.visit(node.expression, table)

    def visit_Integer(self, node, table):
        return 'integer'
    
    #Agregado
    def visit_Canvas(self, node, table):
        return 'canvas'

    def visit_Boolean(self, node, table):
        return 'boolean'
        
    #def visit_Float(self, node, table):
    #    return 'float'

    #def visit_String(self, node, table):
    #    return 'string'

    def visit_Variable(self, node, table):
        symbol = table.get(node.name)
        if isinstance(symbol, VariableSymbol):
            return symbol.type
        elif isinstance(symbol, FunctionSymbol):
            print ('Line '+str(node.line)+': '+node.name+' is a function expected a variable ')
            return 'undefined'
        else:
            print ('Line '+str(node.line)+': '+node.name+' is not declared ')
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


