# Parte Teórica:

1. **¿Cuál es la principal diferencia entre C y C++?**
   - La principal diferencia entre C y C++ es la funcionalidad, ya que el lenguaje C++ posee el paradigma de programación orientada a objetos (OOP), lo que facilita la creación de código más modular, reutilizable y orientado a objetos.

2. **¿Cuáles son las diferencias fundamentales entre un lenguaje de programación compilado y uno interpretado? Proporcione ejemplos...**
   - La diferencia clave entre un lenguaje de programación compilado y uno interpretado radica en el proceso de ejecución: los lenguajes compilados se traducen completamente antes de la ejecución, mientras que los interpretados se traducen y ejecutan línea por línea en tiempo real. Lenguajes compilados, como C++, ofrecen rendimiento máximo y son ideales para sistemas embebidos o desarrollo de alto rendimiento, mientras que lenguajes interpretados, como Python, priorizan la portabilidad, la flexibilidad y la rapidez de desarrollo, siendo más adecuados para scripting y aplicaciones web. La elección depende de las necesidades específicas del proyecto, considerando factores como rendimiento, portabilidad y agilidad en el desarrollo.

3. **Explique qué es un linker en el contexto de un lenguaje de programación compilado. ¿Cuál es su función principal y por qué es esencial en el proceso de compilación?**
   - Un linker es una herramienta crucial en el proceso de compilación. Su función principal es vincular múltiples archivos objeto generados durante la compilación en un único programa ejecutable. El linker resuelve símbolos no definidos, vincula funciones y variables a direcciones de memoria específicas, y combina archivos objeto y bibliotecas en un programa cohesivo. También gestiona referencias cruzadas entre diferentes partes del código y puede generar una tabla de símbolos. Sin el linker, el código fuente no podría convertirse en un programa ejecutable, destacando su importancia en la transformación del código compilado en un programa funcional y listo para la ejecución.

4. **Describa las diferencias clave entre los tipos de datos derivados y primarios en C++.**
   - En C++, los tipos de datos primarios representan valores básicos como enteros y caracteres, mientras que los derivados incluyen estructuras, clases y punteros, que se componen de tipos primarios o de sí mismos. Los tipos primarios son simples y ocupan una cantidad fija de memoria, mientras que los tipos derivados pueden ser más complejos y flexibles.

5. **Defina qué significa inicializar y declarar una variable.**
   - Declarar reserva espacio en memoria (ejemplo: `int x;`), inicializar asigna valor durante la declaración (ejemplo: `int y = 10;`).

6. **¿Qué es la sobrecarga de funciones en C++ y cuáles son sus beneficios?**
   - La sobrecarga de funciones permite definir múltiples funciones con el mismo nombre, pero diferentes parámetros. Los beneficios incluyen la claridad del código y la flexibilidad, ya que se pueden adaptar funciones a distintos tipos o cantidades de datos.
7. **¿Qué es un puntero y cómo se utiliza? Explique con un ejemplo de la vida real.**
   - Un puntero en C++ almacena la dirección de memoria de otra variable. Ejemplo: `int* ptr = &x;`.

8. **¿Una variable global almacena el valor original de una operación en una función o una copia? Explique su respuesta. Explique por qué se elige usar variables globales en lugar de locales en ciertos contextos.**
   - Una variable global almacena el valor original en una función. Se prefiere su uso en lugar de variables locales en ciertos contextos para compartir información entre funciones o cuando su vida útil debe extenderse a lo largo del programa.

9. **Investigue y explique tres métodos comunes de la biblioteca string en C++.**
   - Algunos métodos son `length()` para obtener la longitud, `append()` para concatenar y `substr()` para extraer subcadenas.

10. **¿Cuál es la principal diferencia entre un bucle do-while y un bucle while?**
    - Un bucle do-while garantiza al menos una ejecución, ya que evalúa la condición al final del bucle.

