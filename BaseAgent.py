from datetime import datetime
import pytz

# -----------------------------
# Base AI Agent and Extensions
# -----------------------------

class BaseAIAgent:
    def respond(self, *args, **kwargs):
        return "ello"


# Greeting Agent
class GreetingAgent(BaseAIAgent):
    def respond(self, *args, **kwargs):
        return "Hello! How can I assist you today?"

ABBREVIATION_MAP = {
    "IST": "Asia/Kolkata",
    "EST": "America/New_York",
    "PST": "America/Los_Angeles",
    "CST": "America/Chicago",
    "MST": "America/Denver",
    "UTC": "UTC",
}
class TimezoneConverterAgent(BaseAIAgent):
    def respond(self, date_str, from_tz_str, to_tz_str):
        try:
            # Normalize abbreviations
            from_tz_str = ABBREVIATION_MAP.get(from_tz_str.upper(), from_tz_str)
            to_tz_str = ABBREVIATION_MAP.get(to_tz_str.upper(), to_tz_str)

            # Parse input datetime
            naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            from_tz = pytz.timezone(from_tz_str)
            from_dt = from_tz.localize(naive_dt)

            # Convert to target timezone
            to_tz = pytz.timezone(to_tz_str)
            to_dt = from_dt.astimezone(to_tz)

            return f"{date_str} in {from_tz_str} is {to_dt.strftime('%Y-%m-%d %H:%M %Z%z')} in {to_tz_str}"

        except Exception as e:
            return f"Error: {str(e)}. Please ensure your input is in 'YYYY-MM-DD HH:MM' format and valid timezone names."

# -----------------------------
# Sample usage
# -----------------------------
if __name__ == '__main__':
    base_agent = BaseAIAgent()
    greeting_agent = GreetingAgent()
    tz_agent = TimezoneConverterAgent()

    print("BaseAgent:", base_agent.respond())
    print("GreetingAgent:", greeting_agent.respond())

    # Sample timezone conversion usage
    print("\n--- Timezone Converter ---")
    date_str = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    from_tz = input("Enter the source timezone (e.g., UTC): ")
    to_tz = input("Enter the target timezone (e.g., Asia/Kolkata): ")
    result = tz_agent.respond(date_str, from_tz, to_tz)
    print("TimezoneConverterAgent:", result)
