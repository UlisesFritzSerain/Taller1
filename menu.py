from ejercicio1 import Nodo
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog
"""
class MenuGUI:
    def __init__(self, raiz):
        self.raiz = raiz

        self.ventana = tk.Tk()
        self.ventana.title("Menú del Árbol")

        self.etiqueta = tk.Label(self.ventana, text="Nodo actual:")
        self.etiqueta.pack()

        self.valor_actual = tk.StringVar()
        self.valor_actual.set(raiz.valor)
        self.etiqueta_valor_actual = tk.Label(self.ventana, textvariable=self.valor_actual)
        self.etiqueta_valor_actual.pack()

        self.boton_agregar_hijo = tk.Button(self.ventana, text="Agregar hijo", command=self.agregar_hijo)
        self.boton_agregar_hijo.pack()

        self.boton_agregar_hermano = tk.Button(self.ventana, text="Agregar hermano a la derecha", command=self.agregar_hermano)
        self.boton_agregar_hermano.pack()

        self.boton_eliminar_nodo = tk.Button(self.ventana, text="Eliminar nodo", command=self.eliminar_nodo)
        self.boton_eliminar_nodo.pack()

        self.boton_siguiente_nodo = tk.Button(self.ventana, text="Avanzar al siguiente nodo", command=self.avanzar_siguiente_nodo)
        self.boton_siguiente_nodo.pack()

        self.boton_salir = tk.Button(self.ventana, text="Salir del menú", command=self.ventana.quit)
        self.boton_salir.pack()

    def agregar_hijo(self):
        valor_hijo = tkinter.simpledialog.askstring("Agregar hijo", "Ingrese el valor del nuevo hijo:")
        posicion = tkinter.simpledialog.askinteger("Agregar hijo", "Ingrese la posición del nuevo hijo:")
        try:
            self.raiz.add_son_position(valor_hijo, posicion)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        else:
            self.actualizar_interfaz()

    def agregar_hermano(self):
        valor_hermano = tk.simpledialog.askstring("Agregar hermano", "Ingrese el valor del nuevo hermano:")
        self.raiz.get_padre().add_son_position(valor_hermano, self.raiz.get_padre().hijos.index(self.raiz) + 1)
        self.actualizar_interfaz()

    def eliminar_nodo(self):
        if self.raiz.get_padre():
            self.raiz.get_padre().hijos.pop(self.raiz.get_padre().hijos.index(self.raiz))
            messagebox.showinfo("Eliminar nodo", f"El nodo {self.raiz.valor} ha sido eliminado.")
            self.actualizar_interfaz()
        else:
            messagebox.showerror("Error", "No se puede eliminar el nodo raíz.")

    def avanzar_siguiente_nodo(self):
        for hijo in self.raiz.hijos:
            self.mostrar_menu(hijo)

    def mostrar_menu(self, nodo):
        self.valor_actual.set(nodo.valor)

    def actualizar_interfaz(self):
        # Actualizar la interfaz con el nodo actualizado
        pass

    def iniciar_menu(self):
        self.ventana.mainloop()

"""
class Menu:
    def __init__(self, raiz):
        self.raiz = raiz

    def mostrar_menu(self, nodo):
        while True:
            print(f"\nNodo actual: {nodo.valor}")
            print("1. Agregar hijo")
            print("2. Agregar hermano a la derecha")
            print("3. Eliminar nodo")
            print("4. Avanzar al siguiente nodo")
            print("5. Salir del menú (primera vez vuelve a la raiz)")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                valor_hijo = input("Ingrese el valor del nuevo hijo: ")
                posicion = int(input("Ingrese la posición del nuevo hijo: "))
                nodo.add_son_position(valor_hijo, posicion)
            elif opcion == "2":
                valor_hermano = input("Ingrese el valor del nuevo hermano: ")
                nodo.get_padre().add_son_position(valor_hermano, nodo.get_padre().hijos.index(nodo) + 1)
            elif opcion == "3":
                padre = nodo.get_padre()
                hijos_del_nodo = nodo.hijos
                if padre:
                    indice_del_nodo = padre.hijos.index(nodo)
                    for hijo in hijos_del_nodo:
                        hijo.padre = padre
                    padre.hijos.pop(indice_del_nodo)
                    print(f"El nodo {nodo.valor} ha sido eliminado.")
                else:
                    print("No se puede eliminar el nodo raíz.")
            elif opcion == "4":
                for hijo in nodo.hijos:
                    self.mostrar_menu(hijo)
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def iniciar_menu(self):
        self.mostrar_menu(self.raiz)
        self.raiz.preorder()

# Ejemplo de uso
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

    # Crear la interfaz gráfica del menú para el árbol
    menu = Menu(raiz)

    # Iniciar el menú
    menu.iniciar_menu() 
