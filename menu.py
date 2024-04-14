from ejercicio1 import Nodo

class Menu:
    def __init__(self, raiz):
        self.raiz = raiz

    def mostrar_menu(self, nodo):
        while True:
            print("Arbol actual:")
            self.raiz.preorder()
            
            print(f"Nodo actual: {nodo.valor}")
            print("1. Agregar hijo")
            print("2. Agregar hermano a la derecha")
            print("3. Eliminar nodo")
            print("4. Avanzar al siguiente nodo")
            print("5. Salir del menú (primera vez vuelve a la raiz)")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                valor_hijo = input("Ingrese el valor del nuevo hijo: ")
                if len(nodo.hijos)==0:
                    posicion = 0
                else:
                    max_posicion = len(nodo.hijos)
                    posicion = int(input(f"Ingrese la posición del nuevo hijo (0-{max_posicion}): "))
                    while posicion < 0 or posicion > max_posicion:
                        print("Posición no válida. Por favor, ingrese una posición válida.")
                        posicion = int(input(f"Ingrese la posición del nuevo hijo (0-{max_posicion}): "))
                nodo.add_son_position(valor_hijo, posicion)
            elif opcion == "2":
                valor_hermano = input("Ingrese el valor del nuevo hermano: ")
                nodo.get_padre().add_son_position(valor_hermano, nodo.get_padre().hijos.index(nodo) + 1)
            elif opcion == "3":
                padre = nodo.get_padre()
                if padre:
                    hijos_del_nodo = nodo.hijos
                    indice_del_nodo = padre.hijos.index(nodo)
                    for hijo in hijos_del_nodo:
                        hijo.padre = padre
                        padre.hijos.insert(indice_del_nodo, hijo)
                        indice_del_nodo += 1
                    padre.hijos.pop(indice_del_nodo)
                    print(f"El nodo {nodo.valor} ha sido eliminado y sus hijos han sido movidos al nodo padre.")
                else:
                    print("No se puede eliminar el nodo raíz.")
            elif opcion == "4":
                for hijo in nodo.hijos:
                    self.mostrar_menu(hijo)
                break
            elif opcion == "5":
                return
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def iniciar_menu(self):
        self.mostrar_menu(self.raiz)
        self.raiz.preorder()

if __name__ == "__main__":
    # Crear un árbol de ejemplo
    raiz = Nodo("A")
    B = Nodo("B", raiz)
    C = Nodo("C", raiz)
    D = Nodo("D", B)
    E = Nodo("E", B)
    F = Nodo("F", C)
    G = Nodo("G", C)
    raiz.hijos = [B, C]
    B.hijos = [D, E]
    C.hijos = [F, G]

    menu = Menu(raiz)

    # Iniciar el menú
    menu.iniciar_menu() 
