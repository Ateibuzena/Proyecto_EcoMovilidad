import streamlit as st 
import plotly.graph_objects as go

def paginaprincipal_ingles():

    # CENTERED TITLE
    st.write("<span style=' text-align: center;display:block; font-size: 50px; font-weight: bold;'>Make your journey easier!</span>", unsafe_allow_html=True)

    # TO ADD A BLANK SPACE
    st.markdown(" ")

    st.write("""
         
    
       <p style='text-align:center;font-size: 18px'><strong>Have you ever wondered how much your trip will cost based on the car model you choose and the distance you're going to travel?</p> 
       
        <p style='text-align:center;font-size: 18px'><strong>You're in the right place!</p>""", unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown(" ")

    col1, col2, col3 = st.columns([1,0.05,1])

    with col1:
        text = """<div style=' text-align: justify; font-size: 18px;'>
                    This website is a data science project focused on the fuel and electricity consumption of vehicles, including electric, hybrid, and combustion engines.<br>
                    <br>
                    Our goal is to provide users with an easy-to-use and accurate tool to compare different types of vehicles based on their main characteristics and estimate the costs associated with their consumption per trip, so that the user can decide which vehicle they need.
                    We understand that transportation expenses can vary significantly depending on the vehicle model, the type of fuel used, or if it is an electric vehicle.
                    Therefore, we are committed to offering a versatile solution that adapts to various needs and circumstances.<br>
                    <br>
                    Through different data sources, we build our own record of vehicles and their characteristics, in addition to the evolution of fuel prices and the different electric charging points in Spain.<br>
                    <br>
                    Start exploring our page and plan your next trip with us.
                    </div>"""

        st.markdown(text, unsafe_allow_html=True)

    with col3:
        st.image("https://www.vinccihoteles.com/blog/wp-content/uploads/2023/09/disposicion-articulos-viaje-angulo-alto.jpg", caption="", use_column_width=True)
    st.markdown(" ")
    st.markdown(" ")

    col1, col2, col3 = st.columns([1,0.05,1])

    with col3:
        st.markdown(" ")
        st.markdown(" ")
        st.write(""" 
        <p style='text-align:center; font-size: 30px;color:cyan;'><strong>Discover how your choice of transportation can make a difference</p>""", unsafe_allow_html=True) 
        st.markdown(" ")

        text = """<div style=' text-align: justify; font-size: 18px;'>
                    Over the past decade, we have witnessed a steady increase in CO2 emissions, driven by economic growth and our dependence on fossil fuels.
                    Despite advances in clean technologies, the challenge of climate change remains urgent and requires immediate action.<br>
                    <br> That's why we offer a detailed analysis of different vehicles so that you can understand which ones are more "eco-responsible".<br>
                    </div>"""

        st.markdown(text, unsafe_allow_html=True)

        st.markdown(" ")

        st.write("""<p style='text-align:center;font-size: 25px;color:cyan;'><strong>Join our community committed to a cleaner and more sustainable future.</p>""", unsafe_allow_html=True)

    with col1:
        emissions = {"2010":350, "2011":350, "2012":350, "2013":325, "2014":325, "2015":340, "2016":330, "2017":340, "2018":340, "2019":300, "2020":275, "2021":300, "2022":300, "2023":275}

        categories = list(emissions.keys())
        values = list(emissions.values())

        fig = go.Figure(data=[go.Bar(x=categories, y=values)])

        fig.update_layout(  
             xaxis=dict(title=''),
             yaxis=dict(title='CO2 Emissions Mt')
        )

        st.plotly_chart(fig, use_container_width=True)

        for i in range(1,3):
            st.markdown(" ")

    st.write("""<p style='text-align:center;font-size: 30px;'><strong>Explore our website and start traveling consciously today!</p>""", unsafe_allow_html=True)

    for i in range(1,7):
        st.markdown(" ")

    col1, col2, col3 = st.columns([1,0.05,1])

    with col1:

        for i in range(1,1):
            st.markdown(" ")

        st.write("""<p style='text-align:center;font-size: 25px;color:cyan;'><strong>EcoTravel</p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>In EcoMobility section, you will find the EcoTravel tab where you can choose from different vehicles in our database, whether electric, hybrid, or combustion, to make a comparison between them. Additionally, with our trip planner, you can see the distribution of electric chargers and gas stations in Spain, which includes a trip cost calculator so you can decide what type of vehicle you need.</p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan;'><strong>EcoStudy</p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>In EcoMobility section, you will find the EcoStudy tab. There, a complete analysis is carried out of the categories, energy classification, autonomy and battery capacity, consumption, emissions, and motorization of all vehicles in our database.</p>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan;'><strong>EcoQuiz</p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>Do you want to test your level of environmental awareness? In the EcoQuiz tab, we offer you that.</p>""", unsafe_allow_html=True)

    with col3:
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan'><strong> EcoHistorical </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>In EcoMobility section, you will find the EcoHistorical tab. In this tab, we offer the possibility to predict fuel prices in the coming weeks thanks to our time series model. Additionally, we provide an analysis of the historical record of fuel prices per week since 2002 so you can observe its evolution and the reasons behind it.<br> <br>  </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown(" ")
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan'><strong> EcoMeetUs </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>Any information about the members of this project such as CVs, phone numbers, emails, and GitHub and LinkedIn profiles can be found in this section. The entire team is composed of top professionals in Data Science. Visit the section to get to know us!</p>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("""<p style='text-align:center;font-size: 25px; color:cyan;'><strong> EcoFaqs </p>""", unsafe_allow_html=True)
        st.markdown(" ")
        st.write("""<p style='text-align:justify;font-size: 18px'>Do you have questions? You can find a series of frequently asked questions in EcoFaqs section.</p>""", unsafe_allow_html=True)

