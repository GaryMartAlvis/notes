# COMANDOS DE USO EN TERMINAL

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

| Comando                                | Uso                                               |
| -------------------------------------- | ------------------------------------------------- |
| pip install <nombre_del_paquete>       | Instalar un paquete                               |
| pip uninstall <nombre_del_paquete>     | Desinstalar un paquete                            |
| pip show <nombre_del_paquete>          | Mostrar información sobre un paquete instalado    |
| pip list                               | Listar todos los paquetes instalados              |
| pip install --upgrade <nombre_paquete> | Actualizar un paquete a la última versión         |
| pip search <término_de_búsqueda>       | Buscar paquetes                                   |
| pip freeze > requirements.txt          | Crear un archivo de requisitos (requirements.txt) |
| pip install -r requirements.txt        | Instalar paquetes desde un archivo de requisitos  |
| pip show -f <nombre_del_paquete>       | Mostrar la ubicación de un paquete instalado      |
| pip list --outdated                    | Listar los paquetes obsoletos                     |

</details>


<details>
<summary>Python</summary>

> Ejecucion de archivos '.py' & Entornos virtuales con Python

| Comando                                     | Uso                                   |
| ------------------------------------------- | ------------------------------------- |
| python <nombre_script.py>                   | Ejecuta un script de python           |
| virtualenv <nombre_del_entorno>             | OP1 Crear un entorno virtual          |
| python -m venv <nombre_del_entorno_virtual> | OP2 Crear un entorno virtual          |
| .\<nombre_entorno_virtual>\Scripts\activate | Activar un entorno virtual en Windows |
| deactivate                                  | Desactivar un entorno virtual         |

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