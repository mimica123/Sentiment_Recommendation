""" 
In this file there are all the functions definitions
that we are going to use during all the project, each of 
this definitions have their own explanation of what they
do and how to use it. At the same time, it is include
what kind of parameters receive and return and an example
to ilustrate how to use it. Inside of the code, I also 
include comments to guide what I am doing in each step,
and that way makes it easy to understand and follow.

The form this document should be used is in the .ipynb in
a cell write:
    from Definitions import name_of_the_function

Example:
    from Definitions import Change_Name
"""

def Change_Name(directory, new_directory, name):
    """Changing the name of all the images in a directory to 
        a especific name and adding a number at the end of that name
        in a new directory, if the name is the same it will rewrite them.
        The images extension will be PNG, but it can be easyly change
        if it is needed. This means that all the images will have
        extension PNG after this, so be careful with what kind of 
        extension the images have.
        
        Expected value:
            -The path of a directory.
            
            -The path of the directory we want to save our images.
            
            -The name that we want our images have, the function is
            in charge to add the numbers at the end, so you do not 
            need to add it
            
        Return:
            -It does not return anything because the images have new 
            names after the function is used
            
        Example:
            Change_Name("C:/Users/directory", "C:/Users/new_directory","Rename")
            
            In the directory all the images are named in the
            following way:
                Rename0.PNG
                Rename1.PNG
                Rename2.PNG
                Rename3.PNG
                ...
    """
    
    import os
    #Creating a loop to go through all the images in the directory
    for count, filename in enumerate(os.listdir(directory)):
        #dst is the new name that images will have
        dst = name + str(count) + ".PNG"
        #src is the old name we are going to replace
        src = directory + "/" + filename
        #dst is the path plus the new name
        dst = new_directory + "/" + dst
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        

def Resize_Image(directory,new_directory, height, width):
    """
    This function change the size of all images in a directory,
    and add it to a new directory. If the name of directory and
    new_directory are the same, the images will be rewritten.
    
    Expected value:
            -The path of a directory.
            
            -The path of the directory we want to save our images.
            
            -The desire height of the image we want to resize.
            
            -The desire width of the image we want to resize.
            
        Return:
            -It does not return anything because the images have new 
            size after the function is used. They are add it to the
            new_directory
            
        Example:
            Resize_Image("C:/Users/directory", "C:/Users/new_directory", 48, 48)
            
            In the new directory all the images change size and 
            keep their name.
    
    """
    
    import os
    from PIL import Image
    #We need a loop to go through all the images in the directory
    for count, filename in enumerate(os.listdir(directory)):
        #open each image in the directory and save it in im
        im = Image.open(directory + '/' + filename)
        #change the size of the image in im to the height and
        #width inputed
        out = im.resize((height, width))
        #save the new image in the new_directory
        out.save(new_directory + '/' + filename)
        
def Graph_Accuracy_Loss(history):
    """
    This function plot accuracy and loss versus epoch of the model after is
    trained to compare the performance between the train and 
    test dataset.
    
    Expected value:
            -History of the model.
            
        Return:
            -It does not return anything because plot accuracy and
            loss graphs
            
        Example:
            Graph_Accuracy_Loss(history)
    
    """
    
    import matplotlib.pyplot as plt
    history_dict = history.history
    loss_values = history_dict['loss']
    val_loss_values = history_dict['val_loss']
    accuracy = history_dict['accuracy']
    val_accuracy = history_dict['val_accuracy']
  
    epochs = range(1, len(loss_values) + 1)
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    #
    # Plot the model accuracy vs Epochs
    #
    ax[0].plot(epochs, accuracy, 'bo', label='Training accuracy')
    ax[0].plot(epochs, val_accuracy, 'b', label='Validation accuracy')
    ax[0].set_title('Training & Validation Accuracy', fontsize=16)
    ax[0].set_xlabel('Epochs', fontsize=16)
    ax[0].set_ylabel('Accuracy', fontsize=16)
    ax[0].legend()
    #
    # Plot the loss vs Epochs
    #
    ax[1].plot(epochs, loss_values, 'bo', label='Training loss')
    ax[1].plot(epochs, val_loss_values, 'b', label='Validation loss')
    ax[1].set_title('Training & Validation Loss', fontsize=16)
    ax[1].set_xlabel('Epochs', fontsize=16)
    ax[1].set_ylabel('Loss', fontsize=16)
    ax[1].legend()