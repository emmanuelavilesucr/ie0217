#include <iostream>
#include <vector>
#include <complex>
#include <stdexcept>
#include <typeinfo>



template <typename T>
class Matriz {
private:
    std::vector<std::vector<T>> matriz;

    /**
     * @brief Constructor de la clase Matriz.
     * @param filas Numero de filas de la matriz.
     * @param columnas Numero de columnas de la matriz.
     */

public:
    Matriz(int filas, int columnas) : matriz(filas, std::vector<T>(columnas)) {}

    /**
     * @brief Este metodo se utiliza para ingresar datos en la matriz desde la entrada estandar.
     */

    void pedirDatos() {
        std::cout << "Ingrese el tamaño de la matriz (filas columnas): ";
        int filas, columnas;
        std::cin >> filas >> columnas;

        matriz.resize(filas, std::vector<T>(columnas));

        std::cout << "Ingrese los datos para la matriz:\n";
        for (int i = 0; i < filas; ++i) {
            for (int j = 0; j < columnas; ++j) {
                try {
                    T valor;
                    std::cout << "Ingrese el elemento [" << i+1 << "][" << j+1 << "]: ";
                    std::cin >> valor;
                    matriz[i][j] = valor;
                } catch (const std::invalid_argument &e) {
                    std::cerr << "Error: Tipo de dato no válido. Debe ingresar un valor del tipo " << typeid(T).name() << '\n';
                    throw;
                }
            }
        }
    }

    /**
     * @brief Este metodo se utiliza para obtener el número de filas de la matriz.
     * @return Numero de filas de la matriz.
     */

    int obtenerFilas() const {
        return matriz.size();
    }

    /**
     * @brief Este metodo se utiliza para obtener el numero de columnas de la matriz.
     * @return Numero de columnas de la matriz.
     */

    int obtenerColumnas() const {
        return matriz.empty() ? 0 : matriz[0].size();
    }

    /**
     * @brief Este mtodo se utiliza para obtener el elemento en una posición específica de la matriz.
     * @param fila Fila del elemento.
     * @param columna Columna del elemento.
     * @return Elemento en la posición (fila, columna).
     */

    T obtenerElemento(int fila, int columna) const {
        return matriz.at(fila).at(columna);
    }

    /**
     * @brief Este metodo se utiliza para asignar un valor a un elemento específico de la matriz.
     * @param fila Fila del elemento.
     * @param columna Columna del elemento.
     * @param valor Valor a asignar al elemento.
     */

    void asignarElemento(int fila, int columna, T valor) {
        matriz.at(fila).at(columna) = valor;
    }

    /**
     * @brief Sobrecarga del operador de suma para matrices.
     * @param otraMatriz Matriz a sumar.
     * @return Matriz resultante de la suma.
     */

    Matriz<T> operator+(const Matriz<T> &otraMatriz) const {
        if (this->obtenerFilas() != otraMatriz.obtenerFilas() || this->obtenerColumnas() != otraMatriz.obtenerColumnas()) {
            throw std::invalid_argument("Las matrices deben tener las mismas dimensiones para la suma");
        }

        Matriz<T> resultado(this->obtenerFilas(), this->obtenerColumnas());
        for (int i = 0; i < this->obtenerFilas(); ++i) {
            for (int j = 0; j < this->obtenerColumnas(); ++j) {
                resultado.asignarElemento(i, j, this->obtenerElemento(i, j) + otraMatriz.obtenerElemento(i, j));
            }
        }
        return resultado;
    }

    /**
     * @brief Sobrecarga del operador de resta para matrices.
     * @param otraMatriz Matriz a restar.
     * @return Matriz resultante de la resta.
     */

    Matriz<T> operator-(const Matriz<T> &otraMatriz) const {
        if (this->obtenerFilas() != otraMatriz.obtenerFilas() || this->obtenerColumnas() != otraMatriz.obtenerColumnas()) {
            throw std::invalid_argument("Las matrices deben tener las mismas dimensiones para la resta");
        }

        Matriz<T> resultado(this->obtenerFilas(), this->obtenerColumnas());
        for (int i = 0; i < this->obtenerFilas(); ++i) {
            for (int j = 0; j < this->obtenerColumnas(); ++j) {
                resultado.asignarElemento(i, j, this->obtenerElemento(i, j) - otraMatriz.obtenerElemento(i, j));
            }
        }
        return resultado;
    }

