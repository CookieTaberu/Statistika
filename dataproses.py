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
    # Filter records where 'revol.util' is greater than 100%
    over_100_util_records = df[df['revol.util'] > 100]
    # Add row numbers to the DataFrame after resetting the index
    over_100_util_records.insert(0, 'Row Number', over_100_util_records.index + 1)
    # Reset the index to remove the default index and avoid duplicates
    over_100_util_records.reset_index(drop=True, inplace=True)
