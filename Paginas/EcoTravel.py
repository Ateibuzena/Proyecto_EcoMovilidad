# --------------------------------------------------- FUNCION PÁGINA ECOVIAJE ------------------------------------------------------
import pandas as pd
import streamlit as st

from PIL import Image

from funciones.funciones_ecoviaje_ingles import *


def pagina_ecoviaje_ingles():
    st.write("<span style='display:block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>Vehicle Comparator</span>", unsafe_allow_html=True)

    text = """<div style=' text-align: justify; font-size: 18px;'>
                How many times have you wondered if buying an electric or hybrid car would save you more than a combustion one?
                With our comparator, you can choose from a wide variety of vehicles with all the features
                you need and see the differences between them. Also, everything you need to organize your trips 
                efficiently and economically you will find in this application.
                </div>"""

    # Display the text centered

    st.markdown(text, unsafe_allow_html=True)

    st.markdown("<span style='white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>- - - - - - - - - -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - - - - - - - - - - - - - - - - - - - - - - - - -</span>", unsafe_allow_html=True)

    columna_1, columna_2, columna_3 = st.columns([1, 0.1, 1])


# ---------------------------------------------- ELÉCTRICOS --------------------------------------------------------------------------
    modelo_electrico_puro = funcion_seleccion_modelos_electricos(columna_1, "Electric","Pure Electric", ["e_1", "e_2", "e_3", "e_4", "e_5", "e_6", "e_7", "e_8", "e_9"])

# ------------------------------------------------- Hybrids ---------------------------------------------------------------------------------
    modelo_hibrido = funcion_seleccion_modelos_hibridos(columna_3, "Hybrids", ["h_1", "h_2", "h_3", "h_4", "h_5", "h_6", "h_7", "h_8", "h_9"])

# ------------------------------------------------- COMPARADOR ELÉCTRICO ---------------------------------------------------------------
    #columna_1, columna_2 = st.columns(2)
    
    if modelo_hibrido and modelo_electrico_puro:
        with columna_3:
            
            # Crea el botón utilizando la clase CSS personalizada
            boton_modelos_e = st.button(use_container_width=True, label="Compare Electric vs Hybrid", key="o_1")
        if boton_modelos_e:
            st.session_state.grafico_visible = True
        if "grafico_visible" not in st.session_state:
                st.session_state.grafico_visible = False
            
        if not st.session_state.grafico_visible:
            pass
        else:
            #st.write(modelo_hibrido)
            #st.write(modelo_electrico_puro)
            funcion_comparacion_seleccion_usario_modelo(2, ["Pure Electrical", "Hybrid"], seleccionElectrico= str(modelo_electrico_puro),seleccionGasoi=None,seleccionGasolina=None ,seleccionHibrido=str(modelo_hibrido))
        with columna_1:
            
    
            st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Compare and resolve your doubts!</span>", unsafe_allow_html=True)
    else:
        with columna_1:
            st.markdown("")
            st.markdown("")
            
            boton_modelos_e = st.button(key= "o_1", label="Compare Electric vs Hybrid")
        if boton_modelos_e:
            st.write("You need to select another model")

    st.markdown("<span style='white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>- - - - - - - - - -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - - - - - - - - -  - - - - - - - - - - - - - - -  </span>", unsafe_allow_html=True)

