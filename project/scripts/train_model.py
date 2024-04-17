# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib

def train_model():
    file_path = "melb_data.csv"
    house_data = pd.read_csv(file_path)
    house_data = house_data.dropna(axis=0)
    
    x = house_data.drop("Price", axis=1)
    y = house_data['Price']
    x_train, _, y_train, _ = train_test_split(x, y, test_size=0.3)
    
    house_model = DecisionTreeRegressor()
    house_model.fit(x_train, y_train)
    
    # Save the trained model to a file
    joblib.dump(house_model, 'trained_model.pkl')

if __name__ == "__main__":
    train_model()
