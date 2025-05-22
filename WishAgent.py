from BaseAgent import BaseAgent

def wish_agent(name: str):
    return f"Hello , {name}! Hope you're doing well!"

class WishAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="WishAgent",
            description="Wishes a person with Hello.",
            action=wish_agent
        )