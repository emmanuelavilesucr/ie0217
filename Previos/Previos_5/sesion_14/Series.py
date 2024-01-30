import pandas as pd  # Importa la libreria de pandas

ages = pd.Series([22, 35, 58], name="Age")  # Crea una Serie y le asigna el nombre Age

ages.max()  # Calcula el valor máximo de la Serie