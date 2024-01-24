CXX = g++
CXXFLAGS = -std=c++11 -Wall

TARGET = Matriz.exe

# Para ejcutar en windows. 
ifeq ($(OS),Windows_NT)
	RM = del /Q
else
	RM = rm -f
endif

$(TARGET): Matriz.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) Matriz.cpp

.PHONY: clean

clean:
	$(RM) $(TARGET)
