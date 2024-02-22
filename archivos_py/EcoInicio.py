import streamlit as st

import plotly.graph_objects as go



def paginaprincipal():

    
    #TITULO CENTRADO
    
    st.write("<span style=' text-align: center;display:block; font-size: 50px; font-weight: bold;'>¡ Hacemos tu viaje más fácil !</span>", unsafe_allow_html=True)
    

    
    #PARA AÑADIR UN ESPACIO EN BLANCO
    
    st.markdown(" ")
    
    st.write("""
         
    
       <p style='text-align:center;font-size: 18px'><strong>  ¿Te has preguntado alguna vez cuánto te costará viajar en función del modelo de coche que elijas y la distancia que vas a recorrer?  </p> 
       
        <p style='text-align:center;font-size: 18px'><strong>   ¡Estás en el lugar correcto! </p>""", unsafe_allow_html=True)
    
    st.markdown(" ")
    st.markdown(" ")
        
    col1, col2, col3 = st.columns([1,0.05,1])
    
    with col1:
        texto = """<div style=' text-align: justify; font-size: 18px;'>
                    Esta página web es un proyecto de ciencia de datos enfocado en el consumo 
                    combustible y electricidad de los vehículos tanto eléctricos, híbridos, como de combustión.<br>
                    <br>
                    Nuestro objetivo es proporcionar a los usuarios una herramienta fácil de usar y precisa con la que comparar
                    distintos tipos de vehículos en función de sus características principales y
                    estimar los costes asociados a su consumo por recorrido para que así el usuario pueda decidir qué vehículo necesita. 
                    Entendemos que los gastos de transporte pueden variar significativamente según el modelo del vehículo, el tipo de combustible utilizado o si se trata de un vehículo eléctrico. 
                    Por lo tanto, nos comprometemos a ofrecer una solución versátil que se adapte a diversas necesidades y circunstancias.<br>
                    <br>
                    A través de diferentes fuentes de datos construimos un registro propio de vehículos y sus características, además de la evolución en el precio del combustible y
                    los diferentes puntos de carga eléctrica en España.<br>
                    <br>
                    Comienza a explorar nuestra página y planifica tu próximo viaje con nosotros.
                    </div>"""
    
        st.markdown(texto, unsafe_allow_html=True)
        
    with col3:
        st.image("https://www.vinccihoteles.com/blog/wp-content/uploads/2023/09/disposicion-articulos-viaje-angulo-alto.jpg", caption="", use_column_width=True)
    st.markdown(" ")
    st.markdown(" ")
        
        # Dividir la página en dos columnas
    col1, col2, col3 = st.columns([1,0.05,1])

    # Contenido de la primera columna
 
      
    with col3:
        st.markdown(" ")
        st.markdown(" ")
        st.write(""" 
        <p style='text-align:center; font-size: 30px;color:cyan;'><strong>Descubre cómo tu elección de transporte puede marcar la diferencia</p>""", unsafe_allow_html=True) 
        st.markdown(" ")

        texto = """<div style=' text-align: justify; font-size: 18px;'>
                    Durante la última década, hemos sido testigos de un crecimiento constante en las emisiones de CO2, 
                    impulsadas por el auge económico y nuestra dependencia de los combustibles fósiles. 
                    A pesar de los avances en tecnologías limpias, el desafío del cambio climático sigue 
                    siendo urgente y requiere acción inmediata.<br>
                    <br> Es por eso que ofrecemos un análisis detallado de los distintos vehículos para que 
                    puedas entender cuáles son más "ecoresponsables".<br>
                    </div>"""
    
        st.markdown(texto, unsafe_allow_html=True)

        st.markdown(" ")

        st.write("""<p style='text-align:center;font-size: 25px;color:cyan;'><strong>Únete a nuestra comunidad comprometida con un futuro más limpio y sostenible.</p>""", unsafe_allow_html=True)
            
    with col1:

            # Define el diccionario con los valores de las emisiones
        emisiones = {"2010":350, "2011":350, "2012":350, "2013":325, "2014":325, "2015":340, "2016":330, "2017":340, "2018":340, "2019":300, "2020":275, "2021":300, "2022":300, "2023":275}


    # Extrae las categorías y los valores del diccionario
        categorias = list(emisiones.keys())
        valores = list(emisiones.values())

    # Crea la figura del gráfico de barras
        fig = go.Figure(data=[go.Bar(x=categorias, y=valores)])

    # Personaliza el diseño del gráfico (opcional)
        fig.update_layout(  
             xaxis=dict(title=''),
             yaxis=dict(title='Emisiones CO2 Mt')
    )

    # Muestra el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)
        
        for i in range(1,3):
                st.markdown(" ")
                

    st.write("""<p style='text-align:center;font-size: 30px;'><strong>¡ Explora nuestra página web y comienza a viajar con conciencia hoy mismo !</p>""", unsafe_allow_html=True)
    
    for i in range(1,7):
        st.markdown(" ")
    
    col1, col2, col3=st.columns([1,0.05,1])
    
    with col1:
        
        for i in range(1,1):
                st.markdown(" ")
                
        st.write("""<p style='text-align:center;font-size: 25px;color:cyan;'><strong> EcoViaje </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'> En el apartado EcoMovilidad, encontrarás la pestaña EcoViaje donde podrás elegir entre distintos vehículos de nuestra base de datos, tanto eléctricos, híbridos o de combustión, para poder hacer una comparativa entre ellos. Además, con nuestro planificador de viajes puedes ver la distribución de los cargadores eléctricos y las gasolineras en España, que incluye un calculador de coste de tu viaje para que puedas decidir qué tipo de vehículo es el que necesitas.   </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan;'><strong> EcoEstudio </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'> En el apartado EcoMovilidad, encontrarás la pestaña EcoEstudio. Allí, se realiza un análisis completo de las categorías, clasificación energética, autonomía y capacidad de la batería, consumo, emisiones y motorización de todos los vehículos de nuestra base de datos.   </p>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan;'><strong>EcoEncuesta</p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>¿Quieres poner a prueba tu nivel de concienciación ambiental? En la pestaña EcoEncuesta te ofrecemos esa</p>""", unsafe_allow_html=True)
        
    
    with col3:
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan'><strong> EcoHistórico </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>En el apartado EcoMovilidad encontrarás la pestaña EcoHistórico. En esta pestaña, ofrecemos la posibilidad de predecir el precio del combustible en las siguientes semanas gracias a nuestro modelo de series temporales. Además de un análisis del registro histórico del precio del combustible por semanas desde el 2002 para que puedas observar su evolución y el por qué de la misma.<br> <br>  </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan'><strong> EcoEquipo </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'> Cualquier información de los miembros de este proyecto tales como currículum vitae, teléfono, email y perfiles de GitHub y LinkedIn lo puedes encontrar en este apartado. Todo el equipo está formado con los mejores profesionales en Ciencia de Datos. ¡Visita el apartado para conocernos!</p>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan;'><strong> EcoFaqs </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>¿Tienes preguntas? Podrás encontrar una serie de preguntas frecuentes en la parte de EcoFaqs.</p>""", unsafe_allow_html=True)
