import pandas as pd
import streamlit as st

import re
import numpy as np
# Visualizaciones

import plotly.subplots as sp
import plotly.graph_objects as go

# Visualizaciones de mapas
import folium
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from PIL import Image


from tensorflow.keras.models import load_model
#Importar archivos relevantes

df_coches = pd.read_csv("./Data/df_coches_escrapeo.csv")

df_coches = df_coches[~(df_coches["Motorización"]=="Híbridos de gasóleo")]
df_cargadores = pd.read_csv("./Data/df_cargadores.csv")
df_gasolineras = pd.read_csv('./Data/gasolineras_espana.csv')


# ------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------- ECOVIAJE -----------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------


# -------------------------------------------------------------  FUNCION GASOLINERAS -------------------------------------------------------------
def funcion_folium_cp_radio_gasolineras(cp,radio):
# Define el nombre de tu aplicación o proyecto
    nombre_app = "Mi Aplicación de Geolocalización"
    
    # Crea una instancia del geolocalizador y proporciona el nombre de tu aplicación como user_agent
    geolocator = Nominatim(user_agent=nombre_app)
    
    direccion = f"{str(cp)}, España"
    # Obtener las coordenadas de la dirección
    location = geolocator.geocode(direccion)
    
    # Imprimir las coordenadas
    if location:
        localizacion_inicial = [location.latitude, location.longitude]

    else:
        print("La dirección no se encontró.")

    # Crear un mapa centrado en las coordenadas iniciales
    mapa = folium.Map(location=localizacion_inicial, zoom_start=8)

    # Iterar sobre las filas del DataFrame y agregar marcadores al mapa
    for index, row in df_gasolineras.iterrows():
        coordenadas_punto = (row['Latitud'], row['Longitud'])
        distancia = geodesic(localizacion_inicial, coordenadas_punto).kilometers

  
        html_popup = f'''
                <div style="min-width: 300px; max-width: 300px; font-size: 12px;">
                    <p><strong>Dirección:</strong> {str(row["Dirección"])}</p>
                    <p><strong>Localidad:</strong> {str(row["Localidad"])}</p>
                    <p><strong>Provincia:</strong> {str(row["Provincia"])}</p>
                    <p><strong>Distancia a tu ubicación:</strong> {distancia:.2f} km</p>
            '''
        
        #Agregar marcador solo si la distancia es menor o igual a 1 km
        if distancia <= radio:
            # Crear un icono con un color específico (por ejemplo, rojo)
            icono_personalizado = folium.Icon(color='red', icon='star')

            # Crear un marcador con el icono personalizado
            folium.Marker(location=coordenadas_punto, popup=folium.Popup(html=html_popup), icon=icono_personalizado).add_to(mapa)

    mapa_html = mapa._repr_html_()
    return mapa_html

# ------------------------------------------------------------ FUNCION CARGADORES ELÉCTRICOS ------------------------------------------------------------------
def funcion_folium_cp_radio(cp = None,radio = None):
        
    try:
        cp = str(cp)
        radio = int(radio)   
        # Define el nombre de tu aplicación o proyecto
        nombre_app = "Mi Aplicación de Geolocalización"
        
        # Crea una instancia del geolocalizador y proporciona el nombre de tu aplicación como user_agent
        geolocator = Nominatim(user_agent=nombre_app)
        
        direccion = f"{str(cp)}, España"
        # Obtener las coordenadas de la dirección
        location = geolocator.geocode(direccion)
        
        # Imprimir las coordenadas
        if location:
            localizacion_inicial = [location.latitude, location.longitude]

        else:
            print("La dirección no se encontró.")

        # Crear un mapa centrado en las coordenadas iniciales
        mapa = folium.Map(location=localizacion_inicial, zoom_start=8)
        
        lista_indices = []
        # Iterar sobre las filas del DataFrame y agregar marcadores al mapa
        for index, row in df_cargadores.iterrows():
            coordenadas_punto = (row['latitude'], row['longitude'])
            distancia = geodesic(localizacion_inicial, coordenadas_punto).kilometers
            
            
            tiene_carga_rapida = False
            
            for valor in row['isfastChargeCapable']:
                if valor == "S": 
                    tiene_carga_rapida = True
                    break  
            html_popup = f'''
                    <div style="min-width: 300px; max-width: 300px; font-size: 12px;">
                        <p><strong>Dirección:</strong> {str(row["addressLine1"])}</p>
                        <p><strong>Tipo de cargadores:</strong> {str(row["title"]).replace("[", "").replace("]", "").replace("'", "")}</p>
                        <p><strong>Energía de cada cargador:</strong> {str(row["energia"]).replace("[", "").replace("]", "").replace("'", "")}</p>
                        <p><strong>Precio del kW/h:</strong> {str(row["usageCost"]).replace("[", "").replace("]", "").replace("'", "")}</p>
                        <p><strong>¿Tiene carga rápida?:</strong> {str(row["isfastChargeCapable"]).replace("[", "").replace("]", "").replace("'", "")}</p>
                        <p><strong>Distancia a tu ubicación:</strong> {distancia:.2f} km</p>
                        <p><strong>Indice del cargador :</strong> {index}<p>
                    </div>
                '''
            
            if tiene_carga_rapida == True:
            # Agregar marcador solo si la distancia es menor o igual a 1 km
                if distancia <= radio:

                    folium.Marker(location=coordenadas_punto, popup=folium.Popup(html=html_popup),  icon=folium.Icon(icon='flash')).add_to(mapa)
                    lista_indices.append(index)

            else:        
                if distancia <= radio:
                    folium.Marker(location=coordenadas_punto, popup=folium.Popup(html=html_popup)).add_to(mapa)
                    lista_indices.append(index)

        mapa_html = mapa._repr_html_()

        return mapa_html, lista_indices
    
    except:
        mapa = folium.Map(location=["38.5", "-4.5"], zoom_start=5)
        mapa_html = mapa._repr_html_()
        return mapa_html

