import pandas as pd # Se importa la libreria de pandas

#  Se crea un DataFrame utilizando un constructor
df = pd.Dataframe(
    {
        "Name" : [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],  # Esta es la columna de las edades
        "Sex": ["male", "male", "female"]   # Esta es la columna de los generos
    }
)

df # Muestra el DataFrame 
