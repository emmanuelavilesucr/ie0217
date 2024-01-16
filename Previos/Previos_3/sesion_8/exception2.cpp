#include <iostream>
#include <stdexcept>

using namespace std;

int main() {
    int numerador, denominador, resultado;

    cout << "Ingrese el numerador: ";
    cin >> numerador;

    cout << "Ingrese el denominador: ";
    cin >> denominador;

    try {
        if (denominador == 0) {
            throw runtime_error("Error: el denominador no puede ser cero.");
        }
        
        resultado = numerador / denominador;
        cout << "El resultado es: " << resultado << endl;
    } catch (const exception& e) {
        cerr << e.what() << endl;
    }

    return 0;
}