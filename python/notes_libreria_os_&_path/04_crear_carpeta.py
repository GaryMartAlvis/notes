import os
from pathlib import Path

# Crear carpeta con la libreria os
os.mkdir('carpeta_creada_os') # Si el directorio existe da error 

# Crear carpeta con la libreria pathlib
Path('carpeta_creada_path').mkdir() # Si el directorio existe da error
Path('carpeta_creada_path').mkdir(exist_ok=True) # Si el directorio existe no da error

