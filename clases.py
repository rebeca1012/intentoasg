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

    def add_partes(self, partes):
        self.partes += partes
        return self
