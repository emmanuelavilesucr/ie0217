#include "Agenda.hpp"

template<typename T>
void Agenda<T>::agregarContacto(const Contacto<T>& contacto){
    typename std::list<Contacto<T> >::const_iterator it;
    for( it = contactos.begin(); it != contactos.end(); it++){
        if (it->getTelefono() == contacto.getTelefono()){
            throw std::invalid_argument("Ya existe un contacto con este numero");
        }    
    }
    contactos.push_back(contacto);
}

template<typename T>
void Agenda<T>::eliminarContacto(const T& telefono){
    typename std::list<Contacto<T> >::const_iterator it;
    for( it = contactos.begin(); it != contactos.end(); it++){
        if (it->getTelefono() == telefono){
            contactos.erase(it);
            return;
        }    
    }
    throw std::out_of_range("No se encuentra un contacto con ese numero");
}

template<typename T>
void Agenda<T>::mostrarContactos() const{
    typename std::list<Contacto<T> >::const_iterator it;
    for(it = contactos.begin(); it != contactos.end(); ++it){
        std::cout << "Nombre: "     << it->getNombre() << " "
                  << "Telefono: "   << it->getTelefono() << " "
                  << "Email: "      << it->getEmail() << std::endl;
    
    }
}