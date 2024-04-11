import streamlit as st
from googletrans import Translator

st.header('Machine Translation Demo')
input=st.text_area('please enter the text',value='')
option =st.selectbox(
      'To which language you wish to translate this text to?',
      ('Malaylam','Hindi','Bengali'))
if st.button('Translate'):
    translator=Translator()
    translation=translator.translate(input,dest=option)
    st.write(translation.text)