    /**
     * @brief Sobrecarga del operador de multiplicación para matrices.
     * @param otraMatriz Matriz a multiplicar.
     * @return Matriz resultante de la multiplicación.
     */

    Matriz<T> operator*(const Matriz<T> &otraMatriz) const {
        if (this->obtenerColumnas() != otraMatriz.obtenerFilas()) {
            throw std::invalid_argument("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para la multiplicación");
        }

        Matriz<T> resultado(this->obtenerFilas(), otraMatriz.obtenerColumnas());
        for (int i = 0; i < this->obtenerFilas(); ++i) {
            for (int j = 0; j < otraMatriz.obtenerColumnas(); ++j) {
                T sum = 0;
                for (int k = 0; k < this->obtenerColumnas(); ++k) {
                    sum += this->obtenerElemento(i, k) * otraMatriz.obtenerElemento(k, j);
                }
                resultado.asignarElemento(i, j, sum);
            }
        }
        return resultado;
    }

    /**
     * @brief Sobrecarga del operador de salida para imprimir la matriz.
     * @param os Flujo de salida.
     * @param matriz Matriz a imprimir.
     * @return Flujo de salida modificado.
     */

    friend std::ostream &operator<<(std::ostream &os, const Matriz<T> &matriz) {
        for (const auto &fila : matriz.matriz) {
            for (const auto &elemento : fila) {
                os << elemento << ' ';
            }
            os << '\n';
        }
        return os;
    }
};

template <typename T>
class OperacionesBasicas {
public:

    /**
     * @brief Este metodo se utiliza para validar la compatibilidad de matrices en una operacion.
     * @param matriz1 Primera matriz.
     * @param matriz2 Segunda matriz.
     * @param operacion Tipo de operacion a realizar (suma, resta, multiplicacion).
     */

    static void validar(const Matriz<T> &matriz1, const Matriz<T> &matriz2, const std::string &operacion) {
        if (typeid(T) != typeid(float)) {
            throw std::invalid_argument("Las matrices deben tener el mismo tipo de datos");
        }

        if (operacion == "suma" || operacion == "resta") {
            if (matriz1.obtenerFilas() != matriz2.obtenerFilas() || matriz1.obtenerColumnas() != matriz2.obtenerColumnas()) {
                throw std::invalid_argument("Las matrices deben tener las mismas dimensiones para suma/resta");
            }
        } else if (operacion == "multiplicacion") {
            if (matriz1.obtenerColumnas() != matriz2.obtenerFilas()) {
                throw std::invalid_argument("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para multiplicación");
            }
        } else {
            throw std::invalid_argument("Operación no válida");
        }
    }

    /**
     * @brief Este metodo se utiliza para realizar la suma de dos matrices.
     * @param matriz1 Primera matriz.
     * @param matriz2 Segunda matriz.
     * @return Matriz resultante de la suma.
     */

    static Matriz<T> suma(const Matriz<T> &matriz1, const Matriz<T> &matriz2) {
        validar(matriz1, matriz2, "suma");
        return matriz1 + matriz2;
    }

    /**
     * @brief Este metodo se utiliza para realizar la resta de dos matrices.
     * @param matriz1 Primera matriz.
     * @param matriz2 Segunda matriz.
     * @return Matriz resultante de la resta.
     */

    static Matriz<T> resta(const Matriz<T> &matriz1, const Matriz<T> &matriz2) {
        validar(matriz1, matriz2, "resta");
        return matriz1 - matriz2;
    }

    /**
     * @brief Este metodo se utiliza para realizar la multiplicacion de dos matrices.
     * @param matriz1 Primera matriz.
     * @param matriz2 Segunda matriz.
     * @return Matriz resultante de la multiplicacion.
     */

    static Matriz<T> multiplicacion(const Matriz<T> &matriz1, const Matriz<T> &matriz2) {
        validar(matriz1, matriz2, "multiplicacion");
        return matriz1 * matriz2;
    }
};


