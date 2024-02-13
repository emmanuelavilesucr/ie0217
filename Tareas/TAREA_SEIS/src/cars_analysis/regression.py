from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def regresion_lineal(X_train, X_test, y_train, y_test):
    
    reg_lineal = LinearRegression()
    reg_lineal.fit(X_train, y_train)
    y_pred = reg_lineal.predict(X_test)
    return r2_score(y_test, y_pred), mean_squared_error(y_test, y_pred), mean_absolute_error(y_test, y_pred)

def regresion_polinomial(X_train, X_test, y_train, y_test, grado=3):
    poly = PolynomialFeatures(degree=grado)
    X_poly = poly.fit_transform(X_train)
    reg_polinomial = LinearRegression()
    reg_polinomial.fit(X_poly, y_train)
    X_test_poly = poly.transform(X_test)
    y_pred_poly = reg_polinomial.predict(X_test_poly)
    return r2_score(y_test, y_pred_poly), mean_squared_error(y_test, y_pred_poly), mean_absolute_error(y_test, y_pred_poly)
