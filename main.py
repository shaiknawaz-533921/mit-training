from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
from WeatherAgent import WeatherAgent
from ReminderAgent import ReminderAgent

if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉
    
    weather_agent = WeatherAgent()
    print(weather_agent.process_request("New York"))  # Output: The current weather in New York is Sunny with 25°C temperature. 

    reminder_agent = ReminderAgent()
    print(reminder_agent.process_request("take a break", 0.1))       