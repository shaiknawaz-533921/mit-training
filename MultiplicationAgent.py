from BaseAgent import BaseAgent

def multiply_numbers(*args):
    
    result = 1
    for num in args:
        try:
            result *= float(num)
        except ValueError:
            raise ValueError(f"Invalid number: {num}")
    
    return result

class MultiplicationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Multiplication Agent",
            description="Multiplies of numbers",
            action=multiply_numbers
        ) 