import pandas as pd
from saeonobspy.api import view_datasets, get_datasets

def test_view_datasets():
    df = view_datasets()

    # Test if the returned object is a DataFrame
    assert isinstance(df, pd.DataFrame)

    # Test if the DataFrame has the expected columns
    expected_columns = ['id', 'siteName', 'stationName', 'phenomenonName', 'phenomenonCode', 'offeringName', 'offeringCode', 'unitName', 'unitCode', 'latitudeNorth', 'longitudeEast', 'startDate', 'endDate', 'valueCount', 'obs_type_code', 'description']
    assert set(df.columns) == set(expected_columns)

def test_get_datasets():
    datasets_df = view_datasets()
    filtered_datasets = datasets_df.head(1)  # Select only the first row for testing purposes

    obs_df = get_datasets(filtered_datasets)

    # Test if the returned object is a DataFrame
    assert isinstance(obs_df, pd.DataFrame)

    # Test if the DataFrame has the expected columns
    expected_columns = ['instrument', 'sensor', 'date', 'latitude', 'longitude', 'value', 'phenomenon', 'offering', 'variable', 'unit']
    assert set(obs_df.columns) == set(expected_columns)

    # Test if the DataFrame is not empty
    assert not obs_df.empty


