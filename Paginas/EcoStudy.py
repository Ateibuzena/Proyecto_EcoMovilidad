import streamlit as st
from funciones import funciones_ecoestudio_ecohistorico_ingles




def EcoStudy():
    motorization_vehicle = ['All', 'Gasoline', 'Diesel', 'Pure Electric', 'Plug-in Hybrid', 'Gasoline Hybrid']

    options_list = ['Vehicle Categories', 'Energy Efficiency Rating', 'Battery Capacity and Range', 'Vehicles and Consumption']
    st.sidebar.markdown("<h2>Select the information you want to obtain:</h2>", unsafe_allow_html=True)
    user_input = st.sidebar.radio("", options_list)
    #-----------------------------------------------------------

    if user_input == "Vehicle Categories":
        #
        # Eco-study1-Types of Vehicles
        #

        # Basic information about the type of vehicle-------------

        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Vehicle Categories</span>", unsafe_allow_html=True)
    
        st.write("<div style='text-align: justify; font-size: 18px;'> You will be informed about the different types of vehicles according to their class. The classification refers to a way of categorizing them according to certain characteristics such as size, weight, capacity, among others.</div>", unsafe_allow_html=True)
        st.markdown(" ")

        col1, col2 = st.columns(2)
        with col1:

            st.markdown(" ") 
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Categories L :</span>", unsafe_allow_html=True)
            st.write("<div style='text-align: justify; font-size: 18px;'>These categories (L3e, L5e, L6e, L7e) are related to light vehicles, especially vehicles with two, three or four wheels. They can be light motorcycles and quadricycles, and the letter 'L' probably indicates 'light'.</div>",unsafe_allow_html= True)
            st.markdown(" ") 
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Categories M :</span>", unsafe_allow_html=True)
            st.write("<div style='text-align: justify; font-size: 18px;'> These categories (M1, M2, M3) are associated with heavier vehicles, such as cars and other motor vehicles. 'M1' generally refers to vehicles intended for the carriage of passengers and their luggage.</div>",unsafe_allow_html= True)
            st.markdown(" ")
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Categories N :</span>", unsafe_allow_html=True)
            st.write("<div style='text-align: justify; font-size: 18px;'> These categories (N1, N2, N3) could be related to industrial and commercial vehicles, such as trucks. 'N1' generally refers to vehicles intended for the carriage of goods and their trailers.</div>",unsafe_allow_html= True)

        with col2:

            col3, col4, col5 = st.columns([0.5, 1, 0.5])
            for i in range (1, 1):
                st.markdown(" ") 
            with col4:

                user_vehicle_input = st.selectbox("Select the motorization:", motorization_vehicle)
            funciones_ecoestudio_ecohistorico_ingles.funcion_categorias_e_c(user_vehicle_input)

                    
        st.markdown("")
        st.markdown("")
        st.write("<div style='text-align: justify; font-size: 18px;'>In the analysis, it is highlighted that electric vehicles cover a wider range of categories compared to non-electric ones, which are mainly limited to categories M1 and N1. The most representative categories for electric vehicles are sedans, freight transport vehicles, and motorcycles. We can understand the importance of these in the market, as the different categories have a wide range of applications beyond individual use and their adoption in various contexts can contribute to environmental sustainability, operational efficiency, and innovation in mobility.</div>",unsafe_allow_html= True)

        #
        #Fin Ecoestudio1-Clase de Vehiculos
        # 


    elif user_input == 'Energy Efficiency Rating':
        #
        #Ecoestudio2-Energy classification
        #
        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Energy Classification</span>", unsafe_allow_html=True)
        funciones_ecoestudio_ecohistorico_ingles.funcion_calsificacion_e_c('All')
        col1,col2 = st.columns(2)
        with col1:
            st.markdown("<span style='color:cyan;font-size:30px;font-weight: bold' >Energy Classification labels refer to a vehicle's CO2 emissions relative to the average</span>", unsafe_allow_html=True)

        with col2:
            col1,col2 = st.columns([0.5,1])
            with col2:
                texto = """
                            <div style='text-align: justify;font-size:18px '>
                            

                            - **Label A:** -25% (or less)
                            - **Label B:** -15% to -25%
                            - **Label C:** -5% to -15%
                            - **Label D:** -5% to +5%
                            - **Label E:** +5 to +15%
                            - **Label F:** +15% to +25%
                            - **Label G:** +25% or more
                            """

                    # Center-align the text
                st.markdown(texto, unsafe_allow_html=True) 

        st.markdown(" ")
        st.markdown(" ")
        
        #------------------------Graph---------------------------
        # Add selectbox to Streamlit's sidebar
        vehicle_powertrain = ['Gasoline','Diesel', 'Plug-in Hybrid','Gasoline Hybrid']
        user_input_vehicles = st.selectbox("Select the vehicles' powertrain:", vehicle_powertrain)
        funciones_ecoestudio_ecohistorico_ingles.funcion_calsificacion_e_c(user_input_vehicles)
        texto = """
                    <div style='text-align: justify;font-size:18px'>
                    In the energy efficiency review, it is observed that most electric vehicles achieve the maximum classification (A). Those without specific classification are pure electric vehicles. On the other hand, vehicles with the worst classification (G) are usually plug-in hybrids, followed by gasoline hybrids.
                    Among non-electric vehicles, those with label C predominate, followed by categories B and D. A more detailed review of vehicles with label G reveals that they are mostly gasoline cars, followed by diesel ones.
                """

            # Center-align the text
        st.markdown(texto, unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        #----------------------------------------------------------
        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>What happens with vehicles labeled G and Unclassified?</span>", unsafe_allow_html=True)
        c_1,c_2, c_3 = st.columns([1, 0.05, 1])
        with c_1:
        #Notas del autor: aqui no le voy a poner en principio el seleccionable por que es interesante ver todos no uno por uno
            funciones_ecoestudio_ecohistorico_ingles.funcion_etiqueta_g_sin_especificar()
        
        with c_3:
            import pandas as pd
            import plotly.express as px
            import numpy as np
            df_coches = pd.read_csv("data/df_coches_escrapeo_ingles.csv")
            df_filtrado = df_coches[(df_coches["G"] == 1) | (df_coches["Unclassified"] == 1)][["Minimum Emissions", "Maximum Emissions", "Engine Type", "G", "Unclassified"]].copy()
            df_filtrado['Energy Clasification'] = np.where(df_filtrado['G'] == 1, 'G', 'Unclassified')
            df_filtrado['Energy Clasification'] = np.where(df_filtrado['Unclassified'] == 1, 'Unclassified', df_filtrado['Energy Clasification'])
            fig = px.scatter(data_frame  = df_filtrado,
                    x           = "Minimum Emissions",
                    y           = "Maximum Emissions",
                    hover_name  = "Engine Type",
                    color       = "Energy Clasification"
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
                    The first graph shows that vehicles with energy label G 
                    are mainly diesel, followed by gasoline, while unclassified vehicles 
                    are mostly gasoline, followed by diesel. In the second graph, it is observed 
                    that unclassified vehicles have slightly lower minimum emissions than those 
                    with label G, but considerably higher maximum emissions. The implications are 
                    that vehicles with label G and unclassified ones are more polluting, so it is 
                    recommended to avoid purchasing them if concerned about the environment, and to 
                    opt for electric and hybrid vehicles to reduce carbon footprint. It is advisable 
                    to check the energy label and the IDAE website before making a purchase decision.
                """

            # Center-align the text
        st.markdown(texto, unsafe_allow_html=True)
        #
        #End Ecoestudio2-Energy classification
        #
    elif user_input == 'Battery Capacity and Range':
        #
        #Ecoestudio3-Autonomy and Battery Capacity
        #
        st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Relationship Between Autonomy and Battery Capacity</span>", unsafe_allow_html=True)


        funciones_ecoestudio_ecohistorico_ingles.funcion_autonomia_bateria()
        
        
        st.markdown("<span style='color:cyan;font-size:30px;font-weight:bold'>There is a direct correlation between both variables</span>", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<div style='text-align: justify; font-size: 18px;'> In other words, the higher the battery capacity, the greater the electric autonomy.
                    This is because batteries with higher capacity can store more energy, allowing the vehicle to travel a greater distance before needing to recharge. The graph shows that, in general, pure electric vehicles have the highest electric autonomy, followed by plug-in hybrids and gasoline hybrids.
                    In the case of pure electric vehicles, electric autonomy can vary between 100 and 600 kilometers, depending on the battery capacity. Plug-in hybrids typically have an electric autonomy between 20 and 80 kilometers, while gasoline hybrids only have an electric autonomy of a few kilometers.
                    Of course, electric autonomy also depends on other factors such as driving style, weather conditions, and battery condition. However, battery capacity is one of the most important factors determining the electric autonomy of a vehicle.</div>""",unsafe_allow_html= True)
    
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
            st.markdown("<span style='display: block;font-size:50px;text-align :center;font-weight:bold'>What electric autonomy do electric vehicles have?</span>", unsafe_allow_html=True)
        with col2:
            funciones_ecoestudio_ecohistorico_ingles.funcion_violin_autonomia_conjunta_e()

        texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                    The graph shows that the autonomy of vehicles is condensed between 66 and 313 km.
                    According to the data, the most popular electric vehicles are those with an autonomy of less than 100 km. The market is divided into different categories according to different autonomies.
                    Vehicles with autonomy from 285 km onwards become vehicles with a higher cost and in relation to autonomy from 500 km onwards we are talking about luxury or exotic vehicles such as Tesla, for example.
                """

            # Center-align the text
        
        st.markdown(texto, unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("<span  style='color:cyan;font-size:30px;font-weight:bold'>What categories are within the most common vehicles?</span>", unsafe_allow_html=True)
    
        funciones_ecoestudio_ecohistorico_ingles.funcion_autonomia_por_categoria_e()
        col1,col2,col3 = st.columns([1,0.25,1])
        with col1:
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                        Within the popular vehicles, it is observed that the predominant category is M1,
                        which corresponds to vehicles intended for the transportation of passengers with a maximum of 8 seats in addition to the driver's seat.
                        For more information, visit the section "Vehicle Categories".
                    """
            st.markdown(texto, unsafe_allow_html=True)
        with col3:
            texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                
                    | Category | Min  | Mean | Max  |
                    |----------|------|------|------|
                    | L3e      | 100.0| 100.0| 100.0|
                    | L5e      | 97.0 | 97.0 | 97.0 |
                    | L6e      | 48.0 | 79.43| 100.0|
                    | L7e      | 45.0 | 75.88| 100.0|
                    | M1       | 42.0 | 60.12| 100.0|
                    | N1       | 54.0 | 79.64| 100.0|
                
                """
            st.markdown(texto, unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")

        st.markdown("<span  style='color:cyan;font-size:30px;font-weight:bold'>What is the relationship between Electric Power and Autonomy?</span>", unsafe_allow_html=True)
        col1,col2 = st.columns([1.2,2])
        with col1:
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                        Pure electric vehicles have the greatest autonomy, followed by plug-in hybrids
                        with extended autonomy. Gasoline hybrids have lower electric autonomy.
                        Factors such as driving style, weather conditions, and load affect autonomy. It is crucial to consult
                        the manufacturer's information to know the specific autonomy. Also, in warm climates, air conditioning can
                        reduce autonomy. It is advisable to plan trips in advance to ensure charging stations available en route.
                    """
            st.markdown(texto, unsafe_allow_html=True)
            st.markdown(" ")            
            motorizacion_vehiculo = ['All','Pure Electric','Plug-in Hybrid',
            'Gasoline Hybrid']
            input_usuario_vehiculos = st.selectbox("Select the vehicles' powertrain:", motorizacion_vehiculo)
        with col2:

            funciones_ecoestudio_ecohistorico_ingles.funcion_scater_potencia_autonomia_e(input_usuario_vehiculos)

        st.markdown("<span  style='font-size:50px;font-weight:bold'>How does Electric Power vary?</span>", unsafe_allow_html=True) 
        col7,col8 = st.columns(2)
        with col7:
            st.markdown("<span  style='color:cyan;font-size:30px;font-weight:bold'>Pure Electric</span>", unsafe_allow_html=True)
            texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                    The histogram shows that most pure electric cars in Spain have an electric power 
                    between 100 and 300 kW. This means that most pure electric cars have power similar 
                    to that of a medium-sized gasoline or diesel car.  
                
                """
            st.markdown(texto, unsafe_allow_html=True)

            funciones_ecoestudio_ecohistorico_ingles.funcion_potencia_caja_e(['Pure Electric'])
        with col8:
            funciones_ecoestudio_ecohistorico_ingles.funcion_potencia_barras_e(['Pure Electric'])

            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                    There is a small proportion of pure electric cars with an electric power greater than 300 kW. These cars are usually 
                    sports or luxury cars, and have enough power to accelerate quickly and reach high speeds.
                    
                    """
            st.markdown(texto, unsafe_allow_html=True)


        texto = """
                    <div style='text-align: justify; font-size: 18px;'>
                Most pure electric cars in Spain have sufficient electric power to meet the needs of the majority of drivers. 
                There is a small proportion of pure electric cars with above-average electric power, designed for drivers seeking superior performance. 
                """
        st.markdown(texto, unsafe_allow_html=True)

        st.markdown(" ")
        col1,col2 = st.columns([0.7,1])
        with col2:
            st.markdown("<span  style='color:cyan;font-size:30px;font-weight:bold'>Hybrid</span>", unsafe_allow_html=True)
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                    The histogram shows that most plug-in hybrids in Spain have an electric power 
                    between 100 and 200 kW. This means that most plug-in hybrids have power similar 
                    to that of a compact-sized gasoline or diesel car.  The histogram also shows that there is a small 
                    proportion of plug-in hybrids with an electric power greater than 200 kW. These cars are usually 
                    high-end, and have enough power to accelerate quickly and reach high speeds. 
                    """
            st.markdown(texto, unsafe_allow_html=True)
            lista_posibles_motorizaciones = ['Plug-in Hybrid', 'Gasoline Hybrid']
            input_usuario_vehiculos = st.multiselect("Select the vehicles' powertrain:", lista_posibles_motorizaciones,default=lista_posibles_motorizaciones)
            st.markdown(" ")
            st.markdown(" ")
            st.markdown(" ")
            funciones_ecoestudio_ecohistorico_ingles.funcion_potencia_barras_e(input_usuario_vehiculos)
        with col1:

            funciones_ecoestudio_ecohistorico_ingles.funcion_potencia_caja_e(input_usuario_vehiculos)
            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                    Compared to the histogram of pure electric cars, it can be observed that most plug-in hybrids 
                    have lower electric power. This is because plug-in hybrids also have a gasoline or diesel engine, 
                    which provides additional power when needed. It can also be observed that the distribution of 
                    electric power of plug-in hybrids is more uniform than that of pure electric cars. This is because 
                    plug-in hybrid car manufacturers offer a wider range of electric powers to meet the needs of different types of drivers.
                    """
            st.markdown(texto, unsafe_allow_html=True)

    # ------------------------------------'Vehicles Distribution and their Consumption'------------------------------------

    elif user_input == 'Vehicles and Consumption':

        st.write("<span style='text-align: center; font-size: 50px; font-weight: bold;display:block'>Vehicles Distribution</span>", unsafe_allow_html=True)

        columna_1, columna_2, columna_3 = st.columns([1, 0.2, 1])

        with columna_1:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            texto = """<div style='text-align: justify; font-size: 18px;'>
                This bar chart reflects the proportion of different types of powertrains currently available. Gasoline models are the most prevalent, followed by diesel.
            An increase in electric and hybrid models is observed, which reflects the concern for emissions. Today, we know that the number of electric and hybrid vehicles is increasing considerably due to the commitment to the environment and renewable energy sources, however, we still have a long way to go to even match the number of gasoline-powered vehicles. Gradually, efforts are being made to minimize the use of fuel vehicles, for example, in the transportation of goods and passengers.\n</div>"""

            st.markdown(texto, unsafe_allow_html=True)

            st.markdown("")

        with columna_3:
            st.markdown("")
            funciones_ecoestudio_ecohistorico_ingles.funcion_proporcion_motorizacion()

        st.markdown("<span style='color:cyan;font-size:30px;font-weight:bold'>Consumption in Vehicles</span>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col2:
            st.markdown("")

            options = ['Pure Electric', 'Gasoline', 'Diesel', 'Plug-in Hybrid',
       'Gasoline Hybrid', 'Natural Gas']

            # Show the selection box
            selected_option = st.selectbox('Select an option:', options)

            if selected_option == "Pure Electric":

                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Average Electric Consumption 16.6kWh </span>", unsafe_allow_html=True)
                texto = """<div style='text-align: justify; font-size: 18px;'>
        These data indicate that pure electric cars have relatively low energy consumption compared to gasoline or diesel cars. This is because electric motors are much more efficient than internal combustion engines.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True) 

            if selected_option == "Diesel":

                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Average Diesel Consumption 5.7l </span>", unsafe_allow_html=True)

                texto = """<div style='text-align: justify; font-size: 18px;'>
        These data indicate that diesel cars have relatively low consumption. This is due to several factors such as the efficiency of the engine, differences in the operating cycle, and the compression ratio, which allow for more complete combustion and greater thermal efficiency in diesel engines, higher energy density that makes diesel vehicles cover longer distances with a smaller amount of fuel compared to gasoline vehicles, and their greater efficiency under heavy load conditions.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)


            if selected_option == "Gasoline":

                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Average Gasoline Consumption 6.3l </span>", unsafe_allow_html=True)

                texto = """<div style='text-align: justify; font-size: 18px;'>
    These data indicate that gasoline cars have relatively high consumption compared to other types of vehicles, such as electric cars or hybrids. This is because gasoline engines are less efficient than other types of engines.
    The gasoline consumption of a car can vary depending on a number of factors, such as the size of the vehicle, aerodynamics, type of transmission, and driving style. In general, larger and less aerodynamic cars tend to consume more gasoline.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)   

            if selected_option == "Gasoline Hybrid":

                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Average Gasoline Consumption 5.8l</span>", unsafe_allow_html=True)            

                texto = """<div style='text-align: justify; font-size: 18px;'>
    These data indicate that gasoline hybrid cars have relatively low consumption compared to conventional gasoline cars. This is because the combustion engines of gasoline hybrid cars are only used when the electric motor does not have enough range to cover the journey.\n</div>"""

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

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'>Average Electric Consumption 24.3kWh</span>", unsafe_allow_html=True) 

                texto = """<div style='text-align: justify; font-size: 18px;'>
                        The data from the graph also indicate that hybrid gasoline cars have higher consumption than plug-in hybrids because they use an internal combustion engine, typically gasoline, along with an electric motor and a small battery to provide assistance to the main engine and recover energy during deceleration. These vehicles cannot be externally recharged and depend mainly on energy generated during driving and energy regeneration during braking.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)


            if selected_option == "Plug-in Hybrid":

                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Average Gasoline Consumption 1.4l</span>", unsafe_allow_html=True)    

                texto = """<div style='text-align: justify; font-size: 18px;'>
                These data indicate that plug-in hybrids have relatively low 
                consumption compared to gasoline or diesel cars.<br><br> This is because the combustion engines of plug-in hybrids are only 
                used when the electric motor does not have enough range to cover the journey.</div>"""

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
                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Average Electric Consumption 16.1kWh</span>", unsafe_allow_html=True)    

                texto = """<div style='text-align: justify; font-size: 18px;'>
                The data from the graph also indicate that there is a small number of plug-in hybrids that have very high consumption. These cars are usually high-end models with large capacity batteries, designed to offer very high electric range.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)


            if selected_option == "Natural Gas":

                st.markdown("")
                st.markdown("")
                st.markdown("")

                st.write("<span style='color: cyan; text-align: center; font-size: 25px; font-weight: bold;'> Average Natural Gas Consumption 4.3kg</span>", unsafe_allow_html=True) 

                texto = """<div style='text-align: justify; font-size: 18px;'>
    Natural gas engines tend to be quite efficient in terms of fuel consumption. Methane has a high hydrogen-carbon ratio and a good air-fuel ratio, which allows for more complete combustion and, in general, higher thermal efficiency than gasoline or diesel engines.
    Although natural gas may be more efficient in terms of combustion, it has a lower energy content per unit volume compared to gasoline or diesel. This means that natural gas vehicles may require larger or more frequent fuel tanks to achieve the same range as a gasoline or diesel vehicle.\n</div>"""

                st.markdown(texto, unsafe_allow_html=True)   


        with col1:

            funciones_ecoestudio_ecohistorico_ingles.funcion_boxplot_motorizacion_usuario(selected_option)


        col1, col2 = st.columns([0.9, 1])

        with col2:
            funciones_ecoestudio_ecohistorico_ingles.funcion_quesito_emisiones()

        with col1:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.markdown("<span style='color:cyan;font-size:25px;font-weight:bold'>Do Fuel Cars Emit More or Less CO2 Than Hybrid?</span>", unsafe_allow_html=True)

            texto = """
                        <div style='text-align: justify; font-size: 18px;'>
                    In this graph, we can observe that CO2 emissions, both in gasoline hybrids and combustion vehicles, are around 20%. The least polluting vehicles are plug-in hybrids due to their ability to operate in fully electric mode, where no exhaust emissions are produced at all.
                    """

            st.markdown(texto, unsafe_allow_html=True)

        st.markdown("<span style='color:cyan;font-size:25px;font-weight:bold'>Relationship between Emissions and Consumption</span>", unsafe_allow_html=True)

        funciones_ecoestudio_ecohistorico_ingles.funcion_emisiones_consumo("All")

        texto = """
                    <div style='text-align: justify; font-size: 18px;'>
        There is a direct relationship between fuel consumption and greenhouse gas emissions (such as carbon dioxide, CO2) in vehicles with internal combustion. This is because the amount of CO2 emitted is directly related to the amount of fuel burned. The more fuel burned, the more CO2 is produced.
    The relationship between emissions and fuel consumption in vehicles, whether hybrid or gasoline, is complex and influenced by several factors.
    The more efficient an engine is, the lower its fuel consumption and, therefore, the lower its greenhouse gas and pollutant emissions. Hybrid, especially plug-in hybrids, tend to be more efficient due to their ability to use electric energy and recover energy during deceleration.
    The size and weight of the vehicle can also influence its fuel consumption and emissions. In general, larger and heavier vehicles tend to consume more fuel and emit more pollutants than smaller and lighter vehicles.</div>"""
        st.markdown(texto, unsafe_allow_html=True)








   