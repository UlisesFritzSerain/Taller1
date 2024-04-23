# Ejercicio 2

### Arboles en Archivos Indexados
***
### Arboles B
Son estructuras de datos de busqueda que estan diseñadas para mantener datos ordenados y permitir operaciones de busqueda eficientes. Especialmente diseñados para ser utilizados en sistemas de almacenamiento de base de datos y sistemas de archivos, donde el acceso rapido a los datos es esencial.
La idea de los Arboles B es que los nodos internos deben tener un numero variable de nodos hijo dentro de un rango predefinido. Cuando se inserta o se elimina un dato de la estructura, la cantidad de nodos hijo varia dentro de un nodo. Para que siga manteniendose el numero de nodos dentro del rango predefinido, los nodos internos se juntan o se parten.  
**Caracteristicas:** Son eficientes en busqueda, insercion y eliminacion de datos. mantiene un factor de equilibrio para asegurar tiempos de busqueda predecibles, ademas de que cada nodo contiene informacion sobre el rango de claves que abarca y como llegar a los nodos hijos.  
**Variantes:** Arboles B+ / Arboles B*

**Ejemplo de un Arbol B**  
![Ejemplo ArbolB](https://www.apinem.com/wp-content/uploads/2024/02/arbol-b-ejemplo.png)  
**Estructura de un Nodo (Arbol B)**
```
struct Nodo {
      int claves[m - 1];  // Array de claves
      int n;            // Numero de claves almacenadas
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
  int n;            // Numero de claves almacenadas
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
  int n;           // Numero de claves almacenadas
  Nodo* hijos[m];   // Array de punteros a nodos hijos (puede tener punteros nulos)
  bool es_hoja;     // Indica si es un nodo hoja
  Nodo* enlaceHermano // (Si es hoja) Puede ser que tenga enlace al hermano a derecha
  int nClavesMin;   // Numero minimo de claves permitido (porcentaje del tamaño del array)
  int nClavesMax;   // Numero maximo de claves permitido (porcentaje del tamaño del array)
  Nodo* padre;     // Puntero al nodo padre (NULL para la raiz)
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
### Indice B TREE (Arbol B)

Como anteriormente dijimos, este tipo de indice tiene una estructura de indice jerarquica para busquedas rapidas y eficientes, especialmente en conjuntos de datos grandes. Tiene una estructura de datos en forma de arbol, busquedas eficientes de rangos, prefijos y valores exactos. Tambien es altamente escalable y eficiente para conjuntos de datos grandes y soporta ordenamiento natural de las claves.  
Sigue presentando las **variantes** de: Indice B+Tree y Indice B*Tree  

**Ejemplo de Tablas con Indice B TREE**  
![Tablas B TREE](https://static1.squarespace.com/static/53528f90e4b0768cad09d33b/53c6505be4b0b16e59d8552b/5513c203e4b0e200574cca3c/1427358552743/11.png?format=1500w)  
**Implementacion en Base de Datos (Lenguaje PostgreSQL)**
```
CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(255),
  email VARCHAR(255),
  direccion VARCHAR(255)
);
CREATE INDEX clientes_nombre_idx ON clientes USING btree (name);
```
### Indice Hash

Un Indice Hash es una estructura de datos avanzada que se utiliza en el campo de las bases de datos y sirve como mecanismo de busqueda para localizar registros de datos basandose en una clave hash unica, que se genera a partir de la clave principal del registro u otros atributos de identificacion.  
El objetivo principal de un indice hash es proporcionar una forma rapida y eficiente de buscar y acceder a datos en grandes bases de datos, donde los algoritmos de busqueda lineal serian ineficientes y consumirian mucho tiempo.
En cuanto a sus **variantes**: Puede ser de **Hash abierto**: Almacena valores en una tabla con listas enlazadas; o de **Hash cerrado**: Almacena valores directamente en la tabla, ya que tiene limitaciones.  

**Ejemplo de Tablas con Indice Hash**  
![Tablas Hash](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Tabla_hash2.png/350px-Tabla_hash2.png)  
**Implementacion en Base de Datos (PostgreSQL)**
```
CREATE TABLE productos (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  nombre_producto VARCHAR(255) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  categoria VARCHAR(50) NOT NULL
);
CREATE INDEX idx_producto_categoria ON productos USING HASH (categoria);
```

### Indice Invertido

Un indice invertido es una forma de estructurar la informacion que va a ser recuperada por un motor de busqueda. Por tanto, el objetivo es crear la estructura de datos para llevar a cabo una busqueda de texto completa. En un indice invertido, el buscador crea los indices, o terminos de busqueda, a partir de una serie de documentos, indicando el o los documentos que los contienen.  
De esta manera, cuando el usuario teclea un termino de busqueda determinado, el buscador le indica los documentos que contienen dicho termino.  

**Ejemplo de Tabla con Indice Invertido**  
![Tabla Indice Invertido](https://i.ytimg.com/vi/TvHv2UZvx74/maxresdefault.jpg)  
**Implementacion en Base de Datos (PostgreSQL)**
```
CREATE TABLE documentos (
  id_documento INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(255) NOT NULL,
  contenido TEXT NOT NULL
);
CREATE INDEX idx_palabras_documento USING gin ON documentos USING gin(contenido);
```
***
## Bibliografia
https://es.wikipedia.org/wiki/%C3%81rbol-B  
https://es.wikipedia.org/wiki/%C3%81rbol-B*  
https://es.wikipedia.org/wiki/%C3%81rbol_B%2B  
https://www.apinem.com/arboles-programacion/  
https://es.wikipedia.org/wiki/%C3%81rbol_binario_indexado  
https://www.adesso.es/es/noticias/blog/indices-de-bases-de-datos-la-clave-para-la-optimizacion-del-rendimiento.jsp  
https://www.youtube.com/watch?v=E3r4maNRReo  
https://appmaster.io/es/glossary/indice-hash-es  
https://medium.com/@lordmoma/why-using-b-tree-indexing-in-sql-6a3203ed57a5  
https://www.postgresql.org/docs/current/indexes-types.html  
https://es.wikipedia.org/wiki/%C3%8Dndice_invertido  
https://www.postgresql.org/docs/current/gin-intro.html  
https://www.youtube.com/watch?v=MeR7byPjnpI  
