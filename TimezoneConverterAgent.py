# TimezoneConverterAgent.py

from BaseAgent import BaseAgent
from datetime import datetime
import pytz

def timezone_conversion_action(date_str, from_tz_str, to_tz_str):
    try:
        from_tz = pytz.timezone(from_tz_str)
        to_tz = pytz.timezone(to_tz_str)

        naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        from_dt = from_tz.localize(naive_dt)
        to_dt = from_dt.astimezone(to_tz)

        return f"{date_str} in {from_tz_str} is {to_dt.strftime('%Y-%m-%d %H:%M %Z%z')} in {to_tz_str}"

    except Exception as e:
        return f"Error: {e}. Please check your input."

class TimezoneConverterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="TimezoneConverterAgent",
            description="Converts datetime from one timezone to another.",
            action=timezone_conversion_action
        )
