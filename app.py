from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['GET'])
def get_weather():
    zip_code = request.args.get('zipCode')

    if not zip_code:
        return render_template('index.html')

    # Define the API endpoint URL, API key, and query parameters as before
    url = "http://api.weatherapi.com/v1/current.json"
    api_key = "37454b3619c84b7c9b1222054232308"
    params = {
        "key": api_key,
        "q": zip_code,
        "aqi": "no"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        location = data['location']['name']
        temperature_celsius = data['current']['temp_c']
        temperature_fahrenheit = data['current']['temp_f']
        condition = data['current']['condition']['text']

        return render_template('index.html', location=location, temperature=temperature_celsius, temperature_fahrenheit=temperature_fahrenheit, condition=condition)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    print("Server is running")
    app.run(debug=True, port=8080)
