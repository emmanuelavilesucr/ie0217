#include <iostream>
#include <string>
#ifndef FUNCIONES_HPP
#define FUNCIONES_HPP

const int MAX_EMPLEADOS = 10;

struct Empleado {
    int id;
    std::string nombre;
    double salario;
};

void mostrarmenu();
void procesarOpcion(Empleado empleados[], int& numEmpleados);
void agregarEmpleado(Empleado empleados[], int& numEmpleados);
void listarEmpleados(const Empleado empleados[], int& numEmpleados);
void eliminarEmpleado(Empleado empleados[], int& numEmpleados);
#endif