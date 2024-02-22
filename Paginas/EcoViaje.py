# --------------------------------------------------- FUNCION PÁGINA ECOVIAJE ------------------------------------------------------
import pandas as pd
import streamlit as st

from PIL import Image

from funciones.funciones_ecoviaje import *

def pagina_ecoviaje():
    # --------------------------------------------------- SUB MAPA -----------------------------------------------------------------
    
    st.write("<span style='display:block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>Comparador de vehículos</span>", unsafe_allow_html=True)
    
    texto = """<div style=' text-align: justify; font-size: 18px;'>
                ¿Cuantas veces te has preguntado si comprando un coche eléctrico o híbrido ahorrarías más que con uno de combustión?
                Con nuestro comparador podrás escoger entre una amplia variedad de vehículos con todas las carácteristicas
                que tú necesitas y ver las diferencias entre ellos. Además todo lo que necesitas para organizar tus desplazamientos 
                de manera eficiente y económica lo encontrarás en esta aplicación.
                </div>"""
    
    # Mostrar el texto alineado al centro
    
    st.markdown(texto, unsafe_allow_html=True)

    st.markdown("<span style='white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>- - - - - - - - - -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - - - - - - - - - - - - - - - - - - - - - - - - -</span>", unsafe_allow_html=True)
    
    columna_1, columna_2, columna_3= st.columns([1, 0.1, 1])

# ---------------------------------------------- ELÉCTRICOS --------------------------------------------------------------------------
    modelo_electrico_puro = funcion_seleccion_modelos_electricos(columna_1, "Eléctricos","Eléctricos puros", ["e_1", "e_2", "e_3", "e_4", "e_5", "e_6", "e_7", "e_8", "e_9"])

# ------------------------------------------------- HÍBRIDOS ---------------------------------------------------------------------------------
    modelo_hibrido = funcion_seleccion_modelos_hibridos(columna_3, "Híbridos", ["h_1", "h_2", "h_3", "h_4", "h_5", "h_6", "h_7", "h_8", "h_9"])

# ------------------------------------------------- COMPARADOR ELÉCTRICO ---------------------------------------------------------------
    #columna_1, columna_2 = st.columns(2)
    
    if modelo_hibrido and modelo_electrico_puro:
        with columna_3:
            
            # Crea el botón utilizando la clase CSS personalizada
            boton_modelos_e = st.button(use_container_width=True, label="Comparar Eléctricos vs Híbridos", key="o_1")
        if boton_modelos_e:
            st.session_state.grafico_visible = True
        if "grafico_visible" not in st.session_state:
                st.session_state.grafico_visible = False
            
        if not st.session_state.grafico_visible:
            pass
        else:
            #st.write(modelo_hibrido)
            #st.write(modelo_electrico_puro)
            funcion_comparacion_seleccion_usario_modelo(2, ["Eléctricos puros", "Híbridos"], seleccionElectrico= str(modelo_electrico_puro),seleccionGasoi=None,seleccionGasolina=None ,seleccionHibrido=str(modelo_hibrido))
        with columna_1:
            
    
            st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>¡ Compara y resuelve tus dudas !</span>", unsafe_allow_html=True)
    else:
        with columna_1:
            st.markdown("")
            st.markdown("")
            
            boton_modelos_e = st.button(key= "o_1", label="Comparar Eléctricos vs Híbridos")
        if boton_modelos_e:
            st.write("Falta que selecciones algún modelo más")

    st.markdown("<span style='white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>- - - - - - - - - -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - - - - - - - - -  - - - - - - - - - - - - - - -  </span>", unsafe_allow_html=True)

