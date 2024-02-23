import pandas as pd
import streamlit as st

import numpy as np
import pickle
# Visualizaciones
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
from tensorflow.keras.models import load_model




#Importar archivos relevantes

df_coches = pd.read_csv("Data/df_coches_escrapeo.csv")
df_coches = df_coches[~(df_coches["Motorización"] == "Híbridos de gasóleo")]

#--------------------------INFO FUNCIONES EN ORDEN--------------------------------------------------

# funcion_categorias_e_c(input_usuario_vehiculos)----> Segun la seleccion de la Motorización del vehiculo imprime una grafica o varias
#


#___________________________________________________________________________________________________


#Funciones EcoEstudio
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________



#Funciones para graficas


#Grafica para las categorias de los diferentes vehiculos
def funcion_categorias_e_c(input_usuario_vehiculos):
    categorias = ['L3e','L5e', 'L6e','L7e','M1','M2','M3', 'N1', 'N2', 'N3' ]

    if  input_usuario_vehiculos == 'Todos':

        # Con la columna 'Consumo Eléctrico (kWh/100km)' vamos a dividir la base de datos en vehículos eléctricos (No nulos) Y vehículos no eléctricos (Nulos)
        df_electricos = df_coches[df_coches['Consumo Eléctrico (kWh/100km)'].notnull()]
        df_no_electricos = df_coches[df_coches['Consumo Eléctrico (kWh/100km)'].isnull()]

        # Suma acumulada de las categorías para cada tipo de coche
        grupo_electricos = df_electricos[categorias][df_electricos[categorias] == 1].count().reset_index(name='Número de Vehículos')
        grupo_no_electricos = df_no_electricos[categorias][df_no_electricos[categorias] == 1].count().reset_index(name='Número de Vehículos')

        # Renombramos las columnas
        grupo_electricos.columns = ['Categoría', 'Número de Vehículos']
        grupo_no_electricos.columns = ['Categoría', 'Número de Vehículos']


        # Crear subplots con 1 fila y 2 columnas
        fig = sp.make_subplots(
                            rows=1, 
                            cols=2, 
                            subplot_titles=['Vehículos Eléctricos', 'Vehículos No Eléctricos']
                            )

        # Añadir las gráficas a las subplots
        fig.add_trace(go.Bar(
                            x=grupo_electricos['Categoría'], 
                            y=grupo_electricos['Número de Vehículos'],
                            marker_color=px.colors.qualitative.Set3, 
                            name='Número de Vehículos'), 
                            row=1, col=1
                            )
        fig.add_trace(go.Bar(
                                    x=grupo_no_electricos['Categoría'], 
                                    y=grupo_no_electricos['Número de Vehículos'],
                                    marker_color=px.colors.qualitative.Set3, 
                                    name='Número de Vehículos'),
                                    row=1, col=2
                                    )

        # Actualizar el diseño del diseño y las etiquetas
        fig.update_layout(

                        yaxis=dict(title='Número de Vehículos'),
                        showlegend=False)  # Puedes cambiar a True si deseas mostrar la leyenda
        # fig.update_xaxes(title_text = 'Categoría')

        # Retornar la figura
        return st.plotly_chart(fig,use_container_width = True )
    elif input_usuario_vehiculos != 'Todos':
        # Filtrar el DataFrame por la categoría seleccionada por el usuario
        df_categoria_seleccionada = df_coches[df_coches['Motorización'] == input_usuario_vehiculos]

        # Calcular el número de vehículos en la categoría seleccionada
        grupo_categoria_seleccionada = df_categoria_seleccionada[categorias].sum().reset_index(name='Número de Vehículos')

# Renombrar la columna de categoría
        grupo_categoria_seleccionada.columns = ['Categoría', 'Número de Vehículos']


# Crear la figura de la gráfica de barras
        fig = go.Figure(go.Bar(
                                x=grupo_categoria_seleccionada['Categoría'],
                                y=grupo_categoria_seleccionada['Número de Vehículos'],
                                marker_color=px.colors.qualitative.Set3,
                                )
                        )

        # Actualizar el diseño del diseño y las etiquetas
        fig.update_layout(
                        title=' Vehículos   {}'.format(input_usuario_vehiculos),

                        yaxis=dict(title='Número de Vehículos'),
                        showlegend=False
                        )

        # Retornar la figura
        return st.plotly_chart(fig,use_container_width = True )

    


