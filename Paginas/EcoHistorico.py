import streamlit as st

from funciones.funciones_ecoestudio_ecohistorico import *



def pagina_historico(): 

    st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Gasolina vs. Gasóleo</span>", unsafe_allow_html=True)
    
    
    #texto titulo
    texto = """<div style='text-align: justify; font-size: 18px;'>
            ¡Bienvenido a nuestra página de análisis sobre la evolución de los precios del gasóleo y la gasolina desde el año 2002 hasta la actualidad! Aquí encontrarás datos detallados y visualizaciones sobre cómo han fluctuado los precios de estos combustibles semana tras semana. Exploraremos la trayectoria de los precios del gasoil y la gasolina a lo largo de las semanas, permitiéndote comprender mejor las tendencias y los posibles factores que influyen en sus variaciones. Desde los altibajos económicos hasta los cambios estacionales, examinaremos cómo estos precios han respondido a diversos eventos y condiciones del mercado a lo largo del tiempo. Además, ofrecemos predicciones sobre los precios para un rango de semanas, basadas en modelos y análisis predictivos. Estas predicciones pueden brindarte una visión útil para planificar y comprender las posibles direcciones futuras de los precios de estos combustibles. Por último, te proporcionamos visualizaciones gráficas dinámicas que ilustran la evolución de los precios del gasóleo y la gasolina a lo largo del tiempo. Estas representaciones visuales te ayudarán a identificar patrones, tendencias y anomalías de manera clara y efectiva.</div>"""

    st.markdown(texto, unsafe_allow_html=True)
    funcion_line_precio("Seleccione época")

    #Subtitulo  30px
           

    st.write("<span style='display: block; font-size: 50px; font-weight: bold;'>Momentos Destacados</span>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns([1,0.05,1])

    
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        

        funcion_line_precio("2002-2008")

        st.write("<span style='color:cyan;font-size:25px;font-weight: bold'>2011 - 2014</span>", unsafe_allow_html=True)
        texto = ("""<div style='text-align: justify; font-size: 18px;'>
Las revoluciones árabes en 2011 provocaron inestabilidad política en algunos países productores de petróleo, como Libia y Yemen, lo que redujo la oferta global de petróleo. La guerra civil en Libia, que comenzó en 2011, provocó una caída significativa en la producción de petróleo del país.
Las protestas en Yemen también afectaron la producción de petróleo del país.<br>
<br>
La crisis del euro llevó a una recesión en algunos países europeos, lo que redujo el consumo de petróleo.El aumento de la producción de petróleo de esquisto en Estados Unidos contribuyó a un aumento de la oferta global de petróleo y a una bajada del precio.El desarrollo de nuevas tecnologías de fracking permitió a Estados Unidos aumentar significativamente su producción de petróleo de esquisto. Este aumento en la producción de petróleo de Estados Unidos ayudó a aliviar la presión sobre los precios del petróleo.</div>
    """)
        st.markdown(texto, unsafe_allow_html=True)

        
        st.markdown("")
        st.markdown("")
        st.markdown("")
        funcion_line_precio("2022-Actualidad")

    with col3:
        
        st.write("<span style='color:cyan;font-size:25px;font-weight: bold'>2002 - 2008</span>", unsafe_allow_html=True)  
        texto = ("""<div style='text-align: justify; font-size: 18px;'>
        La economía global experimentó un fuerte crecimiento durante la primera mitad de la década del 2000, lo que generó un aumento en la demanda de petróleo y, por ende, en el precio de los combustibles.<br>
<br>
Inestabilidad política en Oriente Medio, la región de Oriente Medio, donde se encuentran algunos de los principales productores de petróleo, experimentó una serie de conflictos políticos durante este periodo, lo que generó incertidumbre en el mercado petrolero y contribuyó al aumento del precio del crudo.
China, como economía emergente, experimentó un crecimiento acelerado en su demanda de energía, lo que también contribuyó al aumento del precio del petróleo a nivel internacional.<br>
<br>
En España el gobierno aumentó los impuestos sobre los combustibles en varias ocasiones durante este periodo, lo que contribuyó al alza en el precio final.
Además el euro se debilitó frente al dólar estadounidense durante este periodo, lo que encareció las importaciones de petróleo, ya que se cotizan en dólares.""")

        st.markdown(texto, unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        
        funcion_line_precio("2011-2014")
        
   
       
        st.write("<span style='white-space: nowrap;color:cyan; text-align: center; font-size: 25px; font-weight: bold;'>2021 - 2024</span>", unsafe_allow_html=True)

        texto = ("""<div style='text-align: justify; font-size: 18px;'>
La pandemia de COVID-19 y las medidas de restricción asociadas provocaron una caída en la demanda de petróleo en 2020. Sin embargo, la recuperación económica en 2021 generó un aumento en la demanda, lo que contribuyó al alza del precio del crudo. La guerra en Ucrania a partir de febrero de 2022 generó una gran incertidumbre en el mercado energético global, lo que provocó un aumento significativo en el precio del petróleo y del gas natural.
Las sanciones impuestas a Rusia por parte de la Unión Europea y otros países afectaron el suministro de petróleo y gas natural, lo que también contribuyó al aumento del precio del combustible.<br>
<br>
Así mismo, la depreciación del euro frente al dólar estadounidense encareció las importaciones de petróleo, ya que se cotizan en dólares y la Organización de Países Exportadores de Petróleo (OPEP) y sus aliados acordaron reducir la producción de petróleo para mantener el precio del crudo alto.</div>
    """)
        st.markdown(texto, unsafe_allow_html=True)




    st.write("<span style=' text-align: center;display:block; font-size: 50px; font-weight: bold;'>¡ Predice el precio del combustible en el futuro !</span>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")    

    col1,col2= st.columns([1,1])
    with col1:
        with st.form("my_form"):

            texto = ("""<div style='text-align: justify; font-size: 18px;'>
    Ingrese rango de semanas entre 2 y 5""")

            st.markdown(texto,  unsafe_allow_html=True)
            num_semanas = st.slider("", min_value=2, max_value=5)

            texto = ("""<div style='text-align: justify; font-size: 18px;'>
    Ingrese el precio del gasóleo para la semana actual""")

            st.markdown(texto,  unsafe_allow_html=True) 

            input_usuario_precio_gasoleo_semana_corriente = st.number_input(" ", max_value=5.00,step=0.10, min_value=0.00)




            texto = ("""<div style='text-align: justify; font-size: 18px;'>
    Ingrese el precio de la gasolina para la semana actual""")

            st.markdown(texto,  unsafe_allow_html=True)            
            input_usuario_precio_gasolina_semana_corriente = st.number_input("",min_value = 0.00, max_value=5.00,step=0.10)
   # Every form must have a submit button.

            submitted = st.form_submit_button("Submit")
            if submitted:
                if input_usuario_precio_gasoleo_semana_corriente == 0 and input_usuario_precio_gasolina_semana_corriente == 0:
                    with col2:
                        st.markdown("")

                        st.image("https://c.tenor.com/dZwkAAJEtYwAAAAC/tenor.gif", use_column_width=True)
                    texto = ("""<div style='font-size:24px;font-weight:bold;'>
                               Debe introducir un precio diferente a 0 en algún combustible.""")

                    st.markdown(texto,  unsafe_allow_html=True) 
                else:
                    with col2:
                        funcion_agregado_prediccion(input_usuario_precio_gasoleo_semana_corriente = input_usuario_precio_gasoleo_semana_corriente, input_usuario_precio_gasolina_semana_corriente =        input_usuario_precio_gasolina_semana_corriente , num_semanas=num_semanas)
            else:
                with col2:
                    st.image("https://c.tenor.com/dZwkAAJEtYwAAAAC/tenor.gif", use_column_width=True)

    st.markdown("")
    st.markdown("")
    st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Conoce las métricas de nuestros modelos de series temporales</span>", unsafe_allow_html=True)

    columna_1, columna_2 = st.columns(2)

    with columna_1:
        st.write("<span style='color: cyan; display: block; text-align: center; font-size: 30px; font-weight: bold;'>Gasolina</span>", unsafe_allow_html=True)

    with columna_2:
        st.write("<span style='color: cyan; display: block; text-align: center; font-size: 30px; font-weight: bold;'>Gasóleo</span>", unsafe_allow_html=True)
   
    texto = ("""<div style='display:block; text-align: center; font-size: 25px;'>
                Historial de las diferencias absolutas entre las predicciones
                del modelo y los valores reales durante el entrenamiento""")

    st.markdown(texto,  unsafe_allow_html=True)

    columna_1, columna_2 = st.columns(2)

    with columna_1:
        df_metricas_gasolina = pd.read_csv("./data/df_metricas_gasolina.csv")
        # Historial del mae
        mae = df_metricas_gasolina['mae'].to_list()
        val_mae = df_metricas_gasolina['val_mae'].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(mae))), y=mae, mode='lines', name='Mae')
        val_trace = go.Scatter(x=list(range(len(val_mae))), y=val_mae, mode='lines', name='val_Mae')

        # Diseño del gráfico
        layout = go.Layout(
                        xaxis=dict(title='Época'),
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
        df_metricas_gasoleo = pd.read_csv("./data/df_metricas_gasoleo.csv")
        # Historial de mae
        mae = df_metricas_gasoleo['mae'].to_list()
        val_mae = df_metricas_gasoleo["val_mae"].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(mae))), y=mae, mode='lines', name='Mae')
        val_trace = go.Scatter(x=list(range(len(val_mae))), y=val_mae, mode='lines', name='val_Mae')

        # Diseño del gráfico
        layout = go.Layout(
                        xaxis=dict(title='Época'),
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
                El MAE (Error Absoluto Medio) es la media de las diferencias absolutas entre las predicciones 
                del modelo y los valores reales. Aquí, el MAE en ambos modelos es de 0.01. 
                Esto significa que, en promedio, las predicciones del modelo están desviadas 
                en 0.01 unidades del valor real. 
                Un MAE bajo es una señal positiva de que el modelo está haciendo predicciones precisas.""")

    st.markdown(texto,  unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")
    st.markdown("")

    texto = ("""<div style='display:block; text-align: center; font-size: 25px;'>
                Historial de pérdida durante el entrenamiento""")

    st.markdown(texto,  unsafe_allow_html=True)

    columna_1, columna_2 = st.columns(2)

    with columna_1:
        df_metricas_gasolina = pd.read_csv("./data/df_metricas_gasolina.csv")
        # Historial de pérdida
        loss = df_metricas_gasolina['loss'].to_list()
        val_loss = df_metricas_gasolina["val_loss"].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(loss))), y=loss, mode='lines', name='Pérdida')
        val_trace = go.Scatter(x=list(range(len(val_loss))), y=val_loss, mode='lines', name='Pérdida Valdación')

        # Diseño del gráfico
        layout = go.Layout(
                        xaxis=dict(title='Época'),
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
        df_metricas_gasoleo = pd.read_csv("./data/df_metricas_gasoleo.csv")
        # Historial de pérdida
        loss = df_metricas_gasoleo['loss'].to_list()
        val_loss = df_metricas_gasoleo['val_loss'].to_list()

        # Crear traza
        trace = go.Scatter(x=list(range(len(loss))), y=loss, mode='lines', name='Pérdida')
        val_trace = go.Scatter(x=list(range(len(val_loss))), y=val_loss, mode='lines', name='Pérdida Valdación')

        # Diseño del gráfico
        layout = go.Layout(
                            xaxis=dict(title='Época'),
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
                La pérdida (loss) es una medida del error de predicción del modelo. 
                En ambos modelos, es de 3.3043e-04, lo que indica que el modelo tiene una pérdida 
                ínfima durante el entrenamiento. Una pérdida baja es indicativa de que el modelo está 
                haciendo buenas predicciones en comparación con los valores reales.""")

    st.markdown(texto,  unsafe_allow_html=True)

