import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import dataproses
from dataproses import preproses
import pickle
def ProcessingInput(newInput):
    clf = DecisionTreeClassifier()
    X_train,y_train = preproses(newInput)
    clf.fit(X_train,y_train)
    # Create a DataFrame from the new applicant's features
    new_applicant_df = pd.DataFrame([newInput])

    # Reorder columns to match the training data
    new_applicant_df = new_applicant_df[X_train.columns]

    # Predict loan repayment for the new applicant
    prediction = clf.predict(new_applicant_df)
    return new_applicant_df

def predict(newInput):
    with open('tree_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
        
    prepas = ProcessingInput(newInput)
    
    predict = loaded_model.predict(prepas)

    if predict[0] == 0:
        print("Prediction: Fully Paid")
    else:   
        print("Prediction: Not Fully Paid")
