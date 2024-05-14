import pandas as pd
from modeling import train_model
from dataproses import preproses
import InputProcess
from InputProcess import predict

def main():
    # Load your data (replace 'your_data.csv' with your actual data file)
    data = pd.read_csv('loan_data.csv')
    
    # Train the model
    train_model(data)
    
    # Example of predicting with new input data
    new_input_data = { 'int.rate': 0.1,
        'installment': 500,
        'dti': 0.3,
        'fico': 700,
        'days.with.cr.line': 2000,
        'revol.bal': 200,
        'revol.util': 40,
        'delinq.2yrs': 0,
        'inq.last.6mths': 1}  # Replace {...} with your new input data
    user=InputProcess.ProcessingInput(new_input_data)
    predict(user)

if __name__ == "__main__":
    main()
