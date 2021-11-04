# Sentiment_Recommendation

### Treat Recommendation From Sentiment Analysis

Bussines field is one of the most fearest industry, when referring to competition for high sales. Big companies fight for maintening the number of sales while startups try to increase them using all the possible techniques known in the area. Latetly, the form that companies are selling have changed with the introduction of social media. This open a new world for exploring from the business perspective and new tendencies have appeared, from promoting products in videos of influencers to advertisments in social media dashboard. The only important goal is to motivate users to adquired a service or brand. Giants such as Amazon and Netflix took sentiment analysis to another level to attract more people based in users preferences and the reward of that effort has been generated billion of dollars. In social media the most common post is a picture which in the majority of cases represents users mood and emotions. This was the motivation to develop an application that can connects pictures linked to users emotions with a product recommendation as a strategy to attract customers and increase purchases.

### Blending AI

Machine Learning and Deep Learning are powerful tools in Artificial Intelligence. However, combining more than one can make huge improvements in applications. For this particular case, Convolutional Neural Network has fused with Decision Tree and Naive Bayes to complement among them and create a recommended system using sentiment analysis. Lastly, the result is deployed throughout Streamlit to apport a polish finish.

### The Dataset

Working with images is an expensive task during the learning process and an important fact to have in mind. For the first model, the dataset used was a gray scale with seven emotion (happy, sad, angry, fear, disgust, surprise and neutral). Unfortunately,if the Convolutional Neural Network is trained with gray scale images, it won't be able to predict for colour pictures, which represented a limitant for the project due to  most of images posted are in colour. However, it was helpful to see the performance of the Convolutional Neural Network and for the first view of the app.

![im0](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Gray%20scale/im0.png) ![im1](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Gray%20scale/im1.png) ![im4](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Gray%20scale/im4.png) ![im6](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Gray%20scale/im6.png) ![im8](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Gray%20scale/im8.png) 

There was no dataset available that satisfy the requirements (images representing emotions and in color). For that reason, it was necesary to create one with a google extension called "Download all images". Only five different emotions were chosen and thousand images per each of them. Because images had diverse size and extension, it was essential preproccessing them first to have them ready for the Convolutional Neural Network.

![Angry804](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Colour/Angry804.PNG) ![Disgust801](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Colour/Disgust801.PNG) ![Fear804](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Colour/Fear804.PNG) ![Happy804](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Colour/Happy804.PNG) ![Sad804](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Data/Colour/Sad804.PNG)

### Preprocesing

Clean all images is a vital task in order to have them ready for inputing them in the Convolutional Neural Network. The first step is to change the name of all the images in each of the folders created for each emotion: happy, sad, angy, fear and disgust. Then images need to have the same size for matching the entry of the Convolutional Neural Network. In this particular case the input of the images size will be 48 by 48, which means the height will be 48 and the width will be 48 also. To avoid future problems with images, the raw images will be conserved in their respective classification folders and new ones will be created for each of the emotions with the new names and sizes. Also, the data will be split in train and test to have it ready for the Convolutional Neural Network step in future files.

### Training

During the training step, a base model was created with a Convoltional Neural Network with just three layers: the input, the hiden and the output layer. With this model the gray scale dataset was trained as a way to look at the functionality of the model for sixty epochs and a batch step of thirty-two. Next, the same base model was applied to the colour dataset using again sixty epochs and thrirty-two as a batch step. Now more layers are included in the model to make the learning process more effective. In addition to more layers, BatchNormalization and Dropout have been included to help in the model performace. Initially, the model was trained with 180 epochs and the same batch step as before, but the results were not satisfactory because the accuracy and loss became worse. For that reason, this time 150 epochs were used instead. The batch step was maintened as thirty-two.

### Results

Using the colour set and the base model, the results in accuracy and loss were the following:

![colour_model](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Images/colour_model.png)

For the model with more layers the accuracy and loss results are the following:

![more_layers](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Images/more_layers.png)

There are a lot of things to considered in this particular case. Firs of all, the dataset is composed by just thousand images per emotion given a total of five thousand, from where four thousands were destinated to the training stage and thousand to the validation stage. Another aspects to consider is that all the images were not limited to just faces and people because the idea was to create a model able to recognize emotions even in images containing words such as book covers, birthday messages, landscapes, food, etc. In the initial case, the results are very good knowing that the Convolutional Neural Network is the most simple one and has just one hidden layer which is the one that permits the learning process. Notice how the model improve when the number of layers increase in the second case, which is reflected in accuracy and loss results making the model to adjust better to the dataset.

### Streamlit

One useful tool to make the model more interactive with users is Streamlit. It will permit to acces to the prediction application from anywhere in a friendly form and more adecuated for inputing information.

![streamlit](https://share.streamlit.io/mimica123/sentiment_recommendation/main/streamlit.py)

### What is Next?

Definitively increasing the dataset, this was the major limitant during the proyect and obviously the first improvement to do. That will contribute to get better results from the model because it will have the opportunity to learn more about emotions. The second further step will be add more emotions and even combined them. The model could output a percentage of each emotion in each images instead of just one which will make it more adapted to reality. Another excellent improvement is to connect it to social media extracting images from post and then adding a personalized advertisement based in user's post. Combining this with Natural Language Processing will make a very powerful complement in reading emotions. Applications in business is endless and the limit is the sky.

## Navigating Through the Repository

### Folders

- **`/Data/`** - It contains sample of both datasets
- **`/Images/`** - Images used for the README file and Streamlit
- **`/Models/`** - Models saved to be used with Streamlit

### Files

- **`1.0 Cleaning.ipynb`** - Preprocesing of the colour dataset
- **`2.0 Final_version_0.ipynb`** - Base model with gray scale dataset
- **`3.0 Final_version_1.ipynb`** - Base model with colour dataset
- **`4.0 Final_version_2.ipynb`** - Model with more layers using the colour dataset
- **`README.md`** - Readme file
- **`packages`** - Packages requiered by Streamlit
- **`requirements`** - Packages version required by Streamlit
- **`streamlit.py`** - File containing the treatment recommendation using Streamlit