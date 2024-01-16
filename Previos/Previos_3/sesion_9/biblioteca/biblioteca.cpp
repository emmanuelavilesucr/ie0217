#include <iostream>
#include "biblioteca.hpp"

void Biblioteca::agregarLibro(
    const std::string& titulo,
    const std::string& autor
) {
    catalogo.emplace_back(titulo, autor);
}

void Biblioteca::mostrarCatalogo() {
    for (const auto& libro : catalogo) {
        libro.mostrarInfo();
    }
}