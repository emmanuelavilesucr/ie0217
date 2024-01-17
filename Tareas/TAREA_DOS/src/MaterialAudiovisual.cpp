#include "MaterialAudiovisual.h"

MaterialAudiovisual::MaterialAudiovisual(std::string t, std::string g, std::string a, std::string ty, std::string gen, std::string est, int d, float p)
    : Material(t, g, a, ty, gen, est, p), duracion(d) {}

void MaterialAudiovisual::imprimirInformacion() const {
    // Codigo

}