# ------------------------------------------------ Gasoline -----------------------------------------------------------------------------------------------------
    st.markdown("")
    
    
    columnita_1, columnita_2 = st.columns(2)
    modelo_gasoleo = funcion_seleccion_modelos_gasolina(columnita_1, "Diesel", "Diesel",["g_1", "g_2", "g_3", "g_4", "g_5", "g_6", "g_7", "g_8", "g_9"])
    modelo_gasolina = funcion_seleccion_modelos_gasolina(columnita_2, "Gasoline", "Gasoline", ["l_1", "l_2", "l_3", "l_4", "l_5", "l_6", "l_7", "l_8", "l_9"])

    columna_1, columna_2, columna_3= st.columns([1.1, 0.5, 1])

    if modelo_gasolina and modelo_gasoleo:
        with columna_2:
            boton_modelos_g = st.button(key= "o_2", label="Compare Gasoline vs Diesel")
        if boton_modelos_g:
            st.session_state.grafico2_visible = True
        if "grafico2_visible" not in st.session_state:
                st.session_state.grafico2_visible = False
            
        if not st.session_state.grafico2_visible:
            pass
        else:
            #st.write(modelo_hibrido)
            #st.write(modelo_electrico_puro)
            funcion_comparacion_seleccion_usario_modelo(2, ["Diesel", "Gasoline"], seleccionElectrico= None,seleccionGasoi=str(modelo_gasoleo),seleccionGasolina=str(modelo_gasolina) ,seleccionHibrido=None)
    else:
        with columna_2:
            boton_modelos_g = st.button(key= "o_2", label="Compare Gasoline vs Diesel")
        if boton_modelos_g:
            st.write("You need to select another model")

    st.markdown("")

    columna_1, columna_2, columna_3= st.columns([1.05, 0.4, 1])
    
    if modelo_electrico_puro and modelo_hibrido and modelo_gasolina and modelo_gasoleo:
        
        with columna_2:
            boton_comparar = st.button(key = "o_3", label = "Compare all cars")
        if boton_comparar:
            funcion_comparacion_seleccion_usario_modelo(4, ["Pure Electrical","Hybrid","Diesel", "Gasoline"], seleccionElectrico= str(modelo_electrico_puro),seleccionGasoi=str(modelo_gasoleo),seleccionGasolina=str(modelo_gasolina) ,seleccionHibrido=str(modelo_hibrido))

    else:
        with columna_2:
            boton_comparar = st.button(key = "o_3", label = "Compare all cars")
            if boton_comparar:
                st.write("For this you must select a model of each type of Vehicle")

    # ---------------------------------------------------- CALCULADOR DE RUTAS -------------------------------------------------------
    st.write("<span style='display:block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>Travel Planner</span>", unsafe_allow_html=True)
    
    texto = """<div style=' text-align: justify; font-size: 18px;'>
                Are you worried about finding a gas station on your route or a charger for your electric vehicle?
                Our application allows you to easily explore the options of Gas stations and charging points
                electricity within a specific radius from your zip code.</div>"""

    st.markdown(texto, unsafe_allow_html=True)

    #---------------------------------------------------------- CABECERA --------------------------------------------------------
        
    st.markdown(" ")
    st.markdown(" ")
    columna_1, columna_2, columna_3 = st.columns([3, 1, 1])
    with columna_1:

        st.markdown("""<div style=' text-align: justify; font-size: 40px; font-weight: bold'>Start planning your trips smartly with our app!</div>""", unsafe_allow_html=True)

    foto_flecha = Image.open("images/flecha.png")
    # Cambiar el tamaño de la imagen
    ancho_deseado = 300
    alto_deseado = 150
    foto_flecha = foto_flecha.resize((ancho_deseado, alto_deseado))

    with columna_3:
        st.image(foto_flecha)

