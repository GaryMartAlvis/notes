# Apis

Una API es un conjunto de reglas y protocolos que permiten que diferentes aplicaciones se comuniquen entre sí. Es una interfaz que define cómo los diferentes componentes de software deben interactuar.

API significa Application Programming Interface, que en español se traduce como Interfaz de Programación de Aplicaciones.

---

### Apis REST

REST, que significa Representational State Transfer (Transferencia de Estado Representacional), es un estilo arquitectónico utilizado en el diseño de sistemas distribuidos.
1. **Protocolo basado en HTTP:** REST utiliza los métodos estándar de HTTP o HTTP Verbs.
2. **Sin estado:** REST es sin estado (stateless), lo que significa que cada solicitud HTTP contiene toda la información necesaria para comprender y procesar la solicitud.
3. **Orientado a recursos:** los recursos son la parte central de REST. Cada recurso tiene una identificación única (URI) y se accede a través de esa URI.


### Metodos HTTP

| Metodos | Descripcion                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------- |
| GET     | El verbo GET se utiliza para recuperar o solicitar datos de un recurso específico en un servidor.                 |
| POST    | El verbo POST se utiliza para enviar datos al servidor y crear un nuevo recurso.                                  |
| PUT     | El verbo PUT se utiliza para actualizar o reemplazar un recurso existente en el servidor.                         |
| PATHC   | El verbo PATCH se utiliza para realizar modificaciones parciales en un recurso existente en el servidor.          |
| DELETE  | El verbo DELETE se utiliza para eliminar un recurso en el servidor.                                               |
| HEAD    | El verbo HEAD se utiliza para solicitar información sobre un recurso sin recibir su contenido completo.           |
| OPTIONS | El verbo OPTIONS se utiliza para obtener información sobre las opciones y capacidades disponibles en un servidor. |

---

### Libreria requests

requests es una libreria de Python ampliamente utilizada y popular para realizar solicitudes HTTP y trabajar con APIs.

> ```
> pip install requests
> ```

> ```
> import request
>
> response = requests.get(url)  # Solicitud HTTP
>
> # Getionar la respuesta de la solicitud anterior
>   print(response.status_code) # Estado de la respuesta
>   print(response.json())      # Contenido de la respuesta en formato JSON
>   print(response.headers)     # Encabezados de la respuesta
>
> # Enviar datos y parametros
>   data = {"name": "Jonh", "age": 25}
>   response = requests.post(url, data=data)
>   
>   params = {"category": "books", "limit": 10}
>   response = requests.get(url, params=params)
> ```

<details>
<summary>Ejemplo de Cars API</summary>

> Podemos utilizar la siguiente API para solicitar información de vehículos: https://api-ninjas.com/api/cars
> Realizamos la solicitud de datos:

```
import requests

model = "camry"
api_url = f"https://api.api-ninjas.com/v1/cars?model={model}"
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    to_df(response.json())
```
> Implementamos la función to_df
```
import pandas as pd

def to_df(api_data):
    df = pd.DataFrame(api_data)
    return df
```
> gracias al formato json consistente, pandas es capaz de cargar la información y convertirlo automáticamente a un DataFrame, el cual puede exportarse en el formato tabular deseado.
</details>