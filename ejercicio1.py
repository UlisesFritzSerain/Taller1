class Nodo:
    def __init__(self,valor,padre=None):
        self.valor = valor
        self.padre = padre
        self.hijos = [] #inicalizamos arreglo

    def get_hijoPos(self,posicion): #Contemplar caso Hijo fuera de rango o inexistente
        if not self.hijos[posicion].es_nulo():
            return self.hijos[posicion]
        else:
            return None

    def es_nulo(self):
        return self is None

    def tiene_hijos(self):
        return not len(self.hijos) == 0
    
    def get_contenido(self): 
        if self is not None:
            return self.valor
        else:
            return None

    def get_raiz(self):
        if self.padre is None:
            return self
        else:
            return self.padre.get_raiz()
        
    def get_padre(self): #Arreglar caso raiz
        if self.padre is None:
            return None
        else:
            return self.padre
        
    def get_hijoizq(self): #NO FUNCIONA CUANDO NO TIENE HIJOS 
        if not self.tiene_hijos():
            return None
        else:
            return self.hijos[0]
        
    def get_hermanoder(self): #NO FUNCIONA FUERA DE RANGO 
        posicion_hermano = self.get_padre().hijos.index(self) + 1
        if self.get_padre().hijos[posicion_hermano] is None:
            return None
        else:
            return self.get_padre().hijos[posicion_hermano]

        
    def add_hijo(self,value):
        new_hijo = Nodo(value,self)
        self.hijos.append(new_hijo)

    def add_son_position(self, valor, position):
        nuevo_hijo = Nodo(valor, self)
        if position < 0 or position > len(self.hijos):  # Verifica si la posicion es valida
            raise ValueError("Posicion no valida")
        self.hijos.insert(position, nuevo_hijo)  # Insertar el nuevo hijo en la posicion especificada
        # Desplazar los hijos existentes a posiciones mayores
        for i in range(position + 1, len(self.hijos)):
            self.hijos[i].padre = self  # Actualizar el padre del hijo

    def imprimir_hijos(self):
        for elemento in self.hijos:
            if elemento is not None:    
                print(elemento.get_contenido())

    def preorder(self, nivel = 0):
        if not self.es_nulo():
            print("  " * nivel + self.valor) # Muestro Valor
            for hijo in self.hijos:
                hijo.preorder(nivel+1)

    def inorder(self, nivel=0):
        if self is None:
            return
        if len(self.hijos) > 0:
            self.hijos[0].inorder(nivel + 1)
        print(self.valor+" ", end='') # Muestro Valor
        for hijo in self.hijos[1:]:
            hijo.inorder(nivel + 1)

    def postorder(self, nivel=0):
        if not self.es_nulo():
            for hijo in self.hijos:
                hijo.postorder(nivel + 1)
            print(self.valor+" ", end='') # Muestro Valor



