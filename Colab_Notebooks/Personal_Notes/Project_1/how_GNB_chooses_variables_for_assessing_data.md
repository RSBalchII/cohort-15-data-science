Understanding Variable Selection and the Gaussian Naive Bayes Algorithm
This note explains how variables are chosen for use in the Gaussian Naive Bayes algorithm and the algorithm's process for analyzing a customer transaction dataset.
Variable Selection:
●
The provided source code demonstrates a two-part process for preparing data and training a Gaussian Naive Bayes model.
●
Data Preparation: Irrelevant data is removed from the dataset to ensure that only potentially significant features are used.
●
Feature/Target Split: The dataset is divided into predictor variables (X) and the target variable (Y). The "var\_\*" columns, which reflect customer purchase history data, are used as the predictor variables (X). The "target" column, which shows whether a purchase was made or not, is utilized as the target variable (Y).
How the Gaussian Naive Bayes Algorithm Works:

1.  Assumptions: The algorithm assumes every predictor variable ("var\_\*") is independent of the others. This "naive" assumption, while potentially not entirely realistic, simplifies calculations.
2.  Probability Calculation: The algorithm calculates the probability of a customer making a purchase (target = 1) or not making a purchase (target = 0). These probability calculations are made for each predictor variable, and are based on the specific values of that variable found in the training data. For this calculation, the algorithm assumes a Gaussian (normal) distribution, meaning that the mean and standard deviation for each "var\_\*" feature are calculated separately for both possible classifications of the target variable (target = 0 and target = 1).
3.  Prediction: The algorithm uses the probabilities derived from the training data to predict the likelihood of a purchase when presented with a new customer's data. To do so, it multiplies the individual probabilities associated with each of that customer's "var*\*" values. This multiplication is done for both the purchase and no-purchase scenarios. Whichever class (target = 0 or 1) has the higher resulting probability is the model's prediction for that customer.
    Assessment of the Dataset:
    ●
    Model Training and Accuracy: The source code trains the Gaussian Naive Bayes model using a training subset of data. This training process is conducted within the cross_validate function, which repeatedly splits the data into training and testing sets. First, the model is trained on the training set; then, the model's accuracy is tested using the testing set. The entire process is repeated numerous times in order to produce a more robust estimate of the model's performance. The accuracy score, which measures the percentage of correctly classified instances (purchases or no purchases) allows for assessment of how well the model generalizes to data that it has not yet seen.
    ●
    Correlation Analysis: Though not a direct component of the Gaussian Naive Bayes algorithm, the source code includes analysis of correlations between the "target" variable and the predictor variables. This analysis can be helpful for identifying which "var*_" features share a strong linear relationship with the likelihood of a purchase, and thus might be key drivers of customer behavior. Correlation does not, however, automatically indicate causation.
    In short, the Gaussian Naive Bayes algorithm uses customer shopping history data, represented by the "var\__" variables, to create a model for predicting whether a customer will make a purchase. By using cross-validation, the accuracy of the model, which demonstrates how well the selected variables can predict future transactions, is assessed. While the algorithm's "naive" assumption about the independence of variables is likely an oversimplification, the algorithm is well-suited to this project due to its ability to process continuous numerical data, like prices.
