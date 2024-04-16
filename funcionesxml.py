from ejercicio1 import Nodo
import xml.etree.ElementTree as ET #libreria para usar xML 
#En este archivo presentaremos las funciones para aplicar la persistencia del arbol

def cargar_arbol_desde_xml(nombre_archivo):
    try:
        arbol_xml = ET.parse(nombre_archivo)
        raiz_xml = arbol_xml.getroot()
        return crear_nodo_desde_xml(raiz_xml)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return None


def crear_nodo_desde_xml(elemento_xml, padre=None):
    valor_nodo = elemento_xml.get("valor")
    nodo = Nodo(valor_nodo, padre)
    for hijo_xml in elemento_xml.findall("Nodo"):
        hijo_nodo = crear_nodo_desde_xml(hijo_xml, nodo)
        nodo.hijos.append(hijo_nodo)
    return nodo

def arbol_a_xml(nodo):
    def construir_xml(nodo):
        elemento = ET.Element("Nodo")
        elemento.set("valor", nodo.valor)
        for hijo in nodo.hijos:
            elemento.append(construir_xml(hijo))
        return elemento

    
    raiz_xml = construir_xml(nodo)
    arbol_xml = ET.ElementTree(raiz_xml)
    return arbol_xml

def guardar_xml_en_archivo(arbol_xml, nombre_archivo):
    try:
        arbol_xml.write(nombre_archivo)
        print(f"El árbol ha sido guardado en el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar el árbol en el archivo {nombre_archivo}: {e}")