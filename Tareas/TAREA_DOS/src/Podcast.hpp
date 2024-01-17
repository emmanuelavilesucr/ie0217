#pragma once

#include "MaterialAudiovisual.h"

class Podcast : public MaterialAudiovisual {
public:
    std::string resumen;
    std::string materialRelacionado;

    Podcast(std::string t, std::string a, std::string gen, std::string est, int d, float p, std::string r, std::string mr);
    virtual ~Podcast() {}

    virtual void imprimirInformacion() const override;
    std::string longitudPodcast() const;
};