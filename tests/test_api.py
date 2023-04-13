import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import pytest
from saeonobspy import SAEONObsAPI
from asynctest import CoroutineMock, patch


# Fixtures
@pytest.fixture
def saeon_api():
    with patch.dict(os.environ, {"OBSDB_KEY": "test_key"}):
        saeon_api = SAEONObsAPI()
    return saeon_api


@pytest.fixture
def example_extent():
    return gpd.GeoDataFrame(
        {
            "geometry": [Point(18.5, -33.5).buffer(1)],
            "id": [1],
        },
        crs="EPSG:4326",
    )


@pytest.fixture
def example_datasets():
    return pd.DataFrame(
        {
            "id": ["1", "2", "3"],
            "siteName": ["Site1", "Site2", "Site3"],
            "latitudeNorth": [-33.0, -34.0, -35.0],
            "longitudeEast": [18.0, 19.0, 20.0],
        }
    )


# Tests


def test_init(saeon_api):
    assert saeon_api.BASE_URL == "https://observationsapi.saeon.ac.za/Api/Datasets"
    assert saeon_api.API_KEY == "test_key"
    assert saeon_api.HEADERS == {"Authorization": "Bearer test_key"}


# Tests
def test_view_datasets_without_extent(saeon_api, example_view_datasets_data):
    saeon_api._view_datasets = CoroutineMock(return_value=example_view_datasets_data)
    result = saeon_api.view_datasets()

    assert isinstance(result, pd.DataFrame)
    assert "geometry" not in result.columns


def test_view_datasets_with_extent_non_spatial(
    saeon_api, example_view_datasets_data, example_extent
):
    saeon_api._view_datasets = CoroutineMock(return_value=example_view_datasets_data)
    result = saeon_api.view_datasets(extent=example_extent, spatial=False)

    assert isinstance(result, pd.DataFrame)
    assert "geometry" not in result.columns


def test_view_datasets_with_extent_spatial(
    saeon_api, example_view_datasets_data, example_extent
):
    saeon_api._view_datasets = CoroutineMock(return_value=example_view_datasets_data)
    result = saeon_api.view_datasets(extent=example_extent, spatial=True)

    assert isinstance(result, gpd.GeoDataFrame)
    assert "geometry" in result.columns


def test_get_datasets(saeon_api, example_datasets, example_get_datasets_data):
    saeon_api._get_datasets = CoroutineMock(return_value=example_get_datasets_data)
    result = saeon_api.get_datasets(example_datasets)

    assert isinstance(result, pd.DataFrame)
    assert "value" in result.columns
    assert "site" in result.columns


