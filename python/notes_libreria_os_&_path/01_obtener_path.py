import os
from pathlib import Path

# Obtener path con la libreria os
ruta_actual_os = os.getcwd()
print('-------------------------------------------------------------------------')
print(f'La ruta obtenida con la libreria "os": {ruta_actual_os}')
print(f'Al usar la libreria "os" nos retorna: {type(ruta_actual_os)}')

print('-------------------------------------------------------------------------')

# Obtener path con la libreria pathlib
ruta_actual_pathlib = Path.cwd()
print(f'La ruta obtenida con la libreria "pathlib": {ruta_actual_pathlib}')
print(f'Al usar la libreria "pathlib" nos retorna: {type(ruta_actual_pathlib)}')
print('-------------------------------------------------------------------------')

