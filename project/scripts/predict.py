# predict.py
import os
import joblib

def predict(total_rooms, bedrooms, bathrooms, car_parking, area_size):
    input_data = [[total_rooms, bedrooms, bathrooms, car_parking, area_size]]
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the trained_model.pkl file
    model_path = os.path.join(script_dir, 'trained_model.pkl')
    
    # Load the trained model
    trained_model = joblib.load(model_path)
    
    # Use the trained model to predict
    predicted_price = trained_model.predict(input_data)
    
    return predicted_price

