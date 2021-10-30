"""
This document has been created to deploy the model. For achieve it, it is necesary
to use streamlit and import emotion and recommendation model
"""
import streamlit as st
#import tensorflow as tf
#from tensorflow import keras
import tensorflow.keras
import numpy as np
import pickle
import pandas as pd
from PIL import Image
st.title('Treats Recommendation')

model = tensorflow.keras.models.load_model("Models\streamlit_model.h5")

filename = "Models\Decision_tree_model.sav"
tree_model = pickle.load(open(filename, 'rb'))

image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

prediction = []


def load_image(image_file):
    img = Image.open(image_file)
    return img

if image_file is not None:
    
    image = load_image(image_file)
    image = image.resize((48, 48))
    image = np.array(image)
    image = np.reshape(image, [1,48, 48, 3])
    output = model.predict(image)
    prediction.append(np.argmax(output))

    # To View Uploaded Image
    st.image(load_image(image_file),width=250)
    #st.write(np.argmax(output))
    emotion = ['Angry', 'Disgust','Fear','Happy','Sad']
    st.write("Your emotion prediction is:", emotion[np.argmax(output)])

    preference = st.radio("What do you prefer?",("Movies", "Songs"))
    month = st.radio("What is your month of birth?",("January", "February", "March", "April", "May",
                        "June", "July", "August", "September", "October", "November", "December"))

    dictio = {"January" :1, "February":2, "March":3, "April":4, "May":5,
                        "June":6, "July":7, "August":8, "September":9, 
                        "October":10, "November":11, "December":12}
    if preference=="Movies":
        prediction.append(0)
    else:
        prediction.append(1)

    prediction.append(dictio[month])
    if (preference is not None)&(month is not None): 
        # load the model from disk
        arr = np.array(prediction)
        arr = arr.reshape(1, -1)
        df= pd.DataFrame(arr[0])
        arr_test = np.array([0,1,1])
        arr_test = arr_test.reshape(1, -1)
        final_output = tree_model.predict(arr)
        st.write("Accordig with the information above, your treat is:")
        if final_output==1:
            st.write("Chocolate")
        elif final_output==2:
            st.write("Ice cream")
        else:
            st.write("Cake")
        
