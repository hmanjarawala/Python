# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:30:00 2020

@author: Himanshu.Manjarawala
"""

from flask import Flask, request, jsonify, render_template, Response
from predictcancellation import cleananomalies

import pickle

app = Flask(__name__)

#loading model
with open("./models/RFCmodel.pkl", "rb") as f:
    model = pickle.load(f)
    
def add_trip_type(df):
    is_internal = [0]*len(df)
    destinationCountry = list(df['destinationCountry'])
    guestConuntry = list(df['guest_country_code'])
    count_same =0
    for i in range(len(df)):
        if (destinationCountry[i] == guestConuntry[i]):
            #print("\nSame\nDestination Country=", df['destinationCountry'][i], "\nSource Country     =", df['guest_country_code'][i])
            count_same += 1
            is_internal[i] = 1
    print(count_same/len(df) * 100)
    return is_internal

def process_data():
    import pandas as pd
    
    df = pd.read_csv("./temp/input.csv", sep=',')
    
    temp_df = cleananomalies(filepath="./temp/input.csv")
    
    temp_df.drop(['is_canceled', 'Canceled', 'Check-Out'], axis=1, inplace=True)
    
    columns_list = list(temp_df.columns)
    
    predictions = []
    
    for i in range(len(temp_df)):
        feature_array=[]
        for col in columns_list:
            try:
                feature_array.append(temp_df[col][i])
            except TypeError as e:
                print(e)
                feature_array.append(0)
        prediction = model.predict([feature_array])
        print("Prediction of Row {} is {}".format(i, prediction[0]))
        predictions.append(prediction[0])
    # predictions = model.predict([temp_df])
    
    print(predictions)
        
    df["Prediction"] = predictions
    
    #stream = io.StringIO()
    df.to_csv("./temp/export.csv", index=False)
    with open("./temp/export.csv", "rb") as f:
        stream = f.read()
    # df.to_csv(stream, index=False)
    # print(stream)
    res = Response(stream, mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=export.csv"})
    return res

@app.route("/ordercancellation", methods=["POST"])
def index():
    input_data_csv = request.files.get("inputDataFile")
    
    # print(request.headers["Content-Type"])
    
    if (input_data_csv == None):
        print("Form data: inputDataFile required")
        resp = create_error_json_message('Form data: inputDataFile required', 400)
        return resp

    else:
        with open("./temp/input.csv", "wb") as f:
            f.write(request.files.get('inputDataFile').read())
    
    try:
        res = process_data()
    except Exception as e:
        print(e)
        resp = create_error_json_message('Some error occurred while processing data.', 500)
        return resp
    
    return res

@app.route("/download", methods=["GET"])
def download():
    try:
        res = process_data()
    except Exception as e:
        print(e)
        resp = create_error_json_message('Some error occurred while processing data.', 500)
        return resp
    
    return res

def create_error_json_message(message, status_code):
    message = {
        'status': status_code,
        'message': message,
    }
    resp = jsonify(message)
    resp.status_code = status_code
    return resp

@app.route('/', methods=['POST', 'GET'])
def server_test():
    return "Server is running!"

@app.route('/help', methods=['GET','POST'])
#@cross_origin()
def help():
    return (
        "<br/><h1>Help: Order Cancellation Prediction</h1> <br/><h2>HTTP Request:</h2> <br/><table style=width:50%><tr><td style='color:white;border:1px solid black;background-color:#325396;' valign=middle width=30% height=50px><span style=font-size: 20px>Post</span></td><td width=70% height=50px><span style=font-size: 20px>/ordercancellation</span></td></tr></table> <br/><h2>Description:</h2> <br/><table style=width:50% cellspacing=0><tr><td style='color:white;border:1px solid black;background-color:#325396;' valign=middle width=30% height=50px><span style=font-size: 20px>Parameter</span></td><td style='color:white;border:1px solid black;background-color:#325396;' valign=middle width=70% height=50px><span style=font-size: 20px>Value / Description</span></td></tr><tr><td style='border:1px solid black;' valign=middle width=30% height=60px><span style=font-size: 20px>inputDataFile</span></td><td style='border:1px solid black;' valign=middle width=70% height=60px><span style=font-size: 20px>CSV Data set as form file</span></td></tr></table>")


#@cross_origin()
@app.route('/gui', methods=["GET"])
def gui():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)