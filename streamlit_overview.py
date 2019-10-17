import streamlit as st

import requests
import os

import datetime as dt
import pandas as pd
import time as t
import numpy as np

# from app.constants import locations
# from app.mcp_utils import get_ts
# from app._classes import PreviousUsage, Weather
# from app.main import read_root
read_out = {}
if __name__ == "__main__":
    location = st.selectbox("Location", ["hamburg", "berlin", "stockholm"], index=1)
    date = st.date_input("Date", dt.date(2019, 9, 1))
    time = st.time_input("Time", dt.time(8, 0))
    if not time.minute == 0:
        time = time.replace(minute=0)
        st.warning("Please select a whole hour. Time is now adjusted")
    timestamp = dt.datetime.combine(date, time)
    st.write("selected", timestamp, "to ", timestamp + dt.timedelta(hours=1))
    temp = 273 + st.slider(
        f"Please select the expacted temperature at {location} at {time.strftime('%H:%M')}?",
        -20.0,
        40.0,
        11.0,
        0.1,
    )
    hum = st.slider(
        f"Please select the expacted relative humidity at {location} at {time.strftime('%H:%M')}?",
        0,
        100,
        60,
        1,
    )
    pressure = st.slider(
        f"Please select the expacted pressure at {location} at {time.strftime('%H:%M')}?",
        600,
        1500,
        1000,
        50,
    )
    usage = st.slider(
        f"Please select the usage at {location} at {timestamp-dt.timedelta(days=2)}?",
        0,
        7000,
        1000,
        50,
    )
    usage_var = st.selectbox(
        f"Please select the amount of fluxtution in usage between {timestamp-dt.timedelta(days=2,hours=2)} and {timestamp-dt.timedelta(hours=46)}?",
        ["Flat", "Little", "More", "A lot"],
    )
    usage_var_dct = {"Flat": 0.01, "Little": 0.05, "More": 0.10, "A lot": 0.5}
    name = (
        location
        + str(timestamp)
        + str(temp)
        + str(hum)
        + str(pressure)
        + str(usage)
        + str(usage_var)
    )
    if name in read_out:
        result = read_out[name]
    else:
        result = int(np.random.rand() * (usage_var_dct[usage_var]) + 0.85)
        read_out[name] = result
    st.write(f"Expacted usage = {result} kWh")
    # if not os.path.exists("data"):
    #     os.mkdir("data")
    # if st.button("Collect data from MCP"):
    #     with st.spinner("Downloading in progress"):
    #         ts = get_ts(location, date=timestamp)
    #     st.dataframe(ts)

