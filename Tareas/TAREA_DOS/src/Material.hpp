#pragma once

#include <string>

class Material {
public:
    std::string titulo;
    std::string grupo;
    std::string autor;
    std::string tipo;
    std::string genero;
    std::string estado;
    float precio;

    Material(std::string t, std::string g, std::string a, std::string ty, std::string gen, std::string est, float p);
    virtual ~Material() {}

    virtual void imprimirInformacion() const;
};

