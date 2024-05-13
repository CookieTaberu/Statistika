import pandas as pd
import numpy as np
import main
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree

def preproses(data):
    data_proces=data
    # Convert 'credit.policy' column to boolean type
    data['credit.policy'] = data['credit.policy'].astype(bool)
    # Convert 'not.fully.paid' column to boolean type
    data['not.fully.paid'] = data['not.fully.paid'].astype(bool)
    # Filter records where 'revol.util' is greater than 100%
    over_100_util_records = data[data['revol.util'] > 100]
    # Add row numbers to the DataFrame after resetting the index
    over_100_util_records.insert(0, 'Row Number', over_100_util_records.index + 1)
    # Reset the index to remove the default index and avoid duplicates
    over_100_util_records.reset_index(drop=True, inplace=True)
    # Split dataset into features and target variable
    X = data[['int.rate','installment','dti','fico','days.with.cr.line','revol.bal','revol.util','delinq.2yrs','inq.last.6mths']]
    y = data['not.fully.paid']
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Step 2: Model Training
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    # Step 3: Model Evaluation
    y_pred = clf.predict(X_test)

    return X_train, y_train;

    
def Process():
   return preproses(main.df)