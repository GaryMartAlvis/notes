# PANDAS
### Biblioteca desarrollada sobre la base de NumPy, Pandas extiende las capacidades de NumPy al proporcionar estructura de datos como son los DataFrame y las Series que son esenciales para el análisis y manipulación de datos tabulares. Su uso es especialmente importante en para:
> 1. Análisis de datos
> 2. Procesameinto de datos
> 3. Transformación y limpieza de datos
> 4. Manipulación de datos temporales
> 5. Integración con visualizaciones gráficas
> 6. Análisis de datos financieros
> 7. Tratamiento de datos estructurados
> 8. Aprendizaje automático 
> 9. Automatizaciones con archivos cvs, excel y json 

* Instalación: <code>pip install pandas</code>
* Importación: <code>import pandas as pd</code>
***
Notas: La convención utilizada para nombrar una variable que contiene un DataFrame es 'df'.
***

<details>
<summary>Creación de DataFrames: Lectura y escritura de datos</summary>

| Sintaxi                                                    | Uso                                                                        |
| ---------------------------------------------------------- | -------------------------------------------------------------------------- |
| df = pd.read_csv('file.csv') / df.to_csv('file.csv')       | Lee/Guardar un archivo csv                                                 |
| df = pd.read_excel('file.xlsx') / df.to_excel('file.xlsx') | Lee/Guarda un archivo excel                                                |
| df =pd.read_json('file.json') / df.to_json('file.xlsx')    | Lee/Guarda un archivo json                                                 |
| ---                                                        |                                                                            |
| df = pd.DataFrame()                                        | Crear un DataFrame vacio para el almacenamiento de datos                   |
| df = pd.DataFrame(list, columns=['Col1'])                  | Convertir una lista en DataFrame y asignar nombre de columna               |
| df = pd.DataFrame(tupla, columns=['Col1'])                 | Convertir una tupla en DataFrame y asignar nombre de columna               |
| df = pd.DataFrame(array, columns=['Col1','Col2'])          | Convertir un array en DataFrame y asignar nombre a las columnas            |
| df = pd.DataFrame([dictionary])                            | Convertir un diccionario en DataFrame, la etiqueta es nombre de columna    |
| df = pd.read_json(json, orient='index').T                  | Convertir una varible en json y asigna el index como columan .T Transponer |

</details>

<details>
<summary>Exploración de datos</summary>

| Sintaxi       | Uso                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------- |
| df.head(n)    | Muestras las primeras n filas del DataFrame, si no se adiciona numero de filas por defecto muestra 10 |
| df.info()     | Muestra información sobre el DataFrame                                                                |
| df.describe() | Proporciona estadísticas descriptivas del DataFrame                                                   |
| df.shape      | Devuelve la forma (número de filas y columnas) del DataFrame                                          |

</details>

<details>
<summary>Selección y filtrado</summary>

| Sintaxi                   | Uso                                                         |
| ------------------------- | ----------------------------------------------------------- |
| df['columna']             | Selecciona una columna especifica                           |
| df[df['condición']]       | Filtra filas basadas en una condición                       |
| df.loc[filas, columnas]   | Accede a un grupo específico de filas y columnas            |
| df.iloc[filas, columnas]  | Accede a un grupo específico de filas y columnas por índice |
| df[df['col'].isin(lista)] | Filtra filas donde la columna esta en una lista             |

</details>

<details>
<summary>Manipulación de DataFrame</summary>

| Sintaxi                                           | Uso                                                 |
| ------------------------------------------------- | --------------------------------------------------- |
| df['nueva_col'] = df['col1'] + df['col2']         | Crea una nueva columna calculada                    |
| df.append(df2, ignore_index=True)                 | Añade filas de otro DataFrame                       |
| df.drop('columna', axis=1)                        | Elimina una columna                                 |
| df.drop(index=filas)                              | Elimina filas por índice                            |
| df.drop_duplicate()                               | Elimina duplicados en el DataFrame                  |
| df.dropna()                                       | Elimina filas con valores nulos                     |
| df.fillna(valor)                                  | Rellena los valores nulos con un valor especificado |
| df.sort_values('columna')                         | Ordena el DataFrame por una columna específica      |
| df.groupby('columna').agg({'otra_col':'funcion'}) | Agrega y aplica funciones a grupos de datos         |

