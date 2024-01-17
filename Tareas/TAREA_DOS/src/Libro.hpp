#pragma once

#include "MaterialLectura.h"

class Libro : public MaterialLectura {
public:
    std::string resumen;
    std::string materialRelacionado;

    Libro(std::string t, std::string a, std::string e, std::string gen, std::string est, int h, float p, std::string r, std::string mr);
    virtual ~Libro() {}

    virtual void imprimirInformacion() const override;
    std::string longitudLibro() const;
};