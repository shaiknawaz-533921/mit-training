# -----------------------------
# Base AI Agent and Extensions
# -----------------------------

class BaseAIAgent:
    def respond(self):
        return "Hello"

# Example agent implementation
class GreetingAgent(BaseAIAgent):
    def respond(self):
        return "Hello! How can I assist you today?"

class FarewellAgent(BaseAIAgent):
    def respond(self):
        return "Goodbye! Have a great day!"
    
# Sample usage
if __name__ == '__main__':
    base_agent = BaseAIAgent()
    greeting_agent = GreetingAgent()
    farewell_agent = FarewellAgent()

    print("BaseAgent:", base_agent.respond())
    print("GreetingAgent:", greeting_agent.respond())
    print("FarewellAgent:", farewell_agent.respond())
    
    
