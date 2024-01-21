#include "Matriz.hpp"
#include <iostream>

template <typename T>
Matriz<T>::Matriz() : filas(0), columnas(0) {}

template <typename T>
Matriz<T>::Matriz(int filas, int columnas) : filas(filas), columnas(columnas) {
    datos.resize(filas, std::vector<T>(columnas));
}

template <typename T>
void Matriz<T>::pedirDatos() {

}

template <typename T>
void Matriz<T>::imprimirMatriz() const {

}

template <typename T>
Matriz<T> Matriz<T>::operator+(const Matriz<T>& otra) const {

}

template <typename T>
Matriz<T> Matriz<T>::operator-(const Matriz<T>& otra) const {

}

template <typename T>
Matriz<T> Matriz<T>::operator*(const Matriz<T>& otra) const {

}