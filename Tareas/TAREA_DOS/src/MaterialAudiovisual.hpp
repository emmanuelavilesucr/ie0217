#pragma once

#include "Material.h"

class MaterialAudiovisual : public Material {
public:
    int duracion;

    MaterialAudiovisual(std::string t, std::string g, std::string a, std::string ty, std::string gen, std::string est, int d, float p);
    virtual ~MaterialAudiovisual() {}

    virtual void imprimirInformacion() const override;
};