from ejercicio1 import Nodo
import funcionesxml as fxml
class Menu:
    def __init__(self, raiz):
        self.raiz = raiz

    def mostrar_menu(self, nodo):
        while True:
            print("Arbol Inorden: ",end="")
            self.raiz.inorder()
            print("\nArbol Postorden: ",end="")
            self.raiz.postorder()
            print("\nArbol actual:")
            self.raiz.preorder()
            print(f"\nNodo actual: {nodo.valor}")
            print("1. Agregar hijo")
            print("2. Agregar hermano a la derecha")
            print("3. Eliminar nodo")
            print("4. Avanzar al siguiente nodo")
            print("5. Volver a la raiz")
            print("6. Salir del menu (reiterar)")
            
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                valor_hijo = input("Ingrese el valor del nuevo hijo: ")
                if len(nodo.hijos)==0:
                    posicion = 0
                else:
                    max_posicion = len(nodo.hijos)
                    posicion = int(input(f"Ingrese la posicion del nuevo hijo (0-{max_posicion}): "))
                    while posicion < 0 or posicion > max_posicion:
                        print("Posicion no valida. Por favor, ingrese una posicion valida.")
                        posicion = int(input(f"Ingrese la posicion del nuevo hijo (0-{max_posicion}): "))
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
                    print("No se puede eliminar el nodo raiz.")
                nodo = self.raiz
            elif opcion == "4":
                if nodo.tiene_hijos():
                    nodo = nodo.get_hijoizq()
                else:
                    padre = nodo.get_padre()
                    if padre:
                        indice_del_nodo = padre.hijos.index(nodo)
                        if indice_del_nodo + 1 < len(padre.hijos):
                            nodo = padre.hijos[indice_del_nodo + 1]
                        else:
                # Si no hay mas hermanos, avanzar al primer hermano del padre
                            hermano_izquierdo = padre.get_hijoizq()
                            if hermano_izquierdo:
                                nodo = hermano_izquierdo.get_hermanoder()
                            else:
                                print("No hay mas nodos siguientes.")
                    else:
                        print("No hay nodos siguientes.")
            elif opcion == "5":
                nodo = self.raiz
            elif opcion == "6":
                return
            else:
                print("Opcion no valida. Por favor, seleccione una opcion valida.")

    def iniciar_menu(self):
        self.mostrar_menu(self.raiz)
        self.raiz.preorder()


arbol_cargado = fxml.cargar_arbol_desde_xml("arbol.xml")


if __name__ == "__main__":
    menu = Menu(arbol_cargado) #crea clase menu

    menu.iniciar_menu() # inicia el menu, cuando termina manda el arbol modificado al archivo
    xml_arbol = fxml.arbol_a_xml(arbol_cargado)
    fxml.guardar_xml_en_archivo(xml_arbol, "arbol.xml")