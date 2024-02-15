# COMANDOS DE USO EN TERMINAL
<details>
<summary>Python</summary>

> Shell para trabajar con codigo de python

| File/Comando | Descripción                                            | Entrornos de ejecución                                         |
| ------------ | ------------------------------------------------------ | -------------------------------------------------------------- |
| file.py      | Archivos ejecutables de Python                         | Terminal: python file.py - VSCode Run Code                     |
| file.ipynb   | Archivos ejecutables de Jupyter Notebook               | Cuenta con su propio entorno de ejecución del codigo           |
| python       | Inicialización del interprete de python en la terminal | Se puede escribir y ejecutar codigo python en la terminal      |
| ipython      | Al igual que python inicial en terminal un interprete  | El inteprete inicializado cuenta con caracteristicas mejoradas |

</details>

<details>
<summary>PowerShell</summary>

> PowerShell es un entorno de linea de comandos basados en objetos

| Comando                                  | Complemento | Uso                                                  | Significado      |
| ---------------------------------------- | ----------- | ---------------------------------------------------- | ---------------- |
| cd <ruta>                                | ..          | Cambia de directorio                                 | Change Directory |
| ls                                       | -directory  | Lista todo el contenido del directorio               | List System      |
| ls -directory \| Select-Object -First 40 | n           | Lista todo el contenido del directorio               | List System      |
| cp <.origen> <.destino>                  |             | Copiar archivo y pegar                               | Copy             |
| mv <.origen> <.destino>                  |             | Mueve archivo o directorio                           | Move             |
| rm <nombre_archivo>                      | -r          | Elimina archivo o directorio                         | Remuve           |
| mkdir <nombre_directorio>                |             | Crea un nuevo directorio                             | Make Directory   |
| cls                                      | clear       | Limpia la pantalla de la terminal                    | Clear            |
| code .                                   |             | Abrir directorio con el editor de codigo VSCode      |                  |
| notepad <file_name.txt>                  |             | Abre archivos '.txt' con Block de notas              |                  |
| New-Item -ItemType -Name <file_name.txt> |             | Crea un archivos '.txt'                              |                  |
| hostname                                 |             | Muestra el nombre del host del sistema               |                  |
| ipconfig                                 |             | Muestra la configuracion de la red                   |                  |
| ping <direccion_ip>                      |             | Verificar conectividad con la direccion IP           |                  |
| echo $env:USERNAME                       |             | Muestra el nombre del usuario                        |                  |
| tree <directorio>                        |             | Muestra el arbol del directorio                      |                  |
| Get-Command                              |             | Obtiene todos los comandos disponibles en PowerShell |                  |

</details>

<details>    
<summary>Pip</summary>

> Python Package Index - PyPI: Sistema de gestion de paquetes de python

| Comando                                                             | Uso                                               |
| ------------------------------------------------------------------- | ------------------------------------------------- |
| pip install <nombre_del_paquete>                                    | Instalar un paquete                               |
| pip uninstall <nombre_del_paquete>                                  | Desinstalar un paquete                            |
| pip show <nombre_del_paquete>                                       | Mostrar información sobre un paquete instalado    |
| pip list                                                            | Listar todos los paquetes instalados              |
| pip install --upgrade <nombre_paquete>                              | Actualizar un paquete a la última versión         |
| pip search <término_de_búsqueda>                                    | Buscar paquetes                                   |
| pip freeze > requirements.txt                                       | Crear un archivo de requisitos (requirements.txt) |
| pip install -r requirements.txt                                     | Instalar paquetes desde un archivo de requisitos  |
| pip show -f <nombre_del_paquete>                                    | Mostrar la ubicación de un paquete instalado      |
| pip list --outdated                                                 | Listar los paquetes obsoletos                     |
| pip freeze \| ForEach-Object { pip uninstall -y $_.split('==')[0] } | Desinstalar todas las librerias listadas en pip   |

</details>


<details>
<summary>Virtual Environments</summary>

> Entornos virtuales

| Comando                          | Uso                                   |
| -------------------------------- | ------------------------------------- |
| python -m venv <nombre_venv>     | Crear un entorno virtual              |
| .\<nombre_venv>\Scripts\activate | Activar un entorno virtual en Windows |
| deactivate                       | Desactivar un entorno virtual         |

</details>

<details>
<summary>Git</summary>

