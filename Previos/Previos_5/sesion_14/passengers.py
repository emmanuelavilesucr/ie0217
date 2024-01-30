import pandas as pd  # Se importa la libreria de pandas

# Lee el archivo CSV y lo escribe en un archivo Excel 
titanic = pd.read_csv("data/titanic.csv")
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

titanic.info()  # Muetra informacion sobre el DataFrame 

# Se filtran los pasajeros mayores de 35 años
above_35 = titanic[titanic["Age"] > 35]
above_35.head()

# A continuacion se filtran los pasajeros de clases y se muestran las primeras filas
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
class_23.head()

# Filtra pasajeros con edad no nula 
age_no_na = titanic[titanic["Age"].notna()]
age_no_na.head()


adult_names = titanic.loc[titanic["Age"] > 35, "Name"]  # Se seleccionan nombres de pasajeros mayores de 35 años

# En esta parte se selecciona un rango específico de filas y columnas
titanic.iloc[9:25, 2:5]
titanic.iloc[0:3, 3]

# En esta parte se calculan las estadísticas
titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

titanic["Age"].mean()       # Se calcula la media
titanic[["Age", "Fare"]].median()   # Se calcula la mediana
titanic[["Age", "Fare"]].describe()   # Muestra  las estadisticas
 

titanic[["Sex", "Age"]].groupby("Sex").mean()   # Calcula la media de la columna Age
titanic.groupby(["Sex", "Pclass"])["Fare"].mean()   # Calcula la media de la tarifa

titanic["Pclass"].value_counts()     # Realiza un conteo de la frecuencia de cada clase
titanic.groupby("Pclass")["Pclass"].count() # Realiza un conteo de la frecuencia de cada clase  utilizando groupby

titanic.sort_values(by="Age").head()   # Organiza el DataFrame de forma ascendente 
titanic.sort_values(by=["Pclass", "Age"], ascending=False).head()   # Ordena el DataFrame de forma descendente 