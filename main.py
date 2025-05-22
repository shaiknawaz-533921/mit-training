from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
from CareAgent import CareAgent

if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉

    care_agent = CareAgent()
    print(care_agent.process_request("Iron man"))  