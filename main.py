import pandas as pd
from modeling import train_model
from dataproses import preproses
import InputProcess
from InputProcess import predict

def main(userInputData):
    # Load your data (replace 'your_data.csv' with your actual data file)
    data = pd.read_csv('loan_data.csv')
    
    # Train the model
    train_model(data)

    user=InputProcess.ProcessingInput(userInputData)
    a = predict(user)
    return a
    

if __name__ == "__main__":
    main()
