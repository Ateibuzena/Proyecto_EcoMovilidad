import streamlit as st

def mostrar_encuesta():

    
    # Centrar la encuesta
    c1, c2, c3 = st.columns([0.9, 1.1, 1])

    # Preguntas de la encuesta
    with c2:
        st.write("")
    
      # Inicializar variable para contar respuestas correctas
        respuestas_correctas = 0

    # Pregunta 1: ¿Cuál de estos es un gas de efecto invernadero?
        st.markdown("¿Cuál de estos es un gas de efecto invernadero?")
        gases_efecto_invernadero = st.radio("",
                                        ["Oxígeno", "Nitrógeno", "Dióxido de carbono", "Helio"])
    
        if gases_efecto_invernadero == "Dióxido de carbono":
            respuestas_correctas += 1

    # Pregunta 2: ¿Cuál es la causa principal del calentamiento global?
        st.markdown("¿Cuál es la causa principal del calentamiento global?")
        causa_calentamiento_global = st.radio("",
                                          ["Contaminación del agua", "Deforestación", "Emisiones de gases de efecto invernadero",
                                           "Contaminación del suelo"])
        if causa_calentamiento_global == "Emisiones de gases de efecto invernadero":
            respuestas_correctas += 1

    # Pregunta 3: ¿Cuál de los siguientes no es un recurso renovable?
        st.markdown("¿Cuál de los siguientes no es un recurso renovable?")
        recursos_renovables = st.radio("",
                                   ["Energía solar", "Petróleo", "Viento", "Agua"])
        if recursos_renovables == "Petróleo":
            respuestas_correctas += 1
        
    # Pregunta 4: ¿Cuál es el objetivo principal del reciclaje?
        st.markdown("¿Cuál es el objetivo principal del reciclaje?")
        objetivo_reciclaje = st.radio("",
                                  ["Reducir la basura", "Generar ingresos", "Conservar recursos naturales", "Crear empleo"])
        if objetivo_reciclaje == "Conservar recursos naturales":
            respuestas_correctas += 1
        
    # Pregunta 5: ¿Cuál de las siguientes acciones ayuda a reducir la huella de carbono?
        st.markdown("¿Cuál de las siguientes acciones ayuda a reducir la huella de carbono?")
        reducir_huella_carbono = st.radio("",
                                      ["Usar transporte público", "Comprar productos envasados individualmente",
                                      "Desperdiciar alimentos", "Utilizar energía eléctrica de fuentes no renovables"])
        if reducir_huella_carbono == "Usar transporte público":
            respuestas_correctas += 1

            
    return respuestas_correctas


            
            
            

        
 