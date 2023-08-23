import os
import streamlit as st
import pickle
import numpy as np
import keras
#import urllib.request

#urllib.request.urlretrieve('https://github.com/Parth-root/X-ray_image_classification_dbda2023/blob/main/Ui/your_model.h5', 'your_model.h5')
#filename = 'https://github.com/Parth-root/X-ray_image_classification_dbda2023/blob/main/Ui/your_model.h5'
filename = 'Ui/your_model.h5'
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
    if isPneumonic < 0.0001:
        imgClass = "Unknown image"
    elif isPneumonic < 0.5:
        imgClass = "Normal"
    else:
        imgClass = "Pneumonic"
    return imgClass


# Process the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    #st.image(image, caption='Uploaded Image', use_column_width=True)
    #resized_image = image.resize((200, 200))

    max_dimension = 200

    # Calculate new dimensions while preserving aspect ratio
    width, height = image.size
    if width > height:
        new_width = max_dimension
        new_height = int(height * (max_dimension / width))
    else:
        new_height = max_dimension
        new_width = int(width * (max_dimension / height))

    # Resize the image while preserving aspect ratio
    resized_image = image.resize((new_width, new_height))



    
  
    #resized_image = image.reshape(-1,1)
    st.image(resized_image, caption='Uploaded Image', use_column_width=True)
    #resized_image.show()
    ans=PneumoniaPrediction(image)
   

    # Convert image to numpy array
    image_array = np.array(image)

    # Your image processing code here
    # For example, you could apply filters, transformations, etc.
    processed_image = image_array  # Placeholder for demonstration
    st.title(ans)
    # Display processed image
    st.image(processed_image, caption='Processed Image', use_column_width=True)
