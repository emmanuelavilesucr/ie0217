#include <iostream>
using namespace std;

class Fraccion {
    int numerador, denominador;
    public:
        Fraccion(int n, int d) : numerador(n), denominador(d) {}  // Constructor de la clase Fraccion que inicializa los atributos.


        Fraccion operator+ (const Fraccion &f) {  // Crea una sobrecarga del operador '+' para sumar las dos fracciones.
            Fraccion resultado (
                numerador * f.denominador + f.numerador * denominador, 
                denominador * f.denominador
            );
            return resultado;
        }

        void imprimir() {
            cout << numerador << "/" << denominador << endl;
        }
};

int main(){

    // Crea dos instancias de la clase Fraccion.
    Fraccion f1(1, 2);
    Fraccion f2(3, 4);

    Fraccion f3 = f1 + f2;

    f3.imprimir();

    return 0;
}