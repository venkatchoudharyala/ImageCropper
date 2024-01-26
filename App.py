import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

st.header("Cropper Demo")
img_file = st.file_uploader(label='Upload a file', type=['png', 'jpg'])

if img_file:
    img = Image.open(img_file)
    cropped_img = st_cropper(img, realtime_update = True, box_color = "#FF0012", aspect_ratio = (5, 2))

    st.write("Preview")
    #_ = cropped_img.thumbnail((600, 600))
    st.image(cropped_img)
