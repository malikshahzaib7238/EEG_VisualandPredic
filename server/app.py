from flask import send_file
import plotly.graph_objs as go
import traceback
import io
import base64
import pymysql
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math
import tensorflow as tf
import mne
import os
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from io import BytesIO
import matplotlib
# Set a non-interactive backend for Matplotlib
matplotlib.use("agg")
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})  

host = 'localhost'
user = 'root'
password = 'zaq@12wsx'
database = 'eeg-app'


def create_connection():
    return pymysql.connect(host=host, user=user, password=password, database=database)


def preprocessEDF(file_path):
    # Read a single file and preprocess it
    edf_file = mne.io.read_raw_edf(file_path, eog=['FP1', 'FP2', 'F3', 'F4',
                                                   'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8',
                                                   'T3', 'T4', 'T5', 'T6', 'PZ', 'FZ', 'CZ', 'A1', 'A2'
                                                   ], verbose='error', preload=True)
    edf_file_down_sampled = edf_file.resample(
        250, npad="auto")  # Set sampling frequency to 250 Hz
    ed = edf_file_down_sampled.to_data_frame(picks=None, index=None, scalings=None,
                                             copy=True, start=None, stop=None)  # Converting into dataframe
    Fp1_Fp7 = (ed.loc[:, 'FP1']) - (ed.loc[:, 'F7'])
    FP2_F8 = (ed.loc[:, 'FP2']) - (ed.loc[:, 'F8'])
    F7_T3 = (ed.loc[:, 'F7']) - (ed.loc[:, 'T3'])
    F8_T4 = (ed.loc[:, 'F8']) - (ed.loc[:, 'T4'])
    T3_T5 = (ed.loc[:, 'T3']) - (ed.loc[:, 'T5'])
    T4_T6 = (ed.loc[:, 'T4']) - (ed.loc[:, 'T6'])
    T5_O1 = (ed.loc[:, 'T5']) - (ed.loc[:, 'O1'])
    T6_O2 = (ed.loc[:, 'T6']) - (ed.loc[:, 'O2'])
    A1_T3 = (ed.loc[:, 'A1']) - (ed.loc[:, 'T3'])
    T4_A2 = (ed.loc[:, 'T4']) - (ed.loc[:, 'A2'])
    T3_C3 = (ed.loc[:, 'T3']) - (ed.loc[:, 'C3'])
    C4_T4 = (ed.loc[:, 'C4']) - (ed.loc[:, 'T4'])
    C3_CZ = (ed.loc[:, 'C3']) - (ed.loc[:, 'CZ'])
    CZ_C4 = (ed.loc[:, 'CZ']) - (ed.loc[:, 'C4'])
    FP1_F3 = (ed.loc[:, 'FP1']) - (ed.loc[:, 'F3'])
    FP2_F4 = (ed.loc[:, 'FP2']) - (ed.loc[:, 'F4'])
    F3_C3 = (ed.loc[:, 'F3']) - (ed.loc[:, 'C3'])
    F4_C4 = (ed.loc[:, 'F4']) - (ed.loc[:, 'C4'])
    C3_P3 = (ed.loc[:, 'C3']) - (ed.loc[:, 'P3'])
    C4_P4 = (ed.loc[:, 'C4']) - (ed.loc[:, 'P4'])
    P3_O1 = (ed.loc[:, 'P3']) - (ed.loc[:, 'O1'])
    P4_O2 = (ed.loc[:, 'P4']) - (ed.loc[:, 'O2'])
    data = {
        'Fp1_Fp7': Fp1_Fp7,
        'FP2_F8': FP2_F8,
        'F7_T3': F7_T3,
        'F8_T4': F8_T4,
        'T3_T5': T3_T5,
        'T4_T6': T4_T6,
        'T5_O1': T5_O1,
        'T6_O2': T6_O2,
        'A1_T3': A1_T3,
        'T4_A2': T4_A2,
        'T3_C3': T3_C3,
        'C4_T4': C4_T4,
        'C3_CZ': C3_CZ,
        'CZ_C4': CZ_C4,
        'FP1_F3': FP1_F3,
        'FP2_F4': FP2_F4,
        'F3_C3': F3_C3,
        'F4_C4': F4_C4,
        'C3_P3': C3_P3,
        'C4_P4': C4_P4,
        'P3_O1': P3_O1,
        'P4_O2': P4_O2
    }
    new_data_frame = pd.DataFrame(data, columns=['Fp1_Fp7', 'FP2_F8', 'F7_T3', 'F8_T4', 'T3_T5', 'T4_T6', 'T5_O1',
                                                 'T6_O2', 'A1_T3', 'T4_A2', 'T3_C3', 'C4_T4', 'C3_CZ',
                                                 'CZ_C4', 'FP1_F3', 'FP2_F4', 'F3_C3', 'F4_C4', 'C3_P3',
                                                 'C4_P4', 'P3_O1', 'P4_O2'
                                                 ])
    fs = edf_file_down_sampled.info['sfreq']
    row, col = new_data_frame.shape
    n = math.ceil(row / (15000 - int(fs * 5)))
    i = 0
    j = 15000

    for y in range(n - 1):
        if y == 0:
            example_1 = new_data_frame.iloc[0:15000, :].values
            matrix = np.expand_dims(example_1, axis=0)
        elif j < row:
            example = new_data_frame.iloc[i:j, :].values
            example = np.expand_dims(example, axis=0)
            matrix = np.vstack((matrix, example))
        else:
            example = new_data_frame.iloc[-15000:, :].values
            example = np.expand_dims(example, axis=0)
            matrix = np.vstack((matrix, example))
            break
        i = int(j - (fs * 5))
        j = int(j + 15000 - (fs * 5))
    return matrix.astype('float32')


