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
<summary>Selección</summary>

| Sintaxi                  | Uso                                                         |
| ------------------------ | ----------------------------------------------------------- |
| df['columna']            | Selecciona una columna especifica                           |
| df.loc[filas, columnas]  | Accede a un grupo específico de filas y columnas            |
| df.iloc[filas, columnas] | Accede a un grupo específico de filas y columnas por índice |

</details>

<details>
<summary>Filtros</summary>

| Sintaxi                             | Uso                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------- |
| df[(df['A'] > 5) & (df['B'] < 10)]  | Filtrado con multiples                                                          |
| df[df['col'].isin(lista)]           | .isin() Filtra filas donde la columna esta en una lista                         |
| df[df['col'].between(20, 40)]       | .between() Filtra filas con valores entre 20 y 40                               |
| df[df['col'].str.startswith('Man')] | .str.startswith() Filtra filas donde las cadenas inicien con 'Man'              |
| df[df['col'].str.endswith('na')]    | .str.endswith() Filtra filas donde las cadenas terminan en 'na'                 |
| df[df['col'].str.contains('n')]     | .str.contains() Filtra filas donde las cadenas contenga la letra 'n'            |
| df[df["col"].apply(mi_funcion)]     | .apply(mi_funcion) el mentodo permite pasar una funcion personalizada de filtro |
</details>

<details>
<summary>Filtros - Consultas SQL</summary>

| Sintaxi                                                      | Uso                                                  |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| df.query('col < 50')                                         | Filtra el DataFrame usando una expresión de consulta |
| df.query('col1 == "Producto A" and col2.str.contains("du")') | Filtro con multiples condiciones                     |
| df.query('Ciudad == @ciudad_buscada')                        | Filtro con uso de varible @cuiudad_buscada           |
</details>

<details>
<summary>Manipulación de DataFrame</summary>

| Sintaxi                                   | Uso                                            |
| ----------------------------------------- | ---------------------------------------------- |
| df['nueva_col'] = df['col1'] + df['col2'] | Crea una nueva columna calculada               |
| df.append(df2, ignore_index=True)         | Añade filas de otro DataFrame                  |
| df.drop('columna', axis=1)                | Elimina una columna                            |
| df.drop(index=filas)                      | Elimina filas por índice                       |
| df.sort_values('columna')                 | Ordena el DataFrame por una columna específica |

</details>

<details>
<summary>Manejo de datos duplicados</summary>

| Sintaxi                     | Parametros (keep='')                   | Uso                                                          |
| --------------------------- | -------------------------------------- | ------------------------------------------------------------ |
| df.duplicated()             |                                        | Detecta filas duplicadas en todo el DataFrame                |
| df[df.duplicated()]         | keep='first', keep='last', kepp=False  | Mostar los registros duplicados                              |
| df.duplicated()             | subset=['Nombre', 'Curso'], keep=False | Con los parametros muestra todos los duplicados              |
| df.drop_duplicates()        | keep='first', keep='last', kepp=False  | Elimina duplicados en todo el DataFrame                      |
| df['Ciudad'].value_counts() | normalice=True, sort=True              | Proporciona un recuento de la frecuencia de cada valor único |

</details>

<details>
<summary>Tratamiento de valores faltantes y nulos</summary>

| Sintaxi                   | Uso                                                                  |
| ------------------------- | -------------------------------------------------------------------- |
| df.isna()                 | Detectar valores faltantes en todo el DataFrame                      |
| df['B'].isnull()          | Detectar valores faltantes en una columna específica                 |
| df.fillna(method='bfill') | Rellena valores faltante con el valor anterior                       |
| df.fillna(method='ffill') | Rellena valores faltantes con el valor siguiente                     |
| df.fillna(valor)          | Rellena los valores nulos con un valor especificado                  |
| df.dropna()               | Elimina todas las filas que contiene un valor faltante               |
| df.dropna(axis=1)         | Eliminar todas las columnas que contienen al menos un valor faltante |

</details>

<details>
<summary>Agrupaciones - Creacion de tablas y tablas dinamicas</summary>

| Sintaxi                                           | Uso                                                                     |
| ------------------------------------------------- | ----------------------------------------------------------------------- |
| df.groupby('Ciudad').sum()                        | Agrupa por la columna 'Ciudad' y suma los valores de las demas columnas |
| df.groupby(['Ciudad', 'Edad']).sum()              | Agrupa por 'Ciudad' , 'Edad'  y suma los valores de las demas columnas  |
| df.groupby('columna').agg({'otra_col':'funcion'}) | Agrega y aplica funciones a grupos de datos                             |

```
# Agrupracion | Calculo agrupado | Reseteo de indice | Cambio de nombre a columna

    df_new = df.groupby('Curso')['Calificación'].mean().reset_index()
    df_new = df_new.rename(columns={'Calificación': 'Calf_premd'})
    print(df_new)
```
</details>

<details>
<summary>Operaciones aritmeticas</summary>

| Sintaxi                | Uso                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------ |
| df.sum()               | Suma de todas la columans del DataFrame, si la columna contiene string los concatena |
| df['col'].count()      | Cuenta el numero de valores no nulos en una columna                                  |
| df['col'].std()        | Calcula la desviación estandar de cada columna                                       |
| df['col'].mean()       | Calcula la media de los valores de la columna                                        |
| df['col'].median()     | Calcula la mediana de los valores de columna                                         |
| df['Edad'].min()       | Optiene el valor minimo de una columna                                               |
| df['Puntuación'].max() | Optiene el valor maximo de una columna                                               |
| df.isnull().sum()      | Cuenta los valores nulos en cada columna                                             |

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

| Sintaxi                                         | Uso                                                                  |
| ----------------------------------------------- | -------------------------------------------------------------------- |
| pd.concat([df1, df2], axis=0)                   | Concatena DataFrames por eje [axis=0: Vertical] [axis=1: Horizontal] |
| pd.merge(df1, df2, on='columna_comun')          | Realiza una fusión (merge) de los DataFrame                          |
| df['nueva_col'] = df['col1'] + ' ' + df['col2'] | Combina dos columnas de texto                                        |

</details>

<details>
<summary>Operaciones con el metodo .apply()</summary>

| Sintaxi                   | Uso                                              |
| ------------------------- | ------------------------------------------------ |
| df.apply(lambda x: x * 2) | Aplica una función a cada elemento del DataFrame |
| df.['col1'].apply(sum)    | Aplica la funcion suma a la 'col1'               |

</details>

<details>
<summary>Operaciones con el metodo .map()</summary>

| Sintaxi                   | Uso                                                            |
| ------------------------- | -------------------------------------------------------------- |
| df['Categoria'].map(dic1) | Mapea los valores del diccionario dic1 en su clave 'Categoria' |

</details>

<details>
<summary>Varios</summary>

| Sintaxi      | Uso                                       |
| ------------ | ----------------------------------------- |
| df.sample(n) | Devuelve una muestra aleatoria de n filas |

</details>