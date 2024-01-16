# Nombre del programa de salida

TARGET = gestion_estudiantes.exe

#Compilador de C++
CXX = g++

# Opciones de compilacion 
CXXFLAGS = -Wall -std=c++11

# Lista de archivos fuente
SOURCES = main.cpp estudiante.cpp

# Lista de archivos objeto generados a partir de los archivos fuente
OBJECTS = $(SOURCES:.cpp=.exe)

# Regla para compilar los archivos objeto 
%.exe: %.cpp
    $(CXX) $(CXXFLAGS) -c $< -o $@

# Regla para compilar el programa a partir de los  archivos objeto
$(TARGET): $(CXXFLAGS)
    $(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

# Regla para limpiar los archivos generados
clean:
    del$(TARGET) $(OBJECTS)