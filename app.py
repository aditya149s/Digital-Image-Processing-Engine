import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance, ImageChops

# Page config
st.set_page_config(page_title="Image Processing Engine", layout="wide")

# Custom CSS (Glassmorphism UI)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f, #2c2c54);
        color: white;
    }
    .stSlider label, .stFileUploader label {
        color: #ffffff !important;
        font-weight: 500;
    }
    .stButton button {
        border-radius: 12px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Digital Image Processing Engine")
st.write("Upload an image and apply transformations in real-time")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(img, use_container_width=True)

    # Controls
    st.sidebar.header("Controls")

    brightness = st.sidebar.slider("Brightness", 0.5, 2.0, 1.0)
    crop_x1 = st.sidebar.slider("Crop X1", 0, img.width, 0)
    crop_y1 = st.sidebar.slider("Crop Y1", 0, img.height, 0)
    crop_x2 = st.sidebar.slider("Crop X2", 0, img.width, img.width)
    crop_y2 = st.sidebar.slider("Crop Y2", 0, img.height, img.height)

    # Processing
    grayscale_img = img.convert('L')

    enhancer = ImageEnhance.Brightness(img)
    bright_img = enhancer.enhance(brightness)

    invert_img = ImageChops.invert(img.convert("RGB"))

    img_array = np.array(img.convert("RGB"))
    cropped_array = img_array[crop_y1:crop_y2, crop_x1:crop_x2]
    cropped_img = Image.fromarray(cropped_array)

    # Output
    with col2:
        st.subheader("Processed Output")

        tab1, tab2, tab3, tab4 = st.tabs(["Grayscale", "Brightness", "Invert", "Crop"])

        with tab1:
            st.image(grayscale_img, use_container_width=True)

        with tab2:
            st.image(bright_img, use_container_width=True)

        with tab3:
            st.image(invert_img, use_container_width=True)

        with tab4:
            st.image(cropped_img, use_container_width=True)