#include <iostream>
using namespace std; 

void bubbleSort(int array[], int size) {
    
    // comprobar si se produce el intercambio
    int swapped = 0;

    // bucle para acceder a cada elemento de la matriz
    for(int step = 0; step < (size-1); ++step) {
        
        // Bucle para comparar el elemento de la matriz
        for (int i = 0; i < (size-step-1); ++i){
            // compara dos elementos adyacentes
            // cambiar > a < para ordenar en orden descendente
            if (array[i] > array[i + 1]){
                // intercambiando elementos si hay elementos
                // no están en el orden deseado
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
           }
           swapped = 1;
        } 

        // Sin intercambio significa que la matriz ya está ordenada.
        // por lo que no es necesario realizar más comparaciones.
        if (swapped == 0){
            break;
        }
    }
}

 // Imprime una Array
void printArray(int array[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << " " << array[i];
    }
    cout << "\n";
}


int main() {
    
    int data[] = {-2, 45, 0, 11, -9};

    // encontrar la longitud de las matrices
    int size = sizeof(data) / sizeof(data[0]);

    bubbleSort(data, size);

    cout << "Sorted Array in Ascending Order :\n";
    printArray(data, size);
    
}