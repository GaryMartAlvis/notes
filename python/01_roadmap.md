# PYTHON ROADMAP

***
## Base
***

<details>
<summary>
Caracteristicas de python
</summary>

    - Python es un lenguaje de programación de alto nivel.
    - Es interpretado y de tipado dinámico.
    - Tiene una sintaxis simple y legible.
</details>

<details>
<summary>
Instalación de python
</summary>

    - Descarga el instalador desde el sitio web oficial de Python.
    - Sigue las instrucciones del instalador para tu sistema operativo.
    - web oficial: https://www.python.org/downloads/
    - Se recomienda instalar la última versión estable.
</details>

<details>
<summary>
Editor de código / IDE
</summary>

    - Algunos editores de código populares para Python son VSCode, PyCharm y Sublime Text.
    - Los IDEs como PyCharm ofrecen características adicionales como depuración integrada y administración de proyectos.
</details>

<details>
<summary>
Sistema de gestión de paquetes python (pip)
</summary>

    - `pip` es la herramienta estándar para instalar y gestionar paquetes en Python.
    - Puedes instalar paquetes utilizando el comando `pip install nombre_paquete`.
    
</details>

<details>

<summary>
Entornos virtuales
</summary>

    - Los entornos virtuales permiten aislar las dependencias de tus proyectos.
    - Crea un entorno virtual con `python -m venv nombre_entorno` y actívalo con `nombre_entorno\Scripts\activate`.
</details>

<details>
<summary>
Estructura de python
</summary>

    - Python utiliza indentación para definir bloques de código.
    - La convención es usar 4 espacios para cada nivel de indentación.
</details>

<details>
<summary>
Zen de python
</summary>

    - El Zen de Python es una colección de 19 principios que guían el diseño del lenguaje.
    - Puedes verlo ejecutando `import this` en tu intérprete de Python.
    - Disponible en https://www.python.org/dev/peps/pep-0020/
</details>

<details>
<summary>
Conversiones del lenguaje (PEP8) y codigo limpio
</summary>

    - Indentación: 4 espacios por nivel.
    - Longitud de línea: Máximo 79 caracteres.
    - Nombres: Descriptivos, minúsculas, guiones bajos.
    - Comentarios: Explicativos, actualizados.
    - Espacios en blanco: Consistentes.
    - Importaciones: Ordenadas, agrupadas.
    - Herramientas: pylint, flake8, black.
    - Refactorización: Mejorar legibilidad.
    - Revisión de código: Asegurar buenas prácticas.
</details>

<details>
<summary>
Git
</summary>

    - Sistema de control de versiones para seguimiento de cambios en el código.
    - Permite trabajar en equipo, colaborar y compartir código.
    - Comandos básicos: `git init`  , `git add` , `git commit`, `git push`, `git pull`.
</details>

***
## Basic Level
***

<details>
<summary>
Strings - indexing y slicing
</summary>

    - Cadenas de caracteres.
    - Indexación con [] para acceder a caracteres.
    - Slicing para obtener subcadenas.

    ```
    mensaje = "Hola Mundo"
    print(mensaje[0])  # H
    print(mensaje[2:5])  # la 
    ```
</details>

<details>
<summary>
Mutabilidad e inmutabilidad
</summary>

    - Algunas variables son mutables (se pueden modificar) y otras inmutables.
    - Las listas son mutables, las strings inmutables.
</details>

### Tipo de datos

<details>
<summary>
Variables
</summary>

    - Almacenan datos en memoria.
    - Diferentes tipos: int, float, str, bool, etc.
    - Se declaran con nombre_variable = valor.
</details>

<details>
<summary>
Tuplas
</summary>

    - Las tuplas son secuencias inmutables de elementos.
    - Se definen utilizando paréntesis y pueden contener cualquier tipo de dato.
    
    ```
    tupla = (1, "dos", True)
    ```
</details>

<details>
<summary>
Listas
</summary>

    - Las listas son secuencias mutables de elementos.
    - Se definen utilizando corchetes y pueden contener cualquier tipo de dato.

    ```
    lista = [1, 2, 3, "cuatro"]
    ```
</details>

<details>
<summary>
Sets
</summary>

    - Los sets son colecciones no ordenadas de elementos únicos.
    - Se definen utilizando llaves o la función set().
    
    ```
    conjunto = {1, 2, 3, 4}
    ```
</details>

<details>
<summary>
Frozenset
</summary>

    - Frozenset es similar a un set, pero es inmutable.
    - Se define utilizando la función frozenset().
    
    ```
    conjunto_inmutable = frozenset({1, 2, 3})
    ```
