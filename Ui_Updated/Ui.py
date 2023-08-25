import os
import streamlit as st
import numpy as np
import keras
#import cv2
from PIL import Image
filename = '/Ui_Updated/Pneumonia_model_final.h5'
filename = 'Pneumonia_model_final.h5'
model = keras.models.load_model(filename)

def app():
    #st.title("Page 2")
    #st.write("Welcome ")

    def PneumoniaPrediction(img):
        img = np.array(img)/255
        img = img.reshape(-1, 200, 200, 1)
        isPneumonic = model.predict(img)[0]
        print(isPneumonic)
        if isPneumonic <0.15:
            imgClass = "Normal"
        elif isPneumonic<0.7:
            imgClass = "Normal"
        else:
            imgClass = "pneumonia"
        return imgClass

    def img_proess(img):
        pil_image =img
            # Determine the side length for the square crop
        side_length = min(pil_image.size)*1.4 #1.4 to make more usefull image    
        # Calculate cropping box for center cropping
        left = (pil_image.width - side_length) //2
        top = (pil_image.height - side_length) //2
        right = (pil_image.width + side_length)//2
        bottom = (pil_image.height + side_length) //2
        # Perform the center crop to make the image square
        square_cropped_image = pil_image.crop((left, top, right, bottom))
        final_image=square_cropped_image.resize((200,200),Image.BOX)
        return final_image

    #this code not work in stremlit cloud so use in future
    #def img_proess_V2(img):
    #    img_size = 200
        #img_arr = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    #    resized_arr = cv2.resize(img, (img_size, img_size))
    #    return resized_arr
        
    # Set the title and header
    st.title("chest x-ray image classification for covid-19 detection for pneumonia")
    st.header("Upload an Image and Process It")

    # Upload image through Streamlit UI
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    # Process the uploaded image
    if uploaded_file is not None:
        image_temp = Image.open(uploaded_file)
        image=img_proess(image_temp)
        ans=PneumoniaPrediction(image)
        st.title(ans)
        st.image(image, caption='Uploaded Image after process', use_column_width=True)
    

        # Convert image to numpy array
        image_array = np.array(image)

        # Your image processing code here
        # For example, you could apply filters, transformations, etc.
        processed_image = image_array  # Placeholder for demonstration
    
        # Display processed image
        #st.image(processed_image, caption='Processed Image', use_column_width=True)
