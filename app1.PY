# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:20:20 2020

@author: computer
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('House_Price_Prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('Index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
     if flask.request.method == 'GET':
        return (flask.render_template('Index.html'))

     if flask.request.method == 'POST':
         rooms = flask.request.form['rooms']
         bathroom = flask.request.form['bathroom']
         landsize = flask.request.form['landsize']
         lattitude = flask.request.form['lattitude']
         longtitude = flask.request.form['longtitude']
         distance = flask.request.form['distance']
         car = flask.request.form['car']
         landsize = flask.request.form['landsize']
         buildingarea = flask.request.form['buildingarea']
         yearbuilt = flask.request.form['yearbuilt']

         input_variables = pd.DataFrame([[rooms, bathroom, landsize, lattitude, longtitude, distance, car, landsize, buildingarea, yearbuilt]],
                                       columns=['rooms', 'bathroom', 'landsize', 'lattitude', 'longtitude',
                                                'distance', 'car', 'landsize', 'buildingarea', 'yearbuilt'],
                                       dtype='float',
                                       index=['input'])

         predictions = model.predict(input_variables)[0]
         print(predictions)

  return flask.render_template('Index.html', original_input={'Rooms': rooms, 'Bathroom': bathroom, 'Landsize': landsize, 'Lattitude': lattitude, 'Longtitude': longtitude, 'Distance': distance, 'Car': car, 'Landsize': landsize, 'BuildingArea': buildingarea, 'YearBuilt': yearbuilt},
                                     result=predictions)


if __name__ == '__main__':
    app.run(debug=True)