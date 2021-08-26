from datetime import datetime
import pytz


def is_in_timespan(time_zone, start_time, end_time):
    now = datetime.utcnow()

    tz = pytz.timezone(time_zone)
    local_now = now.replace(tzinfo=pytz.utc).astimezone(tz)

    now_hour_string = datetime.strftime(local_now, '%H:%M:%S')
    now_hour = datetime.strptime(now_hour_string, '%H:%M:%S')

    return start_time < now_hour < end_time
