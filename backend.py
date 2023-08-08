import requests


API_KEY = "e9c8b3df4673c5c879d53092dadfb6b1"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?id={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))

