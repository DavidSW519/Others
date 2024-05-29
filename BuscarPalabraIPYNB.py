import os
import nbformat


palabra = 'Curva_Chevrolet'

carpetas = os.listdir('c:\\Users\\430009360\\HDI')
carpetas = [i for i in carpetas if '.' not in i]
carpetas

for i in [c for c in carpetas if c not in ['Depreciacion','Prediccion_Ventas','David']]:
    directorio_base = f'c:\\Users\\430009360\\HDI\\{i}'
    archivos = os.listdir(directorio_base)
    for archivo in archivos:
        if archivo.endswith('.ipynb'):
            ruta_completa = os.path.join(directorio_base,archivo)
            with open(ruta_completa, 'r', encoding='utf-8') as file:
                contenido = nbformat.read(file, as_version=4)
                if palabra in str(contenido):
                    print(ruta_completa)
        elif '.' not in archivo:
            archivos2 = os.listdir(os.path.join(directorio_base,archivo))
            for archivo2 in archivos2:
                if archivo2.endswith('.ipynb'):
                    ruta_completa = os.path.join(directorio_base,archivo,archivo2)
                    with open(ruta_completa, 'r', encoding='utf-8') as file:
                        contenido = nbformat.read(file, as_version=4)          
                        if palabra in str(contenido):
                            print(ruta_completa)
