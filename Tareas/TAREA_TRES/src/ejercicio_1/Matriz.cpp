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


class OperacionesBasicas {

};


class OperacionesComplejas {

};



int main() {



}