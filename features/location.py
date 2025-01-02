from requests import get
from json import loads

def country():
    IP = get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + IP + ".json"
    geo_reqeust = get(url)
    geo_data = geo_reqeust.json()
    country = geo_data["country"]
    return (f"I'm Guessing You Live in {country}")

def city():
    IP = get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + IP + ".json"
    geo_reqeust = get(url)
    geo_data = geo_reqeust.json()
    city = geo_data["city"]
    return (f"I'm Guessing your City is {city}")

def ip():
    ip = get("https://api.ipify.org").text
    return (f"Your Ip is {ip}")

def get_temperature_openweathermap(city):
    api_key = "57750a40690b5a50f53cc755c386cfbc"  # Replace with your actual OpenWeatherMap API key
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # send GET request to API endpoint
    response = get(
        endpoint, params={"q": city, "appid": api_key, "units": "metric"}
    )

    # check if the request was successful
    if response.status_code == 200:
        # parse JSON response
        data = loads(response.text)

        # check if 'main' key is present
        if "main" in data:
            # extract temperature in Celsius
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(
            f"Error: Failed to fetch data from API. \nStatus code: {response.status_code}"
        )

    return None

def temperature():
    IP = get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + IP + ".json"
    geo_reqeust = get(url)
    geo_data = geo_reqeust.json()
    city = geo_data["city"]
    city = city
    temperature_celsius = get_temperature_openweathermap(city)
    if temperature_celsius is not None:
        return (
            f"So, The weather or temperature in {city} is \ncurrently {temperature_celsius}°C"
        )
    else:
        return None