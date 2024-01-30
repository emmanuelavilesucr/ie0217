import pandas as pd  # Se importa la libreria de pandas

# Lee el archivo CSV y convierte las fechas a formato de fecha y hora
air_quality_pm25 = pd.read_csv("data/air_quality_no2_long.csv",
                               parse_dates=True)

# Se seleccionan las columnas
air_quality_pm25 = air_quality_pm25[["date.utc", "location", 
                                     "parameter", "value"]]
air_quality_pm25.head()   # Muestra las primeras filas del DataFrame

air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv")   # Lee nuevamente el archivo CSV
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]   # Se seleccionan las columnas
air_quality_no2.head()  

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)    # Concatena los DataFrames


# A continuacion se crean la nuevas columnas basadas en los calculos 
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwer"]
)


# Renombra columnas usando el método rename
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp" : "BETR801",
        "station_paris": "FR04014",
        "station_lodon": "London Westminster",
    }
)
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)  # Renombra todas las columnas utilizando el método rename


# Se filtran los datos y se seleccion las dos primeras filas por cada ubicación
no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"].head(2))


no2_subset.pivot(columns="location", values="value")  # Crea una tabla utilizando las columnas de location y value


# Crea tablas para analizar promedios
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)

# Crea tablas con totales generales utilizando el parámetro de margins
air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunx="mean",
    margins=True,
)

