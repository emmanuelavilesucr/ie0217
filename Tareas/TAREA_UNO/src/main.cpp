/**
 * @file main.cpp
 * @brief Programa principal que inicia el juego y muestra el menú.
 */

#include "Juego.hpp" 
#include <iostream>

int main(){

    Juego juego;  ///< Crea una instancia de la clase Juego.
    juego.mostrarMenu();  ///< Llama al método mostrarMenu() para iniciar el juego.
    return 0;  
}