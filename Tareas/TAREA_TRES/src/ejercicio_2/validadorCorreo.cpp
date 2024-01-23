#include "validadorCorreo.hpp"
#include <iostream>
#include <regex>

/**
 * @brief Valida si la dirección de correo electrónico sigue el formato estándar.
 * @param correo Dirección de correo electrónico a validar.
 * @return true si la dirección es válida, false en caso contrario.
 */

bool ValidadorCorreoElectronico::validarCorreo(const std::string& correo) {
        try {
        if (!tieneArroba(correo)) {
            throw std::invalid_argument("La direccion de correo electronico debe contener un '@'.");
        }

        std::regex formatoCorreo("^[a-zA-Z0-9.-]{1,15}@[a-zA-Z]+\\.[a-zA-Z]{2,4}$");

        if (!std::regex_match(correo, formatoCorreo)) {
            throw std::invalid_argument("La direccion de correo electronico no sigue el formato estandar.");
        }

        return true;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return false;
    }
}

/**
 * @brief Verifica si la dirección de correo electrónico contiene el símbolo '@'.
 * @param correo Dirección de correo electrónico.
 * @return true si contiene '@', false en caso contrario.
 */

bool ValidadorCorreoElectronico::tieneArroba(const std::string& correo) {
    return correo.find('@') != std::string::npos;
}