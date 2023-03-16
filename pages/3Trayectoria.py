import streamlit as st
from PIL import Image


st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)


image = Image.open('cv.jpeg')


st.markdown('## Proyectos:')
st.markdown('#### Concurso Ideas Loyola - 2023')
st.write('Premio al mejor proyecto categoría "Ideas de Negocio"')
image = Image.open('cv.jpeg')
st.image(image, caption='Ideas Loyola 2023')

st.markdown('#### Concurso Ideas Factory II - 2020')
st.write('Ganador con el proyecto ConectayPlanta')
image2 = Image.open('online.png')
st.image(image2, caption='Ideas Factory Online 2020')

st.markdown('#### Concurso Ideas Factory I - 2019 ')
st.write('Ganador con el proyecto ROOMBUS')
image3 = Image.open('if_2ed.png')
st.image(image3, caption='Ideas Factory 2019 2º Edición')

st.markdown('## Prácticas:')
st.markdown('#### Empresa DEPROM - 2019')
st.write('Automatización mediante Macros de EXCEL')

