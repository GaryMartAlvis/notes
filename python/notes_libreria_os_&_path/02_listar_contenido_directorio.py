import os
from pathlib import Path

# Listar contenido de directorio con la libreria os
contenido_directorio_os = os.listdir()
print('-------------------------------------------------------------------------')
print(f'Lista de archivos obtenida con la libreria "os": {contenido_directorio_os}')
print(f'Al usar la libreria "os" nos retorna: {type(contenido_directorio_os)}')

print('-------------------------------------------------------------------------')

# Listar contenido de directorio con la libreria pathlib
contenido_directorio_pathlib = Path().iterdir()
contenido_sub_directorio_pathlib = Path("Nueva Carpeta").iterdir()
print(f'Lista de archivos obtenida con la libreria "pathlib": {list(contenido_directorio_pathlib)}')
print(f'Al usar la libreria "pathlib" nos retorna: {type(contenido_directorio_pathlib)}')
print(f'Contenido de sub directorio: {list(contenido_sub_directorio_pathlib)}')
print('-------------------------------------------------------------------------')

