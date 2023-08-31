import requests

# Define the API endpoint URL
url = "http://api.weatherapi.com/v1/current.json"

# Define the API key (replace with your actual API key)
api_key = "37454b3619c84b7c9b1222054232308"

# Prompt the user for their zip code
zip_code = input("Enter your zip code: ")

# Define the query parameters
params = {
    "key": api_key,
    "q": zip_code,
    "aqi": "no"  # Optional: If you don't want AQI data
}

try:
    # Make the API request
    response = requests.get(url, params=params)

    # Check the response status code
    if response.status_code == 200:
        # If the response status code is 200 (OK), parse the JSON response
        data = response.json()

        # Extract and print relevant weather information
        location = data["location"]
        current = data["current"]

        print("Location:", location["name"], ",", location["region"], ",", location["country"])
        print("Temperature (°C):", current["temp_c"])
        print("Temperature (°F):", current["temp_f"])
        print("Condition:", current["condition"]["text"])
        print("Wind Speed (mph):", current["wind_mph"])
        print("Wind Speed (kph):", current["wind_kph"])
        print("Humidity:", current["humidity"])
        print("Pressure (mb):", current["pressure_mb"])
        print("Precipitation (mm):", current["precip_mm"])
        print("Cloud Cover:", current["cloud"])
    else:
        print(f"HTTP Error {response.status_code}: {response.reason}")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
