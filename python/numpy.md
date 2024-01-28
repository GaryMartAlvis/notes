# NUMPY
### Biblioteca cientifica que proporciona soporte para arreglos multidimensionales, operaciones matriciales y funciones matemáticas de alto rendimiento. Su uso es especialmente importante en áreas como:
> 1. Operaciones Numéricas Eficientes
> 2. Álgebra Lineal
> 3. Generación de Números Aleatorios
> 4. Manipulación de Datos
> 5. Integración con Otras Bibliotecas

* Instalación: <code>pip install numpy</code>
* Importación: <code>import numpy as np</code>
---
### Creación  de arrelos

| Sintanxi    | Uso                                                                    | Ejempo de uso        |
| ----------- | ---------------------------------------------------------------------- | -------------------- |
| np.array()  | Crea un array de NumPy a partir de una lista o tupla                   | np.array(arr)        |
| np.zeros()  | Crea un array de ceros con la forma especificada.                      | np.zeros((2, 3))     |
| np.ones()   | Crea un array de unos con la forma especificada.                       | np.ones((3, 2))      |
| np.empty()  | Crea un array sin inicializar sus elementos.                           | np.empty((2, 2))     |
| np.arange() | Crea un array con valores espaciados uniformemente dentro de un rango. | np.arange(0, 10, 2)  |
| np.linspace | Crea un array con valores espaciados linealmente dentro de un rango.   | np.linspace(0, 1, 5) |
| np.eye      | Crea una matriz identidad.                                             | np.eye(3)            |

### Operaciones con arreglos

| Sintaxi          | Uso                                                   | Ejempo de uso                |
| ---------------- | ----------------------------------------------------- | ---------------------------- |
| np.shape()       | Retorna la forma (dimensiones) del array.             | np.shape(arr)                |
| np.ndim()        | Retorna el número de dimensiones del array.           | np.ndim(arr)                 |
| np.size()        | Retorna el número total de elementos en el array.     | np.size(arr)                 |
| np.reshape()     | Cambia la forma del array.                            | arr.reshape((2, 3))          |
| np.flatten()     | Retorna una copia del array aplanado a una dimensión. | np.flatten(arr)              |
| np.transpose()   | Transpone el array (intercambia filas por columnas).  | np.transpose(arr)            |
| np.concatenate() | Concatena dos o más arrays a lo largo de un eje.      | np.concatenate((arr1, arr2)) |
| np.split()       | Divide un array en subarrays a lo largo de un eje.    | np.split(arr, 3)             |
| np.vstack()      | Apila arrays verticalmente.                           | np.vstack((arr1, arr2))      |
| np.hstack()      | Apila arrays horizontalmente.                         | np.hstack((arr1, arr2))      |

### Operaciones matemáticas

| Sintaxi       | Uso                                                          | Ejempo de uso           |
| ------------- | ------------------------------------------------------------ | ----------------------- |
| np.add()      | Suma elementos de dos arreglos.                              | np.add(arr1, arr2)      |
| np.subtract() | Resta elementos de un arreglo a otro.                        | np.subtract(arr1, arr2) |
| np.multiply() | Multiplica elementos de dos arreglos.                        | np.multiply(arr1, arr2) |
| np.divide()   | Divide elementos de un arreglo entre los elementos de otro.  | np.divide(arr1, arr2)   |
| np.power()    | Eleva cada elemento de un arreglo a una potencia dada.       | np.power(arr, 2)        |
| np.sqrt()     | Calcula la raíz cuadrada de cada elemento de un arreglo.     | np.sqrt(arr)            |
| np.exp()      | Calcula la exponencial de cada elemento de un arreglo.       | np.exp(arr)             |
| np.log()      | Calcula el logaritmo natural de cada elemento de un arreglo. | np.log(arr)             |
| np.sin()      | Calcula el seno de cada elemento de un arreglo.              | np.sin(arr)             |
| np.cos()      | Calcula el coseno de cada elemento de un arreglo.            | np.cos(arr)             |
| np.tan()      | Calcula la tangente de cada elemento de un arreglo.          | np.tan(arr)             |

### Operaciones estadísticas

| Sintaxi     | Uso                                                            | Ejempo de uso  |
| ----------- | -------------------------------------------------------------- | -------------- |
| np.mean()   | Calcula la media de los elementos de un arreglo.               | np.mean(arr)   |
| np.median() | Calcula la mediana de los elementos de un arreglo.             | np.median(arr) |
| np.std()    | Calcula la desviación estándar de los elementos de un arreglo. | np.std(arr)    |
| np.var()    | Calcula la varianza de los elementos de un arreglo.            | np.var(arr)    |
| np.min()    | Encuentra el valor mínimo en un arreglo.                       | np.min(arr)    |
| np.max()    | Encuentra el valor máximo en un arreglo.                       | np.max(arr)    |
| np.sum()    | Calcula la suma de los elementos de un arreglo.                | np.sum(arr)    |

### Funciones de comparación y lógicas

| Sintaxi            | Uso                                                       | Ejempo de uso                               |
| ------------------ | --------------------------------------------------------- | ------------------------------------------- |
| np.equal()         | Compara elementos para igualdad.                          | np.equal(arr1, arr1)                        |
| np.not_equal()     | Compara elementos para desigualdad.                       | np.not_equal(arr1, arr2)                    |
| np.less()          | Compara elementos para "menor que".                       | np.less(arr1, arr2)                         |
| np.less_equal()    | Compara elementos para "menor o igual que".               | np.less_equal(arr1, arr2)                   |
| np.greater()       | Compara elementos para "mayor que".                       | np.greater(arr1, arr2)                      |
| np.greater_equal() | Compara elementos para "mayor o igual que".               | np.greater_equal(arr1, arr2)                |
| np.logical_and()   | Realiza una operación lógica "y" elemento por elemento.   | np.logical_and([True, False], [True, True]) |
| np.logical_or()    | Realiza una operación lógica "o" elemento por elemento.   | np.logical_or([True, False], [True, True])  |
| np.logical_not()   | Realiza una operación lógica "not" elemento por elemento. | np.logical_not([True, False])               |

### Funciones especiales

| Sintaxi       | Uso                                                   | Ejempo de uso                               |
| ------------- | ----------------------------------------------------- | ------------------------------------------- |
| np.fft.fft()  | Transformada rápida de Fourier                        | np.fft.fft(arr)                             |
| np.fft.ifft() | Transformada inversa de Fourier.                      | np.fft.ifft(arr)                            |
| np.unique()   | Encuentra elementos únicos en un array.               | np.unique(arr)                              |
| np.where()    | Devuelve elementos seleccionados según una condición. | np.where([True, False, True], [1, 2, 3], 0) |

### Funciones de manipulación de datos

| Sintaxi      | Uso                                      | Ejempo de uso      |
| ------------ | ---------------------------------------- | ------------------ |
| np.copy()    | Copia el contenido de un array a otro.   | np.copy([1, 2, 3]) |
| np.sort()    | Ordena elementos de un array.            | np.sort(arr)       |
| np.argsort() | Devuelve índices de elementos ordenados. | np.argsort(arr)    |
| np.amax()    | Devuelve el valor máximo de un array.    | np.amax(arr)       |
| np.amin()    | Devuelve el valor mínimo de un array.    | np.amin(arr)       |