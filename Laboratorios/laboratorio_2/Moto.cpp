#include "Moto.hpp"

Moto::Moto(int velocidad, bool tieneCasco) : Vehiculo(velocidad), tieneCasco(tieneCasco){}

void Moto::usarCasco() {
    if (tieneCasco) {
        cout << "Usando casco mientras conduzco la moto." << endl;
    } else{
        cout << "¡Alerta! No tengo casco." << endl;
    }
}