import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)


st.markdown('# J. ISMAEL RIVERA')
st.markdown('#### Economista y Estudiante en Inteligencia Artificial')

imagen = Image.open('perfil.jpg')
st.image(imagen,width=500)

st.header('Perfil')
st.write('Persona proactiva con iniciativa y capacidad de decisión y hábil para trabajar en equipo. Muy creativo y siempre con ideas a desarrollar. Tengo un elevado  interés en los datos, inteligencia artificial  y la economía.')

st.header('Sectores en los que me gustaría trabajar')
st.write('Sectores relacionados con la economía, inteligencia artificial, datos, tecnología, etc.')

st.markdown('## CONTACTO ')
st.markdown('### **Móvil:** (+34) 601.429.681')
st.markdown('### **Correo:** jirivchi@gmail.com')
st.markdown('### **Linkedin:** Jonny Ismael Rivera Ch. ')
