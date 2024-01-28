import os

'''Cambiar de directorio a subdirectorio para correr el bucle'''

# Declarar en variables las rutas del directorio actual y el sub directorio
path_actual = os.getcwd()
sub_carpeta = 'compilados'

# Crear una variable con la ruta del sub directorio en el cual se estará trabajando
path_sub_carpeta = os.path.join(path_actual, sub_carpeta)

# Si la sub carpeta no exixte se crea
if not os.path.exists(path_sub_carpeta):
    os.makedirs(sub_carpeta)

# Código para cambiar de directorio 
os.chdir(path_sub_carpeta)

# Renombar todos los archivos .txt dentro de un directorio
for file in os.listdir():
    if file.endswith('.txt'):
        os.rename(file, f'G2024_{file}')

# Volver al directorio original
os.chdir(path_actual)
