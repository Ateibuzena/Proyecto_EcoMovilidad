import streamlit as st
from funciones import funciones_ecoestudio_ecohistorico


def EcoEstudio():
    

    motorizacion_vehiculo = ['Todos','Gasolina','Gasóleo', 'Eléctricos puros', 'Híbridos enchufables',
    'Híbridos de gasolina']

    lista_opciones = ['Categorías de Vehiculos','Clasificación Energetica','Autonomia y Capacidad de batería','Vehículos y Consumos']
    st.sidebar.markdown("<h2>Seleccione la informacion que desea obtener:</h2>", unsafe_allow_html=True)
    input_usuario = st.sidebar.radio("", lista_opciones)
    #-----------------------------------------------------------


    if input_usuario == "Categorías de Vehiculos" :
        #
        #Ecoestudio1-Clase de Vehiculos
        #

        #Informacion basica sobre el tipo de vehiculo-------------
        

        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Categorías de Vehículos</span>", unsafe_allow_html=True)
       
        st.write("<div style='text-align: justify; font-size: 18px;'> Se le va a informas sobre los diferentes tipos de vehiculos  segun su clase.La clasificacion se refiere a una forma de categorizarlos según ciertas características como su tamaño, peso, capacidad, entre otros.</div>", unsafe_allow_html=True)
        st.markdown(" ")
        # st.markdown("<span style='color:cyan; white-space: nowrap; text-align: center; font-size: 30px; font-weight: bold;'>Categorías de vehículos eléctricos y no eléctricos</span>", unsafe_allow_html=True)
        
        
        col1,col2 = st.columns(2)
        with col1:
        
            st.markdown(" ") 
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Categorías L :</span>", unsafe_allow_html=True)
            st.write("<div style='text-align: justify; font-size: 18px;'>Estas categorías (L3e, L5e, L6e, L7e) están relacionadas con vehículos ligeros, especialmente vehículos de motor de dos, tres o cuatro ruedas. Pueden ser motocicletas y cuadriciclos ligeros, y la letra 'L' probablemente indica 'ligero'.</div>",unsafe_allow_html= True)
            st.markdown(" ") 
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Categorías M :</span>", unsafe_allow_html=True)
            st.write("<div style='text-align: justify; font-size: 18px;'> Estas categorías (M1, M2, M3) están asociadas con vehículos más pesados, como automóviles y otros vehículos de motor. 'M1' generalmente se refiere a vehículos destinados al transporte de personas y sus equipajes.</div>",unsafe_allow_html= True)
            st.markdown(" ")
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Categorías N :</span>", unsafe_allow_html=True)
            st.write("<div style='text-align: justify; font-size: 18px;'> Estas categorías (N1, N2, N3) podrían estar relacionadas con vehículos industriales y comerciales, como camiones. 'N1' generalmente se refiere a vehículos destinados al transporte de mercancías y sus remolques.</div>",unsafe_allow_html= True)
        
        with col2:
            
        
          
            
            
            col3,col4,col5 = st.columns([0.5,1,0.5])
            for i in range (1,1):
                st.markdown(" ") 
            with col4:

                input_usuario_vehiculos = st.selectbox("Seleccione la motorización:", motorizacion_vehiculo)
            funciones_ecoestudio_ecohistorico.funcion_categorias_e_c(input_usuario_vehiculos)
         
                
                    
        st.markdown("")
        st.markdown("")
        st.write("<div style='text-align: justify; font-size: 18px;'> En el análisis, se destaca que los vehículos eléctricos abarcan una gama más amplia de categorías en comparación con los no eléctricos, que se limitan principalmente a las categorías M1 y N1. Las categorías más representativas para los eléctricos, son los turismos, vehículos de transporte de mercancía y las motos. Podemos llegar a comprender la importancia de estos en el mercado, ya que las diferentes categorías tienen una amplia gama de aplicaciones más allá del uso individual y su adopción en diversos contextos puede contribuir a la sostenibilidad ambiental, la eficiencia operativa y la innovación en la movilidad.</div>",unsafe_allow_html= True)
       

        
        #
        #Fin Ecoestudio1-Clase de Vehiculos
        # 

    elif input_usuario == 'Clasificación Energetica':
        #
        #Ecoestudio2-Clasificacion energetica
        #
        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Clasificación Energética</span>", unsafe_allow_html=True)
        funciones_ecoestudio_ecohistorico.funcion_calsificacion_e_c('Todos')
        col1,col2 = st.columns(2)
        with col1:
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Las etiquetas de Clasificación Energética hacen referencia a la emisión de CO2 de un vehículo con respecto a la media</span>", unsafe_allow_html=True)

        with col2:
            col1,col2 = st.columns([0.5,1])
            with col2:
                texto = """
                            <div style='text-align: justify;font-size:18px '>
                            

                            - **Etiqueta A:** -25% (o menos)
                            - **Etiqueta B:** -15% a -25%
                            - **Etiqueta C:** -5% a -15%
                            - **Etiqueta D:** -5% a +5%
                            - **Etiqueta E:** +5 a +15%
                            - **Etiqueta F:** +15% a +25%
                            - **Etiqueta G:** +25% o más
                            """

                    # Mostrar el texto alineado al centro
                st.markdown(texto, unsafe_allow_html=True) 

        st.markdown(" ")
        st.markdown(" ")
        
        #------------------------Grafica---------------------------
        # Agregar el selectbox al sidebar de Streamlit
        motorizacion_vehiculo2 = ['Gasolina','Gasóleo', 'Híbridos enchufables',
        'Híbridos de gasolina']
        input_usuario_vehiculos = st.selectbox("Seleccione la motorización de los vehiculos:", motorizacion_vehiculo2)
        funciones_ecoestudio_ecohistorico.funcion_calsificacion_e_c(input_usuario_vehiculos)
        texto = """
                    <div style='text-align: justify;font-size:18px'>
                    En la revisión de eficiencia energética, se observa que la mayoría de los vehículos eléctricos alcanzan la máxima clasificación (A). Aquellos sin clasificación específica son vehículos eléctricos puros. Por otro lado, los vehículos con la peor clasificación (G) suelen ser híbridos enchufables, seguidos por híbridos de gasolina.
                    Entre los vehículos no eléctricos, predominan aquellos con etiqueta C, seguidos por las categorías B y D. Una revisión más detallada de los vehículos con etiqueta G revela que mayoritariamente son coches de gasolina, seguidos por los de gasóleo.
                """

            # Mostrar el texto alineado al centro
        st.markdown(texto, unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        #----------------------------------------------------------
        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>¿Qué ocurre con los vehículos con etiqueta G y Sin especificar?</span>", unsafe_allow_html=True)
        
        c_1,c_2, c_3 = st.columns([1, 0.05, 1])
        with c_1:
        #Notas del autor: aqui no le voy a poner en principio el seleccionable por que es interesante ver todos no uno por uno
            funciones_ecoestudio_ecohistorico.funcion_etiqueta_g_sin_especificar()
        
        with c_3:
            import pandas as pd
            import plotly.express as px
            import numpy as np
            df_coches = pd.read_csv("data/df_coches_escrapeo.csv")
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

        texto = """
                    <div style='text-align: justify;font-size:18px'>
                    La primera gráfica muestra que los vehículos con etiqueta energética G 
                    son principalmente diésel, seguidos de gasolina, mientras que los vehículos
                    sin clasificar son mayoritariamente de gasolina, seguidos de diésel. 
                    En la segunda gráfica, se observa que los vehículos sin clasificar tienen 
                    emisiones mínimas ligeramente más bajas que los de etiqueta G, pero emisiones 
                    máximas considerablemente más altas. Las implicaciones son que los vehículos con 
                    etiqueta G y sin clasificar son más contaminantes, por lo que se recomienda evitar 
                    comprarlos si se preocupa por el medio ambiente, y se sugiere optar por vehículos 
                    eléctricos e híbridos para reducir la huella de carbono. Se recomienda consultar la 
                    etiqueta energética y la web del IDAE antes de tomar una decisión de compra.
                """

            # Mostrar el texto alineado al centro
        st.markdown(texto, unsafe_allow_html=True)
        
        #
        #Fin Ecoestudio2-Clasificacion energetica
        #
            



    elif input_usuario == 'Autonomia y Capacidad de batería':
        #
        #Ecoestudio3-Autonomia y Capacidad de batería
        #
        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Relación Autonomia y Capacidad de batería</span>", unsafe_allow_html=True)


        funciones_ecoestudio_ecohistorico.funcion_autonomia_bateria()
        
        
        st.markdown("<span style='color:cyan;font-size:30px;font-weight:bold'>Existe una correlación directa entre ambas variables</span>", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<div style='text-align: justify; font-size: 18px;'> En otras palabras, a mayor capacidad de la batería, mayor será la autonomía eléctrica.
                    Esto se debe a que las baterías con mayor capacidad pueden almacenar más energía, lo que permite que el vehículo recorra una mayor distancia antes de necesitar recargarse. La gráfica muestra que, en general, los vehículos eléctricos puros tienen la mayor autonomía eléctrica, seguidos por los híbridos enchufables y los híbridos de gasolina.
                    En el caso de los vehículos eléctricos puros, la autonomía eléctrica puede variar entre 100 y 600 kilómetros, dependiendo de la capacidad de la batería. Los híbridos enchufables suelen tener una autonomía eléctrica entre 20 y 80 kilómetros, mientras que los híbridos de gasolina solo tienen una autonomía eléctrica de unos pocos kilómetros.
                    Por supuesto, la autonomía eléctrica también depende de otros factores, como el estilo de conducción, las condiciones climáticas y el estado de la batería. Sin embargo, la capacidad de la batería es uno de los factores más importantes que determinan la autonomía eléctrica de un vehículo.</div>""",unsafe_allow_html= True)
       
        st.markdown(" ")
        st.markdown(" ")
        col1,col2 = st.columns(2)
        with col1:
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown("<span style='display: block;font-size:50px;text-align :center;font-weight:bold'>¿Qué autonomía eléctrica tienen los vehículos electricos?</span>", unsafe_allow_html=True)
        with col2:
            funciones_ecoestudio_ecohistorico.funcion_violin_autonomia_conjunta_e()

        texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                    En la grafica se aprecia que la autonomia de los vehiculos esta condensada entre 66 y 313 km.
                    Según los datos, los vehículos eléctricos más populares son aquellos que tienen una autonomía inferior a 100 km. El 
                    mercado se divide en diferentes categorías según las distintas autonomías.
                    Los vehiculos a partir de 285 km de autonomia pasan a ser vehiculos de un mayor coste y en relacion
                    a partir de 500 km de autonomia hablamos de vehiculos de lujo o exóticos como por ejemplo los Testla.
                """

            # Mostrar el texto alineado al centro
        
        st.markdown(texto, unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("<span style='color:cyan;font-size:30px;font-weight:bold'>¿ Qué categorías hay dentro de los vehículos más comunes ?</span>", unsafe_allow_html=True)
      
        funciones_ecoestudio_ecohistorico.funcion_autonomia_por_categoria_e()
        col1,col2,col3 = st.columns([1,0.25,1])
        with col1:
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                        Dentro de los vehículos populares se observa que la categoría predominante es la M1
                        que corresponde a vehiculos destinados al transporte de pasajeros con un máximo de 8 asientos además del asiento del conductor.
                        Para más información visita el apartado "Categorías de Vehículos"

                       
                    """
            st.markdown(texto, unsafe_allow_html=True)
        with col3:
            texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                  
                    | Categoría | Min  | Media | Max  |
                    |-----------|------|-------|------|
                    | L3e       | 100.0| 100.0 | 100.0|
                    | L5e       | 97.0 | 97.0  | 97.0 |
                    | L6e       | 48.0 | 79.43 | 100.0|
                    | L7e       | 45.0 | 75.88 | 100.0|
                    | M1        | 42.0 | 60.12 | 100.0|
                    | N1        | 54.0 | 79.64 | 100.0|
                  
                """
            st.markdown(texto, unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")

        st.markdown("<span  style='color:cyan;font-size:30px;font-weight:bold'>¿ Qué relación entre Potencia Eléctrica y Autonomía ?</span>", unsafe_allow_html=True)
        col1,col2 = st.columns([1.2,2])
        with col1:
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")

            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                        Los vehículos eléctricos puros tienen la mayor autonomía, seguidos por los híbridos enchufables 
                        con autonomía extendida. Los híbridos de gasolina tienen una autonomía eléctrica menor. 
                        Factores como el estilo de conducción, las condiciones climáticas y la carga afectan la autonomía. Es crucial consultar 
                        la información del fabricante para conocer la autonomía específica. Además, en climas cálidos el aire acondicionado puede 
                        reducir la autonomía. Es recomendable planificar los viajes con antelación para asegurar estaciones de carga disponibles en ruta.
                    """
            st.markdown(texto, unsafe_allow_html=True)
            st.markdown(" ")            
            motorizacion_vehiculo = ['Todos','Eléctricos puros','Híbridos enchufables',
            'Híbridos de gasolina']
            input_usuario_vehiculos = st.selectbox("Seleccione la motorización de los vehiculos:", motorizacion_vehiculo)
        with col2:
            
            
           

            funciones_ecoestudio_ecohistorico.funcion_scater_potencia_autonomia_e(input_usuario_vehiculos)
            
       


        st.markdown("<span  style='font-size:50px;font-weight:bold'>¿Cómo varía la Potencia Eléctrica ?</span>", unsafe_allow_html=True)
       
       
        col7,col8 = st.columns(2)
        with col7:
            st.markdown("<span  style='color:cyan;font-size:30px;font-weight:bold'>Eléctricos Puros</span>", unsafe_allow_html=True)
            texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                  El histograma muestra que la mayoría de los coches eléctricos puros en España tienen una potencia eléctrica 
                  de entre 100 y 300 kW. Esto significa que la mayoría de los coches eléctricos puros tienen una potencia similar 
                  a la de un coche de gasolina o diésel de tamaño medio.  
                 
                """
            st.markdown(texto, unsafe_allow_html=True)




            funciones_ecoestudio_ecohistorico.funcion_potencia_caja_e(['Eléctricos puros'])
        with col8:
            funciones_ecoestudio_ecohistorico.funcion_potencia_barras_e(['Eléctricos puros'])
       
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                    Hay una pequeña 
                    proporción de coches eléctricos puros con una potencia eléctrica superior a 300 kW. Estos coches suelen ser 
                    deportivos o de lujo, y tienen una potencia suficiente para acelerar rápidamente y alcanzar velocidades altas.
                    
                    """
            st.markdown(texto, unsafe_allow_html=True)


        texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                  La mayoría de los coches eléctricos puros en España tienen una potencia eléctrica suficiente para satisfacer las
                  necesidades de la mayoría de los conductores. 
                  Hay una pequeña proporción de coches eléctricos puros con una potencia eléctrica superior a la media, que están 
                  diseñados para conductores que buscan un rendimiento superior. 
                  """
        st.markdown(texto, unsafe_allow_html=True)
      
        st.markdown(" ")
        col1,col2 = st.columns([0.7,1])
        with col2:
            st.markdown("<span  style='color:cyan;font-size:30px;font-weight:bold'>Híbridos</span>", unsafe_allow_html=True)
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                    El histograma muestra que la mayoría de los coches híbridos enchufables en España tienen una potencia eléctrica 
                    de entre 100 y 200 kW. Esto significa que la mayoría de los coches híbridos enchufables tienen una potencia similar 
                    a la de un coche de gasolina o diésel de tamaño compacto.  El histograma también muestra que hay una pequeña 
                    proporción de coches híbridos enchufables con una potencia eléctrica superior a 200 kW. Estos coches suelen ser 
                    de gama alta, y tienen una potencia suficiente para acelerar rápidamente y alcanzar velocidades altas. 
                    """
            st.markdown(texto, unsafe_allow_html=True)
            lista_posibles_motorizaciones = ['Híbridos enchufables', 'Híbridos de gasolina']
            input_usuario_vehiculos = st.multiselect("Seleccione la motorización de los vehiculos:", lista_posibles_motorizaciones,default=lista_posibles_motorizaciones)
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            funciones_ecoestudio_ecohistorico.funcion_potencia_barras_e(input_usuario_vehiculos)
        with col1:
        
            funciones_ecoestudio_ecohistorico.funcion_potencia_caja_e(input_usuario_vehiculos)
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                    En comparación con el histograma de los coches eléctricos puros, se puede observar que la mayoría de los 
                    coches híbridos enchufables tienen una potencia eléctrica inferior. Esto se debe a que los coches 
                    híbridos enchufables también tienen un motor de gasolina o diésel, que proporciona potencia adicional cuando 
                    es necesario.  También se puede observar que la distribución de la potencia eléctrica de los coches híbridos 
                    enchufables es más uniforme que la de los coches eléctricos puros. Esto se debe a que los fabricantes de coches 
                    híbridos enchufables ofrecen una gama más amplia de potencias eléctricas para satisfacer las necesidades de 
                    diferentes tipos de conductores.
                    """
            st.markdown(texto, unsafe_allow_html=True)
        


            
        #------------------------------------'Vehículos y Consumos'------------------------------------

    elif input_usuario == 'Vehículos y Consumos':
        
        st.write("<span style='text-align: center; font-size: 50px; font-weight: bold;display:block'>Distribución de Vehículos</span>", unsafe_allow_html=True)

        columna_1, columna_2, columna_3 = st.columns([1, 0.2, 1])

        with columna_1:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            texto = """<div style='text-align: justify; font-size: 18px;'>
                Con esta gráfica de barras se refleja en proporción la cantidad de tipos de motirazación que existen en la actualidad. Siendo los modelos con mayor presencia los modelos de Gasolina seguidos de Gasóleo.
    Se aprecia el aumento de modelos eléctricos e híbridos, lo cual reflaja la preocupación por las emisiones. A día de hoy sabemos que el número de vehículos eléctricos e híbridos está aumentando considerablemente por el compromiso con el medio ambiente y las energias renovables, sin embargo aún nos queda un camino largo que recorrer para llegar si quiera a igualar en número a los de combustible. Poco a poco se intenta minimizar el uso de vehículos de combustible, por ejemplo en transporte de mercancías y de pasajeros.\n</div>"""


            st.markdown(texto, unsafe_allow_html=True)
            
            st.markdown("")
        
        with columna_3:
            st.markdown("")
            funciones_ecoestudio_ecohistorico.funcion_proporcion_motorizacion()
        
        st.markdown("<span style='color:cyan;font-size:30px;font-weight:bold'>Consumo en los Vehículos</span>", unsafe_allow_html=True)
        
        col1,col2 = st.columns(2)
                   
        with col2:
            st.markdown("")
            
            opciones = ['Gasolina', 'Gasóleo',"Híbridos enchufables","Híbridos de gasolina",'Eléctricos puros',"Gas natural"]

            # Mostrar el cuadro de selección
            opcion_seleccionada = st.selectbox('Selecciona una opción:', opciones)
            
            if opcion_seleccionada == "Eléctricos puros":
                
                st.markdown("")
                st.markdown("")
                st.markdown("")

                
                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Consumo Eléctrico medio 16.6kWh </span>", unsafe_allow_html=True)
                texto = """<div style='text-align: justify; font-size: 18px;'>
    Estos datos indican que los coches eléctricos puros tienen un consumo de energía relativamente bajo, en comparación con los coches de gasolina o diésel. Esto se debe a que los motores eléctricos son mucho más eficientes que los motores de combustión interna.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True) 
                

            if opcion_seleccionada == "Gasóleo":

                st.markdown("")
                st.markdown("")
                st.markdown("")
                

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Comsumo Gasóleo medio 5.7l </span>", unsafe_allow_html=True)

                texto = """<div style='text-align: justify; font-size: 18px;'>
                
Estos datos indican que los coches de gasóleo tienen un consumo relativamente bajo. Esto se debe a varias factores como la eficiencia del motor que a diferencias en el ciclo de funcionamiento y la relación de compresión, permiten una combustión más completa y una mayor eficiencia térmica en los motores diésel, la mayor densidad energética que hace que los vehículos diésel recorran distancias más largas con una cantidad menor de combustible en comparación con los vehículos de gasolina y su mayor eficiencia en condiciones de carga pesada.
    \n</div>"""
                st.markdown(texto, unsafe_allow_html=True)

           

            if opcion_seleccionada == "Gasolina":
                
                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Consumo Gasolina medio 6.3l </span>", unsafe_allow_html=True)

                texto = """<div style='text-align: justify; font-size: 18px;'>
    Estos datos indican que los coches de gasolina tienen un consumo relativamente elevado, en comparación con otros tipos de vehículos, como los coches eléctricos o los híbridos. Esto se debe a que los motores de gasolina son menos eficientes que otros tipos de motores.
    El consumo de gasolina de un coche puede variar en función de una serie de factores, como el tamaño del vehículo, la aerodinámica, el tipo de transmisión y el estilo de conducción. En general, los coches más grandes y con aerodinámica más desfavorable suelen consumir más gasolina.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)   

            if opcion_seleccionada == "Híbridos de gasolina":
                
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Consumo Gasolina medio 5.8l</span>", unsafe_allow_html=True)            

                texto = """<div style='text-align: justify; font-size: 18px;'>
    Estos datos indican que los coches híbridos de gasolina tienen un consumo relativamente bajo, en comparación con los coches de gasolina convencionales. Esto se debe a que los motores de combustión de los coches híbridos de gasolina solo se utilizan cuando el motor eléctrico no tiene suficiente autonomía para cubrir el trayecto.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)
                
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'>Consumo Eléctrico medio 24.3kWh</span>", unsafe_allow_html=True) 

                texto = """<div style='text-align: justify; font-size: 18px;'>
                
    
 Los datos de la gráfica también indican que los ochces híbridos de gasolina tienen un consumo mayor que los híbridos enchufables debido a que utilizan un motor de combustión interna, típicamente de gasolina, junto con un motor eléctrico y una batería pequeña para proporcionar asistencia al motor principal y recuperar energía durante la desaceleración. Estos vehículos no pueden ser recargados externamente y dependen principalmente de la energía generada durante la conducción y la regeneración de energía durante el frenado.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)              


            if opcion_seleccionada == "Híbridos enchufables":
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Consumo Gasolina medio 1.4l</span>", unsafe_allow_html=True)    

                texto = """<div style='text-align: justify; font-size: 18px;'>
Estos datos indican que los coches híbridos enchufables tienen un consumo relativamente bajo, en comparación con los coches de gasolina o los coches diésel. Esto se debe a que los motores de combustión de los coches híbridos enchufables solo se utilizan cuando el motor eléctrico no tiene suficiente autonomía para cubrir el trayecto.\n</div>"""
                st.markdown(texto, unsafe_allow_html=True)
                
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Consumo Eléctrico medio 16.1kWh</span>", unsafe_allow_html=True)    

                texto = """<div style='text-align: justify; font-size: 18px;'>
    Los datos de la gráfica también indican que hay un pequeño número de coches híbridos enchufables que tienen un consumo muy elevado. Estos coches suelen ser modelos de gama alta con baterías de gran capacidad, diseñados para ofrecer una autonomía eléctrica muy elevada.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)            
            
            if opcion_seleccionada == "Gas natural":
                st.markdown("")
                st.markdown("")
                st.markdown("")
                
                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Consumo Gas Natural medio 4.3kg</span>", unsafe_allow_html=True) 

                texto = """<div style='text-align: justify; font-size: 18px;'>
       Los motores de gas natural tienden a ser bastante eficientes en términos de consumo de combustible. El metano tiene una alta relación de hidrógeno-carbono y una buena relación aire-combustible, lo que permite una combustión más completa y, en general, una mayor eficiencia térmica que los motores de gasolina o diésel.
Aunque el gas natural puede ser más eficiente en términos de combustión, tiene un contenido energético más bajo por unidad de volumen en comparación con la gasolina o el diésel. Esto significa que los vehículos de gas natural pueden necesitar tanques más grandes o más frecuentes llenados de combustible para obtener la misma autonomía que un vehículo de gasolina o diésel.\n</div>"""


                
                
                
                
                st.markdown(texto, unsafe_allow_html=True)   
                
        with col1:
            
            funciones_ecoestudio_ecohistorico.funcion_boxplot_motorizacion_usuario(opcion_seleccionada)
        
        
        col1,col2 = st.columns([0.9,1])
        
        
        
        with col2:
            funciones_ecoestudio_ecohistorico.funcion_quesito_emisiones()
            
        with col1:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            
            st.markdown("<span style='color:cyan;font-size:25px;font-weight:bold'>¿Emiten más o menos C02 los coches de combustible frente a los híbridos?</span>", unsafe_allow_html=True)
        
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                      En esta gráfica podemos observar que las emisiones de CO2, tanto en híbridos de gasolina como en vehículos de combustión, rondan el 20%. Los vehículos menos contaminantes son los híbridos enchufables debido a la capacidad de funcinar en modo totalmente eléctrico, donde no se producen emisiones de escape en absoluto.
                    """
        
        
        
            st.markdown(texto, unsafe_allow_html=True)
            
            
            
            
            
            
        st.markdown("<span style='color:cyan;font-size:25px;font-weight:bold'>Relación entre Emisiones y Consumo</span>", unsafe_allow_html=True)
        
        funciones_ecoestudio_ecohistorico.funcion_emisiones_consumo("Todos")
        
        texto = """
                    <div style='text-align: justify; font-size: 18px;'>
Existe una relación directa entre el consumo de combustible y las emisiones de gases de efecto invernadero (como el dióxido de carbono, CO2) en los vehículos que disponen de combustión interna. Esto se debe a que la cantidad de CO2 emitida está directamente relacionada con la cantidad de combustible quemado. Cuanto más combustible se quema, más CO2 se produce.                                       
La relación entre las emisiones y el consumo de combustible en los vehículos, ya sean híbridos o de gasolina, es compleja y está influenciada por varios factores.
Cuanto más eficiente sea un motor, menor será su consumo de combustible y, por lo tanto, menores serán las emisiones de gases de efecto invernadero y contaminantes. Los vehículos híbridos, especialmente los híbridos enchufables, tienden a ser más eficientes debido a la capacidad de utilizar la energía eléctrica y recuperar energía durante la desaceleración.
El tamaño y el peso del vehículo también pueden influir en su consumo de combustible y emisiones. En general, los vehículos más grandes y pesados tienden a consumir más combustible y emitir más contaminantes que los vehículos más pequeños y ligeros.</div>"""
        st.markdown(texto, unsafe_allow_html=True)



        






