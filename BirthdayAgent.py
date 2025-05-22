
from BaseAgent import BaseAgent

def birthday_action(name: str):
    return f"Happy Birthday, {name}! 🎉"

class BirthdayAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="BirthdayAgent",
            description="Wishes a person on their birthday.",
            action=birthday_action
        )