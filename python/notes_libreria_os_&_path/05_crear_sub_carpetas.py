import os
from pathlib import Path, PurePath

# Crear sub_carpeta con la libreria os
os.makedirs(os.path.join('level_1_dir_os', 'level_2_dir_os')) # Si el directorio existe da error 

# Crear sub_carpeta con la libreria pathlib
PurePath.joinpath(Path.cwd(), 'level_1_dir_path', 'level_2_dir_path').mkdir(parents=True) # Si el directorio existe da error

