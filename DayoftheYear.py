from datetime import datetime

def get_day_of_year():
    """Returns the position of today's date in the year."""
    current_date = datetime.now()
    return current_date.timetuple().tm_yday