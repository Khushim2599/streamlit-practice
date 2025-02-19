import streamlit as st  # Import Streamlit

st.title("🌍 My First Streamlit Website!")  # Page title
st.write("Welcome to my practice website! This is my first time using Streamlit. 🎉")

# User Input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Nice to meet you. 😊")

# Button Example
if st.button("Click me!"):
    st.write("You clicked the button! 🚀")

# Slider Example
rating = st.slider("Rate this website (1-10):", 1, 10)
st.write(f"You rated this site: {rating}/10")

# Image Example
st.image("https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2020/01/earth/21500960-1-eng-GB/Earth_pillars.jpg", caption="Beautiful Earth")
