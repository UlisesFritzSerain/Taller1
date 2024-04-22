class Node:
    def __init__(self):
        self.es_hoja = False
        self.puntero = [None] * (tamanio_max_hijos + 1)  # Referencia a los nodos hijos
        self.llave = [None] * tamanio_max_hijos  # llaves guardadas en el nodo
        self.tamanio = 0  # Numero de llaves que estan actualmente en el nodo


class BTree:
    def __init__(self):
        self.raiz = None  # Nodo raiz del arbol

    def get_raiz(self):
        return self.raiz  # Obtener nodo raiz

    def insertar(self, x):
        if self.raiz is None:
            # Si B-tree esta vacio, crea una nueva raiz
            self.raiz = Node()
            self.raiz.llave[0] = x
            self.raiz.es_hoja = True
            self.raiz.tamanio = 1
        else:
            actual = self.raiz
            padre = None

            # Recorre el arbol para encontrar el nodo hoja apropiado para la insercion
            while not actual.es_hoja:
                padre = actual

                for i in range(actual.tamanio):
                    if actual.llave[i] is None or x < actual.llave[i]:
                        actual = actual.puntero[i]
                        break

                    if i == actual.tamanio - 1:
                        actual = actual.puntero[i + 1]
                        break

            if actual.tamanio < tamanio_max_hijos:
                # Inserta en un nodo hoja que no este lleno
                i = 0

                while i < actual.tamanio and (actual.llave[i] is not None and x > actual.llave[i]):
                    i += 1

                # Mueve las llaves y los punteros para hacer espacio a la nueva llave
                for j in range(actual.tamanio, i, -1):
                    actual.llave[j] = actual.llave[j - 1]

                actual.llave[i] = x
                actual.tamanio += 1

                actual.puntero[actual.tamanio] = actual.puntero[actual.tamanio - 1]
                actual.puntero[actual.tamanio - 1] = None
            else:
                # Divide el nodo hoja si esta lleno
                nueva_hoja = Node()
                nodo_temporal = [None] * (tamanio_max_hijos + 1)

                # Copia llaves al arreglo temporal
                for i in range(tamanio_max_hijos):
                    nodo_temporal[i] = actual.llave[i]

                i = 0

                while i < tamanio_max_hijos and (nodo_temporal[i] is not None and x > nodo_temporal[i]):
                    i += 1

                # Mueve las llaves en el arreglo temporal para hacer espacio a la nueva llave
                for j in range(tamanio_max_hijos, i, -1):
                    nodo_temporal[j] = nodo_temporal[j - 1]

                nodo_temporal[i] = x

                # Actualiza el tamaño del nodo actual y del nodo de la nueva hoja
                nueva_hoja.es_hoja = True
                actual.tamanio = (tamanio_max_hijos + 1) // 2
                nueva_hoja.tamanio = tamanio_max_hijos + 1 - (tamanio_max_hijos + 1) // 2

                # Actualiza punteros
                actual.puntero[actual.tamanio] = nueva_hoja
                nueva_hoja.puntero[nueva_hoja.tamanio] = actual.puntero[tamanio_max_hijos]
                actual.puntero[nueva_hoja.tamanio] = actual.puntero[tamanio_max_hijos]
                actual.puntero[tamanio_max_hijos] = None

                # Copy las llaves del arreglo temporal al actual y al de la nueva hoja 
                for i in range(actual.tamanio):
                    actual.llave[i] = nodo_temporal[i]

                for i in range(actual.tamanio, tamanio_max_hijos):
                    nueva_hoja.llave[i - actual.tamanio] = nodo_temporal[i]

                if actual == self.raiz:
                    # Actualiza la raiz si fue dividida
                    new_root = Node()
                    new_root.llave[0] = nueva_hoja.llave[0]
                    new_root.puntero[0] = actual
                    new_root.puntero[1] = nueva_hoja
                    new_root.es_hoja = False
                    new_root.tamanio = 1
                    self.raiz = new_root
                else:
                    # Propaga la division hacia arriba
                    self.cambiar_nivel(nueva_hoja.llave[0], padre, nueva_hoja)

    def cambiar_nivel(self, x, actual, child):
        # Metodo que facilita la division de nodos no hoja
        if actual.tamanio < tamanio_max_hijos:
            i = 0
            while i < actual.tamanio and (actual.llave[i] is not None and x > actual.llave[i]):
                i += 1

            # Mueve las llaves y los punteros para hacer espacio para la nueva llave y el hijo
            for j in range(actual.tamanio, i, -1):
                actual.llave[j] = actual.llave[j - 1]

            for j in range(actual.tamanio + 1, i + 1, -1):
                actual.puntero[j] = actual.puntero[j - 1]

            actual.llave[i] = x
            actual.tamanio += 1
            actual.puntero[i + 1] = child
        else:
            # Divide el nodo no hoja si esta lleno
            nuevo_interno = Node()
            temp_llave = [None] * (tamanio_max_hijos + 1)
            temp_puntero = [None] * (tamanio_max_hijos + 2)

            # Copia las llaves y los punteros al nodo temporal
            for i in range(tamanio_max_hijos):
                temp_llave[i] = actual.llave[i]

            for i in range(tamanio_max_hijos + 1):
                temp_puntero[i] = actual.puntero[i]

            i = 0

            while i < tamanio_max_hijos and (temp_llave[i] is not None and x > temp_llave[i]):
                i += 1

            # Mueve las llaves al arreglo temporal para hacer espacio a la nueva llave
            for j in range(tamanio_max_hijos, i, -1):
                temp_llave[j] = temp_llave[j - 1]

            temp_llave[i] = x

            # Mueve los punteros en el arreglo temporal para hacer espacio al nuevo hijo
            for j in range(tamanio_max_hijos + 1, i + 1, -1):
                temp_puntero[j] = temp_puntero[j - 1]

            temp_puntero[i + 1] = child
            nuevo_interno.es_hoja = False
            actual.tamanio = (tamanio_max_hijos + 1) // 2
            nuevo_interno.tamanio = tamanio_max_hijos - (tamanio_max_hijos + 1) // 2

            # Copia las llaves y los punteros del arreglo temporal al actual y a los nodos nuevo_interno 
            for i in range(actual.tamanio + 1, tamanio_max_hijos + 1):
                nuevo_interno.llave[i - actual.tamanio - 1] = temp_llave[i]

            for i in range(actual.tamanio + 1, tamanio_max_hijos + 2):
                nuevo_interno.puntero[i - actual.tamanio - 1] = temp_puntero[i]

            if actual == self.raiz:
                # Actualiza la raiz si fue dividida
                new_root = Node()
                new_root.llave[0] = actual.llave[actual.tamanio]
                new_root.puntero[0] = actual
                new_root.puntero[1] = nuevo_interno
                new_root.es_hoja = False
                new_root.tamanio = 1
                self.raiz = new_root
            else:
                # Propaga la division hacia arriba
                self.cambiar_nivel(actual.llave[actual.tamanio], self.encontrar_padre(self.raiz, actual), nuevo_interno)

    def busqueda(self, x):
        # busca una llave en el B-Tree
        if self.raiz is None:
            return -1  # El B-tree esta vacio
        else:
            actual = self.raiz
            while not actual.es_hoja:
                for i in range(actual.tamanio):
                    if x < actual.llave[i]:
                        actual = actual.puntero[i]
                        break

                    if i == actual.tamanio - 1:
                        actual = actual.puntero[i + 1]
                        break

            for i in range(actual.tamanio):
                if actual.llave[i] == x:
                    return 1  # La llave se encontro

            return 0  # La llave NO se encontro

    def imprime(self, actual):
        # imprime el B-tree
        if actual is None:
            return

        q = [actual]

        while q:
            l = len(q)

            for _ in range(l):
                t_node = q.pop(0)

                for j in range(t_node.tamanio):
                    if t_node.llave[j] is not None:
                        print(t_node.llave[j], end=' ')

                for j in range(t_node.tamanio + 1):
                    if t_node.puntero[j]:
                        q.append(t_node.puntero[j])

                print('\t', end='')

            print('\n')

    def encontrar_padre(self, actual, child):
        # Metodo de ayuda para encontrar al padre de un nodo dado
        padre = None

        if actual.es_hoja or actual.puntero[0].es_hoja:
            return None  # No hay padre

        for i in range(actual.tamanio + 1):
            if actual.puntero[i] == child:
                padre = actual
                return padre
            else:
                padre = self.encontrar_padre(actual.puntero[i], child)
                if padre:
                    return padre

        return padre


tamanio_max_hijos = 3  # Tamaño maximo de hijos en el B-tree

btree = BTree()  # Crea un nuevo B-tree

print('Cada nodo puede tener como maximo', tamanio_max_hijos, 'hijos!')

# Inserta elementos en el B-tree
btree.insertar(1)
btree.insertar(2)
btree.insertar(3)
btree.imprime(btree.get_raiz())

btree.insertar(4)
btree.insertar(5)
btree.imprime(btree.get_raiz())
