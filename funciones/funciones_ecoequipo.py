import streamlit as st
from PIL import Image

def presentacion():

    st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>¡Bienvenidos al equipo!</span>", unsafe_allow_html=True)
    st.write("")
    st.write("<p style='text-align: justify; font-size: 18px;'>Nos emociona presentarles al increíble equipo detrás de nuestro proyecto de investigación automotriz. Cada miembro aporta su pasión por los automóviles y su experiencia única, creando un equipo diverso y comprometido. En esta sección, podrás conocer a cada uno de nosotros individualmente. ¡Desplázate hacia abajo para conocer a cada miembro del equipo y descubrir qué nos inspira a trabajar juntos en este emocionante proyecto!</p>", unsafe_allow_html=True)

def presentacion_ingles():

    st.write("<span style='display: block; text-align: center; font-size: 50px; font-weight: bold;'>Welcome to the team!</span>", unsafe_allow_html=True)
    st.write("")
    st.write("<p style='text-align: justify; font-size: 18px;'>We are thrilled to introduce you to the incredible team behind our automotive research project. Each member brings their passion for automobiles and unique expertise, creating a diverse and dedicated team. In this section, you'll get to know each of us individually. Scroll down to meet each team member and discover what inspires us to work together on this exciting project!</p>", unsafe_allow_html=True)


def cabecera_maria():

    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
       
        foto_maria = Image.open(r"./images/foto_maria.png")
        st.image(foto_maria, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>María Gómez</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Especialista en Data Science y resolución de problemas complejos mediante análisis de datos a gran escala. Utilizo técnicas avanzadas para extraer información significativa y tomar decisiones estratégicas basadas en datos precisos. Dirijo proyectos con Python para crear modelos avanzados que optimizan análisis y toma de decisiones, incluyendo IA y análisis predictivo.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: mariagomezr96@gmail.com""")


    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
            # Botón de descarga
            st.download_button(use_container_width=True,
                            label="Descargar CV",
                            data=open(r"./images/cv_maria.pdf", "rb").read(),
                            file_name="maria_cv.pdf",
                            key="descargar_cv_maria")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.link_button()

            st.link_button(
                            label = "GitHub",
                            url = "https://github.com/mariagomez96-stack")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(
                            label = "Linkedln",
                            url = "https://www.linkedin.com/in/mariagomezroman/")
            

def cabecera_maria_ingles():

    
    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
       
        foto_maria = Image.open(r"./images/foto_maria.png")
        st.image(foto_maria, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>María Gómez</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Data Science specialist and complex problem solver through large-scale data analysis. I employ advanced techniques to extract meaningful insights and make strategic decisions based on accurate data. I lead projects using Python to develop advanced models that enhance analysis and decision-making, including AI and predictive analytics.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: mariagomezr96@gmail.com""")


    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
            # Botón de descarga
            st.download_button(use_container_width=True,
                            label="Download CV",
                            data=open(r"./images/cv_maria.pdf", "rb").read(),
                            file_name="maria_cv.pdf",
                            key="descargar_cv_maria")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            
            st.link_button(
                        label = "GitHub",
                        url = "https://github.com/mariagomez96-stack")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(label = "Linkedln",
                        
                        url = "https://www.linkedin.com/in/mariagomezroman/")