# ------------------------------------------------ GASOLINA -----------------------------------------------------------------------------------------------------
    st.markdown("")
    
    
    columnita_1, columnita_2 = st.columns(2)
    modelo_gasoleo = funcion_seleccion_modelos_gasolina(columnita_1, "Gasóleo", "Gasóleo",["g_1", "g_2", "g_3", "g_4", "g_5", "g_6", "g_7", "g_8", "g_9"])
    modelo_gasolina = funcion_seleccion_modelos_gasolina(columnita_2, "Gasolina", "Gasolina", ["l_1", "l_2", "l_3", "l_4", "l_5", "l_6", "l_7", "l_8", "l_9"])

    columna_1, columna_2, columna_3= st.columns([1.1, 0.5, 1])

    if modelo_gasolina and modelo_gasoleo:
        with columna_2:
            boton_modelos_g = st.button(key= "o_2", label="Comparar Gasolina vs Gasóleo")
        if boton_modelos_g:
            st.session_state.grafico2_visible = True
        if "grafico2_visible" not in st.session_state:
                st.session_state.grafico2_visible = False
            
        if not st.session_state.grafico2_visible:
            pass
        else:
            #st.write(modelo_hibrido)
            #st.write(modelo_electrico_puro)
            funcion_comparacion_seleccion_usario_modelo(2, ["Gasóleo", "Gasolina"], seleccionElectrico= None,seleccionGasoi=str(modelo_gasoleo),seleccionGasolina=str(modelo_gasolina) ,seleccionHibrido=None)
    else:
        with columna_2:
            boton_modelos_g = st.button(key= "o_2", label="Comparar Gasolina vs Gasóleo")
        if boton_modelos_g:
            st.write("Falta que selecciones algún modelo más")

    st.markdown("")

    columna_1, columna_2, columna_3= st.columns([1.05, 0.4, 1])
    
    if modelo_electrico_puro and modelo_hibrido and modelo_gasolina and modelo_gasoleo:
        
        with columna_2:
            boton_comparar = st.button(key = "o_3", label = "Comparar todos los coches")
        if boton_comparar:
            funcion_comparacion_seleccion_usario_modelo(4, ["Eléctricos puros","Híbridos","Gasóleo", "Gasolina"], seleccionElectrico= str(modelo_electrico_puro),seleccionGasoi=str(modelo_gasoleo),seleccionGasolina=str(modelo_gasolina) ,seleccionHibrido=str(modelo_hibrido))

    else:
        with columna_2:
            boton_comparar = st.button(key = "o_3", label = "Comparar todos los coches")
            if boton_comparar:
                st.write("Para esto debes seleccionar un modelo de cada tipo de vehículo")

    # ---------------------------------------------------- CALCULADOR DE RUTAS -------------------------------------------------------
    st.write("<span style='display:block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>Planificador de Viajes</span>", unsafe_allow_html=True)
    
    texto = """<div style=' text-align: justify; font-size: 18px;'>
                ¿Te preocupa encontrar una gasolinera en tu ruta o un cargador para tu vehículo eléctrico?
                Nuestra aplicación te permite explorar fácilmente las opciones de gasolineras y puntos de carga 
                eléctrica dentro de un radio específico a partir de tu código postal.</div>"""
  
    st.markdown(texto, unsafe_allow_html=True)

    #---------------------------------------------------------- CABECERA --------------------------------------------------------
        
    st.markdown(" ")
    st.markdown(" ")
    columna_1, columna_2, columna_3 = st.columns([3, 1, 1])
    with columna_1:

        st.markdown("""<div style=' text-align: justify; font-size: 40px; font-weight: bold'>¡Empieza a planificar tus viajes de manera inteligente con nuestra aplicación!</div>""", unsafe_allow_html=True)

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
            radio_input = st.text_input(key = "i_1",label="¿En un radio de cuántos Km")
            st.markdown("")
            st.markdown("")
            #st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 20px; font-weight: bold;'></span>", unsafe_allow_html=True)
            cp_input = st.text_input(key = "i_2", label="Introduce tu código postal")
            st.markdown("")
          
            
        # Every form must have a submit button.
            c_1, c_2 = st.columns(2)
            with c_1:
                st.markdown("")
                boton_cargadores = st.form_submit_button("Cargadores",use_container_width=True)
            with c_2:
                st.markdown("")
                boton_gasolineras = st.form_submit_button("Gasolineras", use_container_width=True)
        
        if boton_gasolineras:
            if radio_input.strip() == "" or cp_input.strip() == "":
                    #with columna_2:
                    st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>¡Faltan datos!</span>", unsafe_allow_html=True)
                    # mapa_html = funcion_folium_cp_radio()                                
                    #         # Mostrar el mapa en Streamlit
                    # with columna_2:
                    #     st.components.v1.html(mapa_html, height = 310)

            try:
                if int(radio_input) or int(cp_input):
                    if int(radio_input) < 10:
                    #with columna_2:
                        st.markdown("<span style='white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Introduce un radio mayor de 10 Km.</span>", unsafe_allow_html=True)
                        mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                        with columna_2:
                            st.components.v1.html(mapa_html, height = 310)

                    elif len(str(cp_input.strip())) != 5:
                        #with columna_2:
                        st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Introduce un código postal válido</span>", unsafe_allow_html=True)
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
                            st.write("Inténtelo de nuevo")
            except:
                st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Los kms deben de ser números enteros.</span>", unsafe_allow_html=True)
                mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                with columna_2:
                    st.components.v1.html(mapa_html, height = 310)

        

        elif boton_cargadores:

            if radio_input.strip() == "" or cp_input.strip() == "":
                    #with columna_2:
                    st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>¡Faltan datos!</span>", unsafe_allow_html=True)
                    # mapa_html = funcion_folium_cp_radio()                                
                    #         # Mostrar el mapa en Streamlit
                    # with columna_2:
                    #     st.components.v1.html(mapa_html, height = 310)

            try:
                if int(radio_input) or int(cp_input):
            
                    if int(radio_input) < 10:
                    #with columna_2:
                        st.markdown("<span style='white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Introduce un radio mayor de 10 Km.</span>", unsafe_allow_html=True)
                        mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                        with columna_2:
                            st.components.v1.html(mapa_html, height = 310)

                    elif len(str(cp_input.strip())) != 5:

                        #with columna_2:
                        st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Introduce un código postal válido</span>", unsafe_allow_html=True)
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

                            st.write("Inténtelo de nuevo")
            except:
                st.markdown("<span style=' white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Los kms y códigos postales deben de ser números enteros.</span>", unsafe_allow_html=True)
                mapa_html = funcion_folium_cp_radio()                                
                                    # Mostrar el mapa en Streamlit
                with columna_2:
                    st.components.v1.html(mapa_html, height = 310)
                
                
            
        else:
            mapa_html = funcion_folium_cp_radio() 
            with columna_2:
                st.components.v1.html(mapa_html, height = 310)
        st.markdown("")
        st.write("<span style='display:block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>¡ Calcula el coste de tu viaje !</span>", unsafe_allow_html=True)

        texto = """<div style=' text-align: justify; font-size: 18px;'>
                    Con los coches que has seleccionado y en función de la distancia que planeas recorrer, 
                    nuestro algortimo calculará el costo total de tu viaje. Hemos integrado modelos de 
                    series temporales para ofrecerte una estimación del costo de la gasolina o el diésel 
                    en la semana próxima que puedes encontrar en el apartado "EcoHistórico", 
                    ayudándote así a tomar decisiones informadas sobre tus gastos de combustible en tus viajes.
                    Y en el caso de los eléctricos tendrás que seleccionar un punto de carga en el mapa. ¡ No te
                    lo pierdas !</div>"""
    
        st.markdown(texto, unsafe_allow_html=True)
    

        st.markdown("")
        st.markdown("")



