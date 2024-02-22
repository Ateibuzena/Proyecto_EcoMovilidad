import streamlit as st
import pandas as pd

import plotly.express as px


def pagina_ecofaqs():
    st.write("<p style='display:block;text-align:center;font-size: 50px;'><strong>Preguntas Frecuentes</p>", unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("")
    col1, col2, col3 = st.columns([0.8, 1.4, 0.8])

    with col2:
        df_coches= pd.read_csv("./Data/df_coches_escrapeo.csv")

        with st.expander("**¿Cómo calcula la página el coste del viaje?**"):
            st.write("Utilizamos la distancia del viaje y el consumo de combustible o energía de su vehículo, junto con los precios actuales de la gasolina, gasóleo o kw/h, para calcular el coste estimado del viaje mediante una predicción de dichos precios. En el caso de no conocer el precio actual, se utilizará el precio medio actual. ")
        st.markdown("")


        
        with st.expander("En la actualidad, ¿hay más vehículos eléctricos o de combustible?"):
            st.write("En España, la adopción de vehículos eléctricos ha estado aumentando en los últimos años, aunque aún representan una pequeña parte del total de vehículos en circulación. Sin embargo, los vehículos de combustible convencionales siguen siendo predominantes en España, con una gran mayoría de vehículos impulsados por gasolina y gasóleo en las carreteras del país.")
            fig = px.bar(
            x=df_coches["Motorización"].value_counts().index,  
            y=df_coches["Motorización"].value_counts(),  
            labels={'y': '', 'x': ''},  
            title=''
            )
            
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("")
        
        with st.expander("**¿Cómo encuentro el consumo de combustible o energía por kilómetro de mi vehículo?**"):
            st.write("Puede consultarlo en el manual de su vehículo.")
        st.markdown("")

        with st.expander("¿Los cálculos tienen en cuenta otros factores como el tráfico o la eficiencia del vehículo?"):
            st.write("Los cálculos obtenidos son estimaciones que se basan en el consumo promedio de combustible o energía de su vehículo y las predicciones de precio en base a los precios actuales del combustible o la electricidad. Además, tienen en cuenta otros factores o características del vehículo como es la autonomía del vehículo o la capacidad de la batería, pero no tiene en cuenta ningún factor externo como es el tráfico o las condiciones climáticas.")
        st.markdown("")

        with st.expander("**¿Qué datos necesito proporcionar para obtener un cálculo preciso del coste del viaje?**"):
            st.write("Necesitará ingresar la distancia total del viaje, el modelo de vehículo usado (eléctrico, de combustible o híbrido), el consumo de combustible o energía por kilómetro de su vehículo y los precios actuales de la gasolina, gasóleo o kw/h para así poder predecir el coste del próximo viaje.")
        st.markdown("")

        with st.expander("**¿Los cálculos son válidos para viajes largos o cortos?**"):
            st.write("Nuestra herramienta permite calcular el coste del viaje dentro de todo el territorio nacional, por lo que, sirve tanto para viajes largos como cortos.")
        st.markdown("")

        with st.expander("**En cuanto a emisiones, ¿qué tipo de vehículo contamina más?**"):
            st.write("Los coches eléctricos son cero emisiones, es decir, no contaminan. En cuanto a vehículos de gasolina, gasóleo o híbridos, son muy similares en cuanto a emisiones.")
            fig = px.pie(data_frame = df_coches,
                    values=df_coches.groupby("Motorización")["Emisiones Máximo"].mean().to_list(),
                    names = df_coches.groupby("Motorización")["Emisiones Máximo"].mean().index)
            
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("")

        with st.expander("**¿Existe relación entre el consumo de combustible y lo que contamina un vehículo?**"):
            st.write("Sí. Existe una relación directa entre el consumo según el tipo de combustible y emisiones de CO2, por lo que, a mayor consumo, mayor cantidad de emisiones de C02.")
            fig = px.scatter(data_frame =df_coches,
                x = "Consumo Máximo (l/100km)",
                y = "Emisiones Máximo",
                color = "Motorización" ) 
            fig.update_layout(
            legend=dict(
                x=0.7,
                y=1,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(0, 0, 0, 0)',
                borderwidth=1
                        )
            )
            st.plotly_chart(fig, use_container_width=True)
