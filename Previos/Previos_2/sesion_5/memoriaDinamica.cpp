#include <iostream>
using namespace std;

int main(){
    // Se declara un puntero entero.
    int* pointInt;
    
    // Se declara un puntero float.
    float* pointFloat;

    // Asignacion de valores en memoria.
    pointInt = new int;
    pointFloat = new float;

    *pointInt = 45;
    *pointFloat = 45.45f;

    cout << *pointInt << endl;
    cout << *pointFloat << endl;

    // desasigna la memoria.
    delete pointInt;
    delete pointFloat;

    return 0;
}