#include <iostream>
#include "sum.hpp"


int main(){
    int num1 = 5;
    int num2 = 3;
    int result = sum(num1, num2);
    
    std::cout << "El resultado de la suma de " << num1 << " y " << num2 << " es " << result << std::endl;

    return 0; 

}