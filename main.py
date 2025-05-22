from GreetAgent import GreetAgent
from BirthdayAgent import BirthdayAgent
from BirthDateCalcAgent import BirthdateCalculatorAgent

if __name__ == "__main__":
    greet_agent = GreetAgent()
    print(greet_agent.process_request("Alice"))  # Output: Good morning, Alice!

    birthday_agent = BirthdayAgent()
    print(birthday_agent.process_request("Bob"))  # Output: Happy Birthday, Bob! 🎉

    BirthDate_Calc_Agent = BirthdateCalculatorAgent()
    BirthDate_Calc_Agent.process_request("27-10")