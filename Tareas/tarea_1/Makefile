CXX := g++

CXXFLAGS := -std=c++11 -Wall

SRCS := main.cpp Juego.cpp 

OBJS := $(SRCS:.cpp=.o)

TARGET := Juego.exe

.PHONY: all clean build run

all: build run

build: $(TARGET)

run: $(TARGET)
	./$(TARGET) 0 20

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $(TARGET)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
