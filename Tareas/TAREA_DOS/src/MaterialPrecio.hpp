#pragma once

#include <vector>
#include "MaterialLectura.h"
#include "MaterialAudiovisual.h"

class MaterialPrecio : public MaterialLectura, public MaterialAudiovisual {
public:
    MaterialPrecio(std::string t, std::string ty, float p);

    bool operator<(const MaterialPrecio& otroMaterial) const;
    void ordenarAscendente(std::vector<MaterialPrecio>& materiales) const;
    void ordenarDescendente(std::vector<MaterialPrecio>& materiales) const;
};