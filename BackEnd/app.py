import json
import numpy as np
import joblib
from termcolor import colored

# Load the trained SVM model from a file
model = joblib.load('./assets/data/Model/model.pkl')

# Define a function to preprocess the sensor data
def preprocess_data(sensor_data):
    gyro = sensor_data["gyro"]
    accl = sensor_data["accl"]
    # Separate and attribute the gyro and accelerometer readings in columns
    gyro_scaled = (np.array([gyro["x"], gyro["y"], gyro["z"]]))
    accl_scaled = (np.array([accl["x"], accl["y"], accl["z"]]))
    # Concatenate the scaled readings to form the input data for the SVM model
    input_data = np.concatenate([gyro_scaled, accl_scaled])
    return input_data.reshape(1, -1)

# Define a function to handle incoming sensor data from the API endpoint
def handle_sensor_data(sensor_data_json):
    sensor_data = json.loads(sensor_data_json)
    input_data = preprocess_data(sensor_data)
    # Make a prediction using the SVM model
    prediction = model.predict(input_data)[0]
    # Do something with the predicted movement, e.g. display it or use it for further processing
    movement_attributes = {
        "jodan_ooke" : "red",          # Upper BLOCK
        "choodan_ooke" : "blue",       # Middle BLOCK
        "gedan_ooke" : "yellow",       # Lower BLOCK
        "jodan_zooki" : "cyan",        # Upper PUNCH
        "choodan_zooki" : "magenta",   # Middle PUNCH
        "gedan_zooki" : "light_grey",  # Lower PUNCH
        "random" : "white"             # Random Movements
    }
    color = movement_attributes[prediction]
    print(colored('Predicted movement: ', 'green'), colored(f'{prediction}', f'{color}', attrs=["bold", "underline"]), colored(f' <--', 'green'))
    return prediction

#Sensor data is received via an API endpoint as a JSON object

# sensor_data_json = '{"gyro": {"x": -0.021733524277806282, "y": -0.015322763472795486, "z": 0.002130528911948204}, "accl": {"x": -0.00213623046875, "y": -0.00067138671875, "z": -1.0061187744140625}}'
# handle_sensor_data(sensor_data_json)
