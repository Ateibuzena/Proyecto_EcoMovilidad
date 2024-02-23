import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt
from funciones.funciones_ecoestudio_ecohistorico_ingles import *

#from PIL import Image

def pagina_historico_ingles(): 

    st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Gasoline vs. Diesel</span>", unsafe_allow_html=True)
    
    
    #texto titulo
    texto = """<div style='text-align: justify; font-size: 18px;'>
Welcome to our analysis page on the evolution of diesel and gasoline prices from 2002 to the present day! Here you will find detailed data and visualizations on how the prices of these fuels have fluctuated on a weekly basis. We will explore the trajectory of diesel and gasoline prices over the weeks, allowing you to better understand the trends and possible factors influencing their variations. From economic ups and downs to seasonal changes, we will examine how these prices have responded to various events and market conditions over time. Additionally, we offer predictions about prices for a range of weeks, based on models and predictive analysis. These predictions can provide you with a useful insight for planning and understanding the possible future directions of fuel prices. Finally, we provide dynamic graphical visualizations that illustrate the evolution of diesel and gasoline prices over time. These visual representations will help you identify patterns, trends, and anomalies clearly and effectively.</div>"""

    st.markdown(texto, unsafe_allow_html=True)
    funcion_line_precio("Seleccione época")

    #Subtitulo  30px
           

    st.write("<span style='display: block; font-size: 50px; font-weight: bold;'>Highlighted Moments</span>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns([1,0.05,1])

    
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        

        funcion_line_precio("2002-2008")

        st.write("<span style='color:cyan;font-size:25px;font-weight: bold'>2011 - 2014</span>", unsafe_allow_html=True)
        texto = ("""<div style='text-align: justify; font-size: 18px;'>
The Arab revolutions in 2011 caused political instability in some oil-producing countries, such as Libya and Yemen, which reduced the global oil supply. The civil war in Libya, which began in 2011, led to a significant drop in the country's oil production. Protests in Yemen also affected the country's oil production.<br><br>The Eurozone crisis led to a recession in some European countries, reducing oil consumption. The increase in shale oil production in the United States contributed to a rise in the global oil supply and a decrease in prices. The development of new fracking technologies allowed the United States to significantly increase its shale oil production. This increase in US oil production helped alleviate pressure on oil prices.</div>
    """)
        st.markdown(texto, unsafe_allow_html=True)

        
        st.markdown("")
        st.markdown("")
        st.markdown("")
        funcion_line_precio("2022-Actualidad")

    with col3:
        
        st.write("<span style='color:cyan;font-size:25px;font-weight: bold'>2002 - 2008</span>", unsafe_allow_html=True)  
        texto = ("""<div style='text-align: justify; font-size: 18px;'>
        The global economy experienced strong growth during the first half of the 2000s, leading to an increase in the demand for oil and consequently in fuel prices.<br><br>In the Middle East, where some of the major oil producers are located, experienced a series of political conflicts during this period, creating uncertainty in the oil market and contributing to the rise in crude oil prices.<br><br>China, as an emerging economy, underwent rapid growth in its energy demand, which also contributed to the increase in international oil prices.<br><br>In Spain, the government increased taxes on fuels several times during this period, contributing to the rise in the final price.<br><br>Additionally, the euro weakened against the US dollar during this period, which increased the cost of oil imports as they are priced in dollars.""")

        st.markdown(texto, unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        
        funcion_line_precio("2011-2014")
        
   
       
        st.write("<span style='white-space: nowrap;color:cyan; text-align: center; font-size: 25px; font-weight: bold;'>2021 - 2024</span>", unsafe_allow_html=True)

        texto = ("""<div style='text-align: justify; font-size: 18px;'>
The COVID-19 pandemic and associated restriction measures caused a decline in oil demand in 2020. However, the economic recovery in 2021 led to an increase in demand, contributing to the rise in crude oil prices. The war in Ukraine since February 2022 generated significant uncertainty in the global energy market, leading to a substantial increase in the price of oil and natural gas.<br><br>The sanctions imposed on Russia by the European Union and other countries affected the supply of oil and natural gas, which also contributed to the increase in fuel prices.<br><br>Additionally, the depreciation of the euro against the US dollar increased the cost of oil imports, as they are priced in dollars, and the Organization of the Petroleum Exporting Countries (OPEC) and its allies agreed to reduce oil production to maintain high crude prices.</div>
    """)
        st.markdown(texto, unsafe_allow_html=True)




    st.write("<span style=' text-align: center;display:block; font-size: 50px; font-weight: bold;'>Predict the fuel price in the future!</span>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")    

    col1,col2= st.columns([1,1])
    with col1:
        with st.form("my_form"):

            texto = ("""<div style='text-align: justify; font-size: 18px;'>
    Enter a range of weeks between 2 and 5.""")

            st.markdown(texto,  unsafe_allow_html=True)
            num_semanas = st.slider("", min_value=2, max_value=5)

            texto = ("""<div style='text-align: justify; font-size: 18px;'>
    Enter the price of diesel for the current week.""")

            st.markdown(texto,  unsafe_allow_html=True) 

            input_usuario_precio_gasoleo_semana_corriente = st.number_input(" ", max_value=5.00,step=0.10, min_value=0.00)




            texto = ("""<div style='text-align: justify; font-size: 18px;'>
    Enter the price of gasoline for the current week.""")

            st.markdown(texto,  unsafe_allow_html=True)            
            input_usuario_precio_gasolina_semana_corriente = st.number_input("",min_value = 0.00, max_value=5.00,step=0.10)
   # Every form must have a submit button.
            st.markdown("")
            st.markdown("")
            submitted = st.form_submit_button("Submit")
            if submitted:
                if input_usuario_precio_gasoleo_semana_corriente == 0 and input_usuario_precio_gasolina_semana_corriente == 0:
                    with col2:
                        st.markdown("")

                        st.image("https://c.tenor.com/rob0fK6GFfIAAAAd/tenor.gif", use_column_width=True)
                    texto = ("""<div style='font-size:24px;font-weight:bold;'>
                               You must enter a price different from 0 for any fuel.""")

                    st.markdown(texto,  unsafe_allow_html=True) 
                else:
                    with col2:
                        funcion_agregado_prediccion(input_usuario_precio_gasoleo_semana_corriente = input_usuario_precio_gasoleo_semana_corriente, input_usuario_precio_gasolina_semana_corriente =        input_usuario_precio_gasolina_semana_corriente , num_semanas=num_semanas)
            else:
                with col2:
                    st.image("https://c.tenor.com/rob0fK6GFfIAAAAd/tenor.gif", use_column_width=True)

    st.markdown("")
    st.markdown("")
    st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Get to know the metrics of our time series models.</span>", unsafe_allow_html=True)
    columna_1, columna_2 = st.columns(2)

    with columna_1:
        st.write("<span style='color: cyan; display: block; text-align: center; font-size: 30px; font-weight: bold;'>Gasoline</span>", unsafe_allow_html=True)

    with columna_2:
        st.write("<span style='color: cyan; display: block; text-align: center; font-size: 30px; font-weight: bold;'>Diesel</span>", unsafe_allow_html=True)
   
    texto = ("""<div style='display:block; text-align: center; font-size: 25px;'>
                History of the absolute differences between model predictions and actual values during training.""")

    st.markdown(texto,  unsafe_allow_html=True)
    columna_1, columna_2 = st.columns(2)

    with columna_1:
        df_metricas_gasolina = pd.read_csv("Data/df_metricas_gasolina.csv")
        # Historial del mae
        mae = df_metricas_gasolina['mae'].to_list()
        val_mae = df_metricas_gasolina['val_mae'].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(mae))), y=mae, mode='lines', name='Mae')
        val_trace = go.Scatter(x=list(range(len(val_mae))), y=val_mae, mode='lines', name='val_Mae')

        # Diseño del gráfico
        layout = go.Layout(
                        xaxis=dict(title='epoch'),
                        yaxis=dict(title='Mae'),
                        yaxis_range = [0, 0.2],
                        xaxis_range = [0, 210])

        # Figura
        fig = go.Figure(data=[trace, val_trace], layout=layout)
        fig.update_layout(
            legend=dict(
                x=0.8,
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

        # Mostrar la gráfica
        st.plotly_chart(fig, use_container_width=True)

    with columna_2:
        df_metricas_gasoleo = pd.read_csv("Data/df_metricas_gasoleo.csv")
        # Historial de mae
        mae = df_metricas_gasoleo['mae'].to_list()
        val_mae = df_metricas_gasoleo["val_mae"].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(mae))), y=mae, mode='lines', name='Mae')
        val_trace = go.Scatter(x=list(range(len(val_mae))), y=val_mae, mode='lines', name='val_Mae')

        # Diseño del gráfico
        layout = go.Layout(
                        xaxis=dict(title='epoch'),
                        yaxis=dict(title='Mae'),
                        yaxis_range = [0, 0.2],
                        xaxis_range = [0, 210]
                        )

        # Figura
        fig = go.Figure(data=[trace, val_trace], layout=layout)
        fig.update_layout(
            legend=dict(
                x=0.8,
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

        # Mostrar la gráfica
        st.plotly_chart(fig, use_container_width=True)
    
    texto = ("""<div style='display:block; text-align: justify; font-size: 18px;'>
             The MAE (Mean Absolute Error) is the mean of the absolute differences between model predictions 
             and actual values. Here, the MAE in both models is 0.01. This means that, 
             on average, the model predictions are off by 0.01 units from the actual value.
            A low MAE is a positive sign that the model is making accurate predictions""")

    st.markdown(texto,  unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")
    st.markdown("")

    texto = ("""<div style='display:block; text-align: center; font-size: 25px;'>
                Loss history during training""")

    st.markdown(texto,  unsafe_allow_html=True)

    columna_1, columna_2 = st.columns(2)

    with columna_1:
        df_metricas_gasolina = pd.read_csv("Data/df_metricas_gasolina.csv")
        # Historial de Loss
        loss = df_metricas_gasolina['loss'].to_list()
        val_loss = df_metricas_gasolina["val_loss"].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(loss))), y=loss, mode='lines', name='Loss')
        val_trace = go.Scatter(x=list(range(len(val_loss))), y=val_loss, mode='lines', name='Validation Loss')

        # Diseño del gráfico
        layout = go.Layout(
                        xaxis=dict(title='epoch'),
                        yaxis=dict(title='Mse'),
                        yaxis_range = [0, 0.025],
                        xaxis_range = [0, 210])

        # Figura
        fig = go.Figure(data=[trace, val_trace], layout=layout)
        fig.update_layout(
            legend=dict(
                x=0.8,
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

        # Mostrar la gráfica
        st.plotly_chart(fig, use_container_width=True)

    with columna_2:
        df_metricas_gasoleo = pd.read_csv("Data/df_metricas_gasoleo.csv")
        # Historial de Loss
        loss = df_metricas_gasoleo['loss'].to_list()
        val_loss = df_metricas_gasoleo['val_loss'].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(loss))), y=loss, mode='lines', name='Loss')
        val_trace = go.Scatter(x=list(range(len(val_loss))), y=val_loss, mode='lines', name='Validation Loss')

        # Diseño del gráfico
        layout = go.Layout(
                            xaxis=dict(title='epoch'),
                            yaxis=dict(title='Mse'),
                            xaxis_range = [0, 210],
                            yaxis_range = [0, 0.025]
                        )
                        

        # Figura
        fig = go.Figure(data=[trace, val_trace], layout=layout)
        fig.update_layout(
            legend=dict(
                x=0.8,
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
            )
        )

        # Mostrar la gráfica
        st.plotly_chart(fig, use_container_width=True)
    
    texto = ("""<div style='display:block; text-align: justify; font-size: 18px;'>
                The loss is a measure of the model's prediction error. In both models,
                it is 3.3043e-04, indicating that the model has a minimal loss during the training. A low loss is indicative of the model making good predictions 
                compared to the actual values.""")

    st.markdown(texto,  unsafe_allow_html=True)
