
#include "MaterialPrecio.h"

MaterialPrecio::MaterialPrecio(std::string t, std::string ty, float p)
    : MaterialLectura(t, "", ty, "", "", "", 0, p), MaterialAudiovisual(t, "", "", ty, "", "", 0, p) {}

bool MaterialPrecio::operator<(const MaterialPrecio& otroMaterial) const {
    return precio < otroMaterial.precio;
}

void MaterialPrecio::ordenarAscendente(std::vector<MaterialPrecio>& materiales) const {
    std::sort(materiales.begin(), materiales.end());
}

void MaterialPrecio::ordenarDescendente(std::vector<MaterialPrecio>& materiales) const {
    std::sort(materiales.begin(), materiales.end(), std::greater<MaterialPrecio>());
}