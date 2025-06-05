from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent

from BirthDateCalcAgent import BirthdateCalculatorAgent

from TimezoneConverterAgent import TimezoneConverterAgent

from WeatherAgent import WeatherAgent


if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉


    weather_agent = WeatherAgent()
    print(weather_agent.process_request("New York"))  # Output: The current weather in New York is Sunny with 25°C temperature.     

    BirthDate_Calc_Agent = BirthdateCalculatorAgent()
    BirthDate_Calc_Agent.process_request("27-10")
    tz_agent = TimezoneConverterAgent()
    result = tz_agent.process_request("2025-05-21 22:10", "UTC", "Asia/Kolkata")
    print(result)
    
    weather_agent = WeatherAgent()
    print(weather_agent.process_request("New York"))  # Output: The current weather in New York is Sunny with 25°C temperature.     