</details>

<details>
<summary>
Diccionarios
</summary>

    - Los diccionarios son colecciones de pares clave-valor.
    - Se definen utilizando llaves y los elementos se acceden mediante claves.

    ```
    diccionario = {"nombre": "Juan", "edad": 30}
    ```
</details>

### Estructuras de control

#### Condicionales

<details>
<summary>
if else
</summary>

    - Para tomar decisiones basadas en una condición.
    
    ```
    if x > 5:
        print("Mayor que 5")
    else:
        print("Menor o igual que 5")
    ```
</details>

<details>
<summary>
if else encadenados
</summary>

    - Para tomar decisiones múltiples.

    ```
    if x > 5:
        print("Mayor que 5")
    elif x == 5:
        print("Igual a 5")
    else:
        print("Menor que 5")
    ```
</details>

<details>
<summary>
if else anidado
</summary>

    - Para decisiones más complejas.

    ```
    if x > 0:
        if x % 2 == 0:
            print("Número positivo y par")
        else:
            print("Número positivo e impar")
    else:
        print("Número negativo")
    ```
</details>

<details>
<summary>
operador ternario
</summary>

    - Para expresar condicionales en una sola línea.

    ```
    mensaje = "par" if x % 2 == 0 else "impar"
    print(mensaje)
    ```
</details>


#### Loop

<details>
<summary>
for loop
</summary>

    - Para iterar sobre una secuencia.
    
    ```
    for i in range(5):
        print(i)
    ```
</details>

<details>
<summary>
for loop - range
</summary>

    - Para generar secuencias numéricas.

    ```
    for i in range(1, 6):
    print(i)
    ```
</details>

<details>
<summary>
for loop - enumerate
</summary>

    - Para obtener índices y elementos.

    ```
    for indice, valor in enumerate(["a", "b", "c"]):
        print(indice, valor)
    ```
</details>

<details>
<summary>
while
</summary>

    - Para iterar mientras se cumple una condición.

    ```
    x = 0
    while x < 5:
        print(x)
        x += 1
    ```
</details>

<details>
<summary>
break
</summary>

    - Para salir de un loop antes de completar todas las iteraciones.

    ```
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```
</details>

<details>
<summary>
continue
</summary>

    - Para pasar a la siguiente iteración sin completar el resto del bloque.
    
    ```
    for i in range(5):
        if i == 2:
            continue
        print(i)
    ```
</details>

***
## Intermediate Level
***

### Funciones

<details>
<summary>
Funciones
</summary>

    - Las funciones son bloques de código reutilizables que realizan una tarea específica.
    - Se definen utilizando la palabra clave def.

    ```
    def saludar(nombre):
        print("Hola", nombre)
    ```
</details>

<details>
<summary>
Parámetros de funciones
</summary>

    - Los parámetros permiten pasar información a las funciones.
    - Pueden ser posicionales o de palabras clave.

    ```
    def suma(a, b):
        return a + b

    resultado = suma(2, 3)
    print(resultado)
    ```
</details>

<details>
<summary>
Scopes
</summary>

    - El scope de una variable determina dónde puede ser utilizada dentro del código.
    - Las variables definidas dentro de una función tienen un scope local.

    ```
    def ejemplo():
        x = 5
        print(x)

    ejemplo()
    ```
</details>

<details>
<summary>
return
</summary>

    - La declaración return permite devolver un valor desde una función.
    - Puede devolver múltiples valores separados por comas.

    ```
    def suma(a, b):
        return a + b

    resultado = suma(2, 3)
    print(resultado)
    ```
</details>

<details>
<summary>
multiples return
</summary>

    - Una función puede devolver múltiples valores utilizando una tupla.

    ```
    def coordenadas():
        return 1, 2, 3

    x, y, z = coordenadas()
    print(x, y, z)
    ```
</details>

