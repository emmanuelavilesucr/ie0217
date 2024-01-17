#include "MaterialOrdenado.h"

MaterialOrdenado::~MaterialOrdenado() {
    for (auto& material : materialesLectura)
        delete material;
    for (auto& material : materialesAudiovisual)
        delete material;
}

void MaterialOrdenado::agregarMaterial(MaterialLectura* material) {
    materialesLectura.push_back(material);
}

void MaterialOrdenado::agregarMaterial(MaterialAudiovisual* material) {
    materialesAudiovisual.push_back(material);
}

void MaterialOrdenado::eliminarMaterial(std::string titulo, std::string tipo) {
    if (tipo == "libro" || tipo == "noticia") {
        auto it = std::remove_if(materialesLectura.begin(), materialesLectura.end(),
            [titulo](MaterialLectura* material) { return material->titulo == titulo; });
        materialesLectura.erase(it, materialesLectura.end());
    } else if (tipo == "película" || tipo == "podcast") {
        auto it = std::remove_if(materialesAudiovisual.begin(), materialesAudiovisual.end(),
            [titulo](MaterialAudiovisual* material) { return material->titulo == titulo; });
        materialesAudiovisual.erase(it, materialesAudiovisual.end());
    }
}

void MaterialOrdenado::buscarMaterialPorTitulo(std::string titulo) const {
    for (const auto& material : materialesLectura) {
        if (material->titulo == titulo)
            material->imprimirInformacion();
    }
    for (const auto& material : materialesAudiovisual) {
        if (material->titulo == titulo)
            material->imprimirInformacion();
    }
}

void MaterialOrdenado::buscarMaterialPorTipo(std::string tipo) const {
    if (tipo == "lectura") {
        for (const auto& material : materialesLectura)
            material->imprimirInformacion();
    } else if (tipo == "audiovisual") {
        for (const auto& material : materialesAudiovisual)
            material->imprimirInformacion();
    }
}