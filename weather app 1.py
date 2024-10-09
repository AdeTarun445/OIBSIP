import requests

def get_weather(api_key, location):
    """Fetch weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_weather(data):
    """Display the weather information."""
    if data:
        city = data.get('name')
        temperature = data['main'].get('temp')
        humidity = data['main'].get('humidity')
        weather_condition = data['weather'][0].get('description', 'No description available')

        print(f"\nCurrent weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather condition: {weather_condition.capitalize()}\n")
    else:
        print("No data to display.")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    
    while True:
        location = input("Enter city name or ZIP code (or type 'exit' to quit): ").strip()
        if location.lower() == 'exit':
            print("Exiting the program.")
            break

        weather_data = get_weather(api_key, location)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