# ---------------------------------------------- FUNCION GRAFICO CONSUMO ---------------------------------------------------------
def funcion_comparacion_seleccion_usario_modelo(columnas, lista_titulos, seleccionElectrico= None,seleccionGasoi=None,seleccionGasolina=None ,seleccionHibrido=None):
    lista_columnas = [x for x in range(1,columnas+1)]
    fig = sp.make_subplots(
                            rows=1, 
                            cols=columnas, 
                            subplot_titles=lista_titulos
                        )
    fig_2 = sp.make_subplots(
                            rows=1, 
                            cols=columnas, 
                            subplot_titles=lista_titulos
                        )

    #--------------------------------
    if seleccionElectrico and seleccionHibrido and columnas == 2:
        df_electrico = df_coches[df_coches['Modelo'] == seleccionElectrico].reset_index().copy()
        df_electrico["Modelo"] = df_electrico["Modelo"].values[0].split(" ")[0] + " " + df_electrico["Modelo"].values[0].split(" ")[1] + " " + df_electrico["Modelo"].values[0].split(" ")[2] 

        fig.add_trace(
            go.Bar(x=df_electrico["Modelo"], 
                y=df_electrico['Consumo Eléctrico (kWh/100km)'],
                marker_color="blue", 
                name="Consumo Eléctrico (kWh/100km)"), 
            row=1, col=lista_columnas[0]
        )

        fig_2.add_trace(
            go.Bar(x=df_electrico["Modelo"], 
                y=df_electrico['Emisiones Mínimo'],
                marker_color="orange", 
                showlegend=False), 
            row=1, col=lista_columnas[0]
        )

        df_hibrido = df_coches[df_coches['Modelo'] == seleccionHibrido].reset_index().copy()
        df_hibrido["Modelo"] = df_hibrido["Modelo"].values[0].split(" ")[0] + " " + df_hibrido["Modelo"].values[0].split(" ")[1]  + " " + df_hibrido["Modelo"].values[0].split(" ")[2]


        fig.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                y=df_hibrido['Consumo Eléctrico (kWh/100km)'],
                marker_color="blue",
                showlegend=False), 
            row=1, col=lista_columnas[1]
        )

        fig.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Consumo Mínimo (l/100km)']*9.6,
                    marker_color="green",
                    name="Consumo Combustible (kWh/100km) min"), 
            row=1, col=lista_columnas[1]
        )

        fig.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Consumo Máximo (l/100km)']*9.6,
                    marker_color="purple",
                    name="Consumo Combustible (kWh/100km) max"), 
            row=1, col=lista_columnas[1]
        )

        #------segunda grafica-------

        fig_2.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Emisiones Mínimo'],
                    marker_color="orange",
                    name="Emisiones de co2 min"), 
            row=1, col=lista_columnas[1]
        )

        fig_2.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Emisiones Máximo'],
                    marker_color="red",
                    name="Emisiones de co2 max"), 
            row=1, col=lista_columnas[1]
        )

    #--------------------------------
    if seleccionGasoi and seleccionGasolina and columnas == 2:
        df_gasoi = df_coches[df_coches['Modelo'] == seleccionGasoi].reset_index().copy()
        df_gasoi["Modelo"] = df_gasoi["Modelo"].values[0].split(" ")[0] + " " + df_gasoi["Modelo"].values[0].split(" ")[1]  + " " + df_gasoi["Modelo"].values[0].split(" ")[2] 

        fig.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Consumo Mínimo (l/100km)']*10.7 ,
                marker_color="green",
                name="Consumo Combustible (kWh/100km) min"), 
            row=1, col=lista_columnas[0]
        )

        fig.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Consumo Máximo (l/100km)']*10.7,
                marker_color="purple",
                name="Consumo Combustible (kWh/100km) min"), 
            row=1, col=lista_columnas[0]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Emisiones Mínimo'] ,
                marker_color="orange",
                name="Emisiones de co2 min"), 
            row=1, col=lista_columnas[0]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Emisiones Máximo'],
                marker_color="red",
                name="Emisiones de co2 max"), 
            row=1, col=lista_columnas[0]
        )


        df_gasolina = df_coches[df_coches['Modelo'] == seleccionGasolina].reset_index().copy()
        df_gasolina["Modelo"] = df_gasolina["Modelo"].values[0].split(" ")[0] + " " + df_gasolina["Modelo"].values[0].split(" ")[1]  + " " + df_gasolina["Modelo"].values[0].split(" ")[2] 

        fig.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Consumo Mínimo (l/100km)']*9.6,
                marker_color="green",
                showlegend=False), 
            row=1, col=lista_columnas[1]
        )

        fig.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Consumo Máximo (l/100km)']*9.6,
                marker_color="purple",
                showlegend=False), 
            row=1, col=lista_columnas[1]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Emisiones Mínimo'],
                marker_color="orange",
                showlegend=False), 
            row=1, col=lista_columnas[1]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Emisiones Máximo'],
                marker_color="red",
                showlegend=False), 
            row=1, col=lista_columnas[1]
        )
    
    #--------------------------------
    if seleccionElectrico and seleccionHibrido and seleccionGasoi and seleccionGasolina:
        df_electrico = df_coches[df_coches['Modelo'] == seleccionElectrico].reset_index().copy()
        df_electrico["Modelo"] = df_electrico["Modelo"].values[0].split(" ")[0] + " " + df_electrico["Modelo"].values[0].split(" ")[1] + " " + df_electrico["Modelo"].values[0].split(" ")[2] 

        fig.add_trace(
            go.Bar(x=df_electrico["Modelo"], 
                y=df_electrico['Consumo Eléctrico (kWh/100km)'],
                marker_color="blue", 
                name="Consumo Eléctrico (kWh/100km)"), 
            row=1, col=lista_columnas[0]
        )

        fig_2.add_trace(
            go.Bar(x=df_electrico["Modelo"], 
                y=df_electrico['Emisiones Máximo'],
                marker_color="red", 
                showlegend=False), 
            row=1, col=lista_columnas[0]
        )

        df_hibrido = df_coches[df_coches['Modelo'] == seleccionHibrido].reset_index().copy()
        df_hibrido["Modelo"] = df_hibrido["Modelo"].values[0].split(" ")[0] + " " + df_hibrido["Modelo"].values[0].split(" ")[1]  + " " + df_hibrido["Modelo"].values[0].split(" ")[2]


        fig.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                y=df_hibrido['Consumo Eléctrico (kWh/100km)'],
                marker_color="blue",
                showlegend=False), 
            row=1, col=lista_columnas[1]
        )

        fig.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Consumo Mínimo (l/100km)']*9.6,
                    marker_color="green",
                    name="Consumo Combustible (kWh/100km) min"), 
            row=1, col=lista_columnas[1]
        )

        fig.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Consumo Máximo (l/100km)']*9.6,
                    marker_color="purple",
                    name="Consumo Combustible (kWh/100km) max"), 
            row=1, col=lista_columnas[1]
        )

        fig_2.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Emisiones Mínimo'],
                    marker_color="orange",
                    name="Emisiones de co2 min"), 
            row=1, col=lista_columnas[1]
        )

        fig_2.add_trace(
            go.Bar(x=df_hibrido["Modelo"], 
                    y=df_hibrido['Emisiones Máximo'],
                    marker_color="red",
                    name="Emisiones de co2 max"), 
            row=1, col=lista_columnas[1]
        )

        df_gasoi = df_coches[df_coches['Modelo'] == seleccionGasoi].reset_index().copy()
        df_gasoi["Modelo"] = df_gasoi["Modelo"].values[0].split(" ")[0] + " " + df_gasoi["Modelo"].values[0].split(" ")[1]  + " " + df_gasoi["Modelo"].values[0].split(" ")[2] 

        fig.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Consumo Mínimo (l/100km)']*10.7 ,
                marker_color="green",
                showlegend=False), 
            row=1, col=lista_columnas[2]
        )

        fig.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Consumo Máximo (l/100km)']*10.7 ,
                marker_color="purple",
                showlegend=False), 
            row=1, col=lista_columnas[2]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Emisiones Mínimo'] ,
                marker_color="orange",
                showlegend=False), 
            row=1, col=lista_columnas[2]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasoi["Modelo"], 
                y=df_gasoi['Emisiones Máximo'] ,
                marker_color="red",
                showlegend=False), 
            row=1, col=lista_columnas[2]
        )

        df_gasolina = df_coches[df_coches['Modelo'] == seleccionGasolina].reset_index().copy()
        df_gasolina["Modelo"] = df_gasolina["Modelo"].values[0].split(" ")[0] + " " + df_gasolina["Modelo"].values[0].split(" ")[1]  + " " + df_gasolina["Modelo"].values[0].split(" ")[2] 

        fig.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Consumo Mínimo (l/100km)']*9.6,
                marker_color="green",
                showlegend=False), 
            row=1, col=lista_columnas[3]
        )

        fig.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Consumo Máximo (l/100km)']*9.6,
                marker_color="purple",
                showlegend=False), 
            row=1, col=lista_columnas[3]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Emisiones Mínimo'],
                marker_color="orange",
                showlegend=False), 
            row=1, col=lista_columnas[3]
        )

        fig_2.add_trace(
            go.Bar(x=df_gasolina["Modelo"], 
                y=df_gasolina['Emisiones Máximo'],
                marker_color="red",
                showlegend=False), 
            row=1, col=lista_columnas[3]
        )
        fig.update_layout(
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',
                        )
        
        fig_2.update_layout(
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',
                        )
        
        fig.update_yaxes(range=[0, 100], row=1, col=1)
        fig.update_yaxes(range=[0, 100], row=1, col=2)
        fig.update_yaxes(range=[0, 100], row=1, col=3)
        fig.update_yaxes(range=[0, 100], row=1, col=4)

        fig_2.update_yaxes(range=[0, 200], row=1, col=1)
        fig_2.update_yaxes(range=[0, 200], row=1, col=2)
        fig_2.update_yaxes(range=[0, 200], row=1, col=3)
        fig_2.update_yaxes(range=[0, 200], row=1, col=4)
        # Mostrar la figura
        return st.plotly_chart(fig, use_container_width=True), st.plotly_chart(fig_2, use_container_width=True)

    else:
        fig.update_layout(
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',
                        )
        fig.update_yaxes(range=[0, 100], row=1, col=1)
        fig.update_yaxes(range=[0, 100], row=1, col=2)

        fig_2.update_layout(
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)',
                        )
        fig_2.update_yaxes(range=[0, 200], row=1, col=1)
        fig_2.update_yaxes(range=[0, 200], row=1, col=2)
        # Mostrar la figura
        return st.plotly_chart(fig, use_container_width=True), st.plotly_chart(fig_2, use_container_width=True)

