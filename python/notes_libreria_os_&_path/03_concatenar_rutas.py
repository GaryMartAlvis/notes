import os
from pathlib import Path, PurePath

# Concatenar rutas con la libreria os
concatenar_ruta_os = os.path.join(os.getcwd(), 'Nueva Carpeta')
print('-------------------------------------------------------------------------')
print(f'Concatenar rutas con la libreria "os": {concatenar_ruta_os}')
print(f'Al usar la libreria "os" nos retorna: {type(concatenar_ruta_os)}')

print('-------------------------------------------------------------------------')

# Concatenar rutas con la libreria pathlib

concatenar_ruta_path = PurePath.joinpath(Path.cwd(), 'Nueva Carpeta')
print(f'Concatenar rutas con la libreria "pathlib": {concatenar_ruta_path}')
print(f'Al usar la libreria "pathlib" nos retorna: {type(concatenar_ruta_path)}')
print('-------------------------------------------------------------------------')

