# %% imports
import os
import time

import polars as pl

# %% load data
BASE_PATH = "/home/t12e/Code/Datasets/US Weather Events (2016 - 2022)"
FILENAME = "WeatherEvents_Jan2016-Dec2022.csv"
df = pl.read_csv(os.path.join(BASE_PATH, FILENAME))

# %% eda
df.head(10)
# %%
weather_types = df.select("Type").unique()
weather_types
# %%
severity_levels = df.select("Severity").unique()
severity_levels
# %%
time_zones = df.select("TimeZone").unique()
time_zones
# %%
airport_codes = df.select("AirportCode").unique()
f"Number of airport codes: {airport_codes.shape[0]}"
# %%
cities = df.select("City").unique()
f"Number of cities: {cities.shape[0]}"
# %%
counties = df.select("County").unique()
f"Number of counties: {counties.shape[0]}"
# %%
states = df.select("State").unique()
f"Number of states: {states.shape[0]}"
# %%
zip_codes = df.select("ZipCode").unique()
f"Number of zip codes: {zip_codes.shape[0]}"
# %% feature engeering
