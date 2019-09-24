from datetime import datetime, timedelta


def gigasecond(birthdate):
    return birthdate + timedelta(seconds=1000000000)