<details>
<summary>
Arguments
</summary>

    - Los argumentos de una función pueden ser de diferentes tipos y su manejo es flexible en Python.
    - Positional Args: Argumentos posicionales simples.

    - Positional Args

    ```
    def imprimir_nombre(primer_nombre,
                        segundo_nombre,
                        primer_apellido,
                        segundo_apellido):
        print(f'Bienvenido {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido} al curso de python.')

    imprimir_nombre('Gary', 'Yonathan', 'Martinez', 'Alvis')
    ```

    - Keyword Args

    ```
    imprimir_nombre(segundo_apellido='Alvis', primer_nombre='Gary', primer_apellido='Martinez', segundo_nombre='Yonathan')
    ```

    - Iterable unpacking
    ```
    nombre_tupla = ('Gary','Yonathan','Martinez','Alvis')
    imprimir_nombre(*nombre_tupla)
    ```

    - Dictionary unpacking
    ```
    nombre_dict = {'segundo_apellido':'Alvis', 'primer_nombre':'Gary', 'primer_apellido':'Martinez', 'segundo_nombre':'Yonathan'}
    imprimir_nombre(**nombre_dict)
    ```

    - Argumentos opcionales
    ```
    def calcular_precio(nombre_prod, cant, precio_unt, descuento=0):
        precio_final = (cant * precio_unt) * (1 - descuento)
        print(f'El precio final para {nombre_prod} es: {precio_final}')

    calcular_precio('Pantalones', 12, 120)
    ```
</details>

<details>
<summary>
*args
</summary>

    - *args se utiliza para pasar un número variable de argumentos posicionales a una función.
    - args recoge estos argumentos en una tupla dentro de la función.
    - args recoge estos argumentos en una tupla dentro de la función.
    - Los nombres args es una convención, pero el asterisco (*) es lo que indica que se están pasando múltiples argumentos posicionales.

    ```
    def suma(*args):
        return sum(args)

    resultado = suma(5,5,5,100)
    print(f'El resultado de la funcion suma es: {resultado}')
    ```
</details>

<details>
<summary>
**kwargs
</summary>

    - **kwargs se utiliza para pasar un número variable de argumentos de palabras clave a una función.
    - kwargs recoge estos argumentos en un diccionario dentro de la función.

    - Se utiliza para pasar un número variable de argumentos de palabras clave (argumentos con nombres) a una función.
    - **kwargs recoge estos argumentos en un diccionario dentro de la función.
    - Los nombres kwargs es una convención, pero el doble asterisco (**) es lo que indica que se están pasando múltiples argumentos de palabras clave.

    ```
    def conectar_db(**kwargs):
        nombre = kwargs.get('nombre_db','defaul')
        user = kwargs['usuario']
        password = kwargs['password']
        print(f'Conectando a la base de datos: {nombre}')
        print(f'login with: {user} - {password}')

    conectar_db(nombre_db='produccion', usuario='admin', password='01234', port=5002)
    ```
</details>

<details>
<summary>
Uso de Argument, *args y **kwargs
</summary>

    ```
    def calcular_precio(*args, **kwargs):
        precio_total = sum(args)
        descuento = kwargs.get('descuento', 0)  # Obtiene el valor de 'descuento' o 0 si no está presente
        impuestos = kwargs.get('impuestos', 0)  # Obtiene el valor de 'impuestos' o 0 si no está presente
        precio_total *= 1 - descuento
        precio_total *= 1 + impuestos 
        return precio_total

    lista_productos = [100, 65, 30]
    dict_opcionales = {
        'descuento': 0.2,
        'impuestos': 0.01
    }

    precio_compra = calcular_precio(*lista_productos, **dict_opcionales)
    print(precio_compra)
    ```
</details>

<details>
<summary>
Funciones Lambda
</summary>

    - Las funciones lambda son funciones anónimas de una sola línea.
    - Se utilizan para crear funciones simples sin necesidad de definirlas por separado.

    ```
    cuadrado = lambda x: x ** 2
    print(cuadrado(5))  # Salida: 25
    ```
</details>

### Funciones de orden superior

<details>
<summary>
Map
</summary>

    - La función map aplica una función a cada elemento de un iterable.
    - Retorna un objeto map que se puede convertir en una lista.

    ```
    lista = [1, 2, 3, 4, 5]
    cuadrados = map(lambda x: x ** 2, lista)
    print(list(cuadrados))  # Salida: [1, 4, 9, 16, 25]
    ```
</details>

<details>
<summary>
Filter
</summary>

    - La función filter filtra los elementos de un iterable según una función de filtro.
    - Retorna un objeto filter que se puede convertir en una lista.

    ```
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = filter(lambda x: x % 2 == 0, numeros)
    print(list(pares))  # Salida: [2, 4, 6, 8, 10]
    ```
</details>

<details>
<summary>
Sorted
</summary>

    - La función sorted ordena los elementos de un iterable.
    - Puede ordenar tanto listas como otros iterables.

    ```
    lista = [5, 2, 8, 1, 9]
    lista_ordenada = sorted(lista)
    print(lista_ordenada)  # Salida: [1, 2, 5, 8, 9]
    ```
</details>

