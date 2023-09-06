import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tracking the Pandemic")
st.write("""
# Tracking the Impact of COVID-19 in Indonesia

Delve into the latest COVID-19 insights for Indonesia. Our interactive data visualizations provide a clear, up-to-date snapshot of the pandemic's impact in the country. Explore trends, analyze statistics, and stay informed about the ever-evolving situation. Navigating the data has never been easier.
""")

# csv file
csv_file = 'covid_19.csv'
data_frame = pd.read_csv(csv_file,
                usecols=['Date','Location','Total Cases','Total Deaths',
                'Total Recovered','Total Active Cases'])
df = pd.DataFrame.drop_duplicates(data_frame)

st.write("""
## COVID-19 Data Overview for Indonesia
""")
st.write(df)

# sidebar
select = st.selectbox('**Select the location for which you want to display the data.** Choose location:', df['Location'])

# Filter the DataFrame for the selected location
filtered_data = df[df['Location'] == select]

# Display the area chart
data = pd.DataFrame(filtered_data[['Date', 'Total Cases', 'Total Active Cases',
                    'Total Recovered', 'Total Deaths']].set_index('Date'))
area_chart = px.area(data, title=f'Data for {select}')
st.plotly_chart(area_chart)

# pie chart
total_deaths = filtered_data['Total Deaths'].sum()
total_recovered = filtered_data['Total Recovered'].sum()
data = {'Category':['Total Deaths','Total Recovered'],
        'Value':[total_deaths, total_recovered]}
pie_data = pd.DataFrame(data)
custom_colors = ['#FF9999', '#fa2327']
fig = px.pie(pie_data, names='Category',
            values='Value',
            title=f'Comparison of Total Deaths and Total Recovered Cases in {select}',
            color_discrete_sequence=custom_colors)
st.plotly_chart(fig)

# bar chart
data1 = px.histogram(filtered_data, x=['Total Cases','Total Active Cases'],
                  title=f'The Total Cases & Total Active Cases on {select}')
st.plotly_chart(data1)
