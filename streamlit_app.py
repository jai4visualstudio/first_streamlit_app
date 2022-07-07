import streamlit
streamlit.title('Break Smoothie')
streamlit.header('🎉Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🍛Kale, Spinach & Rocket smoothie')
streamlit.text('🍤Hard boiled free range Egg')

streamlit.header('🍓🍓🍅Build your own fruit smoothie🍂🍂')


import pandas
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
steamlit.multiselect("Pick Some Fruits", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
