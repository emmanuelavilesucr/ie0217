#include "validadorCorreo.hpp"
#include <iostream>
#include <regex>

bool ValidadorCorreoElectronico::validarCorreo(const std::string& correo) {

}

bool ValidadorCorreoElectronico::tieneArroba(const std::string& correo) {
    return correo.find('@') != std::string::npos;
}