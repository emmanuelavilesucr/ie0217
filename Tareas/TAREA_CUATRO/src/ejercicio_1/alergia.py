class Alergia:

    """Clase que representa una alergia con nombre y valor asociado."""
    def __init__(self, nombre, valor):

        """Constructor de la clase Alergia.

        Parameters:
        - nombre (str): El nombre de la alergia.
        - valor (int): El valor asociado a la alergia.
        """
        self.nombre = nombre
        self.valor = valor

    def __str__(self):

        """Devuelve una representación en cadena de la alergia."""
        return f"{self.nombre} ({self.valor})"

