import streamlit as st
from funciones.funciones_ecoencuesta_ingles import mostrar_encuesta_ingles
from time import sleep
from streamlit_extras.let_it_rain import rain


def pagina_ecoencuesta_ingles():

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
        st.write("""<p style='font-size: 50px;'><strong> How can you take care of the planet? </p>""", unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")


        st.write(""" <p style='font-size: 30px; color:cyan; font-weight: bold;'> 
                Discover your level of environmental awareness! Take our brief survey on basic knowledge 
                to contribute to environmental sustainability. 
                🌿 Begin your journey towards a greener future! 🌿</p>""", unsafe_allow_html=True)

    st.write("""<p style='display:block; text-align:center;font-size: 50px;'><strong> Environmental Awareness Survey</p>""", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")

    with st.form("Survey"):

        respuestas_correctas = mostrar_encuesta_ingles()

        c1, c2, c3 = st.columns([0.9, 1.1, 1])

        with c2:
            st.markdown("")
            if st.form_submit_button("Results", use_container_width=True):

                st.write(f"""<p style='font-size: 30px; color:cyan; font-weight: bold;'>You have obtained {respuestas_correctas*2} points out of 10</p>""", unsafe_allow_html=True)

                if respuestas_correctas == 5:
                    st.success("Congratulations!")
                    st.balloons()
                    st.balloons()
                    st.balloons()
                elif respuestas_correctas < 4:
                    st.error("¡You need to improve your environmental awareness.!")
                    contador = 0
                    while contador < 5:
                        bombardeo()
                        bombardeo()
                        contador += 1

                # Mostrar respuestas correctas
                st.write("Correct answers:")
                st.write("1. Which of these is a greenhouse gas? Answer: Carbon dioxide")
                st.write("2. What is the main cause of global warming? Answer: Greenhouse gas emissions")
                st.write("3. Which of the following is not a renewable resource? Answer: Oil")
                st.write("4. What is the main objective of recycling? Answer: To conserve natural resources")
                st.write("5. Which of the following actions helps reduce carbon footprint? Answer: Using public transportation")       
        st.markdown("")
    
    columna1, columna2 = st.columns(2)

    with columna1:
        st.video("https://www.youtube.com/watch?v=Sb-_VAd4RJo")

    with columna2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        
        st.image("https://media.realinstitutoelcano.org/wp-content/uploads/2016/05/ari36-2016-perez-ods-onu-1.jpg", caption="Agenda 2030 de Desarrollo Sostenible", use_column_width=True) 
