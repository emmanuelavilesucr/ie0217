#include <iostream>
using namespace std; 

// Función para imprimir una matriz.
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

void insertionSort(int array[], int size) {
    for (int step = 1; step < size; step++){
        int key = array[step];
        int j = step - 1;


        // Compara la clave con cada elemento a la izquierda hasta que el elemento aj sea más pequeño que el
        // se encuentra.
        // Para orden descendente, cambie key<array[j] a key>array[j].
        while (key < array[j] && j >= 0) {
            array[j + 1] = array[j];
            --j;
        }
        array [j + 1] = key;
    }
}

int main() {
    int data[] = {9, 5, 1, 4, 3};
    int size = sizeof(data) / sizeof(data[0]);
    insertionSort(data, size);
    cout << "Sorted array in Ascending Order: \n";
    printArray(data, size); 
}