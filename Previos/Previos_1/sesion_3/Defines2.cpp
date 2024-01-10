#include <iostream>
using namespace std;

#define BOOK_ID_MAX 10

enum {
    CASA_BADILLA,
    CASA_ALVARADO,
    CASA_SOLANO,
    CASA_MAX
} casas_t;

int main() {

    cout << "El valor de Book ID Max es: " << BOOK_ID_MAX << endl;

    cout << "La cantidad de casas en el condominio es:  " << CASA_MAX << endl;
    return 0;
}