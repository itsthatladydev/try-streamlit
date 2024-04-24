import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('flights.csv')
    return df

df = load_data()

# Title of the app
st.title('Flight Data Explorer')

# Add a sidebar
st.sidebar.header('User Input Features')

# Function to filter data
def user_input_features():
    carrier = st.sidebar.selectbox('Carrier', df['Carrier'].unique())
    origin = st.sidebar.selectbox('Origin Airport', df['OriginAirportName'].unique())
    dest = st.sidebar.selectbox('Destination Airport', df['DestAirportName'].unique())
    return carrier, origin, dest

selected_features = user_input_features()

# Filter the data
df_selected = df[(df['Carrier'] == selected_features[0]) & 
                 (df['OriginAirportName'] == selected_features[1]) & 
                 (df['DestAirportName'] == selected_features[2])]

# Show the data
st.header('Display User Input')
st.write('Carrier :', selected_features[0])
st.write('Origin Airport :', selected_features[1])
st.write('Destination Airport :', selected_features[2])
st.header('Data Information')
st.write(df_selected)