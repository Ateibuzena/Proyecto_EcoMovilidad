import streamlit as st

# Español
from archivos_py.EcoMovilidad import * # e ingles
from archivos_py.EcoInicio import *
from archivos_py.EcoEquipo import *
from archivos_py.EcoFaqs import *
from archivos_py.EcoEncuesta import *

# Inglés
from archivos_py.EcoHome import *
from archivos_py.EcoFaqs_English import *
from archivos_py.EcoQuiz import *


st.set_page_config(layout = "wide")

def main():

    def crowfunding():
        import webbrowser

        browser = webbrowser.get()
        browser.open("https://www.buymeacoffee.com/ecoequipoe3")
    

    seleccion_idioma = st.sidebar.toggle("English")

    if seleccion_idioma:

        st.sidebar.markdown("<h2>Select what you want to see:</h2>" , unsafe_allow_html=True)
        #Seleccion del sidebar
        seleccion_pagina = st.sidebar.radio(label = " ", options = ["EcoHome","EcoMovility", "EcoTeam", "EcoFaqs", "EcoQuiz"])

        if seleccion_pagina == "EcoHome":
            paginaprincipal_ingles()
        elif seleccion_pagina == "EcoMovility":
            pagina_EcoMovilidadIngles()
        elif seleccion_pagina == 'EcoTeam':
            pagina_portfolio_ingles()
        elif seleccion_pagina == "EcoFaqs":
            pagina_ecofaqs_ingles()
        elif seleccion_pagina == "EcoQuiz":
            pagina_ecoencuesta_ingles()
        
        st.sidebar.button("Support our project ❤️", on_click=crowfunding)

    else:

    #Barra lateral con un selectbox para que selecciones si ver el proyecto o el portfolio
        st.sidebar.markdown("<h2>Selecciona qué desea ver:</h2>" , unsafe_allow_html=True)


        #Seleccion del sidebar
        seleccion_pagina = st.sidebar.radio(label = " ", options = ["EcoInicio","EcoMovilidad", "EcoEquipo", "EcoFaqs", "EcoEncuesta"])

        if seleccion_pagina == "EcoInicio":
            paginaprincipal()
        elif seleccion_pagina == "EcoMovilidad":
            pagina_EcoMovilidad()
        elif seleccion_pagina == 'EcoEquipo':
            pagina_portfolio()
        elif seleccion_pagina == "EcoFaqs":
            pagina_ecofaqs()
        elif seleccion_pagina == "EcoEncuesta":
            pagina_ecoencuesta()
       
        st.sidebar.button("Apoya nuestro proyecto ❤️", on_click=crowfunding)

if __name__ == "__main__":
    main()

    