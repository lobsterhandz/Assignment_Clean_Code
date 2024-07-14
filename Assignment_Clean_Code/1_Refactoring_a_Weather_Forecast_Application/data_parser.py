class DataParser:
    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available."
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%."

    def parse_detailed_weather_data(self, data):
        if not data:
            return "Weather data not available."
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        best_time = data["best_time"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%. Best time to visit: {best_time}."
