# Briefing Doc: Data Science Concepts and Techniques

This document reviews key themes and important information extracted from various sources on data science concepts, techniques, and applications.

## 1. Model Validation and Regression

Model validation is crucial for evaluating the performance of machine learning models.

### Validation Set Approach

- Involves splitting a dataset into training and validation sets
- The model is trained on the training set and then evaluated on the validation set to estimate its performance on unseen data

### Cross-Validation

- More robust approach where the data is repeatedly split into different training and testing sets
- Provides a more reliable estimate of model performance

### Common Metrics

- RMSE (Root Mean Squared Error)
  - Measures the average difference between predicted and actual values, in the same units as the response variable
- RMSPE (Root Mean Squared Percentage Error)
  - Scales RMSE based on the magnitude of the response variable
- MAE (Mean Absolute Error)
  - Measures the average absolute difference between predictions and actual values

Linear Regression is a common statistical method for modeling the relationship between a dependent variable and one or more independent variables.

### R-squared

- Statistical measure that indicates the proportion of the variance in the dependent variable that is predictable from the independent variable(s)

### Assumptions

- Linearity
- Normality of residuals
- Homoscedasticity
- Independence of errors

### Outliers and Multicollinearity

- Outliers can significantly influence linear regression models
- Multicollinearity arises when independent variables are highly correlated

## 2. Data Preprocessing and Transformation

Encoding involves converting categorical data into numerical representations for use in machine learning algorithms.

### Label Encoding

- Assigns a unique numerical value to each category
- Useful for ordinal data with a natural order

### One-Hot Encoding

- Creates binary (0/1) dummy variables for each category
- Suitable for nominal data with no inherent order

Feature Scaling standardizes the range of independent variables to improve model performance.

### Standard Scaling (Z-score)

- Transforms data to have zero mean and unit variance
- When to use: When data are normally distributed

### Min-Max Scaling

- Scales data to a specific range, typically between 0 and 1
- When to use: When the standard deviation is small, the data are not normally distributed, and there are no outliers

### Robust Scaling

- Uses the median and interquartile range (IQR) to scale data
- Making it less sensitive to outliers
- When to use: When there are significant outliers

Imputation handles missing data by replacing null values.

### Mean/Median/Mode

- Imputing with the mean (for continuous data) or median/mode (for categorical data) is a simple approach

### Constant Value

- Replacing missing values with a constant

### Machine Learning

- Utilizing algorithms to predict missing values based on other variables

## 3. Regularization Techniques

Regularization methods prevent overfitting in machine learning models.

### Ridge Regression

- Adds a penalty term proportional to the sum of squared coefficients (L2 regularization)
- Shrinking coefficients towards zero

### Lasso Regression

- Uses a penalty term proportional to the sum of absolute values of coefficients (L1 regularization)
- Forcing some coefficients to become exactly zero, leading to feature selection

### Scaling

- Data should be scaled before applying regularization techniques
- To ensure that all features contribute equally to the penalty term

## 4. Data Science Process and Problem Definition

The Data Science Process involves several stages:

### Problem Definition

- Clearly define the business problem and how data science can be utilized to address it

### Data Collection and Cleaning

- Gather relevant data and prepare it for analysis
- Handling missing values, inconsistencies, and errors

### Exploratory Data Analysis (EDA)

- Analyze and visualize data to understand patterns, relationships, and potential insights

### Feature Engineering

- Select, transform, and create relevant features for the machine learning model

### Model Building and Evaluation

- Choose and train appropriate machine learning models
- Evaluate their performance using suitable metrics

### Deployment and Monitoring

- Implement the model and monitor its performance over time

Common Mistakes:

- Not having the right data
- Not thinking about deployment
- Not considering modularity, reproducibility, scalability, extensibility, and testing of the model

## 5. Probability and Probability Distributions

Probability is a fundamental concept in data science, measuring the likelihood of an event occurring.

### Marginal Probability

- Probability of a single event

### Addition Rule

- Calculates the probability of event A or event B occurring

### Multiplication Rule

- Determines the probability of event A and event B occurring (for independent events)

### Conditional Probability

- The probability of an event occurring given that another event has already occurred

Random Variables represent numerical values determined by the outcome of a random phenomenon.

### Discrete Random Variables

- Take on a countable number of values (e.g., number of heads in coin flips)

### Continuous Random Variables

- Can take on an infinite number of values within a given range (e.g., height, weight)

Probability Distributions describe the probabilities of different outcomes for a random variable.

### Common Distributions

- Bernoulli, Binomial, Poisson, Uniform, Normal, Lognormal, Beta

### Choosing a Distribution

- Consider whether data is continuous or discrete, symmetric or asymmetric, bounded or unbounded, and the likelihood of outliers

## 6. Bias-Variance Trade-off

Bias refers to the error introduced by approximating a real-world problem with a simplified model.

Variance represents the sensitivity of a model to changes in the training data.

Underfitting occurs when a model is too simple and has high bias. It fails to capture the underlying patterns in the data.

Overfitting arises when a model is too complex and has high variance. It learns the training data too well, including noise, leading to poor generalization to new data.

The Bias-Variance Trade-off involves finding the right balance between bias and variance to achieve optimal model performance.

This briefing doc summarizes key concepts from various provided materials, aiming to provide a concise overview of essential data science principles and practices.
