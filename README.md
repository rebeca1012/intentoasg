# Informe de la segunda etapa del proyecto

## Autores:

Rebeca Ledesma 15-10771

Diego Lezama 15-10780

## Tecnología utilizada:

Para este proyecto se utilizó el lenguaje de programación Python, y fue escogido porque ambos integrantes
están más familiarizados con él que con los demás lenguajes propuestos, y además es un lenguaje sencillo de usar y cuenta con abundante documentación en línea. 

Adicionalmente, escogimos el módulo llamado Python Lex-Yacc (PLY) para la implementación del Lexer, que es la primera etapa del proyecto, y también será utilizado para las próximas. Es un módulo que también cuenta con bastante documentación, es bastante directo de usar, proporciona funciones muy útiles que simplifican el desarrollo y también es fácil de amoldar para lo que se quiere lograr.

## Resumen de la implementación:

Se creó el archivo pparser.py donde se implementó el parser para Asgard. 

En primer lugar, se definió la precendencia para los operadores.

Luego, se creó la gramática implementando una función dedicada para cada una de las reglas.

También se incluye el manejo de errores en el archivo pparser.py.

Por otro lado, se creó un archivo "clases.py" donde están las clases auxiliares para la creación del Abstract Syntax Tree (AST).

Finalmente, se utilizó el AST para estructurar la salida de los datos como se estableció en el enunciado de esta etapa.

PD: Se logró hacer la tabla del parse pero no se logró construir el AST, por ende, la impresión del AST no se llevó acabo.

*inserte meme adecuado de sufrimiento*

## Ejecución:

Para ejecutar el programa es necesario tener un archivo con los datos del lexer y luego ejecutar el siguiente comando:

>./SintAsgard

Una vez se ejecuta, es necesario introducir en la línea de comando el nombre del archivo.

En caso de no contar con el modulo ply de python, puede instalarlo utilizando el siguiente comando:

>pip install ply

# Dificultades en la implementación:

Una de las primeras dificultades que surgió para la segunda etapa del proyecto fue crear la gramática para
que expresara exactamente las cosas que se requieren. Y luego, fue crear una a una las funciones para
ello.

La más grande dificultad fue la creación de la estructura del AST. Se escogió hacerlo como un árbol que 
tiene una raíz y sus nodos son hijos y tienen hijos. Lograr que los tipos de datos entraran en el lugar
correcto fue bastante difícil.

Otra dificultad fue imprimir el AST tal como lo pedía el enunciado. Se hizo varias iteraciones en el archivo
clases.py para lograr que se imprimiera la estructura correcta.