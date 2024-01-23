CXX := g++
CXXFLAGS := -std=c++11 -Wall

TARGET := ValidacionCorreo.exe

SRCS := main.cpp validadorCorreo.cpp
OBJS := $(SRCS:.cpp=.o)

# Para ejecutarse en Windows. 
ifeq ($(OS),Windows_NT)
    TARGET := $(TARGET).exe
    RM := del /F /Q
else
    RM := rm -f
endif

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS) $(TARGET)