# ------------------------------------------------- MAPA --------------------------------------------------------------------

    st.session_state.indices_puntos_mapa = None
    st.session_state.seleccion_cargador = None
    with st.form("mapa"):
        indice_cargador = 6666666
        # [0.8,1.2]
        columna_1, columna_2 = st.columns(2)
        
        with columna_1:
            st.markdown("")
            st.markdown("")
            #st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 20px; font-weight: bold;'>?</span>", unsafe_allow_html=True)
            radio_input = st.text_input(key = "i_1",label="In a radius of how many km?")
            st.markdown("")
            st.markdown("")
            #st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 20px; font-weight: bold;'></span>", unsafe_allow_html=True)
            cp_input = st.text_input(key = "i_2", label="Enter your zip code")
            st.markdown("")
        
            
        # Every form must have a submit button.
            c_1, c_2 = st.columns(2)
            with c_1:
                st.markdown("")
                submit_1 = st.form_submit_button("Chargers",use_container_width=True)
            with c_2:
                st.markdown("")
                submit_2 = st.form_submit_button("Gas stations", use_container_width=True)
        
        if submit_2:
            if radio_input.strip() == "" or cp_input.strip() == "":
                    #with columna_2:
                    st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Missing data!</span>", unsafe_allow_html=True)
                    # mapa_html = funcion_folium_cp_radio()                                
                    #         # Mostrar el mapa en Streamlit
                    # with columna_2:
                    #     st.components.v1.html(mapa_html, height = 310)

            try:
                if int(radio_input) or int(cp_input):
                    if int(radio_input) < 10:
                        #with columna_2:
                        st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Enter a radius greater than 10 km.</span>", unsafe_allow_html=True)
                        mapa_html = funcion_folium_cp_radio()                                
                                # Mostrar el mapa en Streamlit
                        with columna_2:
                            st.components.v1.html(mapa_html, height = 310)
                    elif len(str(cp_input.strip())) != 5:
                        #with columna_2:
                        st.markdown("<span style='hite-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Enter a valid postal code</span>", unsafe_allow_html=True)
                        mapa_html = funcion_folium_cp_radio()                                
                                # Mostrar el mapa en Streamlit
                        with columna_2:
                            st.components.v1.html(mapa_html, height = 310)
                    else:
                        
                        #indices_puntos_mapa = None 
                        radio = int(radio_input)
                        cp = str(cp_input)

                        try:
                            
                            mapa_html = funcion_folium_cp_radio_gasolineras(cp, radio)                                
                                # Mostrar el mapa en Streamlit
                            with columna_2:
                                st.components.v1.html(mapa_html, height = 310)
                            
                        except:
                            st.write("Try again")

            except:
                st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>The kilometers must be whole numbers.</span>", unsafe_allow_html=True)
                mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                with columna_2:
                    st.components.v1.html(mapa_html, height = 310)

        elif submit_1:

            if radio_input.strip() == "" or cp_input.strip() == "":
                    #with columna_2:
                    st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Missing data!</span>", unsafe_allow_html=True)
                    # mapa_html = funcion_folium_cp_radio()                                
                    #         # Mostrar el mapa en Streamlit
                    # with columna_2:
                    #     st.components.v1.html(mapa_html, height = 310)

            try:
                if int(radio_input) or int(cp_input):        
                    if int(radio_input) < 10:
                        #with columna_2:
                        st.markdown("<span style='white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Enter a radius greater than 10 km.</span>", unsafe_allow_html=True)
                        mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                        with columna_2:
                            st.components.v1.html(mapa_html, height = 310)
                    elif len(str(cp_input.strip())) != 5:
                        #with columna_2:
                        st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Introduce a valid postal code</span>", unsafe_allow_html=True)
                        mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                        with columna_2:
                            st.components.v1.html(mapa_html, height = 310)
                    else:
                        
                        #indices_puntos_mapa = None 
                            radio = int(radio_input)
                            cp = str(cp_input)

                            try:
                                
                                mapa_html, st.session_state.indices_puntos_mapa = funcion_folium_cp_radio(cp, radio)                                
                                    # Mostrar el mapa en Streamlit
                                with columna_2:
                                    st.components.v1.html(mapa_html, height = 310)
                                
                            except:
                                st.write("Try again")

            except:
                st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>The kilometers must be whole numbers.</span>", unsafe_allow_html=True)
                mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                with columna_2:
                    st.components.v1.html(mapa_html, height = 310)
        
        else:
            mapa_html = funcion_folium_cp_radio() 
            with columna_2:
                st.components.v1.html(mapa_html, height = 310)
        st.markdown("")
        st.write("<span style='display:block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'> Calculate the cost of your trip!</span>", unsafe_allow_html=True)

        texto = """<div style=' text-align: justify; font-size: 18px;'>
                    With the cars you have selected and depending on the distance you plan to travel,
                    Our algorithm will calculate the total cost of your trip. We have integrated models of
                    time series to give you an estimate of the cost of gasoline or diesel
                    in the next week that you can find in the "EcoHistoric" section,
                    thus helping you make informed decisions about your fuel expenses on your trips.
                    And in the case of electric ones you will have to select a charging point on the map. Don't you
                    you lose it !</div>"""
    
        st.markdown(texto, unsafe_allow_html=True)
    

        st.markdown("")
        st.markdown("")



