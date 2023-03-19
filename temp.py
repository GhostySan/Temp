import os

temp_dir = os.environ.get('TEMP') or os.environ.get('TMP') # Obtiene la ruta del directorio de archivos temporales de Windows
if temp_dir:
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            try:
                os.remove(os.path.join(root, file)) # Elimina cada archivo en el directorio temporal
            except Exception as e:
                print(f"No se pudo eliminar {os.path.join(root, file)}: {e}")
else:
    print("No se pudo encontrar el directorio temporal de Windows.")
