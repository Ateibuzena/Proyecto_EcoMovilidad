import streamlit as st

from funciones.funciones_ecoequipo import *
from streamlit_extras.colored_header import colored_header

def linea():
        colored_header(
            label="",
            description="",
            color_name="light-blue-70",
        )


def pagina_portfolio():
    presentacion()
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    cabecera_maria() 
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_kevin()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_ana()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_dani()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_lorena()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_cristian()
    



def pagina_portfolio_ingles():

    presentacion_ingles()
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    cabecera_maria_ingles() 
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_kevin_ingles()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_ana_ingles()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_dani_ingles()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_lorena_ingles()
    st.write(" ")
    linea()
    st.write(" ")
    cabecera_cristian_ingles()