11. **¿Es permitido almacenar funciones en una estructura en C++? En el caso de los datos, ¿se pueden encapsular en miembros privados y públicos dentro de una estructura? Explique su respuesta.**
    - En C++, es permitido almacenar funciones en una estructura y encapsular datos en miembros privados y públicos. Esto se logra mediante el uso de clases en lugar de estructuras.

12. **Explique por qué es útil y común dividir el código en archivos .hpp, .cpp y main.cpp en C++. Describa el propósito específico de cada tipo de archivo.**
    - Dividir el código facilita la organización y mantenimiento. Los archivos .hpp contienen declaraciones, .cpp implementaciones, y main.cpp la función principal del programa.

13. **Defina qué es el Type Casting en C++ y explique su utilidad. Proporcione ejemplos de situaciones en las que se emplea el Type Casting y cómo se realiza.**
    - Convertir un tipo de dato a otro. Ejemplo: `int x = (int)3.14;`.

14. **¿Por qué la sentencia goto no es recomendable en programación moderna? Mencione ejemplos de cómo se pueden lograr los mismos resultados sin el uso de goto.**
    - La sentencia goto es desaconsejada por su impacto en la legibilidad y estructura del código. Pueden lograrse resultados similares con estructuras de control más modernas como bucles y condicionales.

15. **¿Dónde y cómo se guardan las variables que se crean en C++? Explique la diferencia entre el almacenamiento de variables locales y globales.**
    - Variables locales en la stack y las globales en el heap.

16. **¿Cuál es la diferencia entre pasar parámetros por valor, por referencia y por puntero?**
    - Por valor crea copia, por referencia permite modificar original, por puntero proporciona dirección de memoria.

17. **Cuando se usa un puntero para apuntar a un arreglo en C++, ¿a qué valor o dirección apunta inicialmente? Describa cómo sería la forma de acceder a todos los datos de ese arreglo mediante el puntero.**
    - Apunta a la primera posición. Acceder a todos los datos se realiza moviéndose a través del puntero.

18. **Explique para qué son empleados los punteros dobles en C++. Proporcione ejemplos de situaciones en las que los punteros dobles son necesarios o beneficiosos.**
    - Punteros dobles son utilizados para almacenar la dirección de un puntero. Beneficios incluyen manipulación de punteros y facilitar el acceso a estructuras de datos complejas.

19. **¿Cuál es la diferencia entre un break y un continue en los bucles de C++?**
    - `break` se utiliza para salir completamente del bucle, `continue` se emplea para saltar a la siguiente iteración.

20. **¿Para qué se utiliza la directiva #ifndef?**
    - Evita la inclusión repetida de un archivo de encabezado o bloque de código en un programa.

21. **¿Qué es el puntero this en C++?**
    - Un puntero implícito que apunta al objeto para el cual se invocó un miembro de clase.

22. **¿Qué es un puntero nullptr?**
    - Es un puntero implícito que apunta al objeto para el cual se invocó un miembro de clase. Es una referencia al objeto actual y se utiliza dentro de los métodos de una clase para acceder a los miembros de esa instancia específica de la clase. El uso de this permite diferenciar entre los miembros de la clase y los parámetros locales que puedan tener el mismo nombre.
23. **¿Cuál es la diferencia entre un arreglo y una lista en C++?**
    - La principal diferencia entre un arreglo y una lista radica en la naturaleza estática y fija de los arreglos en comparación con la naturaleza dinámica y flexible de las listas. Los arreglos son estáticos y de tamaño fijo, mientras que las listas pueden crecer o reducir su tamaño dinámicamente.

24. **¿Qué es una función prototipo?**
    - Es una declaración anticipada de una función en un programa. Se utiliza para informar al compilador sobre la existencia de una función antes de que se utilice o se defina en el programa principal. La función prototipo incluye el tipo de retorno de la función, su nombre y los tipos de sus parámetros, pero no contiene el cuerpo real de la función. 