<details>
<summary>
Reduce
</summary>

    - La función reduce aplica una función a pares de elementos sucesivos de un iterable.
    - Retorna un solo valor que es el resultado de aplicar la función de reducción a todos los elementos.

    ```
    from functools import reduce
    lista = [1, 2, 3, 4, 5]
    suma = reduce(lambda x, y: x + y, lista)
    print(suma)  # Salida: 15
    ```
</details>

<details>
<summary>
Importaciones
</summary>

    - Las importaciones permiten acceder a funcionalidades de otros módulos en Python.
    - Puedes importar módulos completos o partes específicas de ellos.

    ```
    import math
    print(math.sqrt(25))  # Salida: 5.0

    from math import sqrt
    print(sqrt(25))  # Salida: 5.0
    ```
</details>


***
## Advanced Level
***

<details>
<summary>
Intro Programación Orientada a Objetos (POO)
</summary>

    - La programación orientada a objetos es un paradigma de programación que utiliza objetos para modelar el mundo real.
    - En Python, todo es un objeto y se pueden definir clases y crear instancias de ellas.
</details>

<details>
<summary>
Clases y métodos
</summary>

    - Las clases son plantillas para crear objetos.
    - Los métodos son funciones definidas dentro de una clase que actúan sobre los objetos creados a partir de ella.

    ```
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self):
            print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años.')

    juan = Persona('Juan', 30)
    juan.saludar()
    ```
</details>

<details>
<summary>
Encapsulamiento, PRIVADO o PÚBLICO
</summary>

    - En Python, la encapsulación se logra mediante convenciones de nomenclatura.
    - Los miembros que comienzan con doble guion bajo (__) son tratados como privados y no deberían ser accesibles desde fuera de la clase.

    ```
    class Persona:
        def __init__(self, nombre, edad):
            self.__nombre = nombre
            self.__edad = edad

        def get_nombre(self):
            return self.__nombre

        def set_nombre(self, nombre):
            self.__nombre = nombre

    juan = Persona('Juan', 30)
    print(juan.get_nombre())  # Salida: Juan
    juan.set_nombre('Pedro')
    print(juan.get_nombre())  # Salida: Pedro
    ```
</details>

<details>
<summary>
Encapsulamiento, properties
</summary>

    - Las properties son una forma de encapsular los atributos de una clase y definir comportamientos personalizados para acceder y modificar esos atributos.

    ```
    class Persona:
        def __init__(self, nombre):
            self.__nombre = nombre

        @property
        def nombre(self):
            return self.__nombre

        @nombre.setter
        def nombre(self, valor):
            if isinstance(valor, str):
                self.__nombre = valor
            else:
                raise ValueError("El nombre debe ser una cadena de caracteres.")

    juan = Persona('Juan')
    print(juan.nombre)  # Salida: Juan
    juan.nombre = 'Pedro'
    print(juan.nombre)  # Salida: Pedro
    ```
</details>

<details>
<summary>
Herencia
</summary>

    - La herencia permite que una clase herede atributos y métodos de otra clase.
    - Esto promueve la reutilización de código y facilita la creación de jerarquías de clases.

    ```
    class Animal:
        def hacer_sonido(self):
            print("Haciendo sonido")

    class Perro(Animal):
        def hacer_sonido(self):
            print("Ladrando")

    perro = Perro()
    perro.hacer_sonido()  # Salida: Ladrando
    ```
</details>

<details>
<summary>
Herencia de propiedades
</summary>

    - Las clases hijas heredan las propiedades (atributos y métodos) de las clases padre.
    - Pueden sobrescribir los métodos de la clase padre para personalizar su comportamiento.

    ```
    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre

    class Perro(Animal):
        def __init__(self, nombre, raza):
            super().__init__(nombre)
            self.raza = raza

    perro = Perro("Fido", "Labrador")
    print(perro.nombre)  # Salida: Fido
    print(perro.raza)    # Salida: Labrador
    ```
</details>

<details>
<summary>
Línea de herencia
</summary>

    - Una clase puede heredar de múltiples clases, formando una línea de herencia.
    - Los atributos y métodos de todas las clases padre están disponibles en la clase hija.

    ```
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    c = C()
    ```
</details>

<details>
<summary>
Herencia de métodos
</summary>

    - La herencia permite que las clases hijas hereden métodos de las clases padre.
    - Estos métodos pueden ser utilizados directamente por las clases hijas.

    ```
    class A:
        def metodo(self):
            print("Método de A")

    class B(A):
        pass

    b = B()
    b.metodo()  # Salida: Método de A
    ```
</details>