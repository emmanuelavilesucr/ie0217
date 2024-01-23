# Parte Teorica:

<br>
<br>


# Templates:

## 1. Definición de Templates:

Los templates son una característica que permite la creación de código, permitiendo definir funciones o clases sin especificar el tipo de datos con el que se trabajara.

Ejemplo:

```cpp
template <typename T>
T suma(T a, T b) {
    return a + b;
}

int main() {
    int resultado = suma(5, 7);
}
```

## 2. Sobrecarga de Plantillas:

La sobrecarga de funciones se realiza definiendo múltiples versiones de la función con distintos tipos de parámetros.


## 3. Plantillas de Clases:

Las plantillas se pueden utilizar en la definición de clases que puedan manejar diferentes tipos de datos, lo que permite escribir código que es independiente del tipo de datos con el que se trabajara en la clase. 

<br>
<br>

# Excepciones:

## 4. Manejo de Excepciones:

- **try:** Se utiliza para encapsular el código que podría generar una excepción. Si ocurre una excepción dentro del bloque try, el control se transfiere al bloque catch correspondiente.

- **catch:** Se ejecuta cuando ocurre una excepción dentro del bloque try. Puede haber varios bloques catch para manejar diferentes tipos de excepciones.

- **throw:** Se utiliza para lanzar una excepción. Puede lanzar cualquier tipo de objeto, aunque generalmente se lanza un objeto de una clase derivada.

## 5. Excepciones Estándar:

- **std::runtime_error:** Indica errores que solo pueden determinarse durante la ejecución del programa y generalmente indica situaciones excepcionales que no pueden manejarse fácilmente en tiempo de compilación.

```cpp
void funcionEjemplo() {
    throw std::runtime_error("Error en funcionEjemplo");
}
```


- **std::invalid_argument:** Se utiliza para indicar que una función ha recibido un argumento que no tiene sentido en el contexto de la operación realizada.

```cpp 
void dividir(int numerador, int denominador) {
    if (denominador == 0) {
        throw std::invalid_argument("Denominador no puede ser cero");
    }
    int resultado = numerador / denominador;
}
```


- **std::out_of_range:** Indica que un índice o valor está fuera del rango válido para la operación realizada, como en el acceso a un elemento de un contenedor fuera de los límites.

```cpp 
std::vector<int> numeros = {1, 2, 3, 4, 5};
try {
    int valor = numeros.at(10); 
}
catch (const std::out_of_range& e) {
    std::cerr << "Excepción atrapada: " << e.what() << std::endl;
}
```

## 6. Política de Manejo de Excepciones:

Una política de manejo de excepciones es una estrategia para manejar errores. Es importante considerarla para garantizar un comportamiento predecible y robusto del programa.

## 7. Noexcept:

**noexcept** especifica que una función no lanzará excepciones.

<br>
<br>

# STL (Standard Template Library):

## 8. Contenedores STL:

- **std::vector:** Se utiliza en situaciones en las que se necesita acceso rápido a elementos mediante índices, y el tamaño del contenedor puede cambiar dinámicamente.

- **std::list:** Es util cuando se requieren operaciones frecuentes de inserción y eliminación en cualquier punto de una secuencia.

- **std::map:** Se utiliza para asociar valores con claves únicas y recuperar rápidamente el valor asociado a una clave específica.

- **std::set:** Es util cuando se necesita mantener una colección ordenada y garantizar la unidad de los elementos.

- **std::queue:** Se utiliza para modelar situaciones donde se sigue el principio "primero en entrar, primero en salir".


## 9. Iteradores en STL:

Los iteradores son objetos que facilitan el acceso secuencial a elementos en contenedores, proporcionando una interfaz uniforme independientemente del tipo específico del contenedor. Su flexibilidad y abstracción hacen que los iteradores sean fundamentales para la escritura de código modular, facilitando la manipulación y recorrido de datos en diversas estructuras de la STL.


## 10. Algoritmos STL:

- **std::copy:** Copia elementos desde un rango de origen a un rango de destino.

Ejemplo:

```cpp 
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> origen = {1, 2, 3, 4, 5};
    std::vector<int> destino(5);

    std::copy(origen.begin(), origen.end(), destino.begin());

    for (const auto& num : destino) {
        std::cout << num << " ";
    }

    return 0;
}
```
- **std::reverse:** Invierte el orden de los elementos en un rango.

Ejemplo:

```cpp 
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> numeros = {1, 2, 3, 4, 5};

    std::reverse(numeros.begin(), numeros.end());

    for (const auto& num : numeros) {
        std::cout << num << " ";
    }

    return 0;
}
```
- **std::transform:** Aplica una operación a cada elemento en un rango y almacena el resultado en otro rango. 

Ejemplo:

```cpp 
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> numeros = {1, 2, 3, 4, 5};
    std::vector<int> cuadrados(5);

    std::transform(numeros.begin(), numeros.end(), cuadrados.begin(), [](int num) {
        return num * num;
    });

    for (const auto& resultado : cuadrados) {
        std::cout << resultado << " ";
    }

    return 0;
}
```


## 11. Algoritmos Personalizados:

Los algoritmos personalizados se pueden integrar de manera armoniosa con los algoritmos estándar de la STL. Se pueden utilizar como argumentos en funciones como std::transform, std::for_each y otros, lo que simplifica el código y mejora la legibilidad.

<br>
<br>

# Expresiones Regulares:

## 12. Definición de Expresiones Regulares:

Las expresiones regulares son patrones de búsqueda que permiten realizar operaciones complejas de coincidencia en cadenas de texto.

Ejemplo: 

```cpp
\d{3}-\d{2}-\d{4}
```

## 13. Caracteres Especiales:

- **^ :** Este carácter se utiliza al principio de una expresión regular para indicar que la coincidencia debe ocurrir al inicio de la cadena de texto. 
- **$ :** Se coloca al final de una expresión regular para indicar que la coincidencia debe ocurrir al final de la cadena de texto.
- **. :** Representa cualquier carácter, excepto el salto de línea. 

## 14. Uso de Expresiones Regulares en C++:

Se puede usar la biblioteca <regex> para trabajar con expresiones regulares.

Ejemplo:

```cpp
std::regex patron("\\d+");  // Busca números
```

## 15. Validación de Patrones:

Las expresiones regulares son útiles para la validación de patrones en cadenas de texto debido a su flexibilidad y poder, dado que permiten especificar reglas detalladas para buscar y validar patrones.