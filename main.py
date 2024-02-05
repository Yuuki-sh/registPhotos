import streamlit as st
from PIL import Image


st.title('写真登録用')

img01 = Image.open('.\pictures\kurumayama.JPG')
st.image(img01, caption='車山高原', use_column_width=300)

img02 = Image.open('.\pictures\IMG_2085.jpg')
st.image(img02, caption='角島', use_column_width=300)

img03 = Image.open('.\pictures\DSC02752--EDIT.jpg')
st.image(img03, caption='灯台', use_column_width=100)
