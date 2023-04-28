#Archivo para crear dashboard en html

import dash 
from dash import dcc #Dash Core Components
from dash import html # Hyper Text Markup Language 

import plotly.graph_objects as go
import numpy as np

from funcionesParaGraficas import graf1_fun, graf2_fun
from limpiezaDeDatos import limpieza,polizas_vig,prima_emi

df = limpieza()
gra1 = polizas_vig(df)
gra2= prima_emi(df)

app = dash.Dash()

app.layout = html.Div([
    html.H1('Actividad: Dashboard 1 Dash'),
    html.H3('Equipo: Elisa, Frida, Iván y Leo'),
    html.P('Para la primera gráfica utilizamos las variables Entidad y Polizas Vigentes para mostrar la suma de Polizas Vigentes durante los últimos 3 años. Como podemos observar tenemos que El Distrio Federal está en el primer lugar con más de 150 millones que fue su máximo en el 2022 y como último lugar de los 5 principales, está Baja California, que durante el mismo año obtuvo más de 25 millones. Un factor en común que presentan los resultados es que todos los estados alcanzan su máximo en el año 2022.'),
    dcc.Graph(
        id='graph_1',
        figure = graf1_fun(gra1)
        ),
    
    html.P("Tomando en consideración la primera gráfica, realizamos una comparativa con las variables de ""Primas Emitidas"" en los últimos 3 años, en dónde, aunque se podría esperar que las entidades Top 5 fueran las mismas, podemos observar que hay una diferencia entre las entidades que tienen una mayor suma de pólizas vigentes y las entidades que tienen mayor suma de prima emitida, siendo estos estados (2da gráfica) en donde la cantidad de dinero que un asegurado paga a una compañía de seguros a cambio de la cobertura de riesgos o pérdidas específicas es mayor, aunque el número de pólizas vigentes sea menor."),
    dcc.Graph(
        id='graph_2',
        figure = graf2_fun(gra2)
        )
    ])

if __name__ == '__main__':
    app.run_server()


