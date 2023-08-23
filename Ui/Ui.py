import os

import streamlit as st
import pickle
import numpy as np
import keras

#filename = 'https://github.com/Parth-root/X-ray_image_classification_dbda2023/blob/main/Ui/your_model.h5'
filename = './your_model.h5'
model = keras.models.load_model(filename)

from PIL import Image

# Set the title and header
st.title("Image Processing with Streamlit")
st.header("Upload an Image and Process It")

# Upload image through Streamlit UI
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])


def PneumoniaPrediction(img):
    img = np.array(img) / 255
    img = img.reshape(-1, 200, 200, 1)
    isPneumonic = model.predict(img)[0]
    print(isPneumonic)
    if isPneumonic == 1:
        imgClass = "Normal"
    elif isPneumonic < 0.5:
        imgClass = "Normal"
    else:
        imgClass = "Pneumonic"
    return imgClass


# Process the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    ans=PneumoniaPrediction(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert image to numpy array
    image_array = np.array(image)

    # Your image processing code here
    # For example, you could apply filters, transformations, etc.
    processed_image = image_array  # Placeholder for demonstration
    st.title(uploaded_file)
    # Display processed image
    st.image(processed_image, caption='Processed Image', use_column_width=True)
