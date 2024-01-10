#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    
    // Asigna memoria de tamaño int a un puntero int.
    int* ptr = (int*) malloc(sizeof(int));

    // Asigna el valor 5 a la memoria asignada.
    *ptr = 5;
    cout << *ptr;

    return 0;
}

// Salida: 5.