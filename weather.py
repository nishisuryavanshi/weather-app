import requests

def get_weather(city):
    api_key = "46c837a1aa87cc5742bc1a2a794a0f4f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        country = data["sys"]["country"]
        
        print("\n" + "="*35)
        print(f"  Weather Report: {city}, {country}")
        print("="*35)
        print(f"  Temperature  : {temp}°C")
        print(f"  Feels Like   : {feels_like}°C")
        print(f"  Humidity     : {humidity}%")
        print(f"  Wind Speed   : {wind_speed} m/s")
        print(f"  Condition    : {condition.title()}")
        print("="*35)
    else:
        print("City not found! Please try again.")

while True:
    city = input("\nEnter city name (or 'quit' to exit): ")
    if city.lower() == "quit":
        print("Goodbye!")
        break
    get_weather(city)