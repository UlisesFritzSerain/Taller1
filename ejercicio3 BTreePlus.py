class Node:
    def __init__(self):
        self.es_hoja = False
        self.puntero = [None] * (maximo_hijos + 1)  # Punteros a los nodos Hijos
        self.clave = [None] * maximo_hijos  # Claves guardadas en el nodo
        self.clavesActualmente_almacenadas = 0  # Numero de claves actualmente guardadas en el nodo


class BTree:
    def __init__(self):
        self.raiz = None  # Nodo raiz del arbol

    def get_raiz(self):
        return self.raiz  # Devuelve nodo raiz

    def buscar(self, x):
        # busca una clave en el arbol
        if self.raiz is None:
            return -1  # El arbol esta vacio
        else:
            actual = self.raiz
            while not actual.es_hoja:
                for i in range(actual.clavesActualmente_almacenadas):
                    if x < actual.clave[i]:
                        actual = actual.puntero[i]
                        break

                    if i == actual.clavesActualmente_almacenadas - 1:
                        actual = actual.puntero[i + 1]
                        break

            for i in range(actual.clavesActualmente_almacenadas):
                if actual.clave[i] == x:
                    return 1  # clave encontrada

            return 0  # clave no encontrada


maximo_hijos = 5  # cantidad maxima de hijos pre-seteada

btree = BTree()  # Crea un nuevo arbol

