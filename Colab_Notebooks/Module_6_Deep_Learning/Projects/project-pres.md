1. **Problem Definition**: You have a clear problem definition at the top of your notebook.

2. **Data Collection**: You've loaded the pickled data from X.pickle and y.pickle from the AWS S3 bucket.

3. **Data Cleaning**: You've scaled the values in X to fall between 0 and 1 by dividing by 255.

4. **Exploratory Data Analysis**:

   - You've looked at the shape of X and y.
   - You've plotted images from X using plt.imshow().
   - You've looked at the response values in y for those images.

5. **Data Processing**:

   - You've split X and y into training and testing sets.
   - You've built a convolutional neural network with:
     - Sequential layers
     - Multiple 2D convolutional layers using 'relu' activation and (3,3) kernel size
     - MaxPooling2D layers after each convolutional layer with pool size (2,2)
     - A dense output layer using 'sigmoid' activation
   - You've compiled the model using 'adam' optimizer and appropriate loss function and metric.
   - You've fitted the model using the training set.
   - You've evaluated the model using the testing set.
   - You've plotted the distribution of probabilities for the testing set.

6. **New Image Prediction**:

   - You've defined a function to read in a new image and convert it to a 4-dimensional array.
   - You've used this function to read in the dog.jpg image from the AWS S3 bucket.
   - You've used your neural network to predict whether the image is a dog or a cat.

7. **Communication of Results**: You've communicated the results of your analysis.

8. **BONUS**: You've included code to handle a new image (url4) from a different source, which meets the bonus requirement.
