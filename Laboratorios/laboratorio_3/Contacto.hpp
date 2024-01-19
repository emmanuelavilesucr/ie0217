#ifndef CONTACTO_HPP
#define CONTACTO_HPP

#include <string>

template <typename T>
class Contacto{
    public:
        Contacto(T nombre, T telefono, T email);
        T getNombre() const;
        T getTelefono() const;
        T getEmail() const;
    
    private:
        T nombre;
        T telefono;
        T email;
};