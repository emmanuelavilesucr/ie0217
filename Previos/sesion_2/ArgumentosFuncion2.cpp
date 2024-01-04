#include <iostream>

using namespace std;

void displayNum(int n1, float n2){
    cout << "Numero de argumentos: " << n1 ;
    cout << "Nombre del programa: " << n2;
}

int main(){
    int num1 = 5;
    double num2 = 5.5;
    displayNum(num1, num2);
    return 0;
}