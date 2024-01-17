# Parte Teórica:

## 1. Conceptos Fundamentales

La programación orientada a objetos (OOP) es un paradigma de programación que organiza el código alrededor de objetos, que son instancias de clases. Sus principios fundamentales son:

- **Abstracción:** Representación de características esenciales sin incluir detalles innecesarios.
- **Encapsulamiento:** Ocultamiento de los detalles internos de un objeto y exposición de una interfaz.
- **Herencia:** Reutilización de código permitiendo que una clase herede propiedades y métodos de otra.
- **Polimorfismo:** Capacidad de un objeto para tomar muchas formas, permitiendo la implementación de un comportamiento de varias maneras.

## 2. Herencia

La herencia en OOP permite que una clase adquiera propiedades y métodos de otra. 

Ejemplo:

```cpp
class Animal {
public:
    void comer() {
        cout << "El animal come." << endl;
    }
};

class Perro : public Animal {
public:
    void ladrar() {
        cout << "El perro ladra." << endl;
    }
};

Perro miPerro;
miPerro.comer(); // Hereda el método comer de la clase Animal
miPerro.ladrar(); // Método específico de la clase Perro

```

## 3. Encapsulamiento:

El encapsulamiento es el ocultamiento de los detalles internos de una clase, permitiendo el acceso controlado a través de interfaces. Protege la integridad de los datos y promueve la modularidad. 

Ejemplo:

```cpp
class CuentaBancaria {
private:
    float saldo;

public:
    void setSaldo(float nuevoSaldo) {
        saldo = nuevoSaldo;
    }

    float getSaldo() {
        return saldo;
    }
};

```

## 4. Polimorfismo:
El polimorfismo permite que objetos de diferentes clases se comporten de manera uniforme. Existen dos tipos: polimorfismo de tipo (sobrecarga y sobreescritura) y polimorfismo de operador.

Ejemplo:

```cpp
// Polimorfismo de tipo (sobreescritura)
class Forma {
public:
    virtual void dibujar() {
        // código
    }
};

class Circulo : public Forma {
public:
    void dibujar() override {
        // código
    }
};

```

## 5. Abstracción:
La abstracción simplifica sistemas complejos modelando clases esenciales y omitiendo detalles innecesarios.

Ejemplo:

```cpp
class Vehiculo {
public:
    virtual void conducir() = 0;  // Método abstracto
};

class Automovil : public Vehiculo {
public:
    void conducir() override {
        // código
    }
};
```

## 6. Clases y Objetos:
Una clase es un plano para crear objetos.
Un objeto es una instancia concreta de una clase.

Ejemplo:

```cpp
class Coche {
    // Definición de la clase Coche
};

Coche miCoche;  // Creación de un objeto Coche
```


## 7. Métodos Virtuales
Los métodos virtuales en C++ son importantes para lograr el polimorfismo. Se utilizan para permitir que las clases derivadas implementen sus propias versiones de los métodos de la clase base. Ejemplo:

```cpp
class Animal {
public:
    virtual void hacerSonido() {
        cout << "Haciendo ruido genérico..." << endl;
    }
};

class Perro : public Animal {
public:
    void hacerSonido() override {
        cout << "¡Guau!" << endl;
    }
};

```

## 8. Constructores y Destructores
Constructor: Inicializa los objetos de una clase. Se llama automáticamente al crear un objeto.

Destructor: Libera los recursos asignados a un objeto. Se llama automáticamente al destruir un objeto. Ejemplo:

```cpp
class MiClase {
public:
    MiClase() {
        // Constructor
    }

    ~MiClase() {
        // Destructor
    }
};

```

## 9. Sobrecarga de Operadores
La sobrecarga de operadores permite definir comportamientos específicos para operadores. Ejemplo:

```cpp

class Punto {
public:
    int x, y;

    Punto operator+(const Punto& otro) {
        Punto resultado;
        resultado.x = this->x + otro.x;
        resultado.y = this->y + otro.y;
        return resultado;
    }
};

```

## 10. Templates
Los templates en C++ permiten crear funciones o clases que pueden trabajar con diferentes tipos de datos. Útil para la reutilización de código. Ejemplo:

```cpp
template <typename T>
T suma(T a, T b) {
    return a + b;
}
```

## 11. Memoria Dinámica en C++
La memoria dinámica en C++ se gestiona con new y delete. Se utiliza comúnmente para asignar y liberar memoria durante la ejecución del programa.

## 12. Diferencia entre new y malloc en C++
new y malloc se utilizan para asignar memoria dinámica. La principal diferencia radica en que new también llama al constructor del objeto, mientras que malloc solo asigna memoria.

## 13. Fuga de Memoria (Memory Leak)
Una fuga de memoria ocurre cuando un programa no libera correctamente la memoria asignada dinámicamente. Puede evitarse utilizando delete o delete[] adecuadamente.

## 14. Punteros Inteligentes (Smart Pointers)
Los punteros inteligentes son objetos que actúan como punteros, pero gestionan automáticamente la memoria. Ejemplos en C++ son std::shared_ptr, std::unique_ptr, y std::weak_ptr.

## 15. Diferencia entre delete y delete[] en C++
delete: Se utiliza para liberar la memoria asignada para un solo objeto.
delete[]: Se utiliza para liberar la memoria asignada para un array de objetos.
## 16. Algoritmos de Ordenamiento
Los algoritmos de ordenamiento son importantes para organizar datos. Permiten ordenar elementos en un orden específico, facilitando la búsqueda y manipulación.

## 17. Algoritmo de Ordenamiento "Bubble Sort"
El Bubble Sort compara elementos adyacentes y los intercambia si están en el orden incorrecto. Repite este proceso hasta que la lista esté ordenada. Su complejidad temporal en el peor caso es O(n^2).

## 18. Algoritmo de Ordenamiento "QuickSort"
QuickSort utiliza la estrategia de dividir y conquistar. Su ventaja principal es su eficiencia, especialmente en grandes conjuntos de datos, con una complejidad temporal promedio de O(n log n).

## 19. Diferencia entre Ordenamiento Estable e Inestable
Un algoritmo de ordenamiento estable mantiene el orden relativo de elementos iguales, mientras que uno inestable no garantiza este orden.

## 20. Algoritmo de Ordenamiento "Merge Sort"
Merge Sort divide la lista en mitades, ordena cada mitad y luego fusiona las mitades ordenadas. Tiene una complejidad temporal de O(n log n) y es preferible para grandes conjuntos de datos y listas enlazadas.
