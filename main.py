import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Henry Diaz")
    content = """
    Hello this is my first web app application written in Python, will add more information once my project get better 
    and have more stuffs to show
    """
    st.info(content)