# --------------------------------------------- FUNCION COMPARADOR GASOLINA Y GASOLEO -------------------------------------------
def funcion_seleccion_modelos_gasolina(columna, etiqueta_modelo, motorizacion,  lista_box):
    
    with columna:
        df_filtrado = df_coches[df_coches["Motorización"] == motorizacion].copy() 
        c_1, c_2 = st.columns([1.1, 0.8])

        if motorizacion == "Gasóleo":
            with c_1:
                st.markdown("")
                st.markdown(f"<div style='color: cyan; text-align: justify; font-size: 50px; font-weight: bold'>Vehículos</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='color: cyan; text-align: justify; font-size: 50px; font-weight: bold'>&</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='color: cyan; text-align: justify; font-size: 50px; font-weight: bold'>{etiqueta_modelo}</div>", unsafe_allow_html=True)
            
        else:
            with c_1:
                st.markdown("")
                st.markdown("<div style='color: cyan; text-align: justify; font-size: 50px; font-weight: bold'>Gasolina</div>", unsafe_allow_html=True)
                flecha_gasolina = Image.open("images/flecha_gasolina.png")
                # Cambiar el tamaño de la imagen
                ancho_deseado = 450 
                alto_deseado = 150
                flecha_gasolina = flecha_gasolina.resize((ancho_deseado, alto_deseado))
                st.image(flecha_gasolina)

        consumo_minimo_gasolina = df_filtrado['Consumo Mínimo (l/100km)'].dropna().sort_values().unique()

        with c_2:
            consumo_min_g = st.selectbox(key=f"{lista_box[0]}",label = "Consumo mínimo", options=consumo_minimo_gasolina)
            
            

            st.session_state.modelos_g_visible = True
            st.session_state.consumo_max_visible = True
            st.session_state.emisiones_visible = True
            
        if st.session_state.consumo_max_visible:
            
            df_filtrado = df_filtrado[df_filtrado["Consumo Mínimo (l/100km)"] == consumo_min_g]
            consumo_maximo_gasolina = df_filtrado["Consumo Máximo (l/100km)"].sort_values().unique()

            with c_2:
                consumo_max_g = st.selectbox(key=f"{lista_box[1]}",label="Consumo máximo", options=consumo_maximo_gasolina)
                
                
    
        if st.session_state.emisiones_visible:

            df_filtrado = df_filtrado[df_filtrado["Consumo Máximo (l/100km)"] == consumo_max_g]
            emisiones_gasolina = df_filtrado["Emisiones Máximo"].sort_values().unique()

            with c_2:
                emisiones_g = st.selectbox(key=f"{lista_box[2]}",label="Emisiones de co2", options=emisiones_gasolina)
                
                

        if st.session_state.modelos_g_visible:

            df_filtrado = df_filtrado[df_filtrado["Emisiones Máximo"] == emisiones_g]
            modelos_gasolina = df_filtrado["Modelo"].sort_values().unique()
            modelo_g = st.selectbox(key=f"{lista_box[3]}",label=f"Seleccione un vehículo {motorizacion}", options=modelos_gasolina)

            st.markdown("")
            

            return modelo_g
        
