from BaseAgent import BaseAgent
from datetime import datetime

def care_action(name: str):
    time = datetime.now()
    if (9 <= time.hour <= 12):
        return f"Good morning, {name}! Go and eat your breakfast."
    elif (12 <= time.hour <= 15):
        return f"Good afternoon, {name}! Go and eat your lunch."
    elif (15 <= time.hour <= 18):
        return f"Good evening, {name}! Go and eat your dinner."
    else:
        return f"Good night, {name}! Go and sleep."

class CareAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="CareAgent",
            description="Reminds a person to eat and sleep.",
            action=care_action
        )