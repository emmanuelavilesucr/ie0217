#include <iostream>
using namespace std;


class Distance {
    private:
        int meter;

        // Funcion amiga
        friend int addFive(Distance);
    
    public:
        Distance() : meter(0) {}
};

int addFive(Distance d) {
    // Accesando a los miembros privados de la funcion amiga.
    d.meter += 5;
    return d.meter;
}


int main() {
    Distance D;
    cout << "Distance: " << addFive(D);
    return 0;
}