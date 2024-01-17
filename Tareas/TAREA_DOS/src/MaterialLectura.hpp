#pragma once

#include "Material.h"

class MaterialLectura : public Material {
public:
    int hojas;

    MaterialLectura(std::string t, std::string g, std::string a, std::string ty, std::string gen, std::string est, int h, float p);
    virtual ~MaterialLectura() {}

    virtual void imprimirInformacion() const override;
};
