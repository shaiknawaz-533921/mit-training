from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
from WishAgent import WishAgent

if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉

    wish_agent = WishAgent()
    print(wish_agent.process_request("Rita"))