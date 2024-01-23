#include <iostream>
#include <vector>
#include <complex>
#include <stdexcept>
#include <typeinfo>

template <typename T>
class Matriz {
private:
    std::vector<std::vector<T>> matriz;

public:
    Matriz(int filas, int columnas) : matriz(filas, std::vector<T>(columnas)) {}

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
                    std::cout << "Ingrese el elemento [" << i << "][" << j << "]: ";
                    std::cin >> valor;
                    matriz[i][j] = valor;
                } catch (const std::invalid_argument &e) {
                    std::cerr << "Error: Tipo de dato no válido. Debe ingresar un valor del tipo " << typeid(T).name() << '\n';
                    throw;
                }
            }
        }
    }

    int obtenerFilas() const {
        return matriz.size();
    }

    int obtenerColumnas() const {
        return matriz.empty() ? 0 : matriz[0].size();
    }

    T obtenerElemento(int fila, int columna) const {
        return matriz.at(fila).at(columna);
    }

    void asignarElemento(int fila, int columna, T valor) {
        matriz.at(fila).at(columna) = valor;
    }

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

    static Matriz<T> suma(const Matriz<T> &matriz1, const Matriz<T> &matriz2) {
        validar(matriz1, matriz2, "suma");
        return matriz1 + matriz2;
    }

    static Matriz<T> resta(const Matriz<T> &matriz1, const Matriz<T> &matriz2) {
        validar(matriz1, matriz2, "resta");
        return matriz1 - matriz2;
    }

    static Matriz<T> multiplicacion(const Matriz<T> &matriz1, const Matriz<T> &matriz2) {
        validar(matriz1, matriz2, "multiplicacion");
        return matriz1 * matriz2;
    }
};

template <typename T>
class OperacionesComplejas {
public:
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

class ImpresionMatrices {

};

int main() {



}