import requests
import json


class OpenWeatherMap(object):
    def get_weather(self, city, country, units, weather_type):
        if weather_type == "current":
            weather = self.make_request_current_weather(city, units)
        elif weather_type == "5day":
            weather = self.make_request_5day_weather(city, units)

        return weather

    def make_request_current_weather(self, city, units):
        request_url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&units=%s&appid=%s' \
            % (city,
               units,
               "caf27cac11addaa321b54544b88fc94b")

        current_weather = json.loads(requests.get(request_url).content.decode('utf-8'))

        return current_weather

    def make_request_5day_weather(self, city, units):
        request_url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&units=%s&appid=%s' \
            % (city,
               units,
               "caf27cac11addaa321b54544b88fc94b")

        five_day_weather = json.loads(requests.get(request_url).content.decode('utf-8'))

        return five_day_weather
