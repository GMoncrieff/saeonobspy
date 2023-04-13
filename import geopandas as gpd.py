import geopandas as gpd
from saeonobspy import SAEONObsAPI
import time
import asyncio

import os

os.environ[
    "OBSDB_KEY"
] = "Dgpg1GP7lgMnO68-whKWvqoJok2XYW7GRAcjPRJPbto.DCNe6LUUjEbTXTGBLzNy--EPV_FRJzTnCH1hr7qeWl0"

# Initialize the API
saeon_api = SAEONObsAPI()

datasets_df = saeon_api.view_datasets()

filtered_datasets_df = datasets_df[datasets_df["siteName"] == "Constantiaberg"]
filtered_datasets_df = filtered_datasets_df[
    filtered_datasets_df["description"]
    == "Air Temperature - Daily Minimum - Degrees Celsius"
]
ob = saeon_api.get_datasets(
    filtered_datasets_df, start_date="2020-12-01", end_date="2020-12-07"
)
print(ob)
