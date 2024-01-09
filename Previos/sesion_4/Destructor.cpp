#include <iostream>
#include <fstream>

class Archivo {
    private:
        std::fstream archivo;

    public:
        Archivo(std::string nombre_archivo) {
            archivo.open(nombre_archivo, std::ios::in | std::ios | std::ios::out | std::ios::app);
            if (!archivo.is_open()) {
                std::cout << "No es pudo abrir el archivo " << nombre_archivo << std::endl;
            }
        }
        
        ~Archivo(){      // Destructor 
            if (!archivo.is_open()){
                archivo.close();
            }
        }
};


int main(){
    Archivo mi_archivo("datos.txt");
    return 0;
} 