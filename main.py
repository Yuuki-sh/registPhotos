import streamlit as st
from PIL import Image
from PIL import Image, ImageEnhance

import pandas as pd
import numpy as np 
import csv

from io import BytesIO

import folium
from streamlit_folium import st_folium      # streamlitでfoliumを使う
import branca


st.title('写真登録用')

#画像取込み
uploaded_file = st.file_uploader("画像取込み", type= "jpg")
if uploaded_file != None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(img_array, caption="サムネイル画像", use_column_width = True)



with st.form(key='profile_form'):

    loc = st.text_input("観光場所名")
    lon = st.text_input("経度")
    lat = st.text_input("緯度")
    note = st.text_input("感想")
    url = st.text_input("参考URL")

    #ﾎﾞﾀﾝ
    submit_btn = st.form_submit_button('登録')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'マップに場所と写真登録しました')

        #入力したものをリストに代入する
        data = [[loc, lon, lat, note, url]]

        #csvへの項目追記
        with open('regist.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
        
        #ファイルをクライアントから受ける
        fbytes = uploaded_file.getvalue()
        #modeをwb（バイナリ書き込みモード）にする。encodingを指定するとえらーになる
        with open("raw_data.jpg", mode="wb") as f:
            f.write(fbytes)


img01 = Image.open('kurumayama.JPG')
st.image(img01, caption='車山高原', use_column_width=300)

img02 = Image.open('IMG_2085.jpg')
st.image(img02, caption='角島', use_column_width=300)

img03 = Image.open('DSC02752--EDIT.jpg')
st.image(img03, caption='灯台', use_column_width=100)

img03 = Image.open('raw_data.jpg')
st.image(img03, caption='びわ湖バレイ', use_column_width=100)

