CXX := g++

CXXFLAGS := -std=c++11 -Wall

SRCS := main.cpp Juego.cpp 

OBJS := $(SRCS:.cpp=.o)

TARGET := Juego.exe

# La siguiente lineas estan encargadas de detectar el sistema operativo windows y sus comandos. 
ifeq ($(OS),Windows_NT)
	RM := del /Q
	FIXPATH = $(subst /,\,$1)
else
	RM := rm -f
	FIXPATH = $1
endif


.PHONY: all clean build run

all: build run

build: $(TARGET)

run: $(TARGET)
	./$(TARGET) 0 20

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(call FIXPATH,$(TARGET))

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	$(RM) $(call FIXPATH,$(OBJS)) $(call FIXPATH,$(TARGET))