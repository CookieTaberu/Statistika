import pandas as pd
import numpy as np
import main
df=main.df
def preproses(data):
    data_proces=data
    # Convert 'credit.policy' column to boolean type
    df['credit.policy'] = df['credit.policy'].astype(bool)
    # Convert 'not.fully.paid' column to boolean type
    df['not.fully.paid'] = df['not.fully.paid'].astype(bool)
    
