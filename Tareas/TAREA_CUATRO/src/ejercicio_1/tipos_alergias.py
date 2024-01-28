from alergia import Alergia

class TiposAlergias:
    def __init__(self):
        self.tipos_alergias = []
        self.nombres_desconocidos = []
        self.valores_desconocidos = []



    def cargar_alergias_desde_archivo(self, nombre_archivo):
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
        self.tipos_alergias.append(alergia)
 
 
 
    def analizar_entrada_usuario(self, entrada):
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


