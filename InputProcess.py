import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import dataproses
from dataproses import preproses
import pickle
def ProcessingInput(newInput):
    # Create a DataFrame from the new applicant's features
    new_applicant_df = pd.DataFrame([newInput])
    return new_applicant_df

def predict(newInput):
    with open('tree_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    
    predict = loaded_model.predict(newInput)

    if predict[0] == 0:
        print("Prediction: Fully Paid")
    else:   
        print("Prediction: Not Fully Paid")
