from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
from WeatherAgent import WeatherAgent

if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉
    
    weather_agent = WeatherAgent()
    print(weather_agent.process_request("New York"))  # Output: The current weather in New York is Sunny with 25°C temperature.    