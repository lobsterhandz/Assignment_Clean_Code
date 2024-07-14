from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if data:
            data['city'] = city.title()
        return self.parser.parse_detailed_weather_data(data)

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if data:
            data['city'] = city.title()
        return self.parser.parse_weather_data(data)

    def main(self):
        print("Welcome to the Weather Forecast Application!")
        while True:
            city = input("\nEnter the city to get the weather forecast or 'exit' to quit: ").strip()
            if city.lower() == 'exit':
                print("Exiting the weather forecast application. Goodbye!")
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").strip().lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(f"\n{forecast}")

if __name__ == "__main__":
    ui = UserInterface()
    ui.main()
