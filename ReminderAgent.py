# reminder_agent.py
import time
from datetime import datetime, timedelta
from BaseAgent import BaseAgent  # Import the BaseAgent

class ReminderAgent(BaseAgent):
    """
    ReminderAgent inherits from BaseAgent and implements a reminder action.
    """

    def __init__(self, name="Reminder Agent", description="Sets reminders for the user.", action=None):
        # Define the action as setting a reminder
        action = self.set_reminder
        super().__init__(name, description, action)  # Call the constructor of BaseAgent

    def set_reminder(self, message: str, delay_minutes: int):
        """
        Sets a reminder after a given delay in minutes.

        :param message: The reminder message.
        :param delay_minutes: The delay in minutes before the reminder.
        """
        try:
            remind_time = datetime.now() + timedelta(minutes=delay_minutes)
            print(f"Reminder set for {remind_time.strftime('%H:%M:%S')} — {message}")
            
            # Wait for the reminder time to trigger
            while datetime.now() < remind_time:
                time.sleep(1)  # Check every second

            return f" REMINDER: {message}"
        except Exception as e:
            return f" Error setting reminder: {str(e)}"
