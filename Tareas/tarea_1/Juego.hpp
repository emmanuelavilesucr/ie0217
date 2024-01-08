#ifndef JUEGO_HPP
#define JUEGO_HPP

class Juego() {
public:
    Juego();
    void mostrarMenu();
    void iniciarJuegoFacil();
    void iniciarJuegoDificil();
    
private:
    void jugar(bool modoDificil);
    void imprimirPista(int numeroSecreto, int intentoUsuario);

};

#endif