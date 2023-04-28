#Archivo para incluir funciones del proyecto
#ruta principal de todos los  archivos del proyecto
sio_path = 'data/'
# Importar librerias importantes
import pandas as pd
import plotly.express as px

#lectura del dataframe
ors_entidades_df = pd.read_csv(sio_path + 'Ors_entidad.csv')

def graf1_fun(ors_entidades_df, ENTIDAD, NUMERO_DE_POLIZAS_VIGENTES):
    datos = ors_entidades_df.groupby(ENTIDAD)[NUMERO_DE_POLIZAS_VIGENTES].sum().tolist()
    etiquetas = ors_entidades_df[ENTIDAD].unique().tolist()
    px.bar(etiquetas, datos, tick_label=etiquetas)
    px.show()
    
def graf2_fun(ors_entidades_df, ENTIDAD, PRIMA_EMITDA):
    datos= ors_entidades_df.groupby(ENTIDAD)[PRIMA_EMITDA].sum().tolist()
    etiquetas = ors_entidades_df[ENTIDAD].unique().tolist()
    px.bar(etiquetas, datos, tick_label=etiquetas)
    px.show()
