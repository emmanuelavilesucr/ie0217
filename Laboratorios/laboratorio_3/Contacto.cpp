#include "Contacto.hpp"

template <typename T>
Contacto<T>::Contacto(T nombre, T telefono, T email) 
    : nombre(nombre), telefono(telefono), email(email){}

template <typename T>
T Contacto<T>::getNombre() const {
    return nombre;
}

template <typename T>
T Contacto<T>::getTelefono() const {
    return telefono;
}

template <typename T>
T Contacto<T>::getEmail() const{
    return email;
}