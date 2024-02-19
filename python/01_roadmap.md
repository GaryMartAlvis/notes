# PYTHON ROADMAP

## Base

1. Caracteristicas de python
2. Instalación de python
3. Editor de código / IDE
4. Sistema de gestión de paquetes python (pip)
5. Entornos virtuales
6. Estructura de python
7. Zen de python

<details>
<summary>
8. Conversiones del lenguaje (PEP8) y codigo limpio
</summary>

> **Indentación:** Utiliza espacios en lugar de tabulaciones para la indentación y sigue la convención de 4 espacios por nivel de indentación.

> **Longitud de línea:** Limita cada línea de código a 79 caracteres como máximo. Para líneas largas, puedes utilizar la continuación implícita o explícita.

> **Nombres de variables:** Utiliza nombres descriptivos para tus variables, evitando abreviaturas excesivamente cortas o crípticas. Usa minúsculas y guiones bajos para separar palabras en nombres de variables compuestas (snake_case).

> **Nombres de funciones y métodos:** Sigue las mismas convenciones que para los nombres de variables, pero usa minúsculas y palabras separadas por guiones bajos.

> **Comentarios:** Utiliza comentarios para explicar el propósito de secciones de código, especialmente si no es obvio. Mantén los comentarios actualizados si cambia el código.

> **Espacios en blanco:** Utiliza espacios en blanco de manera consistente para mejorar la legibilidad. Deja una línea en blanco al final del archivo y después de definiciones de clase y funciones.

> **Importaciones:** Importa módulos de manera ordenada, agrupándolos primero por módulos de la biblioteca estándar, seguidos de importaciones de terceros y luego importaciones locales. Separa los grupos de importaciones con una línea en blanco.

> **Concordancia con PEP 8:** Utiliza herramientas como pylint, flake8 o black para verificar automáticamente el cumplimiento con las convenciones de estilo de Python. Estas herramientas pueden identificar y corregir automáticamente muchos problemas de estilo en tu código.

> **Refactorización:** Si encuentras que tu código no sigue las mejores prácticas de limpieza y legibilidad, considera refactorizarlo. A veces, reorganizar el código puede hacerlo más claro y fácil de entender.

> **Revisión de código:** Si trabajas en un equipo, realiza revisiones de código periódicas para asegurarte de que todos estén siguiendo las mismas convenciones y mejores prácticas.
</details>

9. Git

## Basic Level

1. Variables
2. Strings - indexing y slicing
3. Mutabilidad e inmutabilidad
> Tipo de datos
4. Tuplas
5. Listas
6. Sets
7. Frozenset
8. Diccionarios
> Estructuras de control
> 
> Condicionales
9. if else
10. if else encadenados
11. if else anidado
12. operador ternario
> Loop
13. for loop
14. for loop - range
15. for loop - enumerate
16. while
17. break
18. continue

## Intermediate Level

> Funciones
1. Funciones
2. Parámetros de funciones
3. Scopes
<details>
<summary>
4. Arguments
</summary>

* Positional Args

```
def imprimir_nombre(primer_nombre,
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido):
    print(f'Bienvenido {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido} al curso de python.')

imprimir_nombre('Gary', 'Yonathan', 'Martinez', 'Alvis')

```

* Keyword Args

```
imprimir_nombre(segundo_apellido='Alvis', primer_nombre='Gary', primer_apellido='Martinez', segundo_nombre='Yonathan')
```

* Iterable unpacking
```
nombre_tupla = ('Gary','Yonathan','Martinez','Alvis')
imprimir_nombre(*nombre_tupla)
```

* Dictionary unpacking
```
nombre_dict = {'segundo_apellido':'Alvis', 'primer_nombre':'Gary', 'primer_apellido':'Martinez', 'segundo_nombre':'Yonathan'}
imprimir_nombre(**nombre_dict)
```

* Argumentos opcionales
```
def calcular_precio(nombre_prod, cant, precio_unt, descuento=0):
    precio_final = (cant * precio_unt) * (1 - descuento)
    print(f'El precio final para {nombre_prod} es: {precio_final}')

calcular_precio('Pantalones', 12, 120)
```
</details>

5. return
6. multiples return
7. *args
8. **kwargs
9. Funciones Lambda
> Funciones de orden superior
10. Map
11. Filter
12. Sorted
13. Reduce
14. Importaciones

## Advanced Level

1. Intro Programación Orientada a Objetos (POO)
2. Clases y métodos
3. Encapsulamiento, PRIVADO o PÚBLICO
4. Encapsulamiento, properties
5. Herencia
6. Herencia de propiedades
7. Línea de herencia
8. Herencia de métodos
