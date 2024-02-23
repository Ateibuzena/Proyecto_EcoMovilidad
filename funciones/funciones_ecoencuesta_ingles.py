import streamlit as st

def mostrar_encuesta_ingles():

    
    # Centrar la encuesta
    c1, c2, c3 = st.columns([0.9, 1.1, 1])

    # Preguntas de la encuesta
    with c2:
        st.write("")
    
      # Inicializar variable para contar respuestas correctas
        respuestas_correctas = 0

    # Pregunta 1: ¿Cuál de estos es un gas de efecto invernadero?
        st.markdown("Which of these is a greenhouse gas?")
        gases_efecto_invernadero = st.radio("",
                                        ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"])
    
        if gases_efecto_invernadero == "Carbon dioxide":
            respuestas_correctas += 1

    # Pregunta 2: ¿Cuál es la causa principal del calentamiento global?
        st.markdown("What is the main cause of global warming?")
        causa_calentamiento_global = st.radio("",
                                          ["Water pollution", "Deforestation", "Greenhouse gas emissions",
                                           "Soil pollution"])
        if causa_calentamiento_global == "Greenhouse gas emissions":
            respuestas_correctas += 1

    # Pregunta 3: ¿Cuál de los siguientes no es un recurso renovable?
        st.markdown("Which of the following is not a renewable resource?")
        recursos_renovables = st.radio("",
                                   ["Solar energy", "Oil", "Wind", "Water"])
        if recursos_renovables == "Oil":
            respuestas_correctas += 1
        
    # Pregunta 4: ¿Cuál es el objetivo principal del reciclaje?
        st.markdown("What is the main objective of recycling?")
        objetivo_reciclaje = st.radio("",
                                  ["Reducing waste", "Generating income", "Conserving natural resources", "Creating jobs"])
        if objetivo_reciclaje == "Conserving natural resources":
            respuestas_correctas += 1
        
    # Pregunta 5: ¿Cuál de las siguientes acciones ayuda a reducir la huella de carbono?
        st.markdown("Which of the following actions helps reduce carbon footprint?")
        reducir_huella_carbono = st.radio("",
                                      ["Using public transportation", "Buying individually packaged products",
"Wasting food", "Using electricity from non-renewable sources"])
        if reducir_huella_carbono == "Using public transportation":
            respuestas_correctas += 1

            
    return respuestas_correctas


            
            
            

        
 