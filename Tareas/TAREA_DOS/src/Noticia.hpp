#pragma once

#include "MaterialLectura.h"

class Noticia : public MaterialLectura {
public:
    std::string resumen;
    std::string materialRelacionado;

    Noticia(std::string t, std::string a, std::string e, std::string gen, std::string est, int h, float p, std::string r, std::string mr);
    virtual ~Noticia() {}

    virtual void imprimirInformacion() const override;
    std::string longitudNoticia() const;
};
