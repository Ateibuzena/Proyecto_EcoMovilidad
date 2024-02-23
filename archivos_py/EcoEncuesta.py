import streamlit as st
from funciones.funciones_ecoencuesta import mostrar_encuesta
from time import sleep
from streamlit_extras.let_it_rain import rain

def pagina_ecoencuesta():

    def bombardeo():
        rain(
            emoji="💩",
            font_size=100,
            falling_speed=1,
            animation_length="finite",
        )
        
        # Añadir un video desde una URL de YouTube
    col1, col2=st.columns([0.8, 1])
    with col1:
    #
        colum1, colum2= st.columns([1, 0.2])
        with colum1:
            st.markdown("")
            st.image("https://i.pinimg.com/originals/8e/4d/be/8e4dbe2aecba57d88b8837492699826a.gif")

    st.markdown("<br>", unsafe_allow_html=True)
    with col2:
        st.write("""<p style='font-size: 50px;'><strong> ¿Cómo puedes cuidar el planeta? </p>""", unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")


        st.write(""" <p style='font-size: 30px; color:cyan; font-weight: bold;'> 
                ¡ Descubre tu nivel de conciencia ambiental! Realiza nuestra breve encuesta sobre conocimientos 
                básicos para contribuir a la sostenibilidad del medioambiente.<br>       <br>🌿 ¡ Comienza
                tu viaje hacia un futuro más verde ! 🌿</p>""", unsafe_allow_html=True)

    st.write("""<p style='display:block; text-align:center;font-size: 50px;'><strong> Encuesta sobre cociencia medioambiental</p>""", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")

    with st.form("Encuesta"):

        respuestas_correctas = mostrar_encuesta()

        c1, c2, c3 = st.columns([0.9, 1.1, 1])

        with c2:
            st.markdown("")
            if st.form_submit_button("Ver resultados", use_container_width=True):

                st.write(f"""<p style='font-size: 30px; color:cyan; font-weight: bold;'>Has obtenido {respuestas_correctas*2} puntos sobre 10</p>""", unsafe_allow_html=True)

                if respuestas_correctas == 5:
                    st.success("¡Felicidades! Has acertado todas las respuestas.")
                    for i in range(1, 5):
                        st.balloons()
                        st.balloons()
                        sleep(0.5)
                elif respuestas_correctas < 4:
                    st.error("¡Casi! ¡La próxima vez lo harás mejor!")
                    
                    bombardeo()
                    bombardeo()

                # Mostrar respuestas correctas
                st.write("Respuestas correctas:")
                st.write("1. ¿Cuál de estos es un gas de efecto invernadero? Respuesta: Dióxido de carbono")
                st.write("2. ¿Cuál es la causa principal del calentamiento global? Respuesta: Emisiones de gases de efecto invernadero")
                st.write("3. ¿Cuál de los siguientes no es un recurso renovable? Respuesta: Petróleo")
                st.write("4. ¿Cuál es el objetivo principal del reciclaje? Respuesta: Conservar recursos naturales")
                st.write("5. ¿Cuál de las siguientes acciones ayuda a reducir la huella de carbono? Respuesta: Usar transporte público")       
        st.markdown("")
    
    columna1, columna2 = st.columns(2)

    with columna1:
        st.video("https://www.youtube.com/watch?v=Sb-_VAd4RJo")

    with columna2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        
        st.image("https://media.realinstitutoelcano.org/wp-content/uploads/2016/05/ari36-2016-perez-ods-onu-1.jpg", caption="Agenda 2030 de Desarrollo Sostenible", use_column_width=True) 

