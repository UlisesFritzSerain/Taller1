class Nodo:
    def __init__(self, id, dato):
        self.id = id
        self.primerHijo = None
        self.hermanoDer = None
        self.dato = dato

def Padre(p, A, id):
    if p is not None:
        if p.primerHijo is not None and p.primerHijo.id == id:
            return p
        else:
            c = p.primerHijo
            while c is not None:
                padre = Padre(c, A, id)
                if padre is not None:
                    return padre
                c = c.hermanoDer
    return None

def vacio(A):
    return A is None

def nulo(p):
    return p is None

def HijoMasIzq(p, A):
    return p.primerHijo

def HermanoDer(p, A):
    return p.hermanoDer

def Info(p, A):
    return p.dato

def Raiz(A):
    return A

def preorden(A, p):
    c = p
    while c is not None:
        print(c.dato)
        if c.primerHijo is not None:
            preorden(A, c.primerHijo)
        c = c.hermanoDer

def elimina(A, p):
    padre = Padre(p, A)
    if padre:
        padre.primerHijo = p.primerHijo
    del p

# Ejemplo de uso
if __name__ == "__main__":
    # Crear nodos
    A = Nodo(1, "A")
    B = Nodo(2, "B")
    C = Nodo(3, "C")
    D = Nodo(4, "D")
    E = Nodo(5, "E")

    # Construir árbol
    A.primerHijo = B
    B.hermanoDer = C
    B.primerHijo = D
    D.hermanoDer = E

    # Ejecutar funciones
    preorden(A, A)