# ------------------------------------------------------------- FUNCION HIBRIDOS -------------------------------------------------

def funcion_seleccion_modelos_hibridos(columna, etiqueta_modelo, lista_box):
    df_filtrado = df_coches[(df_coches["Motorización"] == "Híbridos de gasolina") | (df_coches["Motorización"] == "Híbridos enchufables")].copy()
    with columna:
        
        st.write(f"<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>{etiqueta_modelo}</span>", unsafe_allow_html=True)
        consumo_electrico_puro = df_filtrado['Consumo Eléctrico (kWh/100km)'].dropna().sort_values().astype(str).unique()

        consumo_electrico_puro = ["Cualquiera"] + list(consumo_electrico_puro)

        consumo_e = st.selectbox(key=f"{lista_box[0]}",label = "Consumo eléctrico", options=consumo_electrico_puro)
        
        if consumo_e == "Cualquiera":
            
            desglosado = Image.open("images/desglosado.png")
            # Cambiar el tamaño de la imagen
            ancho_deseado = 555
            alto_deseado = 557
            desglosado = desglosado.resize((ancho_deseado, alto_deseado))
            st.image(desglosado)

            df_filtrado_copy = df_filtrado.copy()
            
            modelos_electrico = df_filtrado_copy["Modelo"].sort_values().unique()
            modelo_e = st.selectbox(key=f"{lista_box[8]}",label=f"Seleccione un vehículo híbrido", options=modelos_electrico)

            st.markdown("")
        else:
            consumo_e = float(consumo_e)
            st.session_state.potencia_e_visible = True
            st.session_state.autonomia_e_visible = True
            st.session_state.bateria_e_visible = True
            st.session_state.consumo_min_visible = True
            st.session_state.modelos_e_visible = True
            st.session_state.consumo_max_visible = True

            
            if st.session_state.potencia_e_visible:
                st.markdown("")
                df_filtrado = df_filtrado[df_filtrado["Consumo Eléctrico (kWh/100km)"] == consumo_e]
                potencia_electrico_puro = df_filtrado["Potencia eléctrica (kW)"].sort_values().unique()
                potencia_e = st.selectbox(key=f"{lista_box[1]}",label="Potencia eléctrica", options=potencia_electrico_puro)
                st.markdown("")
                
            if st.session_state.autonomia_e_visible:
                st.markdown("")
                df_filtrado = df_filtrado[df_filtrado["Potencia eléctrica (kW)"] == potencia_e]
                autnomia_electrico_puro = df_filtrado["Autonomía eléctrica (km)"].sort_values().unique()
                autonomia_e = st.selectbox(key=f"{lista_box[2]}",label="Autonomía eléctrica", options=autnomia_electrico_puro)
                st.markdown("")
            if st.session_state.bateria_e_visible:
                
                df_filtrado = df_filtrado[df_filtrado["Autonomía eléctrica (km)"] == autonomia_e]
                potencia_electrico_puro = df_filtrado["Capacidad de la batería (kWh)"].sort_values().unique()
                bateria_e = st.selectbox(key=f"{lista_box[3]}",label="Capacidad de batería", options=potencia_electrico_puro)
                st.markdown("")
            if st.session_state.consumo_min_visible:
                st.markdown("")
                df_filtrado = df_filtrado[df_filtrado["Capacidad de la batería (kWh)"] == bateria_e]
                consumo_minimo_hibrido = df_filtrado["Consumo Mínimo (l/100km)"].sort_values().unique()
                consumo_min = st.selectbox(key=f"{lista_box[5]}",label="Consumo mínimo", options=consumo_minimo_hibrido)
                st.markdown("")
            if st.session_state.consumo_max_visible:
                st.markdown("")
                df_filtrado = df_filtrado[df_filtrado["Consumo Mínimo (l/100km)"] == consumo_min]
                consumo_maximo_hibrido = df_filtrado["Consumo Máximo (l/100km)"].sort_values().unique()
                consumo_max = st.selectbox(key=f"{lista_box[6]}",label="Consumo máximo", options=consumo_maximo_hibrido)
                st.markdown("<br>", unsafe_allow_html=True)
            if st.session_state.modelos_e_visible:

                df_filtrado = df_filtrado[df_filtrado["Consumo Máximo (l/100km)"] == consumo_max]
                modelos_electrico = df_filtrado["Modelo"].sort_values().unique()
                modelo_e = st.selectbox(key=f"{lista_box[8]}",label=f"Seleccione un vehículo híbrido", options=modelos_electrico)
      
            st.markdown("")    
           
        return modelo_e
    

