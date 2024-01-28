from alergia import Alergia

class TiposAlergias:

    """Clase que gestiona los tipos de alergias disponibles."""
    def __init__(self):

        """Constructor de la clase TiposAlergias."""
        self.tipos_alergias = []
        self.nombres_desconocidos = []
        self.valores_desconocidos = []



    def carr_alergias_desde_archivo(self, nombre_archivo):

        """Carga los tipos de alergias desde un archivo y los almacena en la lista tipos_alergias.

        Parameters:
        - nombre_archivo (str): El nombre del archivo que contiene las alergias y sus valores.
        """
        try:
            with open(nombre_archivo, 'r') as file:
                for line in file:
                    parts = line.strip().split(' ')
                    if len(parts) >= 2:
                        nombre = ' '.join(parts[:-1])
                        valor = int(parts[-1][1:-1])  
                        alergia = Alergia(nombre, valor)
                        self.tipos_alergias.append(alergia)
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {nombre_archivo}")



    def agregar_alergia(self, alergia):

        """Agrega una nueva alergia a la lista tipos_alergias.

        Parameters:
        - alergia (Alergia): Es la instancia de la clase Alergia.
        """
        self.tipos_alergias.append(alergia)
 
 
 
    def analizar_entrada_usuario(self, entrada):

        """Analiza la entrada del usuario y devuelve la instancia de la clase Alergia correspondiente.

        Parameters:
        - entrada (str): La entrada del usuario, la cual es el nombre o valor de alergia.

        Returns:
        - Alergia or None: La instancia de la clase Alergia correspondiente o None si no se encontro.
        """
        try:
            valor = int(entrada)
            alergia = next((a for a in self.tipos_alergias if a.valor == valor), None)
            if alergia:
                return alergia
            else:
                self.valores_desconocidos.append(valor)
                return None
        except ValueError:
            nombre = entrada.lower()
            alergia = next((a for a in self.tipos_alergias if a.nombre.lower() == nombre), None)
            if alergia:
                return alergia
            else:
                self.nombres_desconocidos.append(nombre)
                return None


