# PatternRecognition_Assignment_1
Student Name (ID)	: Muhammad Athallah Yakarazi (24/532752/PA/22532)

This repository contains the deliverables required by Assignment 1

This repository contains:
1. Part1_String_Matching.py 
2. Part2_Statistical_Text_Representation.ipynb
3. Part3_Text_Classification.ipynb
4. Part4_Conceptual_Questions.pdf
5. spam.csv (the dataset required for the assignment, obtained here: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

Part1_String_Matching.py is a python script while the rest are notebooks because they contain external python libraries that I don't want to install locally (taking up space), part 1 script only uses python built-in libraries.

## External Libraries Used
### 1. Pandas
Pandas dataframes are used to read the .csv dataset, apply operations on the dataset to make the vectors, and store their values.
link: https://pandas.pydata.org/

### 2. Scikit-Learn
Explicitly required by the assignment for the classification stage (Part 3).
link: https://scikit-learn.org/stable/

### 3. NumPy
Because scikit-learn classifiers require the feature matrix (X) to be a two-dimensional array-like structure, such as a 2D NumPy array. This also saves me from building the scikit-learn compatible feature matrix myself from the ground up.
link: https://numpy.org/

### 4. Matplotlib and Seaborn
To visualise the scikit-learn generated confusion matrix better.
link: https://matplotlib.org/
link: https://seaborn.pydata.org/

## Code Snippets
Reference links to code snippets adapted to this can be found within the part where they are used.
