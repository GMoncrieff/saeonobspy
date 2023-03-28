# SAEON ObsPy

SAEON ObsPy is a Python package for interacting with the South African Environmental Observation Network (SAEON) Observation Database API. It provides a simple interface to view available datasets and download observation data.

## Installation

Install SAEON ObsPy using pip:

```bash
pip install saeonobspy
```

## Usage

Below is an example of using the package to view available datasets and download a set of observations:

```python
import geopandas as gpd
from saeonobspy import SAEONObsAPI

# Initialize the API
saeon_api = SAEONObsAPI()

# View available datasets
datasets_df = saeon_api.view_datasets()

# Filter datasets by a specific area (optional)
extent_gdf = gpd.read_file('path/to/extent/shapefile.shp')
spatial_datasets_gdf = saeon_api.view_datasets(extent=extent_gdf, spatial=True)

# Filter the datasets DataFrame based on your criteria
filtered_datasets_df = datasets_df[datasets_df['siteName'] == 'Constantiaberg']
filtered_datasets_df = filtered_datasets_df[filtered_datasets_df['description'] == 'Air Temperature - Daily Minimum - Degrees Celsius']

# Download observation data
obs_data = saeon_api.get_datasets(filtered_datasets_df, start_date='2020-01-01', end_date='2020-12-31')

print(obs_data)
```

For more information on how to use the package, please refer to the documentation in the source code.

## License

This package is licensed under the MIT License. See the LICENSE file for more information.