def predictEDF(file_path):

    model = tf.keras.models.load_model(
        'C:/nmt_scalp_eeg_dataset/modelbest_loss.hdf5')

    input_data = preprocessEDF(file_path)

    input_data = np.swapaxes(input_data, 1, 2)

    predictions = model.predict(input_data)

    predictions = np.mean(predictions, axis=1)

    predictions = np.argmax(predictions)
    if predictions >= 0.5:
        predictions = 1
    else:
        predictions = 0

    return predictions


def generate_eeg_graph(file_path):
    # Read the EDF file
    raw = mne.io.read_raw_edf(file_path, preload=True)

    # Plot the EEG data using matplotlib
    fig = raw.plot(scalings='auto', show=False)

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (uV)')
    plt.grid(True)

    # Automatically adjust the plot layout to prevent overlap
    plt.tight_layout()

    # Convert the Matplotlib figure to a binary format
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    binary_data = buf.getvalue()
    buf.close()

    # Encode the binary data to base64
    base64_data = base64.b64encode(binary_data).decode()

    # Close the plot to release resources
    plt.close()

    return base64_data


@app.route("/graph", methods=['POST'])
def plot_eeg_graph():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request.'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file.'}), 400

        if file:
            filename = secure_filename(file.filename)
            # Save the file to a temporary directory
            file_path = os.path.join('./temp_files', filename)
            file.save(file_path)
            base64_data = generate_eeg_graph(file_path)
            os.remove(file_path)
            return jsonify({'graph': base64_data}), 200
        else:
            return jsonify({'error': 'Error while processing the file.'}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred during processing: ' + str(e)}), 500



@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if the 'temp_files' folder exists, if not, create it
        if not os.path.exists('temp_files'):
            os.makedirs('temp_files')

        print("This function is now called")
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request.'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file.'}), 400

        if file:
            filename = secure_filename(file.filename)
            # Save the file to the 'temp_files' directory
            file_path = os.path.join('temp_files', filename)
            file.save(file_path)
            prediction = predictEDF(file_path)
            # Save the EDF file content to the 'eegdata' table
            try:
                connection = create_connection()
                cursor = connection.cursor()

                with open(file_path, 'rb') as edf_file:
                    file_content = edf_file.read()

                sql = "INSERT INTO eegdata (file, prediction) VALUES (%s, %s)"
                if prediction == 0:
                    content = "Normal"
                else:
                    content = "Abnormal"
                cursor.execute(sql, (file_content, content))
                connection.commit()

                cursor.close()
                connection.close()
                os.remove(file_path)
            except pymysql.Error as e:
                return jsonify({'error': 'Error saving data to the database.'}), 500
            if prediction == 0:
                return jsonify({'prediction': 'Your Report is Normal'}), 200
            else:
                return jsonify({'prediction': 'Your Report is Abnormal'}), 200
        else:
            return jsonify({'error': 'Error while processing the file.'}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred during processing: ' + str(e)}), 500


@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if name and email and message:
        try:
            # Create the folder if it doesn't exist
            if not os.path.exists('contactData'):
                os.makedirs('contactData')

            with open('contactData/form-data.txt', 'a') as file:
                file.write(
                    f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")
            return jsonify({'message': 'Form data submitted successfully.'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Incomplete form data.'}), 400


@app.route('/login_doctor', methods=['POST'])
def login_doctor():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        password = data['password']

        try:
            connection = create_connection()
            cursor = connection.cursor()

            sql = "SELECT * FROM doctor WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return jsonify({"message": "Login successful!"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        except pymysql.Error as e:
            return jsonify({"error": "Login failed"}), 500


@app.route('/view', methods=['GET'])
def view_edf_files():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        sql = "SELECT `No.`, `File`, `Prediction` FROM eegdata"
        cursor.execute(sql)
        edf_files = [{"No": row[0], "Prediction": row[2]}
                     for row in cursor.fetchall()]

        cursor.close()
        connection.close()

        return jsonify({"edf_files": edf_files}), 200

    except pymysql.Error as e:
        print("Database Error:", e)
        return jsonify({"error": "Failed to retrieve EDF files: " + str(e)}), 500


@app.route('/download/<file_no>', methods=['GET'])
def download_file(file_no):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        sql = "SELECT `File` FROM eegdata WHERE `No.` = %s"
        cursor.execute(sql, (file_no,))
        file_data = cursor.fetchone()

        cursor.close()
        connection.close()

        if file_data:
            file_content = file_data[0]
            return send_file(
                io.BytesIO(file_content),
                mimetype='application/octet-stream',  # Set the correct MIME type for EDF files
                as_attachment=True,
                download_name=f'file_{file_no}.edf'
            )
        else:
            return jsonify({"error": "File not found"}), 404

    except Exception as e:
        print("Download Error:", e)
        return jsonify({"error": "Failed to download file"}), 500


@app.route('/login_patient', methods=['POST'])
def login_patient():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        password = data['password']

        try:
            connection = create_connection()
            cursor = connection.cursor()

            sql = "SELECT * FROM patient WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return jsonify({"message": "Login successful!"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        except pymysql.Error as e:
            return jsonify({"error": "Login failed"}), 500


@app.route('/signup', methods=['POST'])
def doctor_signup():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        email = data['email']
        password = data['password']

        # Check if any of the fields are empty
        if not (username and email and password):
            return jsonify({"error": "All fields must be filled"}), 400

        try:
            connection = create_connection()
            cursor = connection.cursor()

            # Check if the username already exists in the database
            sql_check_username = "SELECT * FROM patient WHERE username=%s"
            cursor.execute(sql_check_username, (username,))
            existing_username = cursor.fetchone()

            if existing_username:
                return jsonify({"error": "Username already exists"}), 409

            # Check if the email already exists in the database
            sql_check_email = "SELECT * FROM patient WHERE email=%s"
            cursor.execute(sql_check_email, (email,))
            existing_email = cursor.fetchone()

            if existing_email:
                return jsonify({"error": "Email already exists"}), 409

            # Insert the new user into the database
            sql_insert_user = "INSERT INTO patient (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert_user, (username, email, password))
            connection.commit()

            cursor.close()
            connection.close()

            return jsonify({"message": "Patient signup successful!"}), 201

        except pymysql.Error as e:
            return jsonify({"error": "Patient signup failed"}), 500


if __name__ == "__main__":
    app.run()
