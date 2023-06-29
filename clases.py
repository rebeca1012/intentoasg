#Entrada
class Entrada():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    
    def print_object(self, profund):
        return f'{"-"*profund}Entrada\n{self.hijos.print_object(profund+1)}'    


#Declaraciones
class Declaraciones():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    def print_object(self, profund):
        return f'{"-"*profund}Declaraciones\n{self.hijos.print_object(profund+1)}'
    

#Declaracion
class Declaracion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos
        
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.hijos}'

#Secuencia Declaración
class Secuencia_Declaracion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo} : {self.hijos}'


#Variables
class Variables():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo} : {self.hijos}'    


#Tipo
class Tipo():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos 
   
#     def print_object(self, profund):
#         return f'{"-"*profund}{self.nodo}'  


#Id
class Id():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos 
    
    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo}' 




#PALABRAS RESERVADAS --------

#If
class If():
    def __init__(self, nodo, hijos):
        self.nodo = nodo 
        self.hijos = hijos 

    def print_object(self, profund):
        return f'{"-"*profund}{self.nodo} : {self.hijos}'


#With
class With():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
        #return f'{"-"*profund}{self.iterador} : {self.cota_inf} : {self.cota_sup} : {self.secuenciacion}'

class From():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.cota_inf} : {self.cota_sup} : {self.secuenciacion}'    
    

class While():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.condicion} : {self.secuenciacion}'  


class Read():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.id}'    

class Print():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}{self.exp}'    



#------        

#OPERADORES ARITMÉTICOS -------------

#Mas
class Mas():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mas\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'


#Menos
class Menos():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Menos\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Unary Menos
class UMenos():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = -hijos
    
    def __str__(self):
        return f'{self.hijos}'
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}UMenos\n{self.exp.print_object(profund+1)}'


#Multiplicación
class Mult():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mult\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'


#División
class Div():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Div\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Modulo
class Mod():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mod\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Conjuncion
class Conjuncion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Conjuncion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Disyunción
class Disyuncion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Disyuncion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Igual
class Igual():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Igual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'
    
#Desigual
class Desigual():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Desigual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Menor
class Menor():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Menor\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#MenorIgual
class MenorIgual():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}MenorIgual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Mayor   
class Mayor():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Mayor\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#MayorIgual
class MayorIgual():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}MayorIgual\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'

#Asginación 
class Asignacion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}Asignacion\n{self.id.print_object(profund+1)}\n{self.exp.print_object(profund+1)}'


#Negación
class Negacion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos
    
    #def print_object(self, profund):
    #    return f'{"-"*profund}Negacion\n{self.exp.print_object(profund+1)}'


#Concatenación Horizontal
class ConcatHorizontal():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}ConcatHorizontal\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'


#Concatenación Vertical
class ConcatVertical():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}ConcatVertical\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'  


#Rotación
class Rotacion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Rotacion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'  

#Transposición
class Transposicion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

    #def print_object(self, profund):
    #    return f'{"-"*profund}Transposicion\n{self.exp1.print_object(profund+1)}\n{self.exp2.print_object(profund+1)}'          

#------------------


class Secuenciacion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

class CI():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

class CS():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

class Expresion():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

class Parentesis():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos

class Terminal():
    def __init__(self, nodo, hijos):
        self.nodo = nodo
        self.hijos = hijos