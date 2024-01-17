#include "Libro.h"

Libro::Libro(std::string t, std::string a, std::string e, std::string gen, std::string est, int h, float p, std::string r, std::string mr)
    : MaterialLectura(t, "lectura", a, "libro", gen, est, h, p), resumen(r), materialRelacionado(mr) {}

void Libro::imprimirInformacion() const {
    // Codigo
}

std::string Libro::longitudLibro() const {
    // Codigo
}