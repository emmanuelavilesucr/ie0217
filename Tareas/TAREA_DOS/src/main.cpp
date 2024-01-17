#include "MaterialOrdenado.h"
#include "Libro.h"
#include "Noticia.h"
#include "Pelicula.h"
#include "Podcast.h"

int main() {
    MaterialOrdenado biblioteca;

    Libro* libro1 = new Libro("El nombre del viento", "Patrick Rothfuss", "Anagrama", "Fantasía", "disponible", 700, 19.99, "Un libro muy interesante.", "Libro relacionado: El temor de un hombre sabio.");
    Noticia* noticia1 = new Noticia("Titular de la noticia", "Autor de la noticia", "Editorial de noticias", "Actualidad", "disponible", 2, 0.99, "Resumen de la noticia.", "Noticia relacionada: Otra noticia importante.");
    Pelicula* pelicula1 = new Pelicula("Inception", "Christopher Nolan", "Ciencia Ficción", "disponible", 148, 12.99, "Resumen de la película.", "Pelicula relacionada: Interstellar.");
    Podcast* podcast1 = new Podcast("Podcast interesante", "Host del podcast", "Variedad", "disponible", 45, 0.0, "Resumen del podcast.", "Podcast relacionado: Otro podcast fascinante.");

    biblioteca.agregarMaterial(libro1);
    biblioteca.agregarMaterial(noticia1);
    biblioteca.agregarMaterial(pelicula1);
    biblioteca.agregarMaterial(podcast1);

    // Realizar operaciones adicionales según tus necesidades

    // Limpiar memoria dinámica
    return 0;
}