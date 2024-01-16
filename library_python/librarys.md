# Librerias python
> Clasificado por utilidad

### Utilitarias

<details>
<summary>Librería GetPass</summary>    

<code>import getpass</code>

* DESCRIPCION: 
  <p>
  La librería getpass en Python proporciona una forma segura de solicitar contraseñas o información confidencial del usuario sin mostrarla en la pantalla. Su función principal, getpass.getpass(), solicita al usuario que ingrese datos, como una contraseña, de manera interactiva, pero oculta la entrada en la consola. Esto es especialmente útil en aplicaciones que manejan información sensible, ya que evita que la contraseña se muestre en texto claro, brindando una capa adicional de seguridad al proteger contra posibles miradas indiscretas. La librería getpass es multiplataforma y se utiliza comúnmente en scripts interactivos o programas de línea de comandos donde se requiere la entrada segura de información confidencial por parte del usuario.
  </p>
</details>

<details>
<summary>Librería DateTime</summary>    

<code>import datetime as date</code>

* DESCRIPCION: 
  <p>
  La biblioteca datetime en Python proporciona clases y funciones para trabajar con fechas y horas de una manera eficiente y conveniente. Su funcionalidad incluye la creación, manipulación y formato de objetos de fecha y hora, así como cálculos de diferencia entre fechas. El módulo datetime dentro de esta biblioteca contiene clases como datetime, date, time, entre otras, que permiten representar y manipular componentes específicos de fechas y horas. Además, datetime facilita la realización de operaciones aritméticas en fechas y horas, así como la conversión entre diferentes formatos de fecha. Esta biblioteca es esencial para tareas relacionadas con el manejo de tiempo, como registrar eventos, realizar cálculos de duración y formatear salidas temporales en aplicaciones Python.
  </p>
</details>

---
### Procesamiento y manipulación de datos DataFrame

<details>
<summary>Librería Pandas</summary>    

<code>import pandas as pd</code>

* DESCRIPCION: 
  <p>
  Pandas es una poderosa librería de Python diseñada para la manipulación y análisis de datos de manera eficiente. Proporciona estructuras de datos flexibles, como DataFrames, que permiten organizar y trabajar con conjuntos de datos tabulares de una manera intuitiva. Pandas facilita la limpieza, filtrado y transformación de datos, así como el manejo de operaciones estadísticas básicas. Además, ofrece herramientas para la importación y exportación de datos desde y hacia una variedad de formatos, facilitando la integración con diversas fuentes de datos. Gracias a su versatilidad y eficacia, Pandas se ha convertido en una herramienta fundamental en el ecosistema de ciencia de datos y análisis en Python.
  </p>
</details>

<details>
<summary>Librería Numpy</summary>    

<code>import numpy as np</code>

* DESCRIPCION: 
  <p>
  NumPy es una potente biblioteca para Python que facilita el manejo de arreglos multidimensionales, matrices y operaciones matemáticas en general. Su nombre proviene de "Numerical Python". NumPy proporciona una interfaz flexible y eficiente para realizar operaciones numéricas y algebraicas, lo que lo convierte en una herramienta esencial para la computación científica y el análisis de datos en Python. Su característica clave es el objeto de arreglo (numpy.ndarray), que es una estructura de datos eficiente para almacenar y manipular datos numéricos. NumPy también incluye funciones y métodos optimizados para realizar operaciones vectorizadas, lo que mejora significativamente el rendimiento en comparación con el uso de bucles tradicionales en Python. Además, es ampliamente utilizado en conjunto con otras bibliotecas como SciPy, pandas y matplotlib para realizar análisis de datos, cálculos científicos y visualización de manera eficiente en Python.
  </p>
</details>

---
### Procesamiento y manipulación de datos DataFrame con Query SQL

<details>
<summary>Librería PandasSQL</summary>    

<code>import pandasql as ps</code>

* DESCRIPCION: 
  <p>
  PadasSQL es una biblioteca de Python que facilita la ejecución de consultas SQL sobre objetos DataFrame de pandas. Combina la potencia de la librería pandas para manipulación y análisis de datos con la sintaxis familiar de SQL. Al utilizar pandasql, puedes realizar operaciones SQL directamente en tus conjuntos de datos, aprovechando las capacidades de SQL para filtrar, agrupar y analizar datos tabulares. Esta librería proporciona una interfaz sencilla para aquellos familiarizados con SQL, permitiéndoles realizar operaciones complejas de manera eficiente en DataFrames de pandas sin tener que cambiar drásticamente su enfoque. pandasql actúa como un puente entre el mundo relacional de SQL y las operaciones de manipulación de datos basadas en pandas, facilitando la integración de ambos en el análisis de datos en entornos Python.
  </p>
</details>


---
### Conección a base de datos SQL Server

<details>
<summary>Librería Sqlalchemy | Pypyodbc</summary>
<code>from sqlalchemy import create_engine</code> . <code>from sqlalchemy.engine import URL</code>

<code>import pypyodbc as odbc</code>

* DESCRIPCION: 
  <p>
  Las bibliotecas sqlalchemy y pypyodbc se utilizan en conjunto para facilitar la interacción con bases de datos en entornos de Python. sqlalchemy proporciona una abstracción de alto nivel para trabajar con bases de datos relacionales, permitiendo la creación de motores de base de datos y la construcción de consultas de manera sencilla. El módulo create_engine de sqlalchemy se emplea para establecer una conexión a la base de datos utilizando una URL de conexión. Por otro lado, pypyodbc es un controlador ODBC (Open Database Connectivity) que permite la conexión y ejecución de consultas en bases de datos mediante el protocolo ODBC. Juntas, estas bibliotecas permiten a los desarrolladores gestionar eficientemente conexiones a bases de datos, ejecutar consultas SQL y trabajar con resultados de manera efectiva en aplicaciones Python, proporcionando una capa de abstracción y facilitando la portabilidad entre distintos motores de bases de datos y entornos.
  </p>
</details>