# ----------------------------------------------- FUNCION ELECTRICOS -----------------------------------------------------------
def funcion_seleccion_modelos_electricos(columna, etiqueta_modelo, motorizacion, lista_box):
    
    with columna:
        
        st.markdown(f"<div style='color: cyan; text-align: justify; font-size: 50px; font-weight: bold'>Vehículos</div>", unsafe_allow_html=True)
        foto_dentro_coche = Image.open("images/dentro_electrico.png")
        # Cambiar el tamaño de la imagen
        ancho_deseado = 600
        alto_deseado = 300
        foto_dentro_coche = foto_dentro_coche.resize((ancho_deseado, alto_deseado))
        st.image(foto_dentro_coche)
        c_1, c_2 = st.columns([0.6, 0.8])
        with c_1:
            st.markdown("")
            df_filtrado = df_coches[df_coches["Motorización"] == motorizacion].copy()
            consumo_electrico_puro = df_filtrado['Consumo Eléctrico (kWh/100km)'].dropna().sort_values().astype(str).unique()
            consumo_electrico_puro = ["Cualquiera"] + list(consumo_electrico_puro)
            st.markdown(f"<div style='color: cyan; text-align: justify; font-size: 30px; font-weight: bold'>{etiqueta_modelo}</div>", unsafe_allow_html=True)

        with c_2:
            consumo_e = st.selectbox(key=f"{lista_box[0]}",label = "Consumo eléctrico", options=consumo_electrico_puro) 

        if consumo_e == "Cualquiera":

            st.dataframe(df_coches[(df_coches["Motorización"] != "Gasolina") & (df_coches["Motorización"] != "Gasóleo") & (df_coches["Motorización"] != "Gas natural")][["Modelo", "Motorización", "Consumo Eléctrico (kWh/100km)", "Consumo Mínimo (l/100km)","Consumo Máximo (l/100km)"]], width=1000, height=250)

            df_filtrado_copy = df_filtrado.copy()
            modelos_electrico = df_filtrado_copy["Modelo"].sort_values().unique()
            modelo_e = st.selectbox(key=f"{lista_box[8]}",label=f"Seleccione un vehículo eléctrico puro", options=modelos_electrico)
            st.markdown("")
        else:
            st.markdown("")
    
            consumo_e = float(consumo_e)
            st.session_state.potencia_e_visible = True
            st.session_state.autonomia_e_visible = True
            st.session_state.bateria_e_visible = True
            st.session_state.modelos_e_visible = True

                
            if st.session_state.potencia_e_visible:
                
                df_filtrado = df_filtrado[df_filtrado["Consumo Eléctrico (kWh/100km)"] == consumo_e]
                potencia_electrico_puro = df_filtrado["Potencia eléctrica (kW)"].sort_values().unique()

                #with c_2:
                potencia_e = st.selectbox(key=f"{lista_box[1]}",label="Potencia eléctrica", options=potencia_electrico_puro)
        
            if st.session_state.autonomia_e_visible:

                df_filtrado = df_filtrado[df_filtrado["Potencia eléctrica (kW)"] == potencia_e]

            #with c_2:
                autnomia_electrico_puro = df_filtrado["Autonomía eléctrica (km)"].sort_values().unique()
                autonomia_e = st.selectbox(key=f"{lista_box[2]}",label="Autonomía eléctrica", options=autnomia_electrico_puro)
                
                
            if st.session_state.bateria_e_visible:

                df_filtrado = df_filtrado[df_filtrado["Autonomía eléctrica (km)"] == autonomia_e]
                potencia_electrico_puro = df_filtrado["Capacidad de la batería (kWh)"].sort_values().unique()

                #with c_2:
                bateria_e = st.selectbox(key=f"{lista_box[3]}",label="Capacidad de batería", options=potencia_electrico_puro)
                
                
            if st.session_state.modelos_e_visible:
                
                df_filtrado = df_filtrado[df_filtrado["Capacidad de la batería (kWh)"] == bateria_e]
                modelos_electrico = df_filtrado["Modelo"].sort_values().unique()
                modelo_e = st.selectbox(key=f"{lista_box[4]}",label=f"Seleccione un vehículo eléctrico puro", options=modelos_electrico)

            st.markdown("")
        return modelo_e
            
