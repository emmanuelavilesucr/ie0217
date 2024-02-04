# Parte Teorica:

## Iteradores:

**1. ¿Que es un iterador en Python y cual es su proposito?**

- **Un iterador** es una herramienta considerada como un objeto, la cual implementa metodos magicos para iterar sobre un conjunto. Su proposito principal es el acceso de forma secuencial sobre un conjunto de elementos que pueden ser: tuplas o listas.

<br>

**2. Explica la diferencia entre un iterable y un iterador.**

- La principal diferencia entre un **iterable** y un **iterador** es que un **iterable** es el objecto el cual es iterado, mientras que que el **iterador** es el objeto que lleva la **iteracion** del **iterable.** 

<br>
<br>


## Excepciones:

**1. Define que es una excepcion en Python.**

- **Las excepciones** son una herramienta utilizada para el manejo de error en la ejecucion del codigo. 

<br>

**2. ¿Cual es el proposito de la clausula try...except en el manejo de excepciones?**

- Son utilizadas para evitar el colapso del programa en el surgimineto de errores inesperados. El bloque **try** posee el codigo que normalmente debe ser ejecutado pero que puede contener errores en su ejecucion, mientras que el bloque **except** contiene el manejo del error del bloque **try.** 

<br>

**3. Explica la diferencia entre las clausulas except y finally en el manejo de excepciones.**

- La clausula **Except** maneja los errores ocurridos dentro del bloque **try**, mientras que la clausula **finally** define un codigo que se ejecutara sin importar si se produjo un error durante la ejecucion del programa.   

<br>
<br>


## Generadores:

**1. ¿Que es un generador en Python y cual es su ventaja sobre las listas tradicionales?**

- **Los generadores** son estructuras las cuales son utilizadas en la generacion de secuencias de valores paso por paso(Es similar a una lista). La principal ventaja de los **generadores** en comparacion con las **lista** es que los **generadores** poseen una mayor eficiencia en el uso de la memoria lo que se traduce en un mejor rendimiento computacional.

<br>

**2. Explica como se puede crear un generador usando la funcion yield.**

- Primeramente se llama a la funcion generadora, posteriormente se obtiene un objeto generador que puede ser iterado. Finalmente, la funcion se pausa en cada declaración yield, permitiendo la generacion de valores uno a uno. 

<br>

**3. ¿Cuando es mas apropiado usar generadores en lugar de listas?**

- Principalmente es mas apropiado usar **generadores** en contextos en los que se necesita tarabajar con grandes conjuntos de datos, dado a la eficiencia en el uso de la memoria de los **generadores.**

<br>
<br>

 
## Pandas:

**1.¿Cual es la diferencia entre una Serie y un DataFrame en Pandas?**

- **Una Serie** es una estructura que representa una columna de datos, mientras que un **DataFrame** es una estructura que representa una tabla completa con filas y columnas.

<br>

**2. Explica como manejar valores nulos o faltantes en un DataFrame.**

- El manejo de valores nulos implica la identificacion de celdas con datos faltantes. Primeramente, se utiliza metodos para localizar celdas vacias, para posteriormente eliminar filas o columnas vacias. Por ultimo, mediante un metodo se rellenan los valores nulos.

<br>

**3. ¿Cual es la diferencia entre loc y iloc en Pandas?**

- **loc** se utiliza para seleccionar etiquetas de columnas, mientras que **iloc** se utiliza para seleccionar a traves indices.

<br>
<br>


# Bibliografia:

[1] https://devdocs.io/python~3.11-asynchronous-i-o/

[2] https://docs.python.org/es/3/

[3] https://www.freecodecamp.org/espanol/news/el-manual-de-python/

[4] https://tutorial.recursospython.com/ 

