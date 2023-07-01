class Node(object):
    def accept(self, visitor, table = None):
        return visitor.visit(self)
    def setParent(self, parent):
        self.parent = parent

#Entrada
class Entrada(Node):
    def __init__(self, declaraciones):
        self.declaraciones = declaraciones
        self.hijos = (declaraciones)

    
    #def print_object(self, profund):
    #    return f'{"-"*profund}Entrada\n{self.hijos.print_object(profund+1)}'    


#Declaraciones
class Declaraciones(Node):
    def __init__(self, secuencia_declaracion, secuenciacion):
        self.secuencia_declaracion = secuencia_declaracion
        self.secuenciacion = secuenciacion
        self.hijos = (secuencia_declaracion, secuenciacion)

    #def print_object(self, profund):
    #    return f'{"-"*profund}Declaraciones\n{self.hijos.print_object(profund+1)}'

class Declaraciones2(Node):
    def __init__(self, secuencia_declaracion, secuenciacion):
        self.secuencia_declaracion = secuencia_declaracion
        self.secuenciacion = secuenciacion
        self.hijos = (secuencia_declaracion, secuenciacion)

    #def print_object(self, profund):
    #    return f'{"-"*profund}Declaraciones\n{self.hijos.print_object(profund+1)}'
    

#Declaracion
class Declaracion(Node):
    def __init__(self, variables, tipo):
        self.variables = variables
        self.tipo = tipo
        self.hijos = (variables, tipo)
        
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.hijos}'

#Secuencia Declaración
class Secuencia_Declaracion(Node):
    def __init__(self, declaracion, secuencia_declaracion):
        self.declaracion = declaracion
        self.secuencia_declaracion = secuencia_declaracion
        self.hijos = (declaracion, secuencia_declaracion)
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.nodo} : {self.hijos}'


#Variables
class Variables(Node):
    def __init__(self, variable, variables):
        self.variable = variable
        self.variables = variables
        self.hijos = (variable, variables)
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.nodo} : {self.hijos}'    


#Tipo
class Tipo(Node):
    def __init__(self, tipo):
        self.tipo = tipo
        self.hijos = tipo 
   
#     def print_object(self, profund):
#         return f'{"-"*profund}{self.nodo}'  


#Id
class Id(Node):
    def __init__(self, id):
        self.id = id
        self.hijos = () 
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.nodo}' 




#PALABRAS RESERVADAS --------

#If
class If(Node):
    def __init__(self, guardia, secuenciacion):
        self.guardia = guardia 
        self.secuenciacion = secuenciacion 
        self.hijos = (guardia, secuenciacion)

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.nodo} : {self.hijos}'


#With
class With(Node):
    def __init__(self, id, cotainf, cotasup, secuenciacion):
        self.id = id
        self.cotainf = cotainf
        self.cotasup = cotasup
        self.secuenciacion = secuenciacion
        self.hijos = (id, cotainf, cotasup, secuenciacion)
        

    #def print_object(self, profund):
        #return f'{"-"*profund}{self.iterador} : {self.cota_inf} : {self.cota_sup} : {self.secuenciacion}'

class From(Node):
    def __init__(self, cotainf, cotasup, secuenciacion):
        self.cotainf = cotainf
        self.cotasup = cotasup
        self.secuenciacion = secuenciacion
        self.hijos = (cotainf, cotasup, secuenciacion)
id, 
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.cota_inf} : {self.cota_sup} : {self.secuenciacion}'    
    

class While(Node):
    def __init__(self, expresion, secuenciacion):
        self.expresion = expresion
        self.secuenciacion = secuenciacion
        self.hijos = (expresion, secuenciacion)

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.condicion} : {self.secuenciacion}'  


class Read(Node):
    def __init__(self, id):
        self.id = id
        self.hijos = id

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.id}'    

class Print(Node):
    def __init__(self, expresion):
        self.expresion = expresion
        self.hijos = expresion
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.exp}'    

#------        

#OPERADORES ARITMÉTICOS -------------

#Expresion Binaria
class Expresion_Binaria(Node):
    def __init__(self, izq, opr, der):
        self.izq = izq
        self.opr = opr
        self.der = der
        self.hijos = (izq, opr, der)

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mas\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Unary Menos
class UMenos(Node):
    def __init__(self, expresion):
        self.expresion = -expresion
        self.hijos = -expresion
    
    #def __str__(self):
    #    return f'{self.hijos}'
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}UMenos\n{self.exp.print_object(profund+1)}'

#Asginación 
class Asignacion(Node):
    def __init__(self, id, der):
        self.id = id
        self.der = der
        self.hijos = (der)
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}Asignacion\n{self.id.print_object(profund+1)}\n{self.exp.print_object(profund+1)}'


#Negación
class Negacion(Node):
    def __init__(self, opr, expresion):
        self.opr = opr
        self.expresion = expresion
        self.hijos = (opr, expresion)
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}Negacion\n{self.exp.print_object(profund+1)}'

#Rotación
class Rotacion(Node):
    def __init__(self,opr, expresion):
        self.opr = opr
        self.expresion = expresion
        self.hijos = (opr, expresion)

    #def print_object(self, profund):
    #    return f'{"-"*profund}Rotacion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'  

#Transposición
class Transposicion(Node):
    def __init__(self, expresion, opr):
        self.expresion = expresion
        self.opr = opr
        self.hijos = (expresion, opr)

    #def print_object(self, profund):
    #    return f'{"-"*profund}Transposicion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'          

#------------------


class Secuenciacion(Node):
    def __init__(self, instruccion, secuenciacion):
        self.instruccion = instruccion
        self.secuenciacion = secuenciacion
        self.hijos = (instruccion, secuenciacion)

class CI(Node):
    def __init__(self, terminal):
        self.terminal = terminal
        self.hijos = (terminal)

class CS(Node):
    def __init__(self, terminal):
        self.terminal = terminal
        self.hijos = (terminal)

class Expresion(Node):
    def __init__(self, tipo_expresion):
        self.tipo_expresion = tipo_expresion
        self.hijos = (tipo_expresion)

class Parentesis(Node):
    def __init__(self, expresion):
        self.expresion = expresion
        self.hijos = (expresion)

class Integer(Node):
    def __init__(self, valor):
        self.valor = valor
        self.hijos = ()

class Boolean(Node):
    def __init__(self, valor):
        self.valor = valor
        self.hijos = ()

class Canvas(Node):
    def __init__(self, valor):
        self.valor = valor
        self.hijos = ()

class Empty(Node):
    def __init__(self):
        self.nombre = ""
        self.hijos = ()