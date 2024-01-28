class EvaluacionGeneral:
    def __init__(self, evaluacion_especifica):
        self.evaluacion_especifica = evaluacion_especifica
        self.alergias_evaluadas = []

    def calcular_puntuacion_general(self):
        puntuacion = sum(alergia.valor for alergia in self.alergias_evaluadas)
        return puntuacion

    def imprimir_resultados(self):
                puntuacion_general = self.calcular_puntuacion_general()
        print(f"Puntuación general de alergias: {puntuacion_general}")

        if self.evaluacion_especifica.nombres_desconocidos:
            print("Resultados Desconocidos (nombres):", ', '.join(self.evaluacion_especifica.nombres_desconocidos))

        if self.evaluacion_especifica.valores_desconocidos:
            print("Resultados Desconocidos (valores):", ', '.join(map(str, self.evaluacion_especifica.valores_desconocidos)))

        if self.alergias_evaluadas:
            promedio = sum(alergia.valor for alergia in self.alergias_evaluadas) / len(self.alergias_evaluadas)
            print(f"Promedio de alergias conocidas: {promedio}")
        else:
            print("No se encontraron alergias conocidas.")

    

