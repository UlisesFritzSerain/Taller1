class Nodo:
    def __init__(self, valor, padre=None):
        self.valor = valor
        self.padre = padre
        self.hijos = []

    def no_tiene_hijos(self):
        return len(self.hijos) == 0

    def es_nulo(self):
        return self is None

    def get_raiz(self):
        if self.padre is None:
            return self
        else:
            return self.padre.get_raiz()

    def get_padre(self):
        return self.padre

    def get_primer_hijo(self):
        if self.hijos:
            return self.hijos[0]
        else:
            return None

    def get_hermano_derecha(self):
        if self.padre is None:
            return None
        else:
            indice = self.padre.hijos.index(self)
            if indice < len(self.padre.hijos) - 1:
                return self.padre.hijos[indice + 1]
            else:
                return None

    def get_contenido(self):
        return self.valor

    def __str__(self):
        return str(self.valor)

class ArbolNario:
    def __init__(self):
        self.raiz = None

    def no_tiene_hijos(self):
        return self.raiz is None

    def insertar(self, valor, padre=None):
        if self.no_tiene_hijos():
            self.raiz = Nodo(valor)
        else:
            if padre is None:
                padre = self.raiz
            padre.hijos.append(Nodo(valor, padre))

    def eliminar(self, nodo):
        if not nodo.es_nulo():
            if nodo.no_tiene_hijos():
                if nodo.padre is not None:
                    nodo.padre.hijos.remove(nodo)
            else:
                for hijo in nodo.hijos:
                    self.eliminar(hijo)
                if nodo.padre is not None:
                    nodo.padre.hijos.remove(nodo)

    def preorden(self, nodo):
        if not nodo.es_nulo():
            print(nodo)
            for hijo in nodo.hijos:
                self.preorden(hijo)

    def inorden(self, nodo):
        if not nodo.es_nulo():
            if not nodo.no_tiene_hijos():
                self.inorden(nodo.get_primer_hijo())
            print(nodo)
            if not nodo.no_tiene_hijos():
                self.inorden(nodo.get_hermano_derecha())

    def postorden(self, nodo):
        if not nodo.es_nulo():
            for hijo in nodo.hijos:
                self.postorden(hijo)
            print(nodo)

# Ejemplo de uso
arbol = ArbolNario()

# Inserción de nodos
arbol.insertar("A")
arbol.insertar("B", arbol.raiz)
arbol.insertar("C", arbol.raiz)
arbol.insertar("D", arbol.raiz)
#arbol.insertar("E", arbol.get_primer_hijo(arbol.raiz))
#arbol.insertar("F", arbol.get_primer_hijo(arbol.raiz))


# Recorridos del árbol
print("Preorden:")
arbol.preorden(arbol.raiz)

print("Inorden:")
arbol.inorden(arbol.raiz)

print("Postorden:")
arbol.postorden(arbol.raiz)

# Eliminación de nodos
arbol.eliminar(arbol.get_primer_hijo(arbol.raiz))

print("Inorden después de eliminar un nodo:")
arbol.inorden(arbol.raiz)
