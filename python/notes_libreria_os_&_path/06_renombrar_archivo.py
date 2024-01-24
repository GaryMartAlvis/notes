import os
from pathlib import Path, PurePath

# Para renombar archivos lo que cambia al nombre es adicionar la extension
# Renombrar archivo con la libreria os
os.rename('level_1_dir_os', 'dir_renombrado_os') 

# Renombrar archivo con la libreria pathlib
name_actual = Path('level_1_dir_path')
name_nuevo = Path('dir_renombrado_path')
Path.rename(name_actual, name_nuevo)

