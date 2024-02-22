import streamlit as st

# Español
from Paginas.EcoEstudio import *
from Paginas.EcoHistorico import *
from Paginas.EcoViaje import *
#from funciones import FuncionesEcoMovilidad

# Ingles
from Paginas.EcoTravel import *
from Paginas.EcoStudy import *
from Paginas.EcoHistorical import *





def pagina_EcoMovilidad():
    #Barra lateral con un selectbox para que selecciones si ver el proyecto o el portfolio
    st.sidebar.markdown("<h2>Aqui podrás encontrar:</h2>" , unsafe_allow_html=True)
    #Seleccion del sidebar
    seleccion_pestaña = st.sidebar.radio(label = " ", options = ["EcoEstudio","EcoHistórico","EcoViaje"])

    
    if seleccion_pestaña == "EcoEstudio":
        EcoEstudio()
    elif seleccion_pestaña == "EcoHistórico":
        pagina_historico()
    elif seleccion_pestaña == "EcoViaje":
        pagina_ecoviaje()
    
def pagina_EcoMovilidadIngles():
    #Barra lateral con un selectbox para que selecciones si ver el proyecto o el portfolio
    st.sidebar.markdown("<h2>Here you can find:</h2>" , unsafe_allow_html=True)
    #Seleccion del sidebar
    seleccion_pestaña = st.sidebar.radio(label = " ", options = ["EcoStudy","EcoHistorical","EcoTravel"])

    
    if seleccion_pestaña == "EcoStudy":
        EcoStudy()
    elif seleccion_pestaña == "EcoHistorical":
        pagina_historico_ingles()
    elif seleccion_pestaña == "EcoTravel":
        pagina_ecoviaje_ingles()






       
            
           
           
            

                                        























