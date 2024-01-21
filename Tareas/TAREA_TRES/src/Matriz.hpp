#ifndef MATRIZ_HPP
#define MATRIZ_HPP
#include <vector>

template <typename T>

class Matriz {

    private:
        std::vector<std::vector<T>> datos;
        int filas, columnas;

    public:
        Matriz();
        Matriz(int filas, int columnas);
        void pedirDatos();
        void imprimirMatriz() const;
        
    Matriz<T> operator+(const Matriz<T>& otra) const;
    Matriz<T> operator-(const Matriz<T>& otra) const;
    Matriz<T> operator*(const Matriz<T>& otra) const;


};

#endif