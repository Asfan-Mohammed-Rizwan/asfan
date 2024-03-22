import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a sidebar with user inputs
st.sidebar.title('Input Parameters')
data = pd.DataFrame({'x': range(10), 'y': [i**2 for i in range(10)]})
selected_column = st.sidebar.selectbox('Select a column:', data.columns)

# Filter data based on user selection
filtered_data = data[selected_column]

# Display the plot
st.title('Plot')

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(filtered_data.index, filtered_data)
ax.set_xlabel('Index')
ax.set_ylabel(selected_column)
st.pyplot(fig)