# ---------------------------------------------------------- VIAJE ELÉCTRICO -------------------------------------------------
def funcion_precio_viaje_e(modelo, km ,seleccion_usuario_punto_recarga):
    patron_precio = r"(\d+,\d+)€"
    lista_precio = []
    lista_kW = []
    # Iterar sobre cada fila y extraer el precio si está presente
    
    for cargadores in df_cargadores.loc[seleccion_usuario_punto_recarga, "usageCost"].split(" "):
        try:
            match = re.search(patron_precio, cargadores)
            
            if match:
                
                
                precio = float(match.group(1).replace(",","."))
                df_coches[df_coches["Motorización"]=="Eléctricos puros"]
                datos_coche=df_coches[df_coches["Modelo"] == modelo]
                consumo_kwh_100km = datos_coche["Consumo Eléctrico (kWh/100km)"].reset_index(drop=True)[0]
                precio_km = (consumo_kwh_100km/100)*precio
                
                if precio :
                    lista_kW.append(round(precio, 2))
                    lista_precio.append(round(precio_km*km, 2))
                else:
                    lista_kW.append('Desconocido')
                    lista_precio.append('Desconocido')

        except:
            pass
        
    diccionario = {"Tipo Cargador": df_cargadores.loc[seleccion_usuario_punto_recarga, "title"],
                "Precio del kW" : lista_kW,
                "Coste Viaje €": lista_precio,
                "Modelo": modelo,
                "Consumo Eléctrico kWh/100km": df_coches[df_coches["Modelo"] == modelo]["Consumo Eléctrico (kWh/100km)"].to_list()
                }

    return lista_precio, lista_kW

