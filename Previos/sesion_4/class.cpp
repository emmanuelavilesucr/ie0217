#include <iostream>
using namespace std; 

class Molde {
    public:
        double largo;
        double ancho;
        double altura;

        Molde(){
            cout << "Esto se ejecuta en cada instanciacion" << endl;
            cout << "Iniciando un objeto de la clase Room" << endl;
        }

        double calcularArea(){
            return largo * ancho;
        }

        double calcularVolumen(){
            return largo * ancho * altura;
        }
};


int main(){

    Molde pared;




    return 0;
}