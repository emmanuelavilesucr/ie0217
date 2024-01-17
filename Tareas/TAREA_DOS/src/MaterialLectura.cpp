#include "MaterialLectura.h"

MaterialLectura::MaterialLectura(std::string t, std::string g, std::string a, std::string ty, std::string gen, std::string est, int h, float p)
    : Material(t, g, a, ty, gen, est, p), hojas(h) {}

void MaterialLectura::imprimirInformacion() const {
    // Codigo
}