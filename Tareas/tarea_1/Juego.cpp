#include "Juego.hpp"
#include <iostream>

void Juego::mostrarMenu(){
    int opcion;
    do {
        std::cout << "----Menu----\n";
        std::cout << "1. Jugar (Modo Facil)\n";
        std::cout << "2. Jugar (Modo Dificil)\n";
        std::cout << "3. Salir \n";
        std >> opcion; 

        switch (opcion){
            case 1:
                modoFacil();
                break;
            case 2:
                modoDificil();
                break;
            case 3:
                std::cout << "";
                break;
            default:
                ste::cout << "Opcion invalida. Intentelo de nuevo. \n";

        }
    } while (opcion != 3);
}

void Juego::iniciarJuegoFacil(){


}

void Juego::iniciarJuegoDificil(){

} 