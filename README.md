# saeonobspy
An python package to query available datasets and download selected datasets from the SAEON observations database

# usage
```
import os
import geopandas as gpd
from saeonobspy import SAEONObsAPI

# Set the API key using os.environ
os.environ['OBSDB_KEY'] = 'your_api_key_here'

saeonapi = SAEONObsAPI()
# Use the view_datasets method to get a list of available datasets
# Optionally, you can pass an 'extent' GeoDataFrame and set 'spatial' to True if you want to limit the results to a specific area
datasets_df = saeon_api.view_datasets()

# Filter the datasets DataFrame based on your criteria
filtered_datasets_df = datasets_df[datasets_df['siteName'] == 'Constantiaberg']
filtered_datasets_df = filtered_datasets_df[filtered_datasets_df['description'] == 'Air Temperature - Daily Minimum - Degrees Celsius']

# Use the get_datasets method to download the data for the filtered datasets
# Optionally, you can pass 'start_date' and 'end_date' to limit the data to a specific time range
obs_data = saeon_api.get_datasets(filtered_datasets_df, start_date='2020-01-01', end_date='2020-12-31')

# Now, you can work with the downloaded data in 'obs_data' DataFrame
print(obs_data.head())
```