# ----------------------------------------------------- CALCULADOR VIAJES ---------------------------------------------------------
        if st.session_state.indices_puntos_mapa:

            columna_1, columna_2 = st.columns(2)
            with columna_1:
                input_km_usuario = st.number_input(min_value=10, label= "Enter the Kms of your trip", step = 10)
                st.session_state.seleccion_cargador = st.number_input("Enter the charging point index:", step = 1)

            with columna_2:
                input_precio_gasolina = st.number_input(label= "Current gasoline price:", step = 0.01, min_value= 0.01)
                input_precio_gasoleo = st.number_input("Current diesel price:", step=0.01, min_value= 0.01)

            # Verificar si el número elegido está dentro de la lista permitida
            if st.session_state.seleccion_cargador not in st.session_state.indices_puntos_mapa:
                st.error("The chosen index does not appear on the map!")
            else:
                indice_cargador = st.session_state.seleccion_cargador

                #st.form_submit_button("Calcular coste del recorrido")

                df_coches = pd.read_csv("./Data/df_coches_escrapeo_ingles.csv")

                df_coches = df_coches[~(df_coches["Engine Type"]=="Diesel Hybrid")]
                
                if input_km_usuario != None and input_km_usuario > 0 and input_precio_gasoleo > 0.00 or input_precio_gasolina > 0.00:
                
                    resultado_electrico, diccionario = predicePrecio(modelo_electrico_puro, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)
                    precios_viajes, precio_parte_electrico, diccionario, resultado_gasolina, predic= predicePrecio(modelo_hibrido, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)
                    viaje_gasolina, prediccion_gasolina = predicePrecio(modelo_gasolina, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)
                    viaje_gasoleo, prediccion_gasoleo = predicePrecio(modelo_gasoleo, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)
                    
                    if resultado_electrico != []:

                        if len(resultado_electrico) == 3:
                            data_hibrido = {"Vehicle": [modelo_hibrido, modelo_hibrido, modelo_hibrido],
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_hibrido]["Engine Type"].values, df_coches[df_coches["Model"] == modelo_hibrido]["Engine Type"].values, df_coches[df_coches["Model"] == modelo_hibrido]["Engine Type"].values],
                                            "Distance km": [input_km_usuario, input_km_usuario, input_km_usuario], 
                                            "Total tour price €" : [precios_viajes[0], precios_viajes[1], precios_viajes[2]],
                                            "Electrical part €": [precio_parte_electrico[0], precio_parte_electrico[1], precio_parte_electrico[2]],
                                            "kW/h price": [diccionario[0], diccionario[1], diccionario[2]],
                                            "Gasoline part €": [resultado_gasolina, resultado_gasolina, resultado_gasolina], 
                                            "Gasoline prediction next week €": [predic, predic, predic]}

                            df_hibrido = pd.DataFrame(data_hibrido)


                            data_electrico = {"Vehicle": [modelo_electrico_puro, modelo_electrico_puro, modelo_electrico_puro], 
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_electrico_puro]["Engine Type"].values, df_coches[df_coches["Model"] == modelo_electrico_puro]["Engine Type"].values, df_coches[df_coches["Model"] == modelo_electrico_puro]["Engine Type"].values],
                                            "Distance km": [input_km_usuario, input_km_usuario, input_km_usuario], 
                                            "Total tour price €" : [resultado_electrico[0], resultado_electrico[1], resultado_electrico[2]],
                                            "kW/h price": [diccionario[0], diccionario[1], diccionario[2]]}

                            df_electrico = pd.DataFrame(data_electrico)


                            data_gasolina = {"Vehicle": [modelo_gasolina],
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_gasolina]["Engine Type"].values], 
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [viaje_gasolina],
                                            "Gasoline prediction next week €": [prediccion_gasolina]}

                            df_gasolina = pd.DataFrame(data_gasolina)


                            data_gasoleo = {"Vehicle": [modelo_gasoleo],
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_gasoleo]["Engine Type"].values], 
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [viaje_gasoleo],
                                            "Diesel prediction next week €": [prediccion_gasoleo]}

                            df_gasoleo = pd.DataFrame(data_gasoleo)



                        if len(resultado_electrico) == 2:
                            data_hibrido = {"Vehicle": [modelo_hibrido, modelo_hibrido],
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_hibrido]["Engine Type"].values, df_coches[df_coches["Model"] == modelo_hibrido]["Engine Type"].values], 
                                            "Distance km": [input_km_usuario, input_km_usuario], 
                                            "Total tour price €" : [precios_viajes[0], precios_viajes[1]],
                                            "Electrical part €": [precio_parte_electrico[0], precio_parte_electrico[1]],
                                            "kW/h price": [diccionario[0], diccionario[1]],
                                            "Gasoline part €": [resultado_gasolina, resultado_gasolina], 
                                            "Gasoline prediction next week €": [predic, predic]}

                            df_hibrido = pd.DataFrame(data_hibrido)


                            data_electrico = {"Vehicle": [modelo_electrico_puro, modelo_electrico_puro], 
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_electrico_puro]["Engine Type"].values, df_coches[df_coches["Model"] == modelo_electrico_puro]["Engine Type"].values],
                                            "Distance km": [input_km_usuario, input_km_usuario], 
                                            "Total tour price €" : [resultado_electrico[0], resultado_electrico[1]],
                                            "kW/h price": [diccionario[0], diccionario[1]]}

                            df_electrico = pd.DataFrame(data_electrico)


                            data_gasolina = {"Vehicle": [modelo_gasolina],
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_gasolina]["Engine Type"].values], 
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [viaje_gasolina],
                                            "Gasoline prediction next week €": [prediccion_gasolina]}

                            df_gasolina = pd.DataFrame(data_gasolina)


                            data_gasoleo = {"Vehicle": [modelo_gasoleo], 
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_gasoleo]["Engine Type"].values],
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [viaje_gasoleo],
                                            "Diesel prediction next week €": [prediccion_gasoleo]}

                            df_gasoleo = pd.DataFrame(data_gasoleo)



                        if len(resultado_electrico) == 1:
                            data_hibrido = {"Vehicle": [modelo_hibrido], 
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_hibrido]["Engine Type"].values],
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [precios_viajes[0]],
                                            "Electrical part €": [precio_parte_electrico[0]],
                                            "kW/h price": [diccionario[0]],
                                            "Gasoline part €": [resultado_gasolina], 
                                            "Gasoline prediction next week €": [predic]}

                            df_hibrido = pd.DataFrame(data_hibrido)


                            data_electrico = {"Vehicle": [modelo_electrico_puro],
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_electrico_puro]["Engine Type"].values], 
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [resultado_electrico[0]],
                                            "kW/h price": [diccionario[0]]}

                            df_electrico = pd.DataFrame(data_electrico)


                            data_gasolina = {"Vehicle": [modelo_gasolina],
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_gasolina]["Engine Type"].values], 
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [viaje_gasolina],
                                            "Gasoline prediction next week €": [prediccion_gasolina]}

                            df_gasolina = pd.DataFrame(data_gasolina)


                            data_gasoleo = {"Vehicle": [modelo_gasoleo], 
                                            "Engine Type": [df_coches[df_coches["Model"] == modelo_gasoleo]["Engine Type"].values],
                                            "Distance km": [input_km_usuario], 
                                            "Total tour price €" : [viaje_gasoleo],
                                            "Diesel prediction next week €": [prediccion_gasoleo]}

                            df_gasoleo = pd.DataFrame(data_gasoleo)


                        texto = """<div style=' text-align: justify; font-size: 18px;'>
                                    Analyze the results and compare! Below we show you the results of calculating the price of your trip
                                    Depending on the characteristics of the vehicles you chose, the price per kW/h and the price of fuel.</div>"""

                        st.markdown(texto, unsafe_allow_html=True)
                        columna_1, columna_2 = st.columns(2)
                        altura = 100
                        with columna_1:
                            st.markdown("")
                            st.dataframe(df_electrico, use_container_width=True, height=altura, hide_index=True)
                            st.markdown("")
                            st.dataframe(df_hibrido, use_container_width=True, height=altura, hide_index = True)
                        with columna_2:
                            st.markdown("")
                            st.dataframe(df_gasolina, use_container_width=True, height=altura, hide_index=True)
                            st.markdown("")
                            st.dataframe(df_gasoleo, use_container_width=True, height=altura, hide_index=True)
                        
                    else:
                            st.write("Select a charging point where the price per kW/h is not unknown or free.") 
                else:
                    st.error("Enter a combustible price, minimun one")
                
            
            
            
            
        else:
            columna_1, columna_2 = st.columns(2)

            with columna_1:
                input_km_usuario = st.number_input(min_value=10, label= "Enter the Kms of your trip", step = 10)
                st.session_state.seleccion_cargador = st.selectbox("Enter the charging point index:", options=["You must use the map first"])

            with columna_2:
                input_precio_gasolina = st.number_input(label= "Current gasoline price:", step = 0.01, min_value= 0.01)
                input_precio_gasoleo = st.number_input("Current diesel price:", step=0.01, min_value= 0.01)

