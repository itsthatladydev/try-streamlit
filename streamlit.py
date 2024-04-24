import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Add a title to the top of the app
st.header('My Flight Data Analysis App ✈️')

# Load the data
df = pd.read_csv('flights.csv')

# Display the data
st.title('Flight Data Exploration')
st.write(df)

# Display summary statistics
st.subheader('Summary Statistics')
st.write(df.describe())

# Create a histogram of flight delays
st.subheader('Histogram of Flight Delays')
df['DepDelay'].hist(bins=20)
plt.xlabel('Delay (min)')
plt.ylabel('Flights')
st.pyplot(plt)

# Create a bar chart of flights per carrier
st.subheader('Number of Flights per Carrier')
df['Carrier'].value_counts().plot(kind='bar')
plt.xlabel('Carrier')
plt.ylabel('Number of Flights')
st.pyplot(plt)

# Create a boxplot of delays per carrier
st.subheader('Boxplot of Delays per Carrier')
plt.figure(figsize=(12, 6))
sns.boxplot(x='Carrier', y='ArrDelay', data=df)
plt.xlabel('Carrier')
plt.ylabel('Arrival Delay (min)')
st.pyplot(plt)

# Select a carrier
carrier = st.selectbox('Select a carrier:', df['Carrier'].unique())

# Filter data based on the selected carrier
filtered_data = df[df['Carrier'] == carrier]

# Display the filtered data
st.write(filtered_data)