#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// Creando un nodo 

class Node {
    public:
    int value;
    Node* next;
};

int main() {
    Node* head;
    Node* one = NULL;
    Node* two = NULL;
    Node* three = NULL;

    // Asigna 3 nodos en el montón.
    one->value = 1;
    two->value = 2;
    three->value = 3;

    // Conectar nodos.
    one->next = two;
    two->next = three;
    three->next = NULL;

    // Imprime el valor de la lista vinculada.
    head = one;
    while (head != NULL) {
        cout << head->value;
        head = head->next;
    }
}