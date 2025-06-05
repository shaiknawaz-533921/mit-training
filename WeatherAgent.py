# WeatherAgent.py

from BaseAgent import BaseAgent

def weather_action(location: str):
    return f"The current weather in {location} is Sunny with 25°C temperature."

def bookMyHotel(booking: str):
    return f"your stay is booked."

class WeatherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="WeatherAgent",
            description="Provides mock weather data for a given location.",
            action=weather_action
        )
class bookMyHotel:
    def __init__(self):
        super().__init__(
            name="WeatherAgent",
            description="Provides mock weather data for a given location.",
            action=bookMyHotel
        )

