import streamlit as st
import pandas as pd

st.header('My Flight Data App')

# Load the data
df = pd.read_csv('flights.csv')

# Display the data
st.write(df)

# Get the unique carriers
st.title('Flight Data Analysis')
carriers = df['Carrier'].unique()

# Create a dropdown in the sidebar for the user to select a carrier
selected_carrier = st.sidebar.selectbox('Select a carrier', carriers)

# Create a dropdown in the sidebar for the user to select a carrier
selected_carrier = st.sidebar.selectbox('Select a carrier', carriers, key='carrier_select')

# Filter the data based on the selected carrier
filtered_data = df[df['Carrier'] == selected_carrier]

# Display the filtered data
st.write(filtered_data)

# Count the number of flights for each carrier
carrier_counts = df['Carrier'].value_counts()

# Create a bar chart
st.title('Number of Flights by Carrier')
st.bar_chart(carrier_counts)
