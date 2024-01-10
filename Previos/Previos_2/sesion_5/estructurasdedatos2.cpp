#include <iostream>
#define SIZE 5 

using namespace std;

class Queue {
private:
    int items[SIZE];
    int front, rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    bool isFull() {
        if (front == 0 && rear == SIZE - 1) {
            return true;
        }
        return false;
    }

    bool isEmpty() {
        if (front == -1) {
            return true;
        } else {
            return false;
        }
    }

    void enQueue(int elemento) {
        if (isFull()) {
            cout << "La cola está llena" << endl;
        } else {
            if (front == -1) front = 0; 
            rear++;
            items[rear] = elemento;
            cout << "Insertado " << elemento << endl;
        }
    }

    int deQueue() { 
        int elemento;
        if (isEmpty()) {
            cout << "La cola está vacía" << endl;
            return (-1);
        } else {
            elemento = items[front];
            if (front >= rear) {
                front = -1;
                rear = -1;
            } /* Q tiene un solo elemento. entonces reiniciamos la cola después de eliminarla. */
            else {
                front++;
            }
            cout << "Eliminado -> " << elemento << endl;
            return elemento;
        }
    }

    void display() { 
        /* Función para mostrar elementos de la cola */
        int i;
        if (isEmpty()) {
            cout << "Cola vacía" << endl;
        } else {
            cout << "Índice del frente -> " << front << endl;
            cout << "Elementos ->" << endl;
            for (i = front; i <= rear; i++) {
                cout << items[i] << " ";
            }
            cout << endl;
            cout << "Índice del final -> " << rear << endl;
        }
    }
};

int main() {
    Queue q;

    // deQueue no es posible en una cola vacía
    q.enQueue(1);
    q.enQueue(2);
    q.enQueue(3);
    q.enQueue(4);
    q.enQueue(5);

    // No se puede agregar el sexto elemento porque la cola está llena
    q.enQueue(6);

    q.display();

    // DeQueue elimina el elemento ingresado primero, es decir, 1.
    q.deQueue();

    // Ahora tenemos solo 4 elementos.
    q.display();

    return 0;
}