template <typename T>
class OperacionesComplejas {
public:

    /**
     * @brief Este metodo se utiliza para realizar operaciones complejas en matrices de numeros complejos.
     * @param matriz1 Primera matriz de numeros complejos.
     * @param matriz2 Segunda matriz de numeros complejos.
     * @param operacion Tipo de operacion a realizar (suma, resta, multiplicacion).
     * @return Matriz resultante de la operacion compleja.
     */

    static Matriz<std::complex<T>> operacionesComplejas(const Matriz<std::complex<T>> &matriz1, const Matriz<std::complex<T>> &matriz2, const std::string &operacion) {
        Matriz<std::complex<T>> resultado(matriz1.obtenerFilas(), matriz1.obtenerColumnas());

        for (int i = 0; i < matriz1.obtenerFilas(); ++i) {
            for (int j = 0; j < matriz1.obtenerColumnas(); ++j) {
                if (operacion == "suma") {
                    resultado.asignarElemento(i, j, matriz1.obtenerElemento(i, j) + matriz2.obtenerElemento(i, j));
                } else if (operacion == "resta") {
                    resultado.asignarElemento(i, j, matriz1.obtenerElemento(i, j) - matriz2.obtenerElemento(i, j));
                } else if (operacion == "multiplicacion") {
                    resultado.asignarElemento(i, j, matriz1.obtenerElemento(i, j) * matriz2.obtenerElemento(i, j));
                } else {
                    throw std::invalid_argument("Operación no válida");
                }
            }
        }

        return resultado;
    }
};

/**
 * @brief Clase para imprimir matrices y sus resultados en la salida estandar.
 */

class ImpresionMatrices {
public:

    /**
     * @brief Este metodo se utiliza para imprimir matrices y resultados.
     * @tparam T Tipo de datos de los elementos de las matrices.
     * @param matriz1 Primera matriz.
     * @param matriz2 Segunda matriz.
     * @param resultado Resultado de la operación.
     * @param operacion Tipo de operación realizada.
     */

    template <typename T>
    static void imprimirMatrices(const Matriz<T> &matriz1, const Matriz<T> &matriz2, const Matriz<T> &resultado, const std::string &operacion) {
        std::cout << "Matriz 1:\n"
                  << matriz1;
        std::cout << "Matriz 2:\n"
                  << matriz2;
        std::cout << "Operación: " << operacion << '\n';
        std::cout << "Resultado:\n"
                  << resultado;
    }
};

/**
 * @brief Función principal del programa.
 * @return Codigo de salida del programa.
 */

int main() {
    try {
         
        Matriz<float> matriz1(0, 0);
        Matriz<float> matriz2(0, 0);
        
        std::cout << "Ingrese los datos para la primera matriz:\n";
        matriz1.pedirDatos();

        std::cout << "Ingrese los datos para la segunda matriz:\n";
        matriz2.pedirDatos();
        
        std::cout << "Seleccione la operación a realizar (suma, resta, multiplicacion): ";
        std::string operacion;
        std::cin >> operacion;
        
        if (operacion == "suma") {
            OperacionesBasicas<float>::validar(matriz1, matriz2, "suma");
            Matriz<float> resultado = OperacionesBasicas<float>::suma(matriz1, matriz2);
            ImpresionMatrices::imprimirMatrices(matriz1, matriz2, resultado, "suma");
        } else if (operacion == "resta") {
            OperacionesBasicas<float>::validar(matriz1, matriz2, "resta");
            Matriz<float> resultado = OperacionesBasicas<float>::resta(matriz1, matriz2);
            ImpresionMatrices::imprimirMatrices(matriz1, matriz2, resultado, "resta");
        } else if (operacion == "multiplicacion") {
            OperacionesBasicas<float>::validar(matriz1, matriz2, "multiplicacion");
            Matriz<float> resultado = OperacionesBasicas<float>::multiplicacion(matriz1, matriz2);
            ImpresionMatrices::imprimirMatrices(matriz1, matriz2, resultado, "multiplicacion");
        } else {
            std::cerr << "Error: Operación no válida.\n";
            return 1;
        }

    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << '\n';
        return 1;
    }

    return 0;
}
