#ifndef JUEGO_HPP
#define JUEGO_HPP

/**
 * @file Juego.hpp
 * @brief Definición de la clase Juego.
 */

/**
 * @class Juego
 * @brief Clase que representa el juego principal.
 */
class Juego {
public:
    /**
     * @brief Constructor de la clase Juego.
     */
    Juego();

    /**
     * @brief Muestra el menú principal del juego.
     */
    void mostrarMenu();

    /**
     * @brief Inicia el juego en modo fácil.
     */
    void iniciarJuegoFacil();

    /**
     * @brief Inicia el juego en modo difícil.
     */
    void iniciarJuegoDificil();

private:
    /**
     * @brief Función principal que controla el flujo del juego.
     * @param modoDificil Indica si el juego debe ejecutarse en modo difícil.
     */
    void jugar(bool modoDificil);

    /**
     * @brief Imprime una pista al jugador sobre su intento.
     * @param numeroSecreto El número secreto que el jugador intenta adivinar.
     * @param intentoUsuario El intento del jugador.
     */
    void imprimirPista(int numeroSecreto, int intentoUsuario);

};

#endif