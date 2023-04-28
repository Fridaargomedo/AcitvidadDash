#Archivo para limpiar el dataset
#Limpieza de datos
#Funciones (dos cada equipo)
#Ajustar códgio a visual studio
#Codificar dashboard

# Importar librerias importantes
import pandas as pd

def limpieza():

    #ruta principal de todos los  archivos del proyecto
    sio_path = 'data/'

    #lectura del dataframe
    ors_entidades_df = pd.read_csv(sio_path + 'Ors_entidad.csv')

    #CONVERSION A LOS TIPOS DE DATOS NECESARIOS

    # Lista de columnas que se necesitan modificar
    no_commas_list = ors_entidades_df.columns[5:-1]

    # Quitamos las comas (,) de las columnas para que no interfieran con el parseamiento
    # y las convertimos a su representación numérica en punto flotante
    ors_entidades_df[no_commas_list] = ors_entidades_df[no_commas_list].apply(lambda column: column.replace('[^0-9\.-]', '', regex=True))

    # Cambio completo de objetos a ints
    ors_entidades_df = ors_entidades_df.apply(pd.to_numeric, downcast='integer', errors='ignore')
    ors_entidades_df['AÑO'] = ors_entidades_df['AÑO'].apply(str) #de manera opcional por ser de uso más comun
    return ors_entidades_df

def polizas_vig(ors_entidades_df):
    entidadesTopPolizas =  ors_entidades_df.groupby("ENTIDAD")["NUMERO DE POLIZAS VIGENTES"].sum().nlargest(5).reset_index()["ENTIDAD"]


    #Primer Gráfica
    return ors_entidades_df[ors_entidades_df["ENTIDAD"].isin(entidadesTopPolizas)].groupby(["ENTIDAD", "AÑO"])["NUMERO DE POLIZAS VIGENTES"].sum().reset_index()

def prima_emi(ors_entidades_df):
    entidadesTopPrima =  ors_entidades_df.groupby("ENTIDAD")["PRIMA EMITIDA"].sum().nlargest(5).reset_index()["ENTIDAD"]

#Segunda Gráfica
    return ors_entidades_df[ors_entidades_df["ENTIDAD"].isin(entidadesTopPrima)].groupby(["ENTIDAD", "AÑO"])["PRIMA EMITIDA"].sum().reset_index()