| Comando                                    | Uso                                                                                        |
| ------------------------------------------ | ------------------------------------------------------------------------------------------ |
| git init                                   | Inicia un nuevo repositorio de Git                                                         |
| git status                                 | Agrega cambios al área de preparación                                                      |
| git add <archivo_o_directorio>             | Agrega cambios al área de preparación                                                      |
| git commit -m "Mensaje del commit"         | Registra los cambios en el repositorio                                                     |
| git log --all --oneline                    | Muestra el historial de commits --todos los commit --visualización en una sola línea       |
| git clone <url_del_repositorio>            | Clona un repositorio existente en un nuevo directorio                                      |
| git pull origin <rama>                     | Obtiene cambios desde un repositorio remoto y los fusiona en el repositorio local          |
| git push origin <rama>                     | Sube los cambios locales a un repositorio remoto                                           |
| git branch                                 | Lista las ramas en el repositorio                                                          |
| git checkout <nombre_de_rama>              | Cambia de rama o restaura archivos                                                         |
| git merge <rama_a_fusionar>                | Fusiona una rama en la rama actual                                                         |
| git remote -v                              | Muestra los repositorios remotos configurados                                              |
| git fetch origin                           | Obtiene los cambios del repositorio remoto sin fusionarlos                                 |
| git diff                                   | Muestra las diferencias entre cambios en el área de preparación y el directorio de trabajo |
| git reset --hard                           | Deshace cambios locales                                                                    |
| git tag -a <nombre_etiq> -m "Mensaje Etiq" | Crea, lista o borra etiquetas                                                              |



<details>
<summary>Creación y conexión de repositorio con GitHub</summary>

> Conexion con repositorio de GitHub
```
# Or create a new repository on the command line
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin <URL-Repository>
git push -u origin main

# Or push an existing repository from the command line
git remote add origin <URL-Repository>
git branch -M main
git push -u origin main
```

> Script: Configuracion global
```
git config --global --list

# Abrir editor para cambiar las configuraciones globales 
> git config --global --edit

# Ejemplo de configuración
    	[user]
		    name = GaryMartAlvis
		    email = gary.martinez.alvis@gmail.com

    # Abrir archivo de configuración con notepad
    > notepad ~/.gitconfig

    # Configurar para abrir con un editor especifico
    > git config --global core.editor "notepad"</>
```

</details>

<details>
<summary>Pull request</summary>

Pasos para realizar un pull request
***
**Step 1: Hacer Fork del repositorio original**

Hacer un fork en GitHub significa crear una copia personal de un repositorio ajeno en tu propia cuenta de GitHub. Esto te permite trabajar en el proyecto sin afectar el repositorio original. La copia (fork) está vinculada al repositorio original, lo que facilita la colaboración y la contribución a proyectos de código abierto o a proyectos de otras personas.
- Ingresa a GitHub
- Encuentra el repositorio
- Abre el repositorio
- Hacer Fork:En la esquina superior derecha de la página del repositorio, encontrarás el botón "Fork". Haz clic en él.
- Elige la cuenta: Selecciona tu cuenta como destino para el fork. Esto creará una copia del repositorio en tu propia cuenta.
- Espera a que se complete: GitHub creará una copia del repositorio en tu cuenta. Esto puede tardar un momento, dependiendo del tamaño del repositorio.

****
**Step 2: Clona el repositorio en tu equipo**
~~~ 
git clone [URL_repositorio_original] 
~~~

***
**Step 3: Crea un rama para los trabajar en ella en los cambios del** 
~~~
git checkout -b nombre-de-tu-rama
~~~

***
**Step 4: Realizar cambios locales**

Realiza los cambios que desees en tu rama local. Puedes agregar, modificar o eliminar archivos según sea necesario.

***
**Step 5: Hacer commit de los cambios**

~~~~
git add .
git commit -m "Mensaje descriptivo de tus cambios"
~~~~

***
**Step 6: Subir cambios a tu repositorio Forked**

~~~
git push origin nombre-de-tu-rama
~~~

***
**Step 7: Crear el pull request**

* Ve a tu repositorio forked en GitHub.
* Cambia a la rama que acabas de crear.
* Haz clic en el botón "New Pull Request".

***
**Step 8: Completar la Información del Pull Request**

* Asegúrate de que la rama base (base branch) sea la rama correcta del repositorio original.
* Asegúrate de que la rama de comparación (compare branch) sea tu rama con los cambios.
* Proporciona un título y una descripción descriptiva para explicar tus cambios.

***
**Step 9: Crear el Pull Request**

* Haz clic en el botón "Create Pull Request".
* Añade comentarios adicionales si es necesario.

***
**Step 10: Espera la revisión y fusión**

Los propietarios del repositorio original revisarán tus cambios. Puede haber comentarios, preguntas o solicitudes de ajustes. Una vez que tus cambios sean aceptados y fusionados, tu Pull Request estará cerrado.

</details>
</details>