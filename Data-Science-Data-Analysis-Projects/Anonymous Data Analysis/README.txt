Using Python and data science tools, including libraries sklearn / scikit-learn, numpy, pandas.

ANALYSIS FILES
final code.py - code to solve original problem; 
model test.py - code used to test various statistical models on data to see which gave the best results; 
SVC test.py - SVC model removed from testing code because it kept hanging the kernel and/or computer; 
data_clean_revised.py - methods needed to run final code.py, model test.py, and SVC test.py

DATA FOLDER
Original data consisted of 40,000 records in the training set and 10,000 records in the test set.
Each record in both sets had 100 features.
Data folder contains small samples of training and test sets due to github limitations.

Recent additions/fixes.
Encoded categorical data using only OneHotEncoder.
Used SimpleImputer to replace null values - used most frequent for categorical data and mean for numerical data.
