#ifndef LIBRO_HPP
#define LIBRO_HPP

#include <string>

class Libro {
    public:
        Libro(const std::string& titulo, const std::string& autor);
        void mostrarInfo() const;
    private:
        std::string titulo;
        std::string autor;
};

#endif