# ----------------------------------------------------- CALCULADOR VIAJES ---------------------------------------------------------
        if st.session_state.indices_puntos_mapa:

            columna_1, columna_2 = st.columns(2)
            with columna_1:
                input_km_usuario = st.number_input(min_value=10, label= "Introduzca los Kms de su recorrido", step = 10)
                st.session_state.seleccion_cargador = st.number_input("Introduzca el índice del punto de carga:", step = 1)

            with columna_2:
                input_precio_gasolina = st.number_input(label= "Precio actual de la gasolina:", step = 0.01, min_value=0.01)
                input_precio_gasoleo = st.number_input("Precio actual del gasóleo:", step=0.01, min_value=0.01)

            # Verificar si el número elegido está dentro de la lista permitida
            if st.session_state.seleccion_cargador not in st.session_state.indices_puntos_mapa:
                st.error("¡El índice elegido no aparece en el mapa!")
            else:
                indice_cargador = st.session_state.seleccion_cargador

                #st.form_submit_button("Calcular coste del recorrido")

                df_coches = pd.read_csv("./Data/df_coches_escrapeo.csv")

                df_coches = df_coches[~(df_coches["Motorización"]=="Híbridos de gasóleo")]
                
                if input_km_usuario != None and input_km_usuario > 0 and input_precio_gasoleo > 0.00 or input_precio_gasolina > 0.00:
                    resultado_electrico, diccionario = predicePrecio(modelo_electrico_puro, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)
                    precios_viajes, precio_parte_electrico, diccionario, resultado_gasolina, predic= predicePrecio(modelo_hibrido, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)
                    viaje_gasolina, prediccion_gasolina = predicePrecio(modelo_gasolina, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)
                    viaje_gasoleo, prediccion_gasoleo = predicePrecio(modelo_gasoleo, input_km_usuario, indice_cargador, input_usuario_gasolina = input_precio_gasolina, input_usuario_gasoleo = input_precio_gasoleo)

                    if resultado_electrico != []:
                        if len(resultado_electrico) == 3:
                            data_hibrido = {"Vehículo": [modelo_hibrido, modelo_hibrido, modelo_hibrido],
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_hibrido]["Motorización"].values, df_coches[df_coches["Modelo"] == modelo_hibrido]["Motorización"].values, df_coches[df_coches["Modelo"] == modelo_hibrido]["Motorización"].values],
                                            "Recorrido km": [input_km_usuario, input_km_usuario, input_km_usuario], 
                                            "Precio total recorrido €" : [precios_viajes[0], precios_viajes[1], precios_viajes[2]],
                                            "Parte eléctrica €": [precio_parte_electrico[0], precio_parte_electrico[1], precio_parte_electrico[2]],
                                            "Precio kW/h": [diccionario[0], diccionario[1], diccionario[2]],
                                            "Parte gasolina €": [resultado_gasolina, resultado_gasolina, resultado_gasolina], 
                                            "Predicción gasolina semana siguiente €": [predic, predic, predic]}
                            
                            df_hibrido = pd.DataFrame(data_hibrido)
                            

                            data_electrico = {"Vehículo": [modelo_electrico_puro, modelo_electrico_puro, modelo_electrico_puro], 
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_electrico_puro]["Motorización"].values, df_coches[df_coches["Modelo"] == modelo_electrico_puro]["Motorización"].values, df_coches[df_coches["Modelo"] == modelo_electrico_puro]["Motorización"].values],
                                            "Recorrido km": [input_km_usuario, input_km_usuario, input_km_usuario], 
                                            "Precio total recorrido €" : [resultado_electrico[0], resultado_electrico[1], resultado_electrico[2]],
                                            "Precio kW/h": [diccionario[0], diccionario[1], diccionario[2]]}
                            
                            df_electrico = pd.DataFrame(data_electrico)
                            

                            data_gasolina = {"Vehículo": [modelo_gasolina],
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_gasolina]["Motorización"].values], 
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [viaje_gasolina],
                                            "Predicción gasolina semana siguiente €": [prediccion_gasolina]}
                            
                            df_gasolina = pd.DataFrame(data_gasolina)
                            

                            data_gasoleo = {"Vehículo": [modelo_gasoleo],
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_gasoleo]["Motorización"].values], 
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [viaje_gasoleo],
                                            "Predicción gasóleo semana siguiente €": [prediccion_gasoleo]}
                            
                            df_gasoleo = pd.DataFrame(data_gasoleo)
                        
                            

                        if len(resultado_electrico) == 2:
                            data_hibrido = {"Vehículo": [modelo_hibrido, modelo_hibrido],
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_hibrido]["Motorización"].values, df_coches[df_coches["Modelo"] == modelo_hibrido]["Motorización"].values], 
                                            "Recorrido km": [input_km_usuario, input_km_usuario], 
                                            "Precio total recorrido €" : [precios_viajes[0], precios_viajes[1]],
                                            "Parte eléctrica €": [precio_parte_electrico[0], precio_parte_electrico[1]],
                                            "Precio kW/h": [diccionario[0], diccionario[1]],
                                            "Parte gasolina €": [resultado_gasolina, resultado_gasolina], 
                                            "Predicción gasolina semana siguiente €": [predic, predic]}
                            
                            df_hibrido = pd.DataFrame(data_hibrido)
                        

                            data_electrico = {"Vehículo": [modelo_electrico_puro, modelo_electrico_puro], 
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_electrico_puro]["Motorización"].values, df_coches[df_coches["Modelo"] == modelo_electrico_puro]["Motorización"].values],
                                            "Recorrido km": [input_km_usuario, input_km_usuario], 
                                            "Precio total recorrido €" : [resultado_electrico[0], resultado_electrico[1]],
                                            "Precio kW/h": [diccionario[0], diccionario[1]]}
                            
                            df_electrico = pd.DataFrame(data_electrico)
                        

                            data_gasolina = {"Vehículo": [modelo_gasolina],
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_gasolina]["Motorización"].values], 
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [viaje_gasolina],
                                            "Predicción gasolina semana siguiente  €": [prediccion_gasolina]}
                            
                            df_gasolina = pd.DataFrame(data_gasolina)
                        

                            data_gasoleo = {"Vehículo": [modelo_gasoleo], 
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_gasoleo]["Motorización"].values],
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [viaje_gasoleo],
                                            "Predicción gasóleo semana siguiente  €": [prediccion_gasoleo]}
                            
                            df_gasoleo = pd.DataFrame(data_gasoleo)
                        


                        if len(resultado_electrico) == 1:
                            data_hibrido = {"Vehículo": [modelo_hibrido], 
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_hibrido]["Motorización"].values],
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [precios_viajes[0]],
                                            "Parte eléctrica €": [precio_parte_electrico[0]],
                                            "Precio kW/h": [diccionario[0]],
                                            "Parte gasolina €": [resultado_gasolina], 
                                            "Predicción gasolina semana siguiente  €": [predic]}
                            
                            df_hibrido = pd.DataFrame(data_hibrido)
                        

                            data_electrico = {"Vehículo": [modelo_electrico_puro],
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_electrico_puro]["Motorización"].values], 
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [resultado_electrico[0]],
                                            "Precio kW/h": [diccionario[0]]}
                            
                            df_electrico = pd.DataFrame(data_electrico)
                

                            data_gasolina = {"Vehículo": [modelo_gasolina],
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_gasolina]["Motorización"].values], 
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [viaje_gasolina],
                                            "Predicción gasolina semana siguiente €": [prediccion_gasolina]}
                            
                            df_gasolina = pd.DataFrame(data_gasolina)
            

                            data_gasoleo = {"Vehículo": [modelo_gasoleo], 
                                            "Motorización": [df_coches[df_coches["Modelo"] == modelo_gasoleo]["Motorización"].values],
                                            "Recorrido km": [input_km_usuario], 
                                            "Precio total recorrido €" : [viaje_gasoleo],
                                            "Predicción gasóleo semana siguiente €": [prediccion_gasoleo]}
                            
                            df_gasoleo = pd.DataFrame(data_gasoleo)
                        
                        texto = """<div style=' text-align: justify; font-size: 18px;'>
                                    ¡ Analiza los resultados y compara ! A continuación te mostramos los resultados del cálculo del precio de tu viaje 
                                    según las carcaterísticas de los vehículos que escogistes, el precio el kW/h y el del combustible. </div>"""
    
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
                        st.write("Seleccione un punto de carga donde el precio del kW/h no sea desconocido o gratuito")
                else:
                    st.error("Ingrese al menos el precio de algún combustible de la semana actual") 

        else:
            columna_1, columna_2 = st.columns(2)

            with columna_1:
                input_km_usuario = st.number_input(min_value=10, label= "Introduzca los Kms de su recorrido", step = 10)
                st.session_state.seleccion_cargador = st.selectbox("Introduzca el índice del punto de carga:", options=["Debe usar primero el mapa de cargadores"])

            with columna_2:
                input_precio_gasolina = st.number_input(label= "Precio actual de la gasolina:", step = 0.01, min_value=0.01)
                input_precio_gasoleo = st.number_input("Precio actual del gasóleo:", step=0.01, min_value=0.01)

    