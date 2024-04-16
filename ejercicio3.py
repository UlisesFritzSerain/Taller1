class NodoArbolB:
    def __init__(self, t, padre=None):
        self.t = t #Grado Arbol
        self.claves = [] #Lista claves
        self.padre = padre #Almacena padre
        self.hijos = [] #Lista puntero hijos

    def es_hoja(self):
        return not self.hijos
        
    def get_raiz(self):
        if self.padre is None:
            return self
        else:
            return self.padre.get_raiz()

    def buscar(self, clave):
        nodo_actual = self.get_raiz()
        while nodo_actual is not None:
            #recorrer nodos hasta encontrar clave o nodo hoja
            indice = 0
            #mientras existan claves sin recorrer y la clave del nodo actual sea menor que la clave buscada
            while indice < len(nodo_actual.claves) and nodo_actual.claves[indice] < clave:
                indice += 1

            #en caso de que la clave se encuentre
            if indice < len(nodo_actual.claves) and clave == nodo_actual.claves[indice]:
                #clave encontrada
                return nodo_actual, indice
            
            elif nodo_actual.es_hoja():
                #clave no encontrada en el árbol
                return None, None
            
            else:
                #desciendo al subarbol correspondiente
                if indice > 0 and clave > nodo_actual.claves[indice - 1]:
                    siguiente_indice = indice
                else:
                    siguiente_indice = indice
                nodo_actual = nodo_actual.hijos[siguiente_indice]

        #se llego al final del árbol sin encontrar clave 
        return None, None

    
    def insertar(self,clave): #opcional
        pass
        
    def eliminar(self,clave): #opcional
        pass
       