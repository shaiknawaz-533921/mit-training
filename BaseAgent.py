# -----------------------------
# Base AI Agent and Extensions
# -----------------------------

class BaseAIAgent:
    def respond(self):
        return "ello"

# Example agent implementation
class GreetingAgent(BaseAIAgent):
    def respond(self):
        return "Hello! How can I assist you today?"
    
# Sample usage
if __name__ == '__main__':
    base_agent = BaseAIAgent()
    greeting_agent = GreetingAgent()
    

    print("BaseAgent:", base_agent.respond())
    print("GreetingAgent:", greeting_agent.respond())
    