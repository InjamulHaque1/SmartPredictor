import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib
from sklearn.metrics import r2_score

def train_model():
    file_path = "melb_data.csv"
    house_data = pd.read_csv(file_path)
    house_data = house_data.dropna(axis=0)
    
    x = house_data.drop("Price", axis=1)
    y = house_data['Price']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3 , random_state=1)
    
    house_model = DecisionTreeRegressor(random_state=1)
    house_model.fit(x_train, y_train)
    
    # Save the trained model to a file
    joblib.dump(house_model, 'trained_model.pkl')
    
    # Predict on test set and calculate accuracy
    y_pred = house_model.predict(x_test)
    accuracy = r2_score(y_test, y_pred)
    
    return accuracy

if __name__ == "__main__":
    accuracy = train_model()
    print("Model Accuracy:", accuracy)
