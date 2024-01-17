#include "Noticia.h"

Noticia::Noticia(std::string t, std::string a, std::string e, std::string gen, std::string est, int h, float p, std::string r, std::string mr)
    : MaterialLectura(t, "lectura", a, "noticia", gen, est, h, p), resumen(r), materialRelacionado(mr) {}

void Noticia::imprimirInformacion() const {
    // Codigo
}

std::string Noticia::longitudNoticia() const {
    // Codigo
}