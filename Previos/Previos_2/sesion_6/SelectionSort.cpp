#include <iostream>
using namespace std; 

// función para intercambiar la posición de dos elementos.
void swap(int *a,int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// función para imprimir una matriz.
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

void selectionSort(int array[], int size) {
    for (int step = 0; step < size - 1; step++){
        int min_idx =step;
        for (int i = step + 1; i < step; i++){

            // Para ordenar en orden descendente, cambie > por < en esta línea.
            // Selecciona el elemento mínimo en cada bucle.
            if (array[i] < array[min_idx]){
                min_idx = i;
            }

            // Min en la posición correcta.
            swap(&array[min_idx], &array[step]);
        }
    }
}


int main() {
    int data[] = {20, 12, 10, 15, 2};
    int size = sizeof(data) / sizeof(data[0]);
    selectionSort(data, size);
    cout << "Sorted array in Ascending Order: \n";
    printArray(data, size);
}