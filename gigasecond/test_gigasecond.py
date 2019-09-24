from gigasecond import gigasecond
from datetime import datetime, timedelta

seconds = timedelta(seconds=1000000000)


def test_recent_date_time():
    birthdate = datetime(2011, 4, 25)
    assert gigasecond(birthdate) == birthdate + seconds


def test_very_old_date_time():
    birthdate = datetime(1886, 2, 11)
    assert gigasecond(birthdate) == birthdate + seconds


def test_todays_date():
    current_time = datetime.now()
    assert gigasecond(current_time) == current_time + seconds


def test_future_date_time():
    birthdate = datetime(2020, 4, 11)
    assert gigasecond(birthdate) == birthdate + seconds
