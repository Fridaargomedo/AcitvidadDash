#Archivo para limpiar el dataset
#Limpieza de datos
#Funciones (dos cada equipo)
#Ajustar códgio a visual studio
#Codificar dashboard

# Importar librerias importantes
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import sys

#ruta principal de todos los  archivos del proyecto
sio_path = 'data/'

#lectura del dataframe
ors_entidades_df = pd.read_csv(sio_path + 'Ors_entidad.csv')
print(ors_entidades_df.head())

print(ors_entidades_df.info()) #visualizamos los tipos de datos

#CONVERSION A LOS TIPOS DE DATOS NECESARIOS

# Lista de columnas que se necesitan modificar
no_commas_list = ors_entidades_df.columns[5:-1]

# Quitamos las comas (,) de las columnas para que no interfieran con el parseamiento
# y las convertimos a su representación numérica en punto flotante
ors_entidades_df[no_commas_list] = ors_entidades_df[no_commas_list].apply(lambda column: column.replace('[^0-9\.-]', '', regex=True))

# Cambio completo de objetos a ints
ors_entidades_df = ors_entidades_df.apply(pd.to_numeric, downcast='integer', errors='ignore')
ors_entidades_df['AÑO'] = ors_entidades_df['AÑO'].apply(str) #de manera opcional por ser de uso más comun
print(ors_entidades_df.info())