def cabecera_kevin():

        
    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_kevin = Image.open(r"./images/foto_kevin.png")
        st.image(foto_kevin, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Kevin Espinoza</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Un apasionado de los datos con formación en Data Science y experiencia en delineación. Me dedico a resolver problemas complejos y generar valor aplicando técnicas avanzadas de análisis de datos. Me gradué en Data Science & IA en HACK A BOSS, adquiriendo habilidades en estadística, analítica, ETL, SQL y Python.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: kevinalexisespinoza@gmail.com""")


    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
            # Botón de descarga
            st.download_button(use_container_width=True,
                        label="Descargar CV",
                        data=open(r"./images/CV_Kevin_Espinoza.pdf", "rb").read(),
                        file_name="kevin_cv.pdf",
                        key="descargar_cv_kevin")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            
            st.link_button(
                    label = "GitHub",
                    url = "https://github.com/KevinAlexisEsp")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(label = "Linkedln",
                    
                            url = "https://www.linkedin.com/in/kevin-alexis-espinoza/")


def cabecera_kevin_ingles():

    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_kevin = Image.open(r"./images/foto_kevin.png")
        st.image(foto_kevin, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Kevin Espinoza</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>A data enthusiast with a background in Data Science and experience in drafting. I am dedicated to solving complex problems and creating value by applying advanced data analysis techniques. I graduated in Data Science & AI at HACK A BOSS, acquiring skills in statistics, analytics, ETL, SQL, and Python.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: kevinalexisespinoza@gmail.com""")


    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
            # Botón de descarga
            st.download_button(use_container_width=True,
                        label="Download CV",
                        data=open(r"./images/CV_Kevin_Espinoza.pdf", "rb").read(),
                        file_name="kevin_cv.pdf",
                        key="descargar_cv_kevin")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            
            st.link_button(
                    label = "GitHub",
                    url = "https://github.com/KevinAlexisEsp")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(label = "Linkedln",
                    
                    url = "https://www.linkedin.com/in/kevin-alexis-espinoza/")


def cabecera_lorena():

    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_lorena = Image.open(r"./images/foto_lorena.png")
        st.image(foto_lorena, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Lorena Martínez</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Graduada en Administración y Dirección de Empresas y Economía, con un Máster en Gestión y Dirección de Empresas Turísticas. Actualmente, trabajo en el transporte de mercancías por carretera, donde he aprendido la adaptabilidad y la resiliencia. Me estoy especializando en Data Science e IA para impulsar mi carrera. Mis habilidades incluyen trabajo en equipo, cumplimiento de objetivos y atención a los detalles.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: lorena.aljorra1994@gmail.com""")


    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")

            st.download_button(use_container_width=True,
                        label="Descargar CV",
                        data = open(r"./images/cv_lorena.pdf", "rb").read(),
                        file_name="lorena_cv.pdf",
                        key="descargar_cv_lorena")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(
                        label = "GitHub",
                        url = "https://github.com/LorenaMtnez94")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

        
            st.link_button(label = "Linkedln",
                        
                        url = "https://www.linkedin.com/in/lorenamtnez/")


def cabecera_lorena_ingles():

    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_lorena = Image.open(r"./images/foto_lorena.png")
        st.image(foto_lorena, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Lorena Martínez</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Graduated in Business Administration and Economics, with a Master's in Management and Direction of Tourist Enterprises. Currently, I work in road freight transportation, where I have learned adaptability and resilience. I am specializing in Data Science and AI to boost my career. My skills include teamwork, goal achievement, and attention to detail.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: lorena.aljorra1994@gmail.com""")


    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")

            st.download_button(use_container_width=True,
                        label="Download CV",
                        data = open(r"./images/cv_lorena.pdf", "rb").read(),
                        file_name="lorena_cv.pdf",
                        key="descargar_cv_lorena")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(
                        label = "GitHub",
                        url = "https://github.com/LorenaMtnez94")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

        
            st.link_button(label = "Linkedln",
                        
                        url = "https://www.linkedin.com/in/lorenamtnez/")


