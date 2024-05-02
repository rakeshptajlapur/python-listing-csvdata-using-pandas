import streamlit as st
import pandas
st.set_page_config(layout='wide')

st.title('Python Projects Listing Webapp from CSV')

#create 2 columns
col1, col2 = st.columns(2)

#add image in 1st column
with col1:
    st.image('images/photo.jpg', width=350)

#add name and title in 2nd column
with col2:
    st.header('Rakesh kumar T')
    description = """
    Python Developer & WordPres Expert. 
    Self-taught web developer with 6+ years of experience in Full-stack Web development and 
    Top-Rated Upwork freelancer for the past 4 years. 
    I love to teach Web development and related technologies to newbies and experienced professionals.
   
     """
    st.info(description)


col3,empty_col, col4= st.columns([1.5, 0.5, 1.5]) #creating empty column so to add some spacing in between 3 and 4 column
#read csv data using pandas and save in object df
df = pandas.read_csv('data.csv', sep=';')

#iter rows method to iterate all rows in data frame df and get index, row( actual row data)
#row has full row data in which we grab only values of title column by mentioning it under row['title']
#"""for index,row_data in df.iterrows():
#    print(row_data['title'])"""

with col3:
    for index, row_data in df[:10].iterrows():
        st.image(f'images/{row_data["image"]}', width=200)
        st.header(row_data["title"])
        st.write(row_data["description"])
        st.write(f'[Project Link]({row_data["url"]})')

with col4:
    for index, row_data in df[10:].iterrows():
        st.image(f'images/{row_data["image"]}', width=200)
        st.header(row_data["title"])
        st.write(row_data["description"])
        st.write(f'[Project Link]({row_data["url"]})')






