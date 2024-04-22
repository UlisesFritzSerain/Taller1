# Crear un nodo
class BTreeNode:
  def __init__(self, es_hoja=False):
    self.es_hoja = es_hoja
    self.claves = []
    self.hijos = []
 
 
# Arbol
class BTree:
  def __init__(self, t):
    self.raiz = BTreeNode(True)
    self.t = t
 
  # Buscar clave en el arbol
  def buscar(self, k, x=None):
    if x is not None:
      i = 0
      while i < len(x.claves) and k > x.claves[i][0]:
        i += 1
      if i < len(x.claves) and k == x.claves[i][0]:
        return (x, i)
      elif x.es_hoja:
        return None
      else:
        return self.buscar(k, x.hijos[i])
       
    else:
      return self.buscar(k, self.raiz)
    
  # Imprimir el arbol
  def imprimir(self, nivel=0):
    print("Nivel ", nivel, " ", len(self.claves), end=":")
    for i in self.claves:
      print(i, end=" ")
    print()
    nivel += 1
    if len(self.hijos) > 0:
      for i in self.hijos:
        self.imprimir(i, nivel)
 
 
def main():
  B = BTree(3)
 
 
if __name__ == '__main__':
  main()