class Nodo:
    def __init__(self,valor,padre=None):
        self.valor = valor
        self.padre = padre
        self.hijos = [] #inicalizamos arreglo

    def es_nulo(self):
        return self is None
    

    def tiene_hijos(self):
        return not len(self.hijos) == 0
    
    def get_contenido(self):
        if self is not None:
            return self.valor
        else:
            return ""
    
    def get_raiz(self):
        if self.padre is None:
            return self
        else:
            return self.padre.get_raiz()
        
    def get_padre(self): #PROBAR | contemplar caso raiz
        if self.padre is None:
            return None
        else:
            return self.padre
        
    def get_hijoizq(self): #PROBAR | NO FUNCIONA CUANDO NO TIENE HIJOS 
        if not self.tiene_hijos():
            return None
        else:
            return self.hijos[0]
        
    def get_hermanoder(self): #PROBAR | VERIFICAR FUERA DE RANGO 
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
        if position < 0 or position > len(self.hijos):  # Verifica si la posición es válida
            raise ValueError("Posición no válida")
        self.hijos.insert(position, nuevo_hijo)  # Insertar el nuevo hijo en la posición especificada
        # Desplazar los hijos existentes a posiciones mayores
        for i in range(position + 1, len(self.hijos)):
            self.hijos[i].padre = self  # Actualizar el padre del hijo

    def imprimir_hijos(self):
        for elemento in self.hijos:
            if elemento is not None:    
                print(elemento.get_contenido())

    def preorder(self):
        if not self.es_nulo():
            print(self.valor)
            for hijo in self.hijos:
                hijo.preorder()

#main
nodito = Nodo(1)

nodito.add_hijo(2)
nodito.add_hijo(3)
nodito.add_hijo(5)

nodito.hijos[1].add_hijo(67)

#nodito.add_son_position(4,1)

##print(nodito.hijos[0].get_contenido())
##print(nodito.hijos[0].get_raiz().get_contenido())

#nodito.hijos[1].imprimir_hijos()
#print(nodito.hijos[1].hijos[0].get_contenido())
#print(nodito.hijos[1].hijos[0].get_raiz().get_contenido())
#print(nodito.hijos[0].get_hijoizq().get_contenido())


#print(nodito.hijos[2].get_hermanoder().get_contenido())

nodito.preorder()