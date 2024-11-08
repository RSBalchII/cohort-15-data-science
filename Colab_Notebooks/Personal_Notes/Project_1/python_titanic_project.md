# Python Functions and Methods from the Titanic Survival Prediction Notebook

## IPython.display

### Image(filename)

This function displays an image from a specified file. In this case, it shows the 'confusion_matrix.png' image.

---

## matplotlib.pyplot (as plt)

### figure(figsize=(8,4))

Creates a new figure with a specified size of 8 inches by 4 inches.

### hist(data)

Generates a histogram of the provided data, showing the distribution of accuracy scores from cross-validation.

### savefig(fname)

Saves the current figure to a file with the specified filename, in this case 'confusion_matrix.png'.

### show()

Displays all open figures.

### title(label)

Sets the title of the current axes or figure to the provided label.

## numpy (as np)

### zeros(shape)

Returns a new array of the given shape and type, filled with zeros. Here, it creates an array to store accuracy scores from cross-validation.

### mean()

Calculates the arithmetic mean (average) of the elements in the provided array, which contains accuracy scores.

## pandas (as pd)

### read_csv(filepath)

Reads a CSV (Comma Separated Value) file from the given file path and returns a Pandas DataFrame. This is used to load the Titanic training data from 'Titanic.train.csv'.

### head(n=5)

Returns the first n rows of the DataFrame. By default, n is 5, but it can be specified otherwise. This is used to inspect the first few rows of the DataFrame.

### copy()

Creates a deep copy of the DataFrame. This ensures that modifications made to the copy do not affect the original DataFrame.

### drop(labels, axis=1, inplace=True)

Removes rows or columns from the DataFrame.

- labels: Specifies the row or column labels to drop.
- axis=1: Indicates that columns should be dropped (axis=0 would drop rows).
- inplace=True: Modifies the DataFrame directly instead of creating a new one.

### tail()

Returns the last n rows of the DataFrame, similar to head() but for the end of the DataFrame.

### unique()

Returns an array of the unique values in a specific column of the DataFrame. This is used to inspect the 'Ticket' column for unique values.

### isna()

Returns a DataFrame of the same shape as the original, with True for cells containing missing values (NaN) and False otherwise.

### sum()

Calculates the sum of values along an axis in the DataFrame.

### info()

Prints a concise summary of the DataFrame, including the index dtype and columns, non-null values, and memory usage.

### fillna(value, inplace=True)

Fills missing values (NaN) in the DataFrame with the specified value.

- value: Can be a scalar value or a dictionary specifying different values for each column.
- inplace=True: Modifies the DataFrame directly.

### mean()

Calculates the mean (average) of values in a specific column (in this case, 'Age').

### value_counts()

Returns a Series containing counts of unique values in the specified column. This is useful for understanding the distribution of values in a column.

### astype('int8')

Casts a column ('Cabin') to a specific data type, in this case, a signed 8-bit integer.

### mode()

Returns a Series containing the mode(s) (most frequent value(s)) of the DataFrame.

### get_dummies(data, columns, prefix)

Converts categorical variables into dummy/indicator variables, effectively one-hot encoding the specified columns.

- data: The input DataFrame.
- columns: A list of columns to be one-hot encoded.
- prefix: A string to prepend to the newly created dummy variable column names.

---

## seaborn (as sns)

### set()

Sets the aesthetic style of seaborn plots. This function is often used at the beginning of a script to define the overall look of the plots.

### pairplot(data)

Creates a grid of pairwise relationships between columns in the DataFrame. This is useful for visualizing correlations between different features.

### heatmap(data, cmap, annot)

Generates a heatmap representation of the data, often used to visualize correlation matrices.

- data: The input data, typically a correlation matrix.
- cmap: The colormap to use for the heatmap.
- annot: Whether to annotate the heatmap cells with their values.

---

## sklearn.metrics

### ConfusionMatrixDisplay.from_estimator(estimator, X, y, normalize, values_format, cmap)

Creates a confusion matrix display object from a fitted estimator, test data, and optional parameters for normalization, value formatting, and colormap.

### accuracy_score(y_true, y_pred)

Calculates the accuracy score by comparing the true labels (y_true) with the predicted labels (y_pred).

## sklearn.model_selection

### train_test_split(X, y, test_size, random_state)

Splits arrays or matrices into random train and test subsets.

- X: The features data.
- y: The target data.
- test_size: The proportion of the data to be used for testing (e.g., 0.2 for 20%).
- random_state: Ensures that the data is split the same way each time the code is run, making the results reproducible.

---

## sklearn.naive_bayes

### GaussianNB()

Creates a Gaussian Naive Bayes classifier object. This type of classifier assumes that features follow a Gaussian (normal) distribution.

### fit(X, y)

Trains the Gaussian Naive Bayes model on the provided training data (X for features, y for target).

### predict(X)

After training, predict is used to make predictions on new data using the trained Gaussian Naive Bayes model. It takes the features (X) of the new data as input and returns predicted labels.

Citations:
