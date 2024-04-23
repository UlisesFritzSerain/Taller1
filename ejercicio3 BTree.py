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

  def insertar(self, clave):
      raiz = self.raiz
      if len(raiz.claves) == (2 * self.t) - 1:
          nuevo_nodo = BTreeNode()
          self.raiz = nuevo_nodo
          nuevo_nodo.hijos.append(raiz)
          self.dividir_hijo(nuevo_nodo, 0)
          self.insertar_no_vacio(nuevo_nodo, clave)
      else:
          self.insertar_no_vacio(raiz, clave)

  def insertar_no_vacio(self, nodo, clave):
      i = len(nodo.claves) - 1
      if nodo.es_hoja:
          while i >= 0 and clave < nodo.claves[i]:
              i -= 1
          i += 1
          nodo.claves.insert(i, clave)
      else:
          while i >= 0 and clave < nodo.claves[i]:
              i -= 1
          i += 1
          if len(nodo.hijos[i].claves) == (2 * self.t) - 1:
              self.dividir_hijo(nodo, i)
              if clave > nodo.claves[i]:
                  i += 1
          self.insertar_no_vacio(nodo.hijos[i], clave)

  def dividir_hijo(self, nodo, i):
      t = self.t
      hijo = nodo.hijos[i]
      nuevo_nodo = BTreeNode(hijo.es_hoja)
      nodo.hijos.insert(i + 1, nuevo_nodo)
      nodo.claves.insert(i, hijo.claves[t - 1])
      nuevo_nodo.claves = hijo.claves[t:(2 * t) - 1]
      hijo.claves = hijo.claves[0:t - 1]
      if not hijo.es_hoja:
          nuevo_nodo.hijos = hijo.hijos[t:(2 * t)]
          hijo.hijos = hijo.hijos[0:t]


  # Buscar clave en el arbol 
  def buscar(self, clave):
        return self.buscar_en_nodo(self.raiz, clave)

  def buscar_en_nodo(self, nodo, clave):
      i = 0
      while i < len(nodo.claves) and clave > nodo.claves[i]:
          i += 1
      if i < len(nodo.claves) and clave == nodo.claves[i]:
          return True
      elif nodo.es_hoja:
          return False
      else:
          return self.buscar_en_nodo(nodo.hijos[i], clave)
    
  # Imprimir el arbol
  def imprimir_arbol(self):
          self.imprimir_nodo(self.raiz)

  def imprimir_nodo(self, nodo, nivel=0):
      print("Nivel", nivel, ":", nodo.claves)
      if not nodo.es_hoja:
          for hijo in nodo.hijos:
              self.imprimir_nodo(hijo, nivel + 1)
  # Acceso secuencial al arbol
  def acceso_secuencial(self):
          self.recorrido_secuencial(self.raiz)

  def recorrido_secuencial(self, nodo):
      if nodo:
          for i in range(len(nodo.claves)):
              if not nodo.es_hoja:
                  self.recorrido_secuencial(nodo.hijos[i])
              print(nodo.claves[i], end=" ")
          if not nodo.es_hoja:
              self.recorrido_secuencial(nodo.hijos[-1])

if __name__ == '__main__':
  btree = BTree(3)  # Crear un arbol B con un grado minimo de 3
  claves = [10, 45, 26, 31, 38, 4, 3, 44, 30, 11, 28, 14, 32, 12, 37, 20, 13, 39, 24, 2]
  for clave in claves:
    btree.insertar(clave)
  print("arbol B:")
  btree.imprimir_arbol()

  clave_buscar = 13
  if btree.buscar(clave_buscar):
      print(f"\nLa clave {clave_buscar} esta en el arbol.")
  else:
      print(f"\nLa clave {clave_buscar} no esta en el arbol.")

  print("\nAcceso secuencial a todos los elementos: (Inorden, asi se muestra de forma ascendente y ordenada)")
  btree.acceso_secuencial()