def cabecera_dani():

    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_dani = Image.open(r"./images/foto_dani.png")
        st.image(foto_dani, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Daniel Villa</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Especialista Data Scientist donde destaco en Python, Web scraping, SQL y Machine Learning. Además, poseo competencias en programación en C++ y Java, así como experiencia en Arduino y microcontroladores PIC. Destaco por haber desarrollado un cargador para coches eléctricos con diversas funciones y tipos de carga. Me considero una persona responsable y trabajadora, capaz de contribuir al éxito de proyectos empresariales.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: danielvillarayo@gmail.com""")

    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
        # Botón de descarga
            st.download_button(use_container_width=True,
                            label="Descargar CV",
                            data=open(r"./images/cv_dani.pdf", "rb").read(),
                            file_name="dani_cv.pdf",
                            key="descargar_cv_dani")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(
                        label = "GitHub",
                        url = "https://github.com/Malosy26")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(label = "Linkedln",
                        
                        url = "https://www.linkedin.com/in/dvr0001/")


def cabecera_dani_ingles():

    
    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_dani = Image.open(r"./images/foto_dani.png")
        st.image(foto_dani, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Daniel Villa</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Data Scientist specialist with expertise in Python, web scraping, SQL, and Machine Learning. Additionally, I have skills in programming in C++ and Java, as well as experience with Arduino and PIC microcontrollers. I stand out for having developed a charger for electric cars with various functions and types of charging. I consider myself a responsible and hardworking individual capable of contributing to the success of business projects.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: danielvillarayo@gmail.com""")

    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
        # Botón de descarga
            st.download_button(use_container_width=True,
                            label="Download CV",
                            data=open(r"./images/cv_dani.pdf", "rb").read(),
                            file_name="dani_cv.pdf",
                            key="descargar_cv_dani")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(
                        label = "GitHub",
                        url =  "https://github.com/Malosy26")
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(label = "Linkedln",
                        
                        url = "https://www.linkedin.com/in/dvr0001/")



def cabecera_ana():

    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_ana = Image.open(r"./images/foto_ana.png")
        st.image(foto_ana, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Ana Zubieta</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Data Scientist con experiencia en el desarrollo de soluciones basadas en análisis para organizaciones de diversos sectores. Experta en modelado predictivo, procesamiento y minería de datos, así como en lenguaje Python. Capaz de liderar proyectos de análisis complejos, desde la recopilación de datos hasta la implementación de soluciones.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: ena.ateibuz@gmail.com""")

    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
        # Botón de descarga
            st.download_button(use_container_width=True,
                        label="Descargar CV",
                        data=open(r"./images/cv_ana.pdf", "rb").read(),
                        file_name="cv_ana.pdf",
                        key="descargar_cv_ana") 
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(
                    label = "GitHub",
                    url = "https://github.com/Ateibuzena")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(label = "Linkedln",
                    
                    url = "www.linkedin.com/in/ana-zubieta")

def cabecera_ana_ingles():

    columna_1, columna_2, columna_3 = st.columns([1.5, 2, 1])

    with columna_1:
        st.markdown("")
        st.markdown("")
    
        foto_ana = Image.open(r"./images/foto_ana.png")
        st.image(foto_ana, width=300)

    with columna_2:
        st.write("<span style='display: block; text-align: justify; font-size: 30px; font-weight: bold;'>Ana Zubieta</span>", unsafe_allow_html=True)

        st.markdown("<span style='color: cyan; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Data Scientist</span>", unsafe_allow_html=True)

        st.write("<p style='text-align: justify; font-size: 18px;'>Data Scientist with experience in developing analysis-based solutions for organizations across various sectors. Expert in predictive modeling, data processing, and mining, as well as proficient in Python language. Capable of leading complex analysis projects, from data collection to solution implementation.</p>", unsafe_allow_html=True)

        st.write("")
        st.markdown("""##### :email: ena.ateibuz@gmail.com""")

    with columna_3:
        c_1, c_2 = st.columns(2)

        with c_2:
            st.markdown("")
            st.markdown("")
        # Botón de descarga
            st.download_button(use_container_width=True,
                        label="Download CV",
                        data=open(r"./images/cv_ana.pdf", "rb").read(),
                        file_name="cv_ana.pdf",
                        key="descargar_cv_ana") 
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(
                    label = "GitHub",
                    url = "https://github.com/Ateibuzena")
            
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown("")

            st.link_button(label = "Linkedln",
                    
                    url = "www.linkedin.com/in/ana-zubieta")
