import datetime


def get_previous_monday_timestamp():
    today = datetime.date.today()
    # Calculate the number of days to subtract to get to the previous Monday
    days_to_subtract = (today.weekday() + 1) % 7
    # Subtract the days to get to the previous Monday
    previous_monday = today - datetime.timedelta(days=days_to_subtract)
    # Get the timestamp of the previous Monday at midnight (00:00:00)
    previous_monday_timestamp = datetime.datetime.combine(
        previous_monday, datetime.time.min)
    # Convert the timestamp to Unix timestamp (seconds since the epoch)
    epoch = int(previous_monday_timestamp.timestamp())
    return epoch


def get_next_sunday_timestamp():
    today = datetime.date.today()
    # Calculate the number of days to add to get to the next Sunday
    days_to_add = (6 - today.weekday()) % 7
    # Add the days to get to the next Sunday
    next_sunday = today + datetime.timedelta(days=days_to_add)
    # Get the timestamp of the next Sunday at midnight (00:00:00)
    next_sunday_timestamp = datetime.datetime.combine(
        next_sunday, datetime.time.min)
    # Convert the timestamp to Unix timestamp (seconds since the epoch)
    epoch = int(next_sunday_timestamp.timestamp())
    return epoch


def timestamp_to_datetime(timestamp):
    # convert the timestamp to a datetime object in the local timezone
    return datetime.datetime.fromtimestamp(timestamp)