</details>

<details>
<summary>Operaciones aritmeticas</summary>

| Sintaxi           | Uso                                            |
| ----------------- | ---------------------------------------------- |
| df.mean()         | Calcula la media de cada columna               |
| df.sum()          | Calcula la suma de cada columna                |
| df.std()          | Calcula la desviación estandar de cada columna |
| df.isnull().sum() | Cuenta los valores nulos en cada columna       |

</details>

<details>
<summary>Operaciones con cadenas</summary>

| Sintaxi                              | Uso                                                |
| ------------------------------------ | -------------------------------------------------- |
| df['columna'].str.lower()            | Convierte el contenido de una columna a minúsculas |
| df['columna'].str.contains('patron') | Verifica si una cadena contiene patrón             |

</details>

<details>
<summary>Operaciones de indexado</summary>

| Sintaxi                  | Uso                                                |
| ------------------------ | -------------------------------------------------- |
| df.set_index('columna')  | Establece una columna como índice                  |
| df.reset_index()         | Restablece el índice a los valores predeterminados |
| df.reindex(nuevo_indice) | Reorganiza el índice del DataFrame                 |

</details>

<details>
<summary>Operaciones con fechas</summary>

| Sintaxi                                   | Uso                                        |
| ----------------------------------------- | ------------------------------------------ |
| df['fecha'] = pd.to_datetime(df['fecha']) | Convierte una columna a tipo de dato fecha |
| df[df['fecha']] > '2024-01-31'            | Filtra filas basadas en una fecha          |
| df['fecha'].dt.year                       | Extrae el año de una columna de fecha      |
| df['fecha'].dt.month                      | Extrae el mes de una columna               |
| df['fecha'].dt.strftime('%d-%m-%Y')       | Cambia el formato de fecha                 |

</details>

<details>
<summary>Renombrar columnas</summary>

| Sintaxi                                        | Uso               |
| ---------------------------------------------- | ----------------- |
| df.rename(columns={'antigua_col':'nueva_col'}) | Renombra columnas |

</details>

<details>
<summary>Conversión de tipos de datos</summary>

| Sintaxi                                   | Uso                                       |
| ----------------------------------------- | ----------------------------------------- |
| df.astype({'col1':'float', 'col2':'int'}) | Convierte el tipo de dato de las columnas |

</details>

<details>
<summary>Mergin, concatenación y uniones</summary>

| Sintaxi                                         | Uso                                         |
| ----------------------------------------------- | ------------------------------------------- |
| pd.concat([df1, df2], axis=0)                   | Concatena DataFrames verticalmente          |
| pd.merge(df1, df2, on='clave')                  | Realiza una fusión (merge) de los DataFrame |
| df['nueva_col'] = df['col1'] + ' ' + df['col2'] | Combina dos columnas de texto               |

</details>

<details>
<summary>Filtros avanzados</summary>

| Sintaxi               | Uso                                                  |
| --------------------- | ---------------------------------------------------- |
| df.query('condicion') | Filtra el DataFrame usando una expresión de consulta |

</details>

<details>
<summary>Operaciones .apply(lambda)</summary>

| Sintaxi                   | Uso                                              |
| ------------------------- | ------------------------------------------------ |
| df.apply(lambda x: x * 2) | Aplica una función a cada elemento del DataFrame |

</details>

<details>
<summary>Varios</summary>

| Sintaxi      | Uso                                       |
| ------------ | ----------------------------------------- |
| df.sample(n) | Devuelve una muestra aleatoria de n filas |

</details>