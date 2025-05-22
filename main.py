from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
import DayoftheYear


if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉

    # Get and print today's day number in the year
    day_of_year = DayoftheYear.get_day_of_year()
    print(f"Today is the {day_of_year}th day of the year.")
