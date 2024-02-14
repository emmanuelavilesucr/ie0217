import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import LabelEncoder

def regresion_lineal(data):
  
   X = data[['year']]
   y = data['selling_price']  
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   lin_reg = LinearRegression()
   lin_reg.fit(X_train, y_train)
   y_pred = lin_reg.predict(X_test)
   print("Coeficiente R²:", r2_score(y_test, y_pred))
   print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))
   print("Error absoluto medio:", mean_absolute_error(y_test, y_pred))


def regresion_polinomial(data):
   
   X = data[['km_driven']]
   y = data['selling_price'] 
   poly = PolynomialFeatures(degree=3)
   X_poly = poly.fit_transform(X)
   X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)
   lin_reg_poly = LinearRegression()
   lin_reg_poly.fit(X_train, y_train)
   y_pred_poly = lin_reg_poly.predict(X_test)
   print("Coeficiente R² (Regresión Polinomial):", r2_score(y_test, y_pred_poly))
   print("Error cuadrático medio (Regresión Polinomial):", mean_squared_error(y_test, y_pred_poly))
   print("Error absoluto medio (Regresión Polinomial):", mean_absolute_error(y_test, y_pred_poly))


def categorias(data):
   label_encoders = {}
   for column in ['name', 'fuel', 'seller_type', 'transmission', 'owner']:
       label_encoders[column] = LabelEncoder()
       data[column] = label_encoders[column].fit_transform(data[column])
