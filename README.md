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

During the training step, a base model was created with a Convoltional Neural Network with just three layers: the input, the hiden and the output layer. With this model the gray scale dataset was trained as a way to look at the functionality of the model. Next, the same base model was applied to the colour dataset obteining the following results in accuracy and loss:

![colour_model](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Images/colour_model.png)

The results are very good knowing that the Convolutional Neural Network is the most simple one. Now more layers are included in the model to make the learning process more effective. In addition to more layers, BatchNormalization and Dropout have been included to help in the model performace and the accuracy and loss results are the following:

![more_layers](https://github.com/mimica123/Sentiment_Recommendation/blob/main/Images/more_layers.png)