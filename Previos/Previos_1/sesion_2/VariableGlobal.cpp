#include <iostream>
using namespace std;

int g;    // Variable global

int main() {
    int  a, b;   // Variable local

    a = 10;
    b = 20;
    g = a + b;
    cout << g;
    return 0;
}