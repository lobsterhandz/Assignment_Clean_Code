class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "best_time": "afternoon"},
            "Los Angeles": {"temperature": 75, "condition": "Sunny", "humidity": 30, "best_time": "morning"},
            "Chicago": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "best_time": "afternoon"},
            "Houston": {"temperature": 85, "condition": "Sunny", "humidity": 70, "best_time": "evening"},
            "Phoenix": {"temperature": 95, "condition": "Sunny", "humidity": 20, "best_time": "morning"},
            "Philadelphia": {"temperature": 65, "condition": "Rainy", "humidity": 80, "best_time": "afternoon"},
            "San Antonio": {"temperature": 90, "condition": "Cloudy", "humidity": 60, "best_time": "evening"},
            "San Diego": {"temperature": 75, "condition": "Sunny", "humidity": 50, "best_time": "afternoon"},
            "Dallas": {"temperature": 80, "condition": "Sunny", "humidity": 55, "best_time": "morning"},
            "San Jose": {"temperature": 70, "condition": "Cloudy", "humidity": 65, "best_time": "morning"}
        }

    def fetch_weather_data(self, city):
        city_capitalized = city.title()
        return self.weather_data.get(city_capitalized, None)
