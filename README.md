# Informe de la segunda etapa del proyecto

## Autores:

Rebeca Ledesma 15-10771

Diego Lezama 15-10780

## Tecnología utilizada:

Para este proyecto se utilizó el lenguaje de programación Python, y fue escogido porque ambos integrantes
están más familiarizados con él que con los demás lenguajes propuestos, y además es un lenguaje sencillo de usar y cuenta con abundante documentación en línea. 

Adicionalmente, escogimos el módulo llamado Python Lex-Yacc (PLY) para la implementación del Lexer, que es la primera etapa del proyecto, y también será utilizado para las próximas. Es un módulo que también cuenta con bastante documentación, es bastante directo de usar, proporciona funciones muy útiles que simplifican el desarrollo y también es fácil de amoldar para lo que se quiere lograr.

## Resumen de la implementación:

#Lexer (Taylor's version)
Se creó una nueva versión del Lexer con una clase  para que fuese más sencillo trabajarlo en conjunto con el Parser.

#Nueva etapa, nuevo parser
Se corrigieron pequeños errores en la gramática y además se logró implementar correctamente el AST (Auxilio, Señor, Tqm). 

#(Cara 'e) Tabla de símbolos
Para la tabla de símbolos se creó un nuevo archivo llamado Symboltable donde se implementó la estructura de la tabla de 
símbolos para el proyecto. Cuenta con tres atributos: un diccionario de símbolos donde se almacenarán los símbolos,
el nombre, y la tabla padre para el manejo de los scopes.

## Ejecución:

Para ejecutar el programa es necesario tener un archivo con los datos del lexer y luego ejecutar el siguiente comando:

>./ContAsgard

Una vez se ejecuta, es necesario introducir en la línea de comando el nombre del archivo.

En caso de no contar con el modulo ply de python, puede instalarlo utilizando el siguiente comando:

>pip install ply

# Dificultades en la implementación:

¿Por dónde empezar? Ok, no.

Una de las dificultades más grandes fue trabajar con cada objeto del AST y también de la tabla: ver hacia dónde y cómo
se enviaba la información y llevar orden de todo ello fue difícil. Lograr que los tipos de datos coincidieran, que estuvieran
correctos. 

