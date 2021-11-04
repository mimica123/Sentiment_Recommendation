"""
This document has been created to deploy the model. For achieve it, it is necesary
to use streamlit and import emotion and recommendation models to do the final 
prediction. From the user, the app will requier a picture to predict the emotion 
and after that two questions will show asking for preference between movie and song.
The next question is the month of birth. With these three inputs DecisionTree model
will recommend a treat among Chocolate, Ice cream and Cake.
"""

#The first step is to import packages 

import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import pandas as pd
from PIL import Image

#This will be the title in the page and a small description
st.title("Welcome to Treat Recommendation Model")
st.subheader("This app predict an emotion from a picture and ask two more questions to make a treat recommendation")
st.subheader("Have fun playing around with the different parameters to get another outcome")
st.write("There is one special treat hidden for a specific combination. Try to find it!!!")


#Importing models to use them in the prediction
model = load_model("Models/streamlit_model.h5", compile=False)
filename = "Models/Decision_tree_model.sav"
tree_model = pickle.load(open(filename, 'rb'))

#The image is uploaded and saved it in image_file
image_file = st.file_uploader("Upload Images", type=["jpg","jpeg"])

#We need a list to input the three results from the image
#and the two questions
prediction = []

#List of emotions. One of this will be displayed after
#an image is uploaded
emotion = ['Angry', 'Disgust','Fear','Happy','Sad']

#Dictionary of months associated with a number for the prediction list
dictio = {"January" :1, "February":2, "March":3, "April":4, "May":5,
                        "June":6, "July":7, "August":8, "September":9, 
                        "October":10, "November":11, "December":12}

#An if loop is used to make sure that an image is uploaded
#in other case it would be pointless continuing with the   
#questions, because a piece of information will be missed
if image_file is not None:
    #Preprocesin of the images like resizing, converting to
    # array and flattening
    image = Image.open(image_file)
    image = image.resize((48, 48))
    image = np.array(image)
    image = np.reshape(image, [1,48, 48, 3])

    #Predicting emotion from the image
    output = model.predict(image)

    #Now the first value is inputed in prediction
    prediction.append(np.argmax(output))

    # To View Uploaded Image
    st.image(Image.open(image_file),width=250)
    
    #Print the result to the user
    st.write("Your emotion prediction is:", emotion[np.argmax(output)])

    #First question save it in preference
    preference = st.radio("What do you prefer?",("Movies", "Songs"))
    #Second question saved in month
    month = st.radio("What is your month of birth?",("January", "February", "March", "April", "May",
                        "June", "July", "August", "September", "October", "November", "December"))

    #Inputing the result from the first question to
    #prediction
    if preference=="Movies":
        prediction.append(0)
    else:
        prediction.append(1)

    #Inputing the result from the second question to
    #prediction
    prediction.append(dictio[month])

    #Now the prediction needs to be changed into an array
    #and reshape to make sure the model can read it
    #adecuately
    arr = np.array(prediction)
    arr = arr.reshape(1, -1)

    if st.button('Predict'):
        #Predicting the treat
        final_output = tree_model.predict(arr)
      #Printing to the user the result from the prediction
        st.write("According with the information above, your treat is:")
        if  prediction==[3,1,9]:
            st.write("SPECIAL TREAT!!!!")
            st.image(Image.open("Images/special.jpg"), width=250)
        elif final_output==1:
            st.write("Chocolate")
            st.image(Image.open("Images/chocolate.jpg"),width=250)
        elif final_output==2:
            st.write("Ice cream")
            st.image(Image.open("Images/icecream.jpeg"),width=250)
        else:
            st.write("Cake")
            st.image(Image.open("Images/cake.jpg"),width=250)

    

   
        
