import os
from pathlib import Path, PurePath

# Obtener ruta absoluta de un archivo con la libreria os
ruta_absoluta_os = os.path.abspath('01_obtener_path.py')
print(ruta_absoluta_os)

# Obtener ruta absoluta de un archivo con la libreria path
ruta_absoluta_path = Path('01_obtener_path.py')
print(ruta_absoluta_path.resolve())

# Obtener nombre de archivo
print(ruta_absoluta_path.stem)

# Obtener la extención del archivos
print(ruta_absoluta_path.suffix)

# Obtener el tamaño del archivo
print(ruta_absoluta_path.stat().st_size)