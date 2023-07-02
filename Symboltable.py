class Simbolo:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class SimboloVariable(Simbolo):
    pass

class SimboloScope(Simbolo):
    def __init__(self, ent, boole, canv):
        self.ent= ent
        self.boole = boole
        self.canv = canv

class TablaSimbolos(object):

    def __init__(self, parent, name): # scope padre y nombre de la tabla de simbolos
        self.symbols = {}
        self.name = name
        self.parent = parent

    def put(self, symbol): # Agregar simbolo de variable
        if self.symbols.__contains__(symbol.name):
            return False
        else:
            self.symbols[symbol.name]= symbol
            return True

    def get(self, name): # Obtener simbolo de variable
        if self.symbols.__contains__(name):
            return self.symbols[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            return None


    def getParentScope(self):
        return self.parent