25. **¿Investigue qué es un memory leak?**
    - Es una pérdida gradual de memoria en un programa, que ocurre cuando el programador omite liberar la memoria asignada dinámicamente mediante funciones como "malloc". Esta omisión puede tener consecuencias negativas, ya que la cantidad de memoria utilizada por el programa sigue aumentando con el tiempo, agotando los recursos del sistema y afectando el rendimiento general, incluso pudiendo causar inestabilidad en el programa o el sistema operativo.

## Parte Automatización – Makefile:

1. **¿Qué suelen contener las variables CC, CFLAGS, CXXFLAGS y LDFLAGS en un makefile?**
    - Las variables CC, CFLAGS, CXXFLAGS y LDFLAGS son fundamentales para personalizar las opciones de compilación y enlace. CC especifica el compilador, CFLAGS define opciones para la compilación, CXXFLAGS hace lo mismo para C++, y LDFLAGS configura opciones para el enlazador. Estas variables ofrecen flexibilidad al permitir la adaptación de las configuraciones sin modificar directamente las reglas de compilación en el Makefile, facilitando así el proceso de construcción de manera eficiente y configurable.

2. **¿De qué se compone una regla en un Makefile?**
    - Un archivo Makefile consta de tres elementos esenciales: el target (resultado deseado), los prerequisitos (archivos o acciones necesarios antes de construir o actualizar el target) y los comandos (instrucciones para la construcción o actualización). El Makefile define cómo lograr un target específico en base a sus prerequisitos, y cuando se ejecuta Make, examina las fechas de modificación de los prerequisitos para determinar si es necesario ejecutar los comandos asociados al target y mantenerlo actualizado.

3. **Defina qué es un target y cómo se relaciona con sus prerequisitos.**
    - Un "target" es un resultado específico definido por reglas que indican cómo construirlo o actualizarlo. Representado por un nombre, como un archivo o comando, tiene "prerequisitos" (archivos o acciones necesarios) y "comandos" (instrucciones para construir). Make utiliza timestamps para decidir si un target debe reconstruirse, comparando fechas de modificación de prerequisitos. En resumen, en un Makefile, los targets representan resultados, los prerequisitos son condiciones, y las reglas describen cómo construir o actualizar los targets.

4. **¿Para qué se utiliza la bandera -I, -c y -o del compilador gcc?**
    - Las banderas son esenciales para personalizar el proceso de compilación, ofreciendo mayor flexibilidad y control en el proceso de compilación. La bandera -I se emplea para añadir directorios adicionales a la búsqueda de archivos de encabezado, facilitando la inclusión de encabezados en ubicaciones no estándar.  La bandera -c señala que solo se realice la compilación, generando archivos objeto (.o) en lugar de un ejecutable final.  La bandera -o permite especificar el nombre del archivo de salida generado por el compilador. 

5. **¿Cómo se definen y se utilizan las variables en un Makefile? ¿Qué utilidad tienen?**
    - Las variables se definen con nombre = valor o nombre := valor y almacenan información como directorios o opciones de compilador. Son esenciales para mejorar la mantenibilidad al centralizar configuraciones, proporcionan flexibilidad al adaptarse a distintos entornos, aumentan la legibilidad al evitar repeticiones, favorecen la reutilización del código entre proyectos similares y facilitan la adaptabilidad a diferentes sistemas operativos o entornos de desarrollo. 

6. **¿Qué utilidad tiene un @ en un Makefile?**
    - El símbolo @ se utiliza para suprimir la salida de la línea de comando que se ejecuta. Es una forma de hacer que la ejecución de una regla sea silenciosa, evitando que Make imprima la línea de comando antes de ejecutarla.

7. **¿Para qué se utiliza .PHONY en un Makefile?**
    - Se utiliza para indicar a Make que ciertos objetivos no corresponden a archivos reales y, por lo tanto, no debe buscar ni comprobar la existencia de archivos con esos nombres. Esto es útil cuando se tienen reglas que no generan archivos con el mismo nombre que el objetivo y evita conflictos con archivos reales que pudieran tener el mismo nombre.

---

## Bibliografía:

[1] https://stackoverflow.com/
[2] https://devdocs.io/cpp/
[3] https://en.cppreference.com/w/
