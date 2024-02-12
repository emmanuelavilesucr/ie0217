# Parte Teorica:


## Regresion:

**1. ¿Que es la regresion lineal y como se diferencia de la regresion no lineal?**

- **Las regresiones lineales** modelan la relacion existente entre una variable dependiente y otras variable independientes de una linea recta, mientras que **las regresiones no lineales** modelan las mismas relaciones entre variables pero con una curva. 

<br>

**2. ¿Que son los coeficientes de regresion y que informacion proporcionan sobre la relacion entre las variables?**

- Son los valores relacionados con la variables independientes en un modelo de regresion. Ademas, estan encargados de brindar informacion sobre la magnitud y direccion de las variables.

<br>

**3. ¿Que es el error cuadratico medio (MSE) y como se utiliza para evaluar la precision de un modelo de regresion?**

- Este error consiste en una medida de diferenciacion entre los valores predichos y los valores observados en una prediccion. Por otro lado, se utiliza para calcular la media de los cuadrados de las diferencias, entre mas bajo el MSE posee una mejor capacidad de prediccion.

<br>

**4. ¿Cual es la diferencia entre regresion simple y regresion multiple y cuando se utiliza cada una?**

- **La regresion simple** examina la relacion lineal entre dos variables, una respuesta Y e un predictor X. **La regresion multiple** examina la relacion lineal entre una repuesta Y y dos o mas predictores X. Por otro lado, **la regresion simple** es utilizada en el estudio de la relacion entre una variable independiente y una dependiente, mientras que **la regresion multiple** es utilizada en el estudio de la relacion entre multiples variables tanto independientes como dependientes.  

<br>

## Clustering:

**1. ¿Que es el clustering y cual es su objetivo principal en el analisis de datos?**

- **El clustering** consiste en una herramienta que nos permite la agrupacion de un conjunto de objetos con caracteristicas similares en grupos. Su objetivo principal en el analisis de datos se basa en la busqueda de patrones de datos o datos ocultos.


<br>

**2. Describa brevemente los algoritmos K-Means y DBSCAN y como funcionan.**

- El algoritmo **K-Means** consiste en dividir un conjunto de datos en una cierta cantidad de grupos. Su funcionamiento consiste en minimizar la suma de las distancias cuadradas de cada punto.Mientras, que **DSCAN** es un algoritmo muy utilizado en **clustering** en la agrupacion de puntos. Su funcionamineto es el de dividir los puntos en k grupos  llamados clusteres, homogeneos y compactos con el fin de realizar observaciones de densidad.


<br>

**3. ¿Que es la inercia en el contexto del clustering y como se utiliza para evaluar la calidad de un agrupamiento?**

- Es una medida para saber la agrupacion de los puntos con respecto al centroide en clustering. Se utiliza calcular el nivel de inercia. Por ejemplo: una inercia baja indica que los puntos estan cerca del centroide.


**4. ¿Que son los centroides y como se utilizan en el algoritmo K-Means?**

- Son puntos que representan de un grupo en KMeans. Se utilizan para los centroides  en el calculo de la media de los puntos cercanos al grupo.


<br>

**5. Escriba la diferencia entre datos estructurados y no estructurados para analisis de datos.**

- Los datos estructurados son datos organizados en un formato específico mediante metodos de analisis basicos, mientras  que los datos no estructurados pueden incluir archivos mediante tecnicas avanzadas de analisis.

<br>

## Paquetes en Python ( init .py):

**1. ¿Que es un paquete en Python y como se diferencia de un modulo?**

-   Un **paquete** es una carpeta cuyo contenido con un conjunto de modulos. Por otro lado, un **modulo** consiste en un archivo que contiene codigo y que puede se usado posteriormente en otros programas. 

<br>

**2. ¿Cual es la funcion del archivo __init__.py dentro de un paquete de Python?**

- Su funcion es indicar el contenido dentro del directorio, el cual debe ser un paquete. Lo que permite la importacion de modulos.

<br>

**3. ¿Como se importa un modulo o funcion desde un paquete en Python?**

- Este procedimineto se lleva a cabo mediante la importacion de un modulo o funcion mediante un paquete. La sintaxis que se debe usar es la siguiente: **from paquete import modulo**, o si se necesita una funcion **from paquete.modulo import funcion**. 

<br>

**4. ¿Que es la variable __all__ en el archivo __init__.py y cual es su proposito?**

- La variable **__all__** que contiene una una lista de los nombres de modulos. Su proposito es declarar los modulos se importaran de forma automatica con el paquete.

<br>

**5. ¿Cual es la ventaja de organizar el codigo en paquetes y modulos en Python?**

- La ventaja consiste principalmente en establecer una optima estructuracion y modularizacion del codigo. Esto es importante dado a que facilita su mantenimiento y reutilizacion del codigo.


<br>

## Python HTTP y Servicios Web (API):

**1. ¿Que es una API y cual es su funcion en el contexto de los servicios web?**

- Un **API** es un conjunto de funciones y procedimientos que permite integrar sistemas, permitiendo ser reutilizados por otros software. Su funcionalidad consiste en ser un puente entre diversos tipos de software, con la ventaja de ser multilenguaje.

<br>

**2. ¿Cual es la diferencia entre una API RESTful y una API SOAP?**

- Cuando hablamos de **API**, un **RESTful** utiliza HTTP y REST  para la comunicación entre cliente y servidor, mientras que **SOAP** utiliza el protocolo XML para establecer la comunicacion.

<br>

**3. Describa los pasos basicos para consumir una API utilizando Python.**

- Primeramente, se debe de importar la biblioteca **requets.**

- Despues, se debe de realizar una solicitud HTTP a la pagina web de una API.

- Se procesa la respuesta.

- Finalmente, se utilizan los datos recibidos en el programa. 

<br>

**4. ¿Que es la autenticacion de API y por que es importante?**

- Es un proceso de verificacion de la identidad de un cliente. Es importante en el tema de seguridad, dado a que protege los datos de la API contra accesos externos no autorizados.

<br>

**5. ¿Cual es el papel de los verbos HTTP (GET, POST, PUT, DELETE) en las solicitudes a una API y HTTP?**

- El papel de los verbos HTTP es indicar la accion que se realizara sobre un recurso en una **API**, como por ejemplo: obtener datos mediante el verbo **GET**, enviar datos mediante el verbo **POST**, actualizar datos mediante el verbo **PUT** y eliminar datos mediante **DELETE**.

<br>
<br>

# Bibliografia:

[1] https://rua.ua.es/dspace/bitstream/10045/16373/4/Microsoft%20Word%20-%204.REGRESIONES%20LINEALES%20Y%20NO%20LINEALES.pdf  

[2] https://support.minitab.com/es-mx/minitab/20/help-and-how-to/statistical-modeling/regression/supporting-topics/basics/types-of-regression-analyses/ 

[3] https://www.sydle.com/es/blog/api-6214f68876950e47761c40e7 

[4] https://tutorial.recursospython.com/modulos-y-paquetes/ 

[5] https://datascientest.com/es/machine-learning-clustering-dbscan 
 