def funcion_calsificacion_e_c(input_usuario_vehiculos):
    if input_usuario_vehiculos == 'Todos':
        # Eliminamos estas filas
        # valores_a_eliminar = ['Gases licuados del petróleo (GLP)']

        # df_filtrado = df_coches[~df_coches['Motorización'].isin(valores_a_eliminar)]

        # Lista de columnas booleanas
        clas_ener = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        df_filtrado = df_coches.copy()
        df_filtrado['Sin clasificacion'] = ~df_filtrado[clas_ener].notnull().any(axis=1) #1 si las columnas de clas_ener son todas nulas
        df_filtrado[clas_ener] = df_filtrado[clas_ener].fillna(0) #0 en nulos de clas_ener
        # Lista de categorías
        clasificacion_energetica = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Sin clasificacion']

        # Con la columna 'Consumo Eléctrico (kWh/100km)' vamos a dividir la base de datos en vehículos eléctricos (No nulos) y vehículos no eléctricos (Nulos)
        df_electricos = df_filtrado[df_filtrado['Consumo Eléctrico (kWh/100km)'].notnull()]
        df_no_electricos = df_filtrado[df_filtrado['Consumo Eléctrico (kWh/100km)'].isnull()]

        # Suma acumulada de las categorías para cada tipo de coche
        grupo_electricos = df_electricos[clasificacion_energetica][df_electricos[clasificacion_energetica] == 1].count().reset_index(name='Número de Vehículos')
        grupo_no_electricos = df_no_electricos[clasificacion_energetica][df_no_electricos[clasificacion_energetica] == 1].count().reset_index(name='Número de Vehículos')

        # Renombramos las columnas
        grupo_electricos.columns = ['Clasificacion energética', 'Número de Vehículos']
        grupo_no_electricos.columns = ['Clasificacion energética', 'Número de Vehículos']

        # Crear subplots con 1 fila y 2 columnas
        fig = sp.make_subplots(
                            rows=1, 
                            cols=2, 
                            subplot_titles=['Clasificación Energética de Vehículos Eléctricos', 'Clasificación Energética de Vehículos No Eléctricos']
                            )

        # Añadir las gráficas a las subplots
        fig.add_trace(go.Bar(
                            x=grupo_electricos['Clasificacion energética'], 
                            y=grupo_electricos['Número de Vehículos'],
                            marker_color=px.colors.qualitative.Set3, 
                            name='Número de Vehículos'),
                            row=1, col=1
                            )

        fig.add_trace(go.Bar(
                            x=grupo_no_electricos['Clasificacion energética'], 
                            y=grupo_no_electricos['Número de Vehículos'],
                            marker_color=px.colors.qualitative.Set3, 
                            name='Número de Vehículos'),
                            row=1, col=2
                            )

        # Actualizar el diseño del diseño y las etiquetas
        fig.update_layout(
                            
                            yaxis=dict(title='Número de Vehículos'),
                            showlegend=False
                            
                            )

        # Mostrar la figura
        return st.plotly_chart(fig,use_container_width = True )
    else:
         # Filtrar el DataFrame según la motorización seleccionada por el usuario
        df_filtrado = df_coches[df_coches['Motorización'] == input_usuario_vehiculos]

        # Lista de columnas booleanas
        clas_ener = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        df_filtrado['Sin clasificacion'] = ~df_filtrado[clas_ener].notnull().any(axis=1)  # 1 si las columnas de clas_ener son todas nulas
        df_filtrado[clas_ener] = df_filtrado[clas_ener].fillna(0)  # 0 en nulos de clas_ener

        # Lista de categorías
        clasificacion_energetica = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Sin clasificacion']

        # Suma acumulada de las categorías para el tipo de coche seleccionado
        grupo_motorizacion = df_filtrado[clasificacion_energetica][df_filtrado[clasificacion_energetica] == 1].count().reset_index(name='Número de Vehículos')

        # Renombramos las columnas
        grupo_motorizacion.columns = ['Clasificacion energética', 'Número de Vehículos']

        # Crear la gráfica
        fig = go.Figure()

        # Añadir la gráfica a la figura
        fig.add_trace(go.Bar(
            x=grupo_motorizacion['Clasificacion energética'],
            y=grupo_motorizacion['Número de Vehículos'],
            marker_color=px.colors.qualitative.Set3,
            name=f'Vehículos {input_usuario_vehiculos}'
        ))

        # Actualizar el diseño y las etiquetas
        fig.update_layout(
            title_text=f'Clasificación Energética de Vehículos {input_usuario_vehiculos}',
            xaxis=dict(title='Clasificación Energética'),
            yaxis=dict(title='Número de Vehículos'),
            showlegend=False
        )

        # Mostrar la figura
        return st.plotly_chart(fig,use_container_width = True )
    


