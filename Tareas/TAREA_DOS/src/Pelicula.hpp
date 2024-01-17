#pragma once

#include "MaterialAudiovisual.h"

class Pelicula : public MaterialAudiovisual {
public:
    std::string resumen;
    std::string materialRelacionado;

    Pelicula(std::string t, std::string a, std::string gen, std::string est, int d, float p, std::string r, std::string mr);
    virtual ~Pelicula() {}

    virtual void imprimirInformacion() const override;
    std::string longitudPelicula() const;
};