import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string

# Import: Machine Learning Pipeline Tools
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
import xgboost as xgb
# Import: Pickle for Saving Trained ML Model
import pickle

from dataproses import preproses

def train_model(data):
    pData = preproses(data)
    
    tree_model = tree_model = DecisionTreeClassifier()
    tree_model = tree_model.fit(pData[0], pData[1])
    
    with open('tree_model.pkl', 'wb') as file:
        pickle.dump(tree_model, file)