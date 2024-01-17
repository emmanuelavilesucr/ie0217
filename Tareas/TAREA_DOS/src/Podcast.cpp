#include "Podcast.h"

Podcast::Podcast(std::string t, std::string a, std::string gen, std::string est, int d, float p, std::string r, std::string mr)
    : MaterialAudiovisual(t, "audiovisual", a, "podcast", gen, est, d, p), resumen(r), materialRelacionado(mr) {}

void Podcast::imprimirInformacion() const {
    // Codigo
    
}

std::string Podcast::longitudPodcast() const {
    // Codigo
}