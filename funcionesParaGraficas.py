#Archivo para incluir funciones del proyecto
# Importar librerias importantes
import plotly.express as px

def graf1_fun(gra1):
    fig = px.bar(gra1, x="ENTIDAD", y="NUMERO DE POLIZAS VIGENTES",
             color='AÑO', barmode='group',
             height=400, 
             title="Top 5 Entidades con mayor suma de Polizas Vigentes en los últimos 3 años.")
    fig.update_layout(xaxis = {"categoryorder": "total descending"})
    return fig
    
def graf2_fun(gra2):
    fig = px.bar(gra2, x="ENTIDAD", y="PRIMA EMITIDA",
             color='AÑO', barmode='group',
             height=400, 
             title="Top 5 Entidades con mayor suma de Primas Emitidas en los últimos 3 años.")
    fig.update_layout(xaxis = {"categoryorder": "total descending"})
    return fig
