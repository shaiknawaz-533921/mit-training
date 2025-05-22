from BaseAgent import BaseAgent

def greet_action(name: str):
    return f"Good morning, {name}!"

class GreetAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="GreetAgent",
            description="Greets a person with a good morning message.",
            action=greet_action
        )