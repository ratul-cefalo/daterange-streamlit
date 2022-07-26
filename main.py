from datetime import date, timedelta, datetime
from typing import Iterable
import streamlit as st


strptime = datetime.strptime
today = date.today()
from_date = st.date_input("Start Date", value=today-timedelta(7))
to_date = st.date_input("End Date", value=today)
max_split_days = int(st.number_input("Max Split Days", value=0, step=1))
daysback = today - from_date + timedelta(days=1)
daysahead = to_date - from_date + timedelta(days=2)


def split_days(
    daysback: int = daysback.days,
    daysahead: int = daysahead.days,
    max_days: int = max_split_days,
) -> Iterable:

    if (not max_days) or max_days > daysahead:
        return [(daysback, daysahead)]
    elif max_days < 1:
        raise ValueError("invalid split")
    splits = []
    while daysahead > 0:
        splits.append((daysback, min(daysback, max_days)))
        daysback -= max_days
        daysahead -= max_days
    return splits


def main():
    for begin, end in split_days():
        st.write(f"( {begin}, {end} )")


main()
