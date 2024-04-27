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
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    house_model = DecisionTreeRegressor()
    house_model.fit(x_train, y_train)

    joblib.dump(house_model, 'trained_model.pkl')
    
    x_first_200 = x.head(200)
    predictions_first_200 = house_model.predict(x_first_200)

    accuracy = r2_score(y.head(200), predictions_first_200)
    return accuracy

if __name__ == "__main__":
    accuracy = train_model()
    print("Model Accuracy:", accuracy)
