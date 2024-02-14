ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
else
    DETECTED_OS := $(shell uname -s)
endif

ifeq ($(DETECTED_OS),Windows)
    RM := del /Q
    MKDIR := mkdir
    PYTHON := python
    PIP := pip
    KAGGLE := kaggle
else

    RM := rm -f
    MKDIR := mkdir -p
    PYTHON := python3
    PIP := pip3
    KAGGLE := kaggle
endif

all: main

main:
    $(PYTHON) main.py


download_dataset:
    $(KAGGLE) datasets download -d akshaydattatraykhare/car-details-dataset -p ./Datos
    unzip -o ./Datos/car-details-dataset.zip -d ./Datos


install_requirements:
    $(PIP) install -r requirements.txt

clean:
    $(RM) ./Datos/*
    $(RM) -r __pycache__
    $(RM) -r ./__pycache__

.PHONY: all main download_dataset install_requirements clean
