#include "Agenda.hpp"
#include <iostream>

int main(){

    Contacto<std::string> contacto1("Juanito Mora", "27681234", "dj.juanito@gmail.com");
    Contacto<std::string> contacto2("William Walker", "865488997", "willwalk@outlook.es");
    Contacto<std::string> contacto3("Juan Santamaria", "22315689", "adiosmezon@gmail.com");

    Agenda<std::string> agenda;

    try {
        agenda.agregarContacto(contacto1);
        agenda.agregarContacto(contacto2);
        agenda.agregarContacto(contacto3);
    } catch (const std::exception& e){
        std::cerr << "Error al agregar contacto: " << e.what() << std::endl;
    }

    std::cout <<  "Contactos en la agenda: " << std::endl;
    agenda.mostrarContactos();

    try {
        agenda.eliminarContacto("865488997");
    } catch (const std::exception& e) {
        std::cerr << "Error al eliminar contacto: " << e.what() << std::endl;
    }

    std::cout <<  "Contactos en la agenda: " << std::endl;
    agenda.mostrarContactos();
}