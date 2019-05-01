import json
from flask import Flask, jsonify, request
from weather_service import OpenWeatherMap

app = Flask(__name__)


@app.route('/get_weather', methods=['GET'])
def get_weather():
    # Opens request.json and reads the data to a variable
    with open('./data_specs/request.json', 'r+') as data:
        request_data = json.load(data)

    # Creates an instance of the OpenWeatherMap class
    owmo = OpenWeatherMap()
    # Calls the get_weather method of the OpenWeatherMap class
    # Returns the weather using the request data found in request.json
    weather = owmo.get_weather(city=request_data['MessageRequest']['city'],
                               country=request_data['MessageRequest']['country'],
                               units=request_data['MessageRequest']['units'],
                               weather_type=request_data['MessageRequest']['weather_type'])

    # Displays JSON formatted weather data onto webpage
    return jsonify({
        request_data['MessageRequest']['weather_type'] + " weather": weather
    })


@app.route('/', methods=['GET'])
def main():
    return jsonify({
        "How to modify the weather data recieved": "Edit request.json inside of data_specs folder",
        "How to get weather data": "Go to localhost:5000/get_weather"
    })


if __name__ == "__main__":
    app.run(debug=True)
