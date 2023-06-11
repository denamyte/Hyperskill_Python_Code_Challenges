from datetime import datetime


def convert_to_standard(dt: datetime):
    return dt.strftime('%Y-%m-%d')
