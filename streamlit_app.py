import streamlit
streamlit.title("My Mom's New Healthy Diner")

streamlit.header('🥣 Breakfast Favorites')
streamlit.text('🥗 Omega 3 and Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach, and Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.

fruits_to_show = my_fruit_list.loc[fruits_selected]
