#ifndef VALIDADORCORREO_HPP
#define VALIDADORCORREO_HPP
#include <string>

/**
 * @brief Clase para validar direcciones de correo electrónico.
 */

class ValidadorCorreoElectronico {
public:
    /**
     * @brief Valida si la dirección de correo electrónico sigue el formato estándar.
     * @param correo Dirección de correo electrónico a validar.
     * @return true si la dirección es válida, false en caso contrario.
     */

    bool validarCorreo(const std::string& correo);
    
private:
    /**
     * @brief Verifica si la dirección de correo electrónico contiene el símbolo '@'.
     * @param correo Dirección de correo electrónico.
     * @return true si contiene '@', false en caso contrario.
     */
    
    bool tieneArroba(const std::string& correo);
};

#endif