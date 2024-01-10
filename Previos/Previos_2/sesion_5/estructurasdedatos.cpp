// Implementacion del Stack en lenguaje C++.

#include <iostream>
#include <stdlib.h>

using namespace std;

#define MAX 10

int size = 0;

// Creando Stack.
struct stack {
    int items[MAX];
    int top;
};

typedef struct stack st;

void createEmptyStack(st *s) {
    s->top = -1;
}

// Revisando si el Stack esta lleno.
int isfull(st *s) {
    if (s->top == MAX - 1) {
        return 1;
    } else {
        return 0;
    }
}

// Revisando si el Stack esta vacio.
int isempty(st *s) {
    if (s->top == -1) {
        return 1;
    } else {
        return 0;
    }
}

// Agregar elementos dentro del Stack.
void push(st *s, int newitem) {
    if (isfull(s)) {
        cout << "STACK FULL";
    } else {
        s->top++;
        s->items[s->top] = newitem;
    }
    size++;
}

// Remover elemento del Stack.
void pop(st *s) {
    if (isempty(s)) {
        cout << "\n STACK EMPTY \n";
    } else {
        cout << "Item popped = " << s->items[s->top];
        s->top--;
    }
    size--;
    cout << endl;
}

// Imprimir elementos del Stack.
void printStack(st *s) {
    cout << "Stack: ";
    for (int i = 0; i < size; i++) {
        cout << s->items[i] << " ";
    }
    cout << endl;
}

int main() {
    int ch;
    st *s = (st *)malloc(sizeof(st));

    createEmptyStack(s);

    push(s, 1);
    push(s, 2);
    push(s, 3);
    push(s, 4);

    printStack(s);

    pop(s);

    cout << "\nAfter popping out\n";
    printStack(s);

}