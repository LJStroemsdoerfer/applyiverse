# load libs
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from cryptocast import cryptocast

# create app container
app = Flask(__name__)
app.config["DEBUG"] = True

# create app route
@app.route('/forecast', methods=['GET'])
def home():

    # init the class
    btc_forecast = cryptocast()

    # getting the data
    btc_forecast.get_data()

    # prep the data
    btc_forecast.prep_data()

    # build the forecast
    btc_forecast.forecast()

    # return
    return {'msg': btc_forecast.message}

# run the app
app.run(port = '5555', host = '0.0.0.0')

