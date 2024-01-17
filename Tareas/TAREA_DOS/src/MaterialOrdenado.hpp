#pragma once

#include <vector>
#include "MaterialLectura.h"
#include "MaterialAudiovisual.h"

class MaterialOrdenado {
public:
    std::vector<MaterialLectura*> materialesLectura;
    std::vector<MaterialAudiovisual*> materialesAudiovisual;

    ~MaterialOrdenado();

    void agregarMaterial(MaterialLectura* material);
    void agregarMaterial(MaterialAudiovisual* material);

    void eliminarMaterial(std::string titulo, std::string tipo);
    void buscarMaterialPorTitulo(std::string titulo) const;
    void buscarMaterialPorTipo(std::string tipo) const;
};