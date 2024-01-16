#ifndef BIBLIOTECA_HPP
#define BIBLIOTECA_HPP

#include <vector>
#include "libro.cpp"

class Biblioteca {
    public:
        void agregarLibro(
            const std::string& titulo,
            const std::string& autor
        );
        void mostrarCatalogo();
    private:
        std::vector<Libro> catalogo;
};

#endif