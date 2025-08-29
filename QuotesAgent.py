from BaseAgent import BaseAgent

def Quote_action(Quote: str):
    return f"Today's quote for you, {Quote}!"

class QuotesAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            Quote="Don't let the mistakes and disappointments of the past control and direct your future",
            description="Gives random quotes for the day.",
            action=Quote_action
        )