# Async fixtures
@pytest.fixture
async def example_view_datasets_data():
    return [
        {
            "organisationId": "bea77ec2-5a67-4f29-86df-3e54df40fb6f",
            "organisationCode": "SAEON",
            "organisationName": "South African Environmental Observation Network",
            "organisationDescription": "A sustained, coordinated, responsive and comprehensive South African in-situ environmental observation network that delivers long-term reliable data.",
            "organisationUrl": "https://wwww.saeon.ac.za",
            "programmeId": "8804a516-6eec-4caa-8af0-a9216e601a34",
            "programmeCode": "SAEON",
            "programmeName": "South African Environmental Observation Network",
            "programmeDescription": "A sustained, coordinated, responsive and comprehensive South African in-situ environmental observation network that delivers long-term reliable data.",
            "programmeUrl": "https://wwww.saeon.ac.za",
            "projectId": "407da6d4-7fb1-4a18-992b-d91da254281d",
            "projectCode": "SAEON",
            "projectName": "South African Environmental Observation Network",
            "projectDescription": "A sustained, coordinated, responsive and comprehensive South African in-situ environmental observation network that delivers long-term reliable data.",
            "projectUrl": "https://wwww.saeon.ac.za",
            "siteId": "390fec30-41cf-4744-9922-005a1e4e5f4b",
            "siteCode": "ALN_BEN",
            "siteName": "Arid Lands_Benfontein",
            "siteDescription": "Benfontein Private Reserve - Kimberley",
            "stationCode": "ALN_BEN_AWS",
            "stationName": "Arid Lands Node - Benfontein Automated Weather Station",
            "stationDescription": "Automated weather station, Campbell Scientific instruments measuring Air temp, RH, Nett radiation, UV, rainfall, wind speed & direction, soil moisture, soil temp.",
            "stationUrl": "http://lognet.saeon.ac.za:8088/Benfontein",
            "phenomenonId": "5c029394-6a23-42fe-b227-ea025410b94d",
            "phenomenonCode": "ATMP",
            "phenomenonName": "Air Temperature",
            "phenomenonDescription": "Air Temperature",
            "phenomenonUrl": "urn:ogc:def:phenomenon:OGC:airtemperature",
            "offeringId": "63936e75-a8c4-43a8-8dba-155b43077f65",
            "offeringCode": "AVE",
            "offeringName": "Average",
            "offeringDescription": "Average",
            "unitId": "542e075c-fa6d-4fd9-92b5-75d85c6df713",
            "unitCode": "DEGC",
            "unitName": "Degrees Celsius",
            "unitSymbol": "°C",
            "variable": "Air Temperature, Average, Degrees Celsius",
            "downloadUrl": "https://observations.saeon.ac.za/Dataset/obsdb.0000.013C",
            "doi": "10.15493/obsdb.0000.013C",
            "doiUrl": "https://doi.org/10.15493/obsdb.0000.013C",
            "citation": "SAEON Observations Database (2018): Air Temperature, Average, Degrees Celsius for Arid Lands_Benfontein, Arid Lands Node - Benfontein Automated Weather Station 100,00m above sea level from 2018-02-28 to 2018-05-31. South African Environmental Observation Network (SAEON). (dataset). https://doi.org/10.15493/obsdb.0000.013C",
            "code": "ALN_BEN_AWS~ATMP~AVE~DEGC",
            "name": "Arid Lands Node - Benfontein Automated Weather Station, Air Temperature, Average, Degrees Celsius",
            "title": "Air Temperature, Average, Degrees Celsius for Arid Lands_Benfontein, Arid Lands Node - Benfontein Automated Weather Station 100,00m above sea level from 2018-02-28 to 2018-05-31",
            "description": "Air Temperature, Average, Degrees Celsius for Arid Lands_Benfontein, Arid Lands Node - Benfontein Automated Weather Station 100,00m above sea level from 2018-02-28T16:00:00+02:00 to 2018-05-31T23:55:00+02:00 at -28,89240,24,86410 (+N-S,-W+E)",
            "stationId": "2385269a-8430-448b-9f08-0635efd9199f",
            "phenomenonOfferingId": "8b2ff2df-b036-48b9-b9eb-e7c8771a4378",
            "phenomenonUnitId": "87c9cc59-e858-495f-ae77-a7935b85005b",
            "count": 26591,
            "valueCount": 26591,
            "nullCount": 0,
            "verifiedCount": 26591,
            "unverifiedCount": 0,
            "startDate": "2018-02-28T16:00:00",
            "endDate": "2018-05-31T23:55:00",
            "latitudeNorth": -28.8924,
            "latitudeSouth": -28.8924,
            "longitudeWest": 24.8641,
            "longitudeEast": 24.8641,
            "elevationMinimum": 100,
            "elevationMaximum": 100,
            "id": "1b4696cd-ac6a-4c27-e682-08da7f6a6f8f",
        },
        {
            "organisationId": "bea77ec2-5a67-4f29-86df-3e54df40fb6f",
            "organisationCode": "SAEON",
            "organisationName": "South African Environmental Observation Network",
            "organisationDescription": "A sustained, coordinated, responsive and comprehensive South African in-situ environmental observation network that delivers long-term reliable data.",
            "organisationUrl": "https://wwww.saeon.ac.za",
            "programmeId": "8804a516-6eec-4caa-8af0-a9216e601a34",
            "programmeCode": "SAEON",
            "programmeName": "South African Environmental Observation Network",
            "programmeDescription": "A sustained, coordinated, responsive and comprehensive South African in-situ environmental observation network that delivers long-term reliable data.",
            "programmeUrl": "https://wwww.saeon.ac.za",
            "projectId": "407da6d4-7fb1-4a18-992b-d91da254281d",
            "projectCode": "SAEON",
            "projectName": "South African Environmental Observation Network",
            "projectDescription": "A sustained, coordinated, responsive and comprehensive South African in-situ environmental observation network that delivers long-term reliable data.",
            "projectUrl": "https://wwww.saeon.ac.za",
            "siteId": "390fec30-41cf-4744-9922-005a1e4e5f4b",
            "siteCode": "ALN_BEN",
            "siteName": "Arid Lands_Benfontein",
            "siteDescription": "Benfontein Private Reserve - Kimberley",
            "stationCode": "ALN_BEN_AWS",
            "stationName": "Arid Lands Node - Benfontein Automated Weather Station",
            "stationDescription": "Automated weather station, Campbell Scientific instruments measuring Air temp, RH, Nett radiation, UV, rainfall, wind speed & direction, soil moisture, soil temp.",
            "stationUrl": "http://lognet.saeon.ac.za:8088/Benfontein",
            "phenomenonId": "897ba66c-3c59-4904-8b26-0404519e2e85",
            "phenomenonCode": "GTMP",
            "phenomenonName": "Grass Temperature",
            "phenomenonDescription": "Grass Temperature",
            "offeringId": "63936e75-a8c4-43a8-8dba-155b43077f65",
            "offeringCode": "AVE",
            "offeringName": "Average",
            "offeringDescription": "Average",
            "unitId": "542e075c-fa6d-4fd9-92b5-75d85c6df713",
            "unitCode": "DEGC",
            "unitName": "Degrees Celsius",
            "unitSymbol": "°C",
            "variable": "Grass Temperature, Average, Degrees Celsius",
            "downloadUrl": "https://observations.saeon.ac.za/Dataset/obsdb.0000.0135",
            "doi": "10.15493/obsdb.0000.0135",
            "doiUrl": "https://doi.org/10.15493/obsdb.0000.0135",
            "citation": "SAEON Observations Database (2018): Grass Temperature, Average, Degrees Celsius for Arid Lands_Benfontein, Arid Lands Node - Benfontein Automated Weather Station 100,00m above sea level from 2018-02-28 to 2018-05-31. South African Environmental Observation Network (SAEON). (dataset). https://doi.org/10.15493/obsdb.0000.0135",
            "code": "ALN_BEN_AWS~GTMP~AVE~DEGC",
            "name": "Arid Lands Node - Benfontein Automated Weather Station, Grass Temperature, Average, Degrees Celsius",
            "title": "Grass Temperature, Average, Degrees Celsius for Arid Lands_Benfontein, Arid Lands Node - Benfontein Automated Weather Station 100,00m above sea level from 2018-02-28 to 2018-05-31",
            "description": "Grass Temperature, Average, Degrees Celsius for Arid Lands_Benfontein, Arid Lands Node - Benfontein Automated Weather Station 100,00m above sea level from 2018-02-28T16:00:00+02:00 to 2018-05-31T23:55:00+02:00 at -28,89240,24,86410 (+N-S,-W+E)",
            "stationId": "2385269a-8430-448b-9f08-0635efd9199f",
            "phenomenonOfferingId": "0a7e7016-0f44-4ff5-872d-0f1eef82a3ba",
            "phenomenonUnitId": "c0628d9b-c71c-44da-b706-71e249c59dc4",
            "count": 26591,
            "valueCount": 26591,
            "nullCount": 0,
            "verifiedCount": 26591,
            "unverifiedCount": 0,
            "startDate": "2018-02-28T16:00:00",
            "endDate": "2018-05-31T23:55:00",
            "latitudeNorth": -28.8924,
            "latitudeSouth": -28.8924,
            "longitudeWest": 24.8641,
            "longitudeEast": 24.8641,
            "elevationMinimum": 100,
            "elevationMaximum": 100,
            "id": "88b1fdea-6ede-45c1-e67e-08da7f6a6f8f",
        },
    ]


