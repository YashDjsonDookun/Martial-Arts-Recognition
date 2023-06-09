from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO
import csv
import time
import os
import joblib
from app import *

app = Flask(__name__)
socketio = SocketIO()
socketio.init_app(app)

predictions = [{''}]

def generate_training_file(_request):
    _actionFolder = _request.path[12:]
    _sensor = _request.path[1:5]
    _data = request.get_json()
    timestamp = time.strftime("%H%M%S", time.localtime())
    if (_sensor == "gyro"):
        data_file = f"{timestamp}_{_actionFolder}_gyro.csv"
    else:            
        data_file = f"{timestamp}_{_actionFolder}_acc.csv"

    training_data_dir = (f'assets/Data/Training/{_actionFolder}')

    if not os.path.exists(training_data_dir):
        os.makedirs(training_data_dir)

    with open((f"{training_data_dir}/{data_file}"), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(['x', 'y', 'z'])
        for row in _data:
            writer.writerow([row['x'], row['y'], row['z']])

##################################################################
# 
# Training Endpoints
# 
##################################################################
@app.route('/gyro_train_jodan_ooke', methods=['POST'])
def gyro_train_jodan_ooke():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving Gyro Training Data (Jodan Ooke): {data}')
    return jsonify(data)

@app.route('/gyro_train_choodan_ooke', methods=['POST'])
def gyro_train_choodan_ooke():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving Gyro Training Data (Choodan Ooke): {data}')
    return jsonify(data)

@app.route('/gyro_train_gedan_ooke', methods=['POST'])
def gyro_train_gedan_ooke():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving Gyro Training Data (Gedan Ooke): {data}')
    return jsonify(data)

@app.route('/gyro_train_jodan_zooki', methods=['POST'])
def gyro_train_jodan_zooki():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving Gyro Training Data (Jodan Zooki): {data}')
    return jsonify(data)

@app.route('/gyro_train_choodan_zooki', methods=['POST'])
def gyro_train_choodan_zooki():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving Gyro Training Data (Choodan Zooki): {data}')
    return jsonify(data)

@app.route('/gyro_train_gedan_zooki', methods=['POST'])
def gyro_train_gedan_zooki():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving Gyro Training Data (Gedan Zooki): {data}')
    return jsonify(data)

@app.route('/gyro_train_random', methods=['POST'])
def gyro_train_random():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving Gyro Training Data (Random): {data}')
    return jsonify(data)
##################################################################
@app.route('/accl_train_jodan_ooke', methods=['POST'])
def accl_train_jodan_ooke():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving ACC Training Data (Jodan Ooke): {data}')
    return jsonify(data)

@app.route('/accl_train_choodan_ooke', methods=['POST'])
def accl_train_choodan_ooke():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving ACC Training Data (Choodan Ooke): {data}')
    return jsonify(data)

@app.route('/accl_train_gedan_ooke', methods=['POST'])
def accl_train_gedan_ooke():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving ACC Training Data (Gedan Ooke): {data}')
    return jsonify(data)

@app.route('/accl_train_jodan_zooki', methods=['POST'])
def accl_train_jodan_zooki():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving ACC Training Data (Jodan Zooki): {data}')
    return jsonify(data)

@app.route('/accl_train_choodan_zooki', methods=['POST'])
def accl_train_choodan_zooki():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving ACC Training Data (Choodan Zooki): {data}')
    return jsonify(data)

@app.route('/accl_train_gedan_zooki', methods=['POST'])
def accl_train_gedan_zooki():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving ACC Training Data (Gedan Zooki): {data}')
    return jsonify(data)

@app.route('/accl_train_random', methods=['POST'])
def accl_train_random():
    data = request.get_json()
    generate_training_file(request)
    print(f'Receiving ACC Training Data (Random): {data}')
    return jsonify(data)
##################################################################
@app.route('/gyro_train_undefined', methods=['POST'])
def gyro_train_undefined():
    data = request.get_json()
    print(f'Undefined Gyro Data Received - disregarding:')
    return jsonify(data)

@app.route('/accl_train_undefined', methods=['POST'])
def accl_train_undefined():
    data = request.get_json()
    print(f'Undefined Acc Data Received - disregarding')
    return jsonify(data)
##################################################################
# 
# Live Data Endpoints
# 
##################################################################
@app.route('/live', methods=['POST'])
def live():
    data = json.dumps(request.get_json(silent = True)) 
    movement = handle_sensor_data(data)
    return movement