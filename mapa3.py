import streamlit as st
import pandas as pd
import ast

# load the data from CSV file
df = pd.read_csv('my_data.csv')

# create a Streamlit app
st.title('Recommended Houses')

# create a dropdown menu to select a house
house = st.selectbox('Select a House', df.index)

# display the selected house's information
price, square_meters, bedrooms, bathrooms, summary = df.loc[house, ['price', 'square_meters', 'bedrooms', 'bathrooms', 'summary']]
st.write(f'## {summary}\n\n')
with st.container():
    st.write('**Selected House:**\n\n'
             f'Price: ${price}\n\n'
             f'Square Meters: {square_meters}\n\n'
             f'Bedrooms: {bedrooms}\n\n'
             f'Bathrooms: {bathrooms}\n\n', 
             style='border: 2px solid #f63366; border-radius: 10px; padding: 10px;')
url = ast.literal_eval(df['images'][7])
st.image(url[0], width=400)

# recommend 5 specific houses including the selected one
recommended_houses = df.loc[[0, 1, 2, 8, 16]]
if house not in recommended_houses.index:
    recommended_houses = pd.concat([pd.DataFrame({'price': price, 'square_meters': square_meters, 'bedrooms': bedrooms, 'bathrooms': bathrooms, 'summary': summary}, index=[house]), recommended_houses])

# display the recommended houses in a table
st.write('\n## Recommended Houses:\n\n')
for i, index in enumerate(recommended_houses.index):
    row = recommended_houses.loc[index]
    st.write(f'## Recommendation {i+1}: {row["summary"]}\n\n'
             f'Price: ${row["price"]}\n\n'
             f'Square Meters: {row["square_meters"]}\n\n'
             f'Bedrooms: {row["bedrooms"]}\n\n'
             f'Bathrooms: {row["bathrooms"]}\n\n')
    url = ast.literal_eval(df['images'][index])
    st.image(url[0], width=350)
