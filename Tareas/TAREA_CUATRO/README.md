# Parte Teorica:
<br>

## 1. Explique la diferencia entre una lista y una tupla en Python.

- Las **listas** son mutables, lo que sigunifica que permite modificar sus elementos después de la creación. Por otro lado, las **tuplas** son inmutables, lo que significa que sus elementos no pueden ser modificados después su creación.

<br>

## 2. ¿Que es la sobrecarga de operadores en Python y como se implementa?

- La sobrecarga de operadores es capacidad de definir el comportamiento de los operadores en clases personalizadas. Se implementa mediante métodos, como por ejemplo: **__add__** para la suma.

<br>

## 3. Explique el concepto de .alcanzabilidad”(scope) de una variable en Python.

- Es la visibilidad de una variable en diferentes partes del código.Variables definidas dentro de una función tienen un alcance **local** y  fuera de funciones, tienen un alcance **global**.

<br>

## 4. ¿Que es un decorador en Python y cual es su funcion principal?

- Es una función que envuelve a otra función para extender o modificar su comportamiento y se caracteriza por utilizar el símbolo @ antes de la definición de la funcion. Su principal función es la de reutilizar las funcionalidades sin modificar directamente el código fuente.

<br>


## 5. ¿Como se gestionan las excepciones en Python? Proporcione ejemplos de uso de bloques try, except y finally.

- Los bloques **try**, **except**, y opcionalmente **finally** son utilizados en el manejo de excepciones.

Ejemplo:

```py
try:
    # Codigo
except TipoDeExcepcion as e:
finally:
    # Codigo que se ejecuta siempre
```

<br>

## 6. ¿Que son los generadores en Python y para que se utilizan?

- Son funciones que utilizan la palabra clave yield para producir un valor y ahorrar memoria, ya que generan valores sobre la marcha en lugar de almacenar una lista completa en memoria. Por otro lado, se utilizan para iterar sobre grandes conjuntos de datos.

<br>

## 7. Explique la diferencia entre init y call en clases de Python.

- El metodo **__init__** se utiliza para llamar al instanciar un objeto, lo que significa que inicializa los atributos de la instancia. Mientras que el metodo **__call__** se utiliza para permitir que la instancia sea llamada como una función.

<br>

## 8. ¿Como se organizan los modulos y paquetes en Python? 

- Los modulos se organizan mediante archivos individuales con funciones y clases, mientras que los paquetes se organizan mediante carpetas que contienen modulos. Por otro lado, **__init__.py** es un archivo que se utiliza para indicar que un directorio debe ser tratado como un paquete.

<br>

## 9. Explique la diferencia entre metodos append() e extend() en listas de Python.

- El modulo **append()** agrega un elemento al final de la lista, mientras que el modulo **extend()** extiende la lista con los elementos de otro iterable.

<br>

## 10. ¿Cual es la diferencia entre un metodo de clase y un metodo estatico en Python?

- El **método de clase** recibe la clase como primer argumento y puede acceder a atributos de clase. Por otro lado, el **método estático** no recibe la instancia o la clase como primer argumento y generalmente se utiliza para funciones independientes de la instancia o la clase.

<br>

## 11. Hable sobre las diferencias entre herencia simple y herencia multiple en Python.

- La **Herencia simple** es cuando una clase hereda de una única clase base. La **Herencia múltiple**  es cuando una clase hereda de múltiples clases base.

<br>

## 12. ¿Como se manejan los errores de importacion de modulos en Python?

- Para gestionar errores de importación en Python, se utiliza un bloque try y except para capturar la excepción ImportError. Si el módulo no puede ser importado, se ejecuta el código dentro del bloque except, permitiendo manejar la situación de manera controlada, como imprimir un mensaje de error o tomar acciones específicas. Esto evita que el programa se detenga por completo debido a un problema en la importación de un módulo.

<br>

## 13. ¿Cual es la diferencia entre una clase y un objeto en Python?

-  Las **Clases** son plantillas para crear objetos. Por otro lado, los **Objetos** son instancias específica de una clase.

<br>

## 14. Hable sobre la diferencia entre una clase abstracta y una interfaz en Python.

- **Una clase abstracta** puede tener métodos con y sin implementación, mientras que una **interfaz** solo puede tener métodos sin implementación. La distinción entre ambas es menos rígida en Python, donde la relevancia se centra en el comportamiento de los objetos más que en su tipo específico. Por otro lado, ambas se definen con el módulo abc y se utilizan para establecer requisitos en las clases que las implementan.

<br>

## 15. Explique el concepto de sobreescritura de metodos en Python y como se realiza.

- **La sobreescritura** se refiere a la capacidad de una subclase para proporcionar una implementación específica de un método que ya está definido en su clase base. Se realiza definiendo un método con el mismo nombre en la subclase.

<br>
<br>

# Bibliografia: 

[1] https://docs.python.org/es/3/
[2] https://pyspanishdoc.sourceforge.net/
[3] https://www.freecodecamp.org/espanol/news/el-manual-de-python/
[4] https://campbell-muscle-lab.github.io/howtos_Python/pages/documentation/generating_doxygen_documenation/doxygen_example.html 
[5] https://devdocs.io/python~3.11/library/array 

