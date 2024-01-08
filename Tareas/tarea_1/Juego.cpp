#include "Juego.hpp"
#include <iostream>
#include <cstdlib> 
#include <ctime>  

Juego::Juego() {
    std::srand(std::time(0));    // Inicializa la generacion de números aleatorios
}

void Juego::mostrarMenu(){
    int opcion;
    do {
        std::cout << "----Menu----\n";
        std::cout << "1. Jugar (Modo Facil)\n";
        std::cout << "2. Jugar (Modo Dificil)\n";
        std::cout << "3. Salir \n";
        std::cin >> opcion; 

        switch (opcion){
            case 1:
                iniciarJuegoFacil();
                break;
            case 2:
                iniciarJuegoDificil();
                break;
            case 3:
                std::cout << "Saliendo del juego.\n";
                break;
            default:
                std::cout << "Opcion invalida. Intentelo de nuevo. \n";

        }
    } while (opcion != 3);
}

void Juego::iniciarJuegoFacil(){
    jugar(false);
}

void Juego::iniciarJuegoDificil(){
    jugar(true);
} 

void Juego::jugar(bool modoDificil){
    const int limite = modoDificil ? 100: 50; 
    const int numeroSecreto = std::rand() % limite + 1;
    const int intentos = limite / 3;

    std::cout << "¡Bienvenido!\n";
    std::cout << "Estoy pensando en un número entre 1 y : ??? " << limite << ".\n";
    std::cout << "Tienes " << intentos << " intentos para adivinar.\n";

    for (int intento = 1; intento <= intentos; ++intento){
        int intentoUsuario;
        std::cout << "Intento #" << intento << ": ";
        std::cin << intentoUsuario; 

        if (intentoUsuario == numeroSecreto) {
            std::cout << "¡Felicidades! Has adivinado el número.\n";
            return;
        } else {
            imprimirPista(numeroSecreto, intentoUsuario);
        }
    }
    std::cout << "Lo siento, has agotado tus intentos. El número correcto era: " << numeroSecreto << "\n";

}

void Juego::imprimirPista(int numerosecreto, int intentoUsuario){

    if (intentoUsuario < numeroSecreto) {
        std::cout << "El número es mayor. ";
    } else {
        std::cout << "El número es menor. ";
    }
    std::cout << "¡Sigue intentándolo!\n"; // Se pueden modificar las frases con: "congelado", "frío", "caliente" o "hirviendo".

}