import os
from pathlib import Path, PurePath

# Comprobar si el archivos exixte con la libreria os
test_os = os.path.exists('01_obtener_path.py') 
print(test_os)

# Comprobar si el archivos exixte con la libreria path
archivo = Path('compilados')
print(archivo.exists())

