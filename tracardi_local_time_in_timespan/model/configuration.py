import pytz
from datetime import datetime
from pydantic import BaseModel


class TimeSpanConfiguration(BaseModel):
    timezone: str
    start: datetime
    end: datetime

    def is_in_timespan(self):
        now = datetime.utcnow()

        tz = pytz.timezone(self.timezone)
        local_now = now.replace(tzinfo=pytz.utc).astimezone(tz)

        now_hour_string = datetime.strftime(local_now, '%H:%M:%S')
        now_hour = datetime.strptime(now_hour_string, '%H:%M:%S')

        return self.start < now_hour < self.end
