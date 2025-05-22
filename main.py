from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
from TimezoneConverterAgent import TimezoneConverterAgent

if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉

    tz_agent = TimezoneConverterAgent()
    result = tz_agent.process_request("2025-05-21 22:10", "UTC", "Asia/Kolkata")
    print(result)