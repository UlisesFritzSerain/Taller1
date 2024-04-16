# Ejercicio 2

### Arboles en Archivos Indexados
***
### Arboles B
Son estructuras de datos de busqueda que estan diseñadas para mantener datos ordenados y permitir operaciones de busqueda eficientes. Especialmente diseñados para ser utilizados en sistemas de almacenamiento de base de datos y sistemas de archivos, donde el acceso rapido a los datos es esencial.
La idea de los Arboles B es que los nodos internos deben tener un número variable de nodos hijo dentro de un rango predefinido. Cuando se inserta o se elimina un dato de la estructura, la cantidad de nodos hijo varía dentro de un nodo. Para que siga manteniéndose el número de nodos dentro del rango predefinido, los nodos internos se juntan o se parten.  
**Caracteristicas:** Son eficientes en busqueda, insercion y eliminacion de datos. mantiene un factor de equilibrio para asegurar tiempos de busqueda predecibles, ademas de que cada nodo contiene informacion sobre el rango de claves que abarca y como llegar a los nodos hijos.  
**Variantes:** Arboles B+ / Arboles B*

**Ejemplo de un Arbol B**  
![Ejemplo ArbolB](https://www.apinem.com/wp-content/uploads/2024/02/arbol-b-ejemplo.png)  
**Estructura de un Nodo (Arbol B)**
```
struct Nodo {
      int claves[m - 1];  // Array de claves
      int n;            // Número de claves almacenadas
  Nodo* hijos[m];   // Array de punteros a nodos hijos
};
```
**Funcion de Busqueda (Arbol B)**
```
Nodo* buscar(Nodo* raiz, int clave) {
  if (raiz == NULL) return NULL;

  int i = 0;
  while (i < raiz->n && clave >= raiz->claves[i]) i++;

  if (clave == raiz->claves[i]) return raiz;

  return buscar(raiz->hijos[i], clave);
}
```
**Ejemplo de un Arbol B+**  
![Ejemplo Arbol+](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQvOit-vlTXOW_AiIs8bSbpUQx7Gvh0iSu6VESWMFNxg&s)  
**Estructura de un Nodo (Arbol B+)**
```
struct Nodo {
  int claves[m - 1];  // Array de claves
  int n;            // Número de claves almacenadas
  Nodo* hijos[m];   // Array de punteros a nodos hijos
  bool es_hoja;     // Indica si es un nodo hoja
  Nodo* enlaceHermano // (Si es hoja) Puede ser que tenga enlace al hermano a derecha
};
```
**Funcion de Busqueda (Arbol B+)**
```
function buscar(raiz, clave):
  if raiz == NULL:
        return NULL
  nodo_actual = raiz
  while not nodo_actual.es_hoja:
        i = 0
        while i < nodo_actual.n and clave >= nodo_actual.claves[i]:
             i = i + 1
        if i == nodo_actual.n and nodo_actual.enlaceHermano != NULL:
             nodo_actual = nodo_actual.enlaceHermano
        else:
             nodo_actual = nodo_actual.hijos[i]
  i = 0
  while i < nodo_actual.n and clave > nodo_actual.claves[i]:
     i = i + 1
  if i < nodo_actual.n and clave == nodo_actual.claves[i]:
     return nodo_actual
  return NULL
}
```
**Ejemplo de un Arbol B***  
![Ejemplo de Arbol B*](https://i.ytimg.com/vi/kbbHTXvylqY/hq720.jpg?sqp=-oaymwE7CK4FEIIDSFryq4qpAy0IARUAAAAAGAElAADIQj0AgKJD8AEB-AHUBoAC4AOKAgwIABABGH8gQCgTMA8=&rs=AOn4CLC37vmvD8JAzI8n71X1QycGrwOYXQ)  
**Estructura de un Nodo (Arbol B***)
```
struct Nodo {
  int claves[m - 1]; // Array de claves
  int n;           // Número de claves almacenadas
  Nodo* hijos[m];   // Array de punteros a nodos hijos (puede tener punteros nulos)
  bool es_hoja;     // Indica si es un nodo hoja
  Nodo* enlaceHermano // (Si es hoja) Puede ser que tenga enlace al hermano a derecha
  int nClavesMin;   // Número mínimo de claves permitido (porcentaje del tamaño del array)
  int nClavesMax;   // Número máximo de claves permitido (porcentaje del tamaño del array)
  Nodo* padre;     // Puntero al nodo padre (NULL para la raíz)
}
```
**Funcion de Busqueda (Arbol B***)
```
function buscar(raiz, clave):
  nodo_actual = raiz;
  while not nodo_actual.es_hoja:
    i = 0;
    while i < nodo_actual.n and clave >= nodo_actual.claves[i]:
      i = i + 1
    nodo_actual = nodo_actual.hijos[i]
  i = 0;
  while i < nodo_actual.n and clave > nodo_actual.claves[i]:
    i = i + 1
  if i < nodo_actual.n and clave == nodo_actual.claves[i]:
    return nodo_actual
  return NULL
```

### Indices en Bases de Datos
***
En Proceso...
***
## Bibliografia
https://es.wikipedia.org/wiki/%C3%81rbol-B
https://es.wikipedia.org/wiki/%C3%81rbol-B*
https://es.wikipedia.org/wiki/%C3%81rbol_B%2B
https://www.apinem.com/arboles-programacion/
https://es.wikipedia.org/wiki/%C3%81rbol_binario_indexado
https://www.adesso.es/es/noticias/blog/indices-de-bases-de-datos-la-clave-para-la-optimizacion-del-rendimiento.jsp
https://www.youtube.com/watch?v=E3r4maNRReo
