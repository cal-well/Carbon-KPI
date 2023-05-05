import streamlit as st
import leafmap.kepler as leafmap
import plotly.express as px
import pandas as pd


# Funtions to Load the data
@st.cache_data
def load_Housing_data():
    in_csv = 'Data/Housing Data.csv'
    config = 'Data/config.json'
    return in_csv, config
in_csv, config = load_Housing_data()


@st.cache_data
def load_NTC_data():
    BEIS_csv = pd.read_csv('Data/LA_Emissions.csv')
    BEIS_csv = pd.melt(BEIS_csv, id_vars='Calendar Year', value_vars=['Grand Total',
                              'Agriculture Total',
                              'Transport Total',
                              'Domestic Total',
                              'Industry Total',
                              'Public Sector Total',
                              'Commercial Total'])
    return BEIS_csv

# Function to create the cached map object
@st.cache_resource
def create_housing_map(in_csv, config):
    m = leafmap.Map(width =1000)
    m.add_csv(in_csv, layer_name="Housing Data", config=config)
    return m
m = create_housing_map(in_csv, config)

# Define function to create the line chart
@st.cache_data
def line_chart(data, selected_lines):
    filtered_data = data[data['variable'].isin(selected_lines)]
    fig = px.line(filtered_data, x='Calendar Year', y='value', color='variable')
    fig.update_yaxes(title_text='Emissions (TCO2e)')  # Rename y-axis
    st.plotly_chart(fig, use_container_width=True)

# Define function to create the North Tyneside page
def north_tyneside():
    st.header("Borough Emissions")
    data = load_NTC_data()
    line_names = data['variable'].unique().tolist()
    selected_lines = st.multiselect('Select Emissions Sector:', line_names, default=line_names)
    line_chart(data, selected_lines)

# Define function to create the Housing page
def housing():
    st.header("Housing")
    st.write("Map of Housing Data:")
    m.to_streamlit()

# Define function to create the Waste page
def waste():
    st.header("Waste")
    st.write("Content for the Waste page goes here")

# Define function to create the Transport page
def transport():
    st.header("Transport")
    st.write("Content for the Transport page goes here")

# Define function to create the Natural Environment page
def natural_environment():
    st.header("Natural Environment")
    st.write("Content for the Natural Environment page goes here")

# Define the navigation bar
st.sidebar.title("Navigation")
tabs = ["North Tyneside", "Housing", "Waste", "Transport", "Natural Environment"]
page_choice = st.sidebar.radio("Select a page", tabs)

# Display the selected page
if page_choice == "North Tyneside":
    north_tyneside()
elif page_choice == "Housing":
    housing()
elif page_choice == "Waste":
    waste()
elif page_choice == "Transport":
    transport()
elif page_choice == "Natural Environment":
    natural_environment()