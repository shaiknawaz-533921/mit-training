def farewell_action(name: str):
    return f"Goodbye, {name}. Have a nice day!"

class FarewellAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="FarewellAgent",
            description="It's been a pleasure interacting with you. Wishing you all the best ahead — take care and goodbye!",
            action=farewell_action
        )
