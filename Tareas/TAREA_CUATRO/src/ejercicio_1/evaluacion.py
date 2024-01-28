class EvaluacionEspecifica:

    """Clase que maneja la evaluación específica de alergias."""
    def __int__(self):

        """Constructor de la clase EvaluacionEspecifica."""
        self.alergias = []
        self.nombres_desconocidos = []
        self.valores_desconocidos = []

    def evaluar_alergias(self, puntuacion):

        """Evalúa las alergias activas basándose en la puntuación dada.

        Parameters:
        - puntuacion (int): La puntuación de alergias del usuario.

        Returns:
        - List[Alergia]: Lista de instancias de la clase Alergia a las que el usuario es alérgico.
        """
        alergias_activas = []
        for alergia in self.alergias:
            if puntuacion & alergia.valor:
                alergias_activas.append(alergia)
        return alergias_activas

    def imprimir_evaluacion(self, puntuacion):

         """Imprime la evaluación de alergias para una puntuación dada.

        Parameters:
        - puntuacion (int): La puntuación de alergias del usuario.
        """
        alergias_activas = self.evaluar_alergias(puntuacion)
        print(f"Puntuación general: {puntuacion}")
        print("Alergias activas:")
        for alergia in alergias_activas:
            print(f"- {alergia}")
        print()