@pytest.fixture
async def example_get_datasets_data():
    return [
        [
            {
                "site": "Constantiaberg",
                "station": "Constantiaberg automated weather station",
                "instrument": "Constantiaberg automated weather station",
                "sensor": "Constantiaberg CS215 Air temperature sensor_Daily",
                "phenomenon": "Air Temperature",
                "offering": "Daily Minimum",
                "unit": "Degrees Celsius",
                "unitSymbol": "°C",
                "variable": "Air Temperature, Daily Minimum, Degrees Celsius",
                "date": "2020-12-01T00:00:00+02:00",
                "dateUTC": "2020-11-30T22:00:00+00:00",
                "value": 7.53,
                "rawValue": 7.53,
                "latitude": -34.055,
                "longitude": 18.3874,
                "elevation": 889,
            },
            {
                "site": "Constantiaberg",
                "station": "Constantiaberg automated weather station",
                "instrument": "Constantiaberg automated weather station",
                "sensor": "Constantiaberg CS215 Air temperature sensor_Daily",
                "phenomenon": "Air Temperature",
                "offering": "Daily Minimum",
                "unit": "Degrees Celsius",
                "unitSymbol": "°C",
                "variable": "Air Temperature, Daily Minimum, Degrees Celsius",
                "date": "2020-12-02T00:00:00+02:00",
                "dateUTC": "2020-12-01T22:00:00+00:00",
                "value": 7.542,
                "rawValue": 7.542,
                "latitude": -34.055,
                "longitude": 18.3874,
                "elevation": 889,
            },
            {
                "site": "Constantiaberg",
                "station": "Constantiaberg automated weather station",
                "instrument": "Constantiaberg automated weather station",
                "sensor": "Constantiaberg CS215 Air temperature sensor_Daily",
                "phenomenon": "Air Temperature",
                "offering": "Daily Minimum",
                "unit": "Degrees Celsius",
                "unitSymbol": "°C",
                "variable": "Air Temperature, Daily Minimum, Degrees Celsius",
                "date": "2020-12-03T00:00:00+02:00",
                "dateUTC": "2020-12-02T22:00:00+00:00",
                "value": 7.118,
                "rawValue": 7.118,
                "latitude": -34.055,
                "longitude": 18.3874,
                "elevation": 889,
            },
            {
                "site": "Constantiaberg",
                "station": "Constantiaberg automated weather station",
                "instrument": "Constantiaberg automated weather station",
                "sensor": "Constantiaberg CS215 Air temperature sensor_Daily",
                "phenomenon": "Air Temperature",
                "offering": "Daily Minimum",
                "unit": "Degrees Celsius",
                "unitSymbol": "°C",
                "variable": "Air Temperature, Daily Minimum, Degrees Celsius",
                "date": "2020-12-04T00:00:00+02:00",
                "dateUTC": "2020-12-03T22:00:00+00:00",
                "value": 7.409,
                "rawValue": 7.409,
                "latitude": -34.055,
                "longitude": 18.3874,
                "elevation": 889,
            },
            {
                "site": "Constantiaberg",
                "station": "Constantiaberg automated weather station",
                "instrument": "Constantiaberg automated weather station",
                "sensor": "Constantiaberg CS215 Air temperature sensor_Daily",
                "phenomenon": "Air Temperature",
                "offering": "Daily Minimum",
                "unit": "Degrees Celsius",
                "unitSymbol": "°C",
                "variable": "Air Temperature, Daily Minimum, Degrees Celsius",
                "date": "2020-12-05T00:00:00+02:00",
                "dateUTC": "2020-12-04T22:00:00+00:00",
                "value": 8.42,
                "rawValue": 8.42,
                "latitude": -34.055,
                "longitude": 18.3874,
                "elevation": 889,
            },
            {
                "site": "Constantiaberg",
                "station": "Constantiaberg automated weather station",
                "instrument": "Constantiaberg automated weather station",
                "sensor": "Constantiaberg CS215 Air temperature sensor_Daily",
                "phenomenon": "Air Temperature",
                "offering": "Daily Minimum",
                "unit": "Degrees Celsius",
                "unitSymbol": "°C",
                "variable": "Air Temperature, Daily Minimum, Degrees Celsius",
                "date": "2020-12-06T00:00:00+02:00",
                "dateUTC": "2020-12-05T22:00:00+00:00",
                "value": 10.18,
                "rawValue": 10.18,
                "latitude": -34.055,
                "longitude": 18.3874,
                "elevation": 889,
            },
            {
                "site": "Constantiaberg",
                "station": "Constantiaberg automated weather station",
                "instrument": "Constantiaberg automated weather station",
                "sensor": "Constantiaberg CS215 Air temperature sensor_Daily",
                "phenomenon": "Air Temperature",
                "offering": "Daily Minimum",
                "unit": "Degrees Celsius",
                "unitSymbol": "°C",
                "variable": "Air Temperature, Daily Minimum, Degrees Celsius",
                "date": "2020-12-07T00:00:00+02:00",
                "dateUTC": "2020-12-06T22:00:00+00:00",
                "value": 12.72,
                "rawValue": 12.72,
                "latitude": -34.055,
                "longitude": 18.3874,
                "elevation": 889,
            },
        ]
    ]
