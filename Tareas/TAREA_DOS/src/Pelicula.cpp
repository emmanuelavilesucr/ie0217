#include "Pelicula.h"

Pelicula::Pelicula(std::string t, std::string a, std::string gen, std::string est, int d, float p, std::string r, std::string mr)
    : MaterialAudiovisual(t, "audiovisual", a, "película", gen, est, d, p), resumen(r), materialRelacionado(mr) {}

void Pelicula::imprimirInformacion() const {
    // Codigo
}

std::string Pelicula::longitudPelicula() const {
    // Codigo
}
