import streamlit as st
import pandas as pd

import plotly.express as px

def pagina_ecofaqs_ingles():
    st.write("<p style='display:block;text-align:center;font-size: 50px;'><strong>Frequently Asked Questions</strong></p>", unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")
    col1, col2, col3 = st.columns([0.8, 1.4, 0.8])

    with col2:
        df_coches= pd.read_csv("./Data/df_coches_escrapeo_ingles.csv")
        
        with st.expander("**How does the page calculate the cost of the trip?**"):
            st.write("We use the distance of the trip and the fuel or energy consumption of your vehicle, along with the current prices of gasoline, diesel, or kWh, to calculate the estimated cost of the trip by predicting these prices. In case the current price is unknown, the current average price will be used.")
            st.markdown("")
            
            
            
            
        with st.expander("**Currently, are there more electric vehicles or fuel vehicles?**"):
            st.write("In Spain, the adoption of electric vehicles has been increasing in recent years, although they still represent a small portion of the total vehicles in circulation. However, conventional fuel vehicles remain predominant in Spain, with a large majority of vehicles powered by gasoline and diesel on the country's roads.")
                
            fig = px.bar(
            x=df_coches["Engine Type"].value_counts().index,  
            y=df_coches["Engine Type"].value_counts(),  
            labels={'y': '', 'x': ''},  
            title=''
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("")
            
        with st.expander("**How do I find the fuel or energy consumption per kilometer of my vehicle?**"):
            st.write("You can find it in your vehicle's manual.")
            st.markdown("")

        with st.expander("**Do the calculations take into account other factors such as traffic or vehicle efficiency?**"):
            st.write("The calculations obtained are estimates based on the average fuel or energy consumption of your vehicle and price predictions based on current fuel or electricity prices. Additionally, they take into account other factors or vehicle characteristics such as vehicle range or battery capacity, but do not consider any external factors such as traffic or weather conditions.")
            st.markdown("")
            
            
        with st.expander("**What data do I need to provide to get an accurate calculation of the trip cost?**"):
            st.write("You will need to enter the total distance of the trip, the vehicle model used (electric, fuel, or hybrid), the fuel or energy consumption per kilometer of your vehicle, and the current prices of gasoline, diesel, or kWh in order to predict the cost of the next trip.")
            st.markdown("")

        with st.expander("**Are the calculations valid for both long and short trips?**"):
            st.write("Our tool allows calculating the trip cost within the entire national territory, so it serves for both long and short trips.")
            st.markdown("")
                
        with st.expander("**Regarding emissions, which type of vehicle pollutes more?**"):
            st.write("Electric cars are zero emissions, meaning they do not pollute. As for gasoline, diesel, or hybrid vehicles, they are very similar in terms of emissions.")   
            fig = px.pie(data_frame = df_coches,
                    values=df_coches.groupby("Engine Type")["Maximum Emissions"].mean().to_list(),
                    names = df_coches.groupby("Engine Type")["Maximum Emissions"].mean().index)
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("")
            
            
        with st.expander("**Is there a relationship between fuel consumption and vehicle pollution?**"):
            st.write("Yes. There is a direct relationship between consumption according to the type of fuel and CO2 emissions, so the higher the consumption, the greater the amount of CO2 emissions.")
                
            fig = px.scatter(data_frame =df_coches,
            x = "Maximum Consumption (l/100km)",
            y = "Maximum Emissions",
            color = "Engine Type" ) 
            fig.update_layout(
            legend=dict(
            x=0.7,
            y=1,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderwidth=1
                        )
            )
            st.plotly_chart(fig, use_container_width=True)




