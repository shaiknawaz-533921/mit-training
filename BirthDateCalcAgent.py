from datetime import datetime, date
from abc import ABC
from BaseAgent import BaseAgent

class BirthdateCalculatorAgent(BaseAgent):
    def __init__(self):
        # Initialize the parent class with agent details
        super().__init__(
            name="BirthdateCalculatorAgent",
            description="Calculates days until the next birthday using day and month",
            action=self.calculate_days_until_birthday
        )

    def calculate_days_until_birthday(self, birthdate: str) -> int:
        try:
            # Parse the input birthdate in 'DD-MM' format
            birth_date = datetime.strptime(birthdate, "%d-%m").date()
            today = date.today()

            # Get the birth day and month
            birth_day = birth_date.day
            birth_month = birth_date.month

            # Calculate this year's birthday
            this_year_birthday = date(today.year, birth_month, birth_day)

            # If birthday has already passed this year, use next year's
            if this_year_birthday < today:
                next_birthday = date(today.year + 1, birth_month, birth_day)
            else:
                next_birthday = this_year_birthday

            # Calculate days until next birthday
            days_until = (next_birthday - today).days

            print(f"Days until next birthday (on {next_birthday.strftime('%B %d, %Y')}): {days_until} Days")
            return days_until

        except ValueError as e:
            raise ValueError("Invalid birthdate format. Please use 'DD-MM' (e.g., '15-06').")