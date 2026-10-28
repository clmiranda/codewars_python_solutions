# Calendar Week => https://www.codewars.com/kata/5c2bedd7eb9aa95abe14d0ed

from datetime import date


def get_calendar_week(date_string):
    return date.fromisoformat(date_string).isocalendar()[1]
