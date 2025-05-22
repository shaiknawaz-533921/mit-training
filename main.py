from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
from MultiplicationAgent import MultiplicationAgent

if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉
    
    multiplication_agent = MultiplicationAgent()
    print(multiplication_agent.process_request(2, 3, 4))