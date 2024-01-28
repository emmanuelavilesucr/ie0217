from alergia import Alergia

class EvaluacionEspecifica:
    def __int__(self):
        self.alergias = []
        self.nombres_desconocidos = []
        self.valores_desconocidos = []

    def evaluar_alergias(self, puntuacion):
        alergias_activas = []
        for alergia in self.alergias:
            if puntuacion & alergia.valor:
                alergias_activas.append(alergia)
        return alergias_activas

    def imprimir_evaluacion(self, puntuacion):
        alergias_activas = self.evaluar_alergias(puntuacion)
        print(f"Puntuación general: {puntuacion}")
        print("Alergias activas:")
        for alergia in alergias_activas:
            print(f"- {alergia}")
        print()

