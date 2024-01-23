#ifndef VALIDADORCORREO_HPP
#define VALIDADORCORREO_HPP
#include <string>

class ValidadorCorreoElectronico {
public:
    bool validarCorreo(const std::string& correo);

private:
    bool tieneArroba(const std::string& correo);
};

#endif