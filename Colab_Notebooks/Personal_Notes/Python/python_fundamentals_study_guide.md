Here's the Python Fundamentals Study Guide formatted in pure Markdown:

# Python Fundamentals Study Guide

## Quiz

Instructions: Answer the following questions in 2-3 sentences each.

1. What is the difference between an integer and a float in Python?

2. What does the modulo operator (%) do in Python?

3. How do you add a new element to the end of a list in Python?

4. Explain what slicing my_list[2:5] will do to a list called my_list.

5. What is the difference between a list and a tuple in Python?

6. Describe two advantages of using dictionaries in Python.

7. How do you loop through each key-value pair in a dictionary using a for loop?

8. What is the purpose of an if statement in Python?

9. Explain the difference between elif and else in Python's conditional statements.

10. Give an example of when you might use a nested loop in Python.

## Answer Key

1. An integer is a whole number without a decimal point, while a float is a number that includes a decimal point. For example, 5 is an integer, while 5.0 is a float.

2. The modulo operator (%) returns the remainder of a division operation. For example, 10 % 3 would return 1, because 10 divided by 3 is 3 with a remainder of 1.

3. You can add a new element to the end of a list using the append() method. For example, my_list.append(5) would add the number 5 to the end of my_list.

4. Slicing my_list[2:5] will create a new list containing the elements of my_list from index 2 (inclusive) to index 5 (exclusive). In other words, it will return a list containing the elements at indices 2, 3, and 4 of the original list.

5. A list is mutable, meaning its elements can be changed after it's created, while a tuple is immutable and cannot be changed. Lists are defined using square brackets ([]), while tuples are defined using parentheses (()).

6. Dictionaries allow you to store data in key-value pairs, making it easy to access values based on their associated keys. They are also efficient for looking up values, as the keys act as indices.

7. for key, value in my_dictionary.items():
   print(key, value)
   This code iterates through each key-value pair in my_dictionary and prints them.

8. An if statement allows you to execute a block of code only if a certain condition is true. This allows for conditional execution of code based on specific criteria.

9. elif (short for "else if") is used to check for an additional condition after the initial if condition is false. If the elif condition is true, its code block is executed. else is used as a catch-all block that executes if none of the preceding if or elif conditions are true.

10. You might use a nested loop when you need to iterate through all possible combinations of elements in two or more iterables. For example, you might use nested loops to iterate through the rows and columns of a matrix or to generate all possible pairs of elements from two lists.

## Essay Questions

1. Explain the concept of slicing in Python and provide three examples of how it can be used to manipulate lists and strings.

2. Compare and contrast dictionaries, lists, and sets in Python. Discuss their respective use cases and provide examples of when each data structure would be most appropriate.

3. Describe the importance of indentation in Python code. Explain how incorrect indentation can lead to errors and how to maintain proper indentation for readability and functionality.

4. Discuss the benefits of using functions in Python. Explain how functions promote code reusability, modularity, and readability. Provide an example of a function definition and explain how to call and pass arguments to a function.

5. Explain the concept of Exploratory Data Analysis (EDA) and its significance in the data science process. Describe several techniques commonly used in EDA and provide examples of how these techniques can reveal insights from data.

## Glossary of Key Terms

- Variable: A named storage location in a computer program that holds a value.
- Data Type: A classification of data that determines its characteristics and the operations that can be performed on it.
- Integer: A whole number without a decimal point.
- Float: A number that includes a decimal point.
- String: A sequence of characters enclosed in quotation marks.
- List: An ordered, mutable collection of items, potentially of different data types.
- Tuple: An ordered, immutable collection of items.
- Dictionary: An unordered collection of key-value pairs, where keys are unique and used to access their corresponding values.
- Set: An unordered collection of unique elements.
- Loop: A programming construct that allows a set of instructions to be executed repeatedly.
- Iteration: A single pass through a loop's body of code.
- Conditional Statement: A programming construct that allows for the execution of different blocks of code based on the evaluation of a condition.
- Function: A reusable block of code that performs a specific task.
- Argument: A value passed to a function when it is called.
- Return Value: A value returned by a function after it has completed its task.
- Method: A function associated with an object.
- Slicing: Extracting a portion of a sequence, such as a list or a string.
- Index: A numerical value used to access a specific element within an ordered collection.
- Mutable: Capable of being changed after creation.
- Immutable: Not capable of being changed after creation.
- Key-Value Pair: An association between a unique key and a corresponding value, used in dictionaries.
- Nested Loop: A loop placed within the body of another loop.
- List Comprehension: A concise way to create lists in Python using a single line of code.
- Pandas DataFrame: A two-dimensional, labeled data structure in Python used for data manipulation and analysis.
- Exploratory Data Analysis (EDA): The initial phase of data analysis that involves summarizing, visualizing, and exploring data to gain insights and understand its characteristics.
- Data Cleaning: The process of identifying and correcting errors, inconsistencies, and missing values in a dataset.
- Outlier: A data point that significantly deviates from other data points in a dataset.
- Naive Bayes: A family of probabilistic classifiers based on Bayes' theorem.
- Gaussian Naive Bayes: A type of Naive Bayes classifier that assumes features follow a Gaussian distribution.
