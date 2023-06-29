class Nodo:
    def __init__(self, tipo, partes):
        self.tipo = tipo
        self.partes = partes

    def partes2str(self, separador='\n'):
        st = []

        for parte in self.partes:
            st.append(str(parte))

        return separador.join(st)

    def __repr__(self):
        return self.tipo + ":\n\t" + self.partes2str().replace("\n", "\n\t")

<<<<<<< HEAD
    
    def print_object(self, profund):
        return f'{"-"*profund}Entrada\n{self.hijos.print_object(profund+1)}'    


#Declaraciones
class Declaraciones(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    def print_object(self, profund):
        return f'{"-"*profund}Declaraciones\n{self.hijos.print_object(profund+1)}'
    

#Declaracion
class Declaracion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
        
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.hijos}'

#Secuencia Declaración
class Secuencia_Declaracion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo} : {self.hijos}'


#Variables
class Variables(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo} : {self.hijos}'    


#Tipo
class Tipo(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos 
    
#     def print_object(self, profund):
#         return f'{"-"*profund}{self.nodo}'  


#Id
class Id(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos 
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo}' 




#PALABRAS RESERVADAS --------

#If
class If(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo 
        self.hijos = hijos 

    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo} : {self.hijos}'


#With
class With(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
        #return f'{"-"*profund}{self.iterador} : {self.cota_inf} : {self.cota_sup} : {self.secuenciacion}'

class From(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.cota_inf} : {self.cota_sup} : {self.secuenciacion}'    
    

class While(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.condicion} : {self.secuenciacion}'  


class Read(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.id}'    

class Print(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.exp}'    



#------        

#OPERADORES ARITMÉTICOS -------------

#Mas
class Mas(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mas\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'


#Menos
class Menos(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Menos\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Unary Menos
class UMenos(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = -hijos
    
    def __str__(self):
        return f'{self.hijos}'
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}UMenos\n{self.exp.print_object(profund+1)}'


#Multiplicación
class Mult(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mult\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'


#División
class Div(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Div\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Modulo
class Mod(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mod\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Conjuncion
class Conjuncion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Conjuncion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Disyunción
class Disyuncion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Disyuncion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Igual
class Igual(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Igual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'
    
#Desigual
class Desigual(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Desigual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Menor
class Menor(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Menor\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#MenorIgual
class MenorIgual(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}MenorIgual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Mayor   
class Mayor(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mayor\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#MayorIgual
class MayorIgual(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}MayorIgual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Asginación 
class Asignacion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}Asignacion\n{self.id.print_object(profund+1)}\n{self.exp.print_object(profund+1)}'


#Negación
class Negacion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}Negacion\n{self.exp.print_object(profund+1)}'


#Concatenación Horizontal
class ConcatHorizontal(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}ConcatHorizontal\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'


#Concatenación Vertical
class ConcatVertical(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}ConcatVertical\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'  


#Rotación
class Rotacion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Rotacion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'  

#Transposición
class Transposicion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Transposicion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'          

#------------------


class Secuenciacion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
    

class Secuenciacion2(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

class CI(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

class CS(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

class Expresion(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

class Parentesis(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos

class Terminal(AST):
    def __init__(self, nodo, hijos):
        super().__init__(nodo, hijos)
        self.nodo = nodo
        self.hijos = hijos
=======
    def add_partes(self, partes):
        self.partes += partes
        return self
>>>>>>> 6dad4041c244cf20cdf4f58972e9a34fdd2045a9