def funcion_etiqueta_g_sin_especificar():
    df_filtrado = df_coches.copy()

    # Lista de columnas booleanas
    clas_ener = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    df_filtrado['Sin clasificacion'] = ~df_filtrado[clas_ener].notnull().any(axis=1) #1 si las columnas de clas_ener son todas nulas
    df_filtrado[clas_ener] = df_filtrado[clas_ener].fillna(0) #0 en nulos de clas_ener
    
    # Supongamos que 'df' es tu DataFrame con los datos
    df_suma = df_filtrado.groupby('Motorización')[['G', 'Sin clasificacion']].sum().reset_index()

    # Crear un gráfico de barras con Plotly Express
    fig = px.bar(
                    df_suma, 
                    x='Motorización', 
                    y=['G', 'Sin clasificacion'],
                    
                    labels={'value': 'Número de Vehículos', 'variable': 'Categoría'},
                    color_discrete_sequence=px.colors.qualitative.Set1
                ) 
    fig.update_xaxes(title = None)
    fig.update_layout(
            legend=dict(
                x=0.75,
                y=0.98,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

    return st.plotly_chart(fig,use_container_width = True )


def funcion_autonomia_bateria():
   
    df_filtered = df_coches[['Autonomía eléctrica (km)', 'Capacidad de la batería (kWh)', 'Motorización']].dropna()
    df_filtered = df_filtered[df_filtered['Capacidad de la batería (kWh)'] < 150]
    df_filtered['Tamaño_de_los_Puntos'] = ((df_filtered['Autonomía eléctrica (km)'] + df_filtered['Capacidad de la batería (kWh)']))

    color_discrete_map = {
                        'Eléctricos puros': 'blue',
                        'Híbridos enchufables': 'purple',
                        'Híbridos de gasolina': 'green'
                        }
    # Crear un gráfico de regresión con Plotly Express
    fig = px.scatter(
                        df_filtered, 
                        x='Capacidad de la batería (kWh)', 
                        y='Autonomía eléctrica (km)',
                        
                        labels={'Autonomía eléctrica (km)': 'Autonomía Eléctrica (km)', 'Capacidad de la batería (kWh)': 'Capacidad de la Batería (kWh)'},
                        color = 'Motorización',
                        size="Tamaño_de_los_Puntos",  # Agrega el tamaño de los puntos
                        opacity=0.3,
                        color_discrete_map = color_discrete_map
                         # Define la opacidad de los puntos
                    )  
    fig.update_layout(
            legend=dict(
                x=0,
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

    return st.plotly_chart(fig,use_container_width = True )

def funcion_violin_autonomia_conjunta_e():
    """
    Se devuelve la grafica de violin de la autonomia de coches electricos puros e hibridos
    """
    df_coches2 =df_coches[(df_coches['Autonomía eléctrica (km)'] > 0)]
    
    fig = px.violin(df_coches2, 
                    y='Autonomía eléctrica (km)', 
                    box=True, 
                    
                    labels={'Autonomía eléctrica (km)': 'Autonomía eléctrica (km)'},
                    color_discrete_sequence= ['tomato']
                    )
    fig.update_yaxes(range=[-60, 700])
    return st.plotly_chart(fig,use_container_width = True )


def funcion_autonomia_por_categoria_e():
    """
    Se devuelve el grafico que relaciona la categoria y la autonomia de todos los vehiculos electricos(hibridos y puros)
    """

    df_cochesModa = df_coches[(df_coches['Autonomía eléctrica (km)'] <= 100) & (df_coches['Autonomía eléctrica (km)'] > 41.00)]

    # Filtra para obtener solo vehículos eléctricos
    df_electricos = df_cochesModa.copy()

    # Selecciona solo las columnas de categorías dummy y la autonomía eléctrica
    columnas_categorias = ['L3e', 'L5e', 'L6e', 'L7e', 'M1', 'M2', 'M3', 'N1', 'N2', 'N3']
    df_categorias = df_electricos[['Autonomía eléctrica (km)'] + columnas_categorias]

    # Reshape del DataFrame para facilitar la visualización
    df_categorias_melted = pd.melt(df_categorias, id_vars='Autonomía eléctrica (km)', var_name='Categoría', value_name='Pertenece')

    # Filtra solo los casos donde Pertenece es 1
    df_categorias_melted = df_categorias_melted[df_categorias_melted['Pertenece'] == 1]

    # fig = px.histogram(df_categorias_melted, 
    #                x='Autonomía eléctrica (km)', 
    #                color='Categoría',
    #                marginal='rug+box',  # Puedes elegir 'rug+histogram' si prefieres
    #                labels={'Autonomía eléctrica (km)': 'Autonomía eléctrica (km)'},
    #                color_discrete_sequence=px.colors.qualitative.Set3)

    # Crea un gráfico historiplot
    fig = px.histogram(df_categorias_melted, x='Autonomía eléctrica (km)', color='Categoría',
                    #marginal='rug',  # Añade "rug plot" en los márgenes
                   
                    labels={'Autonomía eléctrica (km)': 'Autonomía eléctrica (km)'},
                    color_discrete_sequence=px.colors.qualitative.Set3)  # Paleta de colores
    
    fig.update_layout(
                        legend=dict(
                        x=0.95,
                        y=0.95,
                        bgcolor='rgba(255, 255, 255, 0)',
                        bordercolor='rgba(0, 0, 0, 0)',
                        borderwidth=1)
                    )

    # Muestra el gráfico
    return st.plotly_chart(fig,use_container_width = True )


def funcion_correlacion_potencia_autonomia_e():
    df_filtrado = df_coches[['Potencia eléctrica (kW)', 'Autonomía eléctrica (km)']].dropna()
    correlation_matrix = df_filtrado.corr()
    fig = px.imshow(
                    correlation_matrix,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    color_continuous_scale='Blues',
                    labels=dict(color='Correlación'),
                    )

    # Agrega ajustes
    fig.update_layout( width=500, height=500, xaxis=dict(tickangle=90))

    # Muestra el mapa de correlación
    return st.plotly_chart(fig,use_container_width = True )


def funcion_scater_potencia_autonomia_e(motorizacion):
    if motorizacion != 'Todos':
        df_filtrado = df_coches[['Potencia eléctrica (kW)', 'Autonomía eléctrica (km)', 'Motorización']].dropna()
        df_filtrado = df_filtrado[df_filtrado["Motorización"].isin([motorizacion])]  # Envuelve motorizacion en una lista
        
        fig = px.scatter(
            df_filtrado,
            x='Potencia eléctrica (kW)', 
            y='Autonomía eléctrica (km)', 
            color='Motorización',  # Utiliza la columna 'Motorización' como color
            labels={'Motorización': 'Motorización'}  # Etiqueta para la leyenda
        )  

        # Mover la leyenda dentro del gráfico
        fig.update_layout(
            legend=dict(
                x=0.80,
                y=0.1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

        # Mostrar el gráfico interactivo
        return st.plotly_chart(fig, use_container_width=True)
    else:
        # Crear un gráfico con todas las motorizaciones
        df_todas = df_coches[['Potencia eléctrica (kW)', 'Autonomía eléctrica (km)', 'Motorización']].dropna()
        
        fig = px.scatter(
            df_todas,
            x='Potencia eléctrica (kW)', 
            y='Autonomía eléctrica (km)', 
            color='Motorización',  # Utiliza la columna 'Motorización' como color
            labels={'Motorización': 'Motorización'}  # Etiqueta para la leyenda
        )

        # Mover la leyenda dentro del gráfico
        fig.update_layout(
            legend=dict(
                x=0.80,
                y=0.1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

        # Mostrar el gráfico interactivo
        return st.plotly_chart(fig, use_container_width=True)

def funcion_potencia_barras_e(motorizacion):
    # Crear un gráfico de barras con Plotly Express
    df_filtrado = df_coches[(df_coches["Motorización"].isin(motorizacion)) & (df_coches["Potencia eléctrica (kW)"].notna())]
    fig = px.histogram(df_filtrado, 
                          x='Potencia eléctrica (kW)',
                          nbins=100)
    # Mostrar el gráfico
    return st.plotly_chart(fig, use_container_width=True)

def funcion_potencia_caja_e(motorizacion):
    df_filtrado = df_coches[(df_coches["Motorización"].isin(motorizacion)) & (df_coches["Potencia eléctrica (kW)"].notna())]
    fig = px.box(df_filtrado, 
                 y = 'Potencia eléctrica (kW)', 
                )
    return st.plotly_chart(fig, use_container_width=True)


def funcion_quesito_emisiones():
    df_filtrado = df_coches[~(df_coches["Motorización"] == "Híbridos de gasóleo")]
    fig = px.pie(data_frame = df_filtrado,
                values=df_filtrado.groupby("Motorización")["Emisiones Máximo"].mean().to_list(),
                names = df_filtrado.groupby("Motorización")["Emisiones Máximo"].mean().index,
                hole = 0.6)
    fig.update_layout(showlegend = False)
    fig.update_traces(textinfo = "label+percent", textposition= "outside")
    #fig.update_traces(textinfo = "percent", textposition = "inside")
    return st.plotly_chart(fig, use_container_width=True)


def funcion_emisiones_consumo(input_usuario_vehiculos):
    if input_usuario_vehiculos == 'Todos':
        df_filtrado = df_coches[~(df_coches["Motorización"] == "Híbridos de gasóleo")]
        fig = px.scatter(
            data_frame=df_filtrado,
            x="Consumo Máximo (l/100km)",
            y="Emisiones Máximo",
            color="Motorización"
        )
        
        fig.update_layout(
            legend=dict(
                x=0.9,
                y=0.9,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )
        return st.plotly_chart(fig, use_container_width=True)
    else:
        # Filtrar el DataFrame por la motorización seleccionada
        df_filtrado = df_coches[df_coches['Motorización'] == input_usuario_vehiculos]
        
        # Verificar si hay datos para la motorización seleccionada
        if not df_filtrado.empty:
            fig = px.scatter(
                data_frame=df_filtrado,
                x="Consumo Máximo (l/100km)",
                y="Emisiones Máximo",
                color="Motorización"
            )
            return st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("No hay datos disponibles para la motorización seleccionada.")


    
def funcion_proporcion_motorizacion():
    fig = px.pie(
        values=df_coches["Motorización"].value_counts(),
        names=df_coches["Motorización"].value_counts().index
            )
    fig.update_traces(textinfo = 'none')
    return st.plotly_chart(fig, use_container_width=True)


def funcion_comparacion_consumo_motorizacion():
    df_filtrado = df_coches.dropna(subset=['Consumo Mínimo (l/100km)', 'Consumo Máximo (l/100km)'], how='all')
    lista_fig = []
    for tipo_motor in df_filtrado["Motorización"].unique():

        if tipo_motor == "Eléctricos puros":
            datos_motorizacion = df_filtrado[df_filtrado["Motorización"] == tipo_motor]["Consumo Eléctrico (kWh/100km)"]
            fig = px.box(datos_motorizacion, x=datos_motorizacion, 
                               labels={'count': 'Frecuencia', 'x': 'Consumo Eléctrico (kWh/100km)'})
            lista_fig.append(fig)


        elif tipo_motor in ["Híbridos de gasolina", "Híbridos enchufables", "Híbridos de gasóleo"]:


            datos_motorizacion = df_filtrado[df_filtrado["Motorización"] == tipo_motor]["Consumo Mínimo (l/100km)"]

            fig = px.box(datos_motorizacion, x=datos_motorizacion, 
                               labels={'count': 'Frecuencia', 'x': 'Consumo (l/100km)'},
                        title = "Consumo mínimo (Azul) - Consumo máximo (Rojo)")


            datos_motorizacion_2 = df_filtrado[df_filtrado["Motorización"] == tipo_motor]["Consumo Máximo (l/100km)"]

            fig.add_trace(px.box(datos_motorizacion_2, x=datos_motorizacion_2, color_discrete_sequence=['red'],
                                        labels={'count': 'Frecuencia', 'x': 'Consumo (l/100km)'}).data[0])
            lista_fig.append(fig)
  


            if tipo_motor != "Híbridos de gasóleo":

                datos_motorizacion = df_coches[df_coches["Motorización"] == tipo_motor]["Consumo Eléctrico (kWh/100km)"]

                fig = px.box(datos_motorizacion, x=datos_motorizacion, 
                               labels={'count': 'Frecuencia', 'x': 'Consumo Eléctrico (kWh/100km)'})
                lista_fig.append(fig)


                
            else:
                pass

        else:

            datos_motorizacion = df_filtrado[df_filtrado["Motorización"] == tipo_motor]["Consumo Mínimo (l/100km)"]

            fig = px.box(datos_motorizacion, x=datos_motorizacion,
                               labels={'count': 'Frecuencia', 'x': 'Consumo (l/100km)'},
                        title = "Consumo mínimo (Azul) - Consumo máximo (Rojo)")


            datos_motorizacion_2 = df_filtrado[df_filtrado["Motorización"] == tipo_motor]["Consumo Máximo (l/100km)"]
            
            fig.add_trace(px.box(datos_motorizacion_2, x=datos_motorizacion_2, color_discrete_sequence=['red'],
                                        labels={'count': 'Frecuencia', 'x': 'Consumo (l/100km)'}).data[0])
            
            
            lista_fig.append(fig)

    return lista_fig


def funcion_boxplot_motorizacion_usuario(tipo_motor):
    box = funcion_comparacion_consumo_motorizacion()
    if tipo_motor == "Eléctricos puros":
        st.plotly_chart(box[0], use_container_width=True)            
    elif tipo_motor == "Gasolina":
        st.plotly_chart(box[1], use_container_width=True)
    elif tipo_motor == "Gasóleo":
        st.plotly_chart(box[2], use_container_width=True)
    elif tipo_motor == "Híbridos enchufables":
        st.plotly_chart(box[3], use_container_width=True)
        st.plotly_chart(box[4], use_container_width=True)
    elif tipo_motor == "Híbridos de gasolina":
        st.plotly_chart(box[5], use_container_width=True)
        st.plotly_chart(box[6], use_container_width=True)
    elif tipo_motor == "Gas natural":
        st.plotly_chart(box[7], use_container_width=True)
    elif tipo_motor == "Híbridos de gasóleo":
        st.plotly_chart(box[8], use_container_width=True)




    



#Fin Funciones EcoEstudio
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
    





#PREDICCIONES
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________

def predicion_gasolina(input_usuario_precio_gasolina_semana_corriente):
    #cargar el df con el registro de la evolucion de precios
    df = pd.read_csv("Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    #cargar el pickle con el modelo entrenado
    modelo_pkl = load_model('./Data/model_gasolina')
    #nos quedamos con las ultimas 9 instancias del modelo
    instancia = df["Precio Gasolina"][-10: -1].to_list()
    #appendeamos la nueva instancia para tener 10
    instancia.append(input_usuario_precio_gasolina_semana_corriente)
    #transformamos a array para predecir con el modelo pkl
    instancia = np.array(instancia).reshape(-1, 10, 1)
    #predecimos
    prediccion_precio = modelo_pkl.predict(instancia)
    prediccion_precio = prediccion_precio[0][0]
    #devolvemos el resultado
    return prediccion_precio

def predicion_gasoleo(input_usuario_precio_gasoleo_semana_corriente):
    #cargar el df con el registro de la evolucion de precios
    df = pd.read_csv("Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    #cargar el pickle con el modelo entrenado
    modelo_pkl = load_model('./Data/model_gasoleo')
    #nos quedamos con las ultimas 9 instancias del modelo
    instancia = df["Precio Gasoleo"][-10: -1].to_list()
    #appendeamos la nueva instancia para tener 10
    instancia.append(input_usuario_precio_gasoleo_semana_corriente)
    #transformamos a array para predecir con el modelo pkl
    instancia = np.array(instancia).reshape(-1, 10, 1)
    #predecimos    
    prediccion_precio = modelo_pkl.predict(instancia)
    prediccion_precio = prediccion_precio[0][0]
    #devolvemos el resultado
    return prediccion_precio

#PREDICCIONES SEMANAS

def predicion_gasolina_semanas(input_usuario_precio_gasolina_semana_corriente, num_semanas):
    #cargamos el df con precios y el modelo pkl  
    df = pd.read_csv("Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    modelo_pkl = load_model('./Data/model_gasolina')
    #recorremos un bucle para predecir la primera instancia, agregar esta a una nueva lista y continuar prediciendo en función de las semanas indicadas.    
    for n in range(num_semanas):
        if n == 0:
            #se hace la primera prediccion y se appe
            prediccion_precio = predicion_gasolina(input_usuario_precio_gasolina_semana_corriente) 
            instancia = df["Precio Gasolina"][-9: -1].to_list()

            instancia.append(input_usuario_precio_gasolina_semana_corriente)
            instancia.append(prediccion_precio)

        else:

            instancia_array = np.array(instancia).reshape(-1, 10, 1)
            prediccion_precio = modelo_pkl.predict(instancia_array)
            prediccion_precio = prediccion_precio[0][0]
            instancia = instancia[1:]
            instancia.append(prediccion_precio)

    return instancia[(len(instancia)-num_semanas):]




def predicion_gasoleo_semanas(input_usuario_precio_gasoleo_semana_corriente, num_semanas):
    
    #cargamos el df con precios y el modelo pkl  
    df = pd.read_csv("Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    modelo_pkl = load_model('./Data/model_gasoleo')
    #recorremos un bucle para predecir la primera instancia, agregar esta a una nueva lista y continuar prediciendo en función de las semanas indicadas.    
    for n in range(num_semanas):
        if n == 0:
            #se hace la primera prediccion y se appe
            prediccion_precio = predicion_gasoleo(input_usuario_precio_gasoleo_semana_corriente) 
            instancia = df["Precio Gasoleo"][-9: -1].to_list()

            instancia.append(input_usuario_precio_gasoleo_semana_corriente)
            instancia.append(prediccion_precio)

        else:

            instancia_array = np.array(instancia).reshape(-1, 10, 1)
            prediccion_precio = modelo_pkl.predict(instancia_array)
            prediccion_precio = prediccion_precio[0][0]
            instancia = instancia[1:]
            instancia.append(prediccion_precio)

    return instancia[(len(instancia)-num_semanas):]





#FUNCION CREAR DF

def funcion_crear_df_predicciones(input_usuario_precio_gasoleo_semana_corriente=None, input_usuario_precio_gasolina_semana_corriente=None, num_semanas=True):
    
    if input_usuario_precio_gasolina_semana_corriente and input_usuario_precio_gasoleo_semana_corriente:
        
        precios_gasolina = predicion_gasolina_semanas(input_usuario_precio_gasolina_semana_corriente, num_semanas)
        precios_gasoleo = predicion_gasoleo_semanas(input_usuario_precio_gasoleo_semana_corriente, num_semanas)
        
        semana = [(semana + 5) for semana in range(len(precios_gasolina))]
        
        df_gasolina = pd.DataFrame({"Año": 2024, "Semana": semana, "Precio Gasolina": precios_gasolina})
        df_gasolina['Fecha'] = df_gasolina.apply(lambda row: pd.to_datetime(f'{int(row["Año"])}-W{int(row["Semana"])}-1', format='%G-W%V-%u'), axis=1)
        
        df_gasoleo = pd.DataFrame({"Año": 2024, "Semana": semana, "Precio Gasoleo": precios_gasoleo})
        df_gasoleo['Fecha'] = df_gasoleo.apply(lambda row: pd.to_datetime(f'{int(row["Año"])}-W{int(row["Semana"])}-1', format='%G-W%V-%u'), axis=1)
        
        df_combinado = pd.merge(df_gasolina, df_gasoleo[['Fecha', 'Precio Gasoleo']], on='Fecha')

        
        return df_combinado
    
    elif input_usuario_precio_gasolina_semana_corriente:    
        precios_gasolina = predicion_gasolina_semanas(input_usuario_precio_gasolina_semana_corriente, num_semanas)
        semana = [(semana + 5) for semana in range(len(precios_gasolina))]
        
        df_gasolina = pd.DataFrame({"Año": 2024, "Semana": semana, "Precio Gasolina": precios_gasolina})
        df_gasolina['Fecha'] = df_gasolina.apply(lambda row: pd.to_datetime(f'{int(row["Año"])}-W{int(row["Semana"])}-1', format='%G-W%V-%u'), axis=1)
        
        return df_gasolina
    
    elif input_usuario_precio_gasoleo_semana_corriente:
        precios_gasoleo = predicion_gasoleo_semanas(input_usuario_precio_gasoleo_semana_corriente, num_semanas)
        semana = [(semana + 5) for semana in range(len(precios_gasoleo))]
        
        df_gasoleo = pd.DataFrame({"Año": 2024, "Semana": semana, "Precio Gasoleo": precios_gasoleo})
        df_gasoleo['Fecha'] = df_gasoleo.apply(lambda row: pd.to_datetime(f'{int(row["Año"])}-W{int(row["Semana"])}-1', format='%G-W%V-%u'), axis=1)
        
        return df_gasoleo
    
    else:
        return None
    
#FUNCION CREAR GRAFICO

def funcion_agregado_prediccion(input_usuario_precio_gasoleo_semana_corriente = None, input_usuario_precio_gasolina_semana_corriente = None , num_semanas=True):
      
    df = pd.read_csv("Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    df["Semana"] = df["Semana"].apply(lambda x: x.split(" ")[1])
    df['Fecha'] = df.apply(lambda row: pd.to_datetime(f'{int(row["Año"])}-W{int(row["Semana"])}-1', format='%G-W%V-%u'), axis=1)
    df = df[df["Año"] == 2024]  
    df_semana_final = df.loc[df.index == df.index[-1]]
    df_combinado = funcion_crear_df_predicciones(input_usuario_precio_gasoleo_semana_corriente,input_usuario_precio_gasolina_semana_corriente,num_semanas)

    if input_usuario_precio_gasolina_semana_corriente and input_usuario_precio_gasoleo_semana_corriente:
 
        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasoleo","Precio Gasolina"],
                      labels={"value": "Precio", "variable": "Tipo de Combustible"},
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        
    
        df_combinado = pd.concat([df_semana_final,df_combinado], axis=0)
        
        traza_prediccion_gasoleo = px.line(df_combinado, x="Fecha", y="Precio Gasoleo",)
        traza_prediccion_gasoleo.data[0].line.color = "purple"  
        traza_prediccion_gasolina = px.line(df_combinado, x="Fecha", y="Precio Gasolina",)
        traza_prediccion_gasolina.data[0].line.color = "magenta"  

        # Agregar la traza de la predicción al gráfico
        fig.add_trace(traza_prediccion_gasoleo.data[0])
        fig.add_trace(traza_prediccion_gasolina.data[0])
        return st.plotly_chart(fig)
  
    elif input_usuario_precio_gasolina_semana_corriente:
 
        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasolina"],
                      labels={"value": "Precio", "variable": "Tipo de Combustible"},
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        

        df_combinado = pd.concat([df_semana_final,df_combinado], axis=0)

        traza_prediccion_gasolina = px.line(df_combinado, x="Fecha", y="Precio Gasolina",)
        traza_prediccion_gasolina.data[0].line.color = "magenta" 
        
        fig.add_trace(traza_prediccion_gasolina.data[0])
        return st.plotly_chart(fig)

    elif input_usuario_precio_gasoleo_semana_corriente:

        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasoleo"],
                      labels={"value": "Precio", "variable": "Tipo de Combustible"},
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        
    
        df_combinado = funcion_crear_df_predicciones(input_usuario_precio_gasoleo_semana_corriente,num_semanas)
        df_combinado = pd.concat([df_semana_final,df_combinado], axis=0)
  
        traza_prediccion_gasoleo = px.line(df_combinado, x="Fecha", y="Precio Gasoleo",)
        traza_prediccion_gasoleo.data[0].line.color = "magenta" 
        
        fig.add_trace(traza_prediccion_gasoleo.data[0])
        
        return st.plotly_chart(fig)
        
    
    #Se entra en ese comprobador cuanto solo la variable de la gasoleo existe
    elif input_usuario_precio_gasoleo_semana_corriente:
        #Se crea el df de la ultima fecha y la fig principal
        df = pd.read_csv("Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
        df["Semana"] = df["Semana"].apply(lambda x: x.split(" ")[1])
        df['Fecha'] = df.apply(lambda row: pd.to_datetime(f'{int(row["Año"])}-W{int(row["Semana"])}-1', format='%G-W%V-%u'), axis=1)
        df = df[df["Año"] == 2024]  
        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasoleo"],
                      labels={"value": "Precio", "variable": "Tipo de Combustible"},
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        
        df_semana_final = df.loc[df.index == df.index[-1]]
        #Se crea un df con las nuevas predicciones
        df_gasoleo = funcion_crear_df_predicciones(input_usuario_precio_gasoleo_semana_corriente,num_semanas)
        #Se combinan los dos df
        df_gasoleo = pd.concat([df_semana_final,df_gasoleo], axis=0)
        #Se agregan las nuevas lineas correspondientes, tanto para gasoleo y gasolina
        traza_prediccion_gasoleo = px.line(df_gasoleo, x="Fecha", y="Precio Gasoleo",)

        traza_prediccion_gasoleo.data[0].line.color = "magenta"  # Cambiar el color de la línea
        fig.add_trace(traza_prediccion_gasoleo.data[0])

         
        return st.plotly_chart(fig)

#funcion crear grafica general
def funcion_line_precio(choice):
    df = pd.read_csv("Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    df["Semana"] = df["Semana"].apply(lambda x: x.split(" ")[1])
    df['Fecha'] = df.apply(lambda row: pd.to_datetime(f'{int(row["Año"])}-W{int(row["Semana"])}-1', format='%G-W%V-%u'), axis=1)
    
    if choice == "Seleccione época":
        
        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasolina", "Precio Gasoleo"],
                      labels={"value": "Precio", "variable": "Tipo de Combustible"},
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        fig.update_layout(
            legend=dict(
                x=0,
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )
        return st.plotly_chart(fig, use_container_width = True )
    
    elif choice == "2002-2008":
        df = df[(df["Año"] >= 2002) & (df["Año"] <= 2008)]
        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasolina", "Precio Gasoleo"],
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        fig.update_layout(showlegend=False, xaxis_title='', yaxis_title='')
        
        return st.plotly_chart(fig, use_container_width = True )

    elif choice == "2011-2014":
        
        df = df[(df["Año"] >= 2011) & (df["Año"] <= 2014)]
        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasolina", "Precio Gasoleo"],
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        fig.update_layout(showlegend=False, xaxis_title='', yaxis_title='')
        
        return st.plotly_chart(fig, use_container_width = True )

    
    elif choice == "2022-Actualidad":
        
        df = df[(df["Año"] >= 2021)]
        
        fig = px.line(data_frame=df, 
                      x="Fecha", 
                      y=["Precio Gasolina", "Precio Gasoleo"],
                      color_discrete_map={"Precio Gasolina": "blue", "Precio Gasoleo": "red"})
        fig.update_layout(showlegend=False, xaxis_title='', yaxis_title='')
        
        return st.plotly_chart(fig, use_container_width = True )
    
        
    # Muestra el gráfico
    st.plotly_chart(fig, use_container_width=True)

def ultima_funcion():
    df_filtrado = df_coches[(df_coches["G"] == 1) | (df_coches["Sin clasificacion"] == 1)][["Emisiones Mínimo", "Emisiones Máximo", "Motorización", "G", "Sin clasificacion"]].copy()
    df_filtrado['Clasificación Energética'] = np.where(df_filtrado['G'] == 1, 'G', 'Sin clasificacion')
    df_filtrado['Clasificación Energética'] = np.where(df_filtrado['Sin clasificacion'] == 1, 'Sin clasificacion', df_filtrado['Clasificación Energética'])
    fig = px.scatter(data_frame  = df_filtrado,
            x           = "Emisiones Mínimo",
            y           = "Emisiones Máximo",
            hover_name  = "Motorización",
            color       = "Clasificación Energética"
            )
    
    fig.update_layout(
                        legend=dict(
                                    x=0.75,
                                    y=0.08,
                                    bgcolor='rgba(255, 255, 255, 0)',
                                    bordercolor='rgba(0, 0, 0, 0)',
                                    borderwidth=1)
                        )
    
    st.plotly_chart(fig,use_container_width = True )

#FIN PREDICCIONES
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________