# ---------------------------------------------------- VIJAE GASOLINA -------------------------------------------------
def predicion_gasolina(input_usuario_precio_gasolina_semana_corriente):
    
    df = pd.read_csv("./Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    modelo_pkl = load_model('./Data/model_gasolina')

    instancia = df["Precio Gasolina"][-10: -1].to_list()
    instancia.append(input_usuario_precio_gasolina_semana_corriente)
    instancia = np.array(instancia).reshape(-1, 10, 1)
    
    prediccion_precio = modelo_pkl.predict(instancia)
    prediccion_precio = prediccion_precio[0][0]

    return round(prediccion_precio, 2)

# ----------------------------------------------------------- VIAJE GASÓLEO -------------------------------------------------
def predicion_gasoleo(input_usuario_precio_gasoleo_semana_corriente):
    
    df = pd.read_csv("./Data/Precios_Gasolina_y_Precios_Gasoleo.csv")
    modelo_pkl = load_model('./Data/model_gasoleo')

    instancia = df["Precio Gasoleo"][-10: -1].to_list()
    instancia.append(input_usuario_precio_gasoleo_semana_corriente)
    instancia = np.array(instancia).reshape(-1, 10, 1)
    
    prediccion_precio = modelo_pkl.predict(instancia)
    prediccion_precio = prediccion_precio[0][0]

    return round(prediccion_precio, 2)

# ----------------------------------------------------- VIAJES --------------------------------------------------------------
def predicePrecio(input_Coche, km, seleccion_usuario_punto_recarga, input_usuario_gasolina = None, input_usuario_gasoleo = None):
    consumo = df_coches[(df_coches['Modelo'] == input_Coche)]["Consumo medio l/1km"].values[0]
    media_diferencia_entre_gasoi_y_gasolina = 0.08364892982456133
    if ((df_coches[df_coches['Modelo'] == input_Coche]['Motorización']).values[0]  == "Eléctricos puros"):
        #Prediccion electrica
        precios_viajes, diccionario = funcion_precio_viaje_e(input_Coche, km, seleccion_usuario_punto_recarga)

        return precios_viajes, diccionario
    elif not input_usuario_gasoleo:
        
        if ((df_coches[df_coches['Modelo'] == input_Coche]['Motorización']).values[0]  == "Gasolina"):
            
            predic = predicion_gasolina(input_usuario_gasolina + media_diferencia_entre_gasoi_y_gasolina)
            resultado = (predic*consumo)*km

            return round(resultado, 2),predic
        
        
        elif ((df_coches[df_coches['Modelo'] == input_Coche]['Motorización']).values[0]  == "Gasóleo"):
            #Prediccion Gasoil
            predic = predicion_gasoleo(input_usuario_gasolina  + media_diferencia_entre_gasoi_y_gasolina)
            resultado = (predic*consumo)*km

            return round(resultado, 2),predic
    
        else:
            precio_parte_electrico, diccionario = funcion_precio_viaje_e(input_Coche, km, seleccion_usuario_punto_recarga)
            predic = predicion_gasolina(input_usuario_gasolina  + media_diferencia_entre_gasoi_y_gasolina)
            resultado_gasolina = (predic*consumo)*km

            precios_viajes = []
            for i in precio_parte_electrico:
                resultado = i +  resultado_gasolina
                precios_viajes.append(round(resultado, 2))
            
            return precios_viajes, precio_parte_electrico, diccionario, round(resultado_gasolina, 2), predic
        
    
    elif not input_usuario_gasolina:

        if ((df_coches[df_coches['Modelo'] == input_Coche]['Motorización']).values[0]  == "Gasolina"):
            
            predic = predicion_gasolina(input_usuario_gasoleo - media_diferencia_entre_gasoi_y_gasolina)
            resultado = (predic*consumo)*km

            return round(resultado, 2),predic
        
        elif ((df_coches[df_coches['Modelo'] == input_Coche]['Motorización']).values[0]  == "Gasóleo"):
            #Prediccion Gasoil
            predic = predicion_gasoleo(input_usuario_gasoleo - media_diferencia_entre_gasoi_y_gasolina)
            resultado = (predic*consumo)*km

            return round(resultado, 2),predic
    
        else:
            precio_parte_electrico, diccionario = funcion_precio_viaje_e(input_Coche, km, seleccion_usuario_punto_recarga)
            predic = predicion_gasolina(input_usuario_gasolina  + media_diferencia_entre_gasoi_y_gasolina)
            resultado_gasolina = (predic*consumo)*km

            precios_viajes = []
            for i in precio_parte_electrico:
                resultado = i +  resultado_gasolina
                precios_viajes.append(round(resultado, 2))

            
            
            return precios_viajes, precio_parte_electrico, diccionario, round(resultado_gasolina, 2), predic

    elif input_usuario_gasolina and input_usuario_gasoleo:

        if ((df_coches[df_coches['Modelo'] == input_Coche]['Motorización']).values[0]  == "Gasolina"):
            
            predic = predicion_gasolina(input_usuario_gasolina)
            resultado = (predic*consumo)*km

            return round(resultado, 2),predic
        
        elif ((df_coches[df_coches['Modelo'] == input_Coche]['Motorización']).values[0]  == "Gasóleo"):
            #Prediccion Gasoil
            predic = predicion_gasoleo(input_usuario_gasoleo)
            resultado = (predic*consumo)*km

            return round(resultado, 2),predic
    
        else:
            precio_parte_electrico, diccionario = funcion_precio_viaje_e(input_Coche, km, seleccion_usuario_punto_recarga)
            predic = predicion_gasolina(input_usuario_gasolina  + media_diferencia_entre_gasoi_y_gasolina)
            resultado_gasolina = (predic*consumo)*km

            precios_viajes = []
            for i in precio_parte_electrico:
                resultado = i +  resultado_gasolina
                precios_viajes.append(round(resultado, 2))

            
            
            return precios_viajes, precio_parte_electrico, diccionario, round(resultado_gasolina, 2), predic
    

    
        
        
