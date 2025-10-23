
"""
loader.py

Script to load geographical data into a pandas DataFrame, and save it as a CSV file.
This script uses geopy to fetch latitude, longitude, and type for a list of locations.
"""

from geopy.geocoders import Nominatim
import pandas as pd
import time

def get_geolocator(agent='h501-student'):
    """
    Create and return a Nominatim geolocator instance.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'.

    Returns
    -------
    Nominatim
        A geopy Nominatim geolocator object.
    """
    return Nominatim(user_agent=agent)


def fetch_location_data(geolocator, loc):
    """
    Fetch latitude, longitude, and type for a given location string using the geolocator.

    Parameters
    ----------
    geolocator : Nominatim
        The geopy Nominatim geolocator object.
    loc : str
        The location name or address to geocode.

    Returns
    -------
    dict
        Dictionary with keys: location, latitude, longitude, type. If not found, latitude/longitude/type are pd.NA.
    """
    location = geolocator.geocode(loc)

    if location is None:
        # Return NA values if location is not found
        return {"location": loc, "latitude": pd.NA, "longitude": pd.NA, "type": pd.NA}
    # Return found location data (type is not available from geopy, so set to pd.NA or a default value)
    return {"location": loc, "latitude": location.latitude, "longitude": location.longitude, "type": pd.NA}


def build_geo_dataframe(geolocator, locations):
    """
    Build a pandas DataFrame with geocoded data for a list of locations.

    Parameters
    ----------
    geolocator : Nominatim
        The geopy Nominatim geolocator object.
    locations : list of str
        List of location names or addresses to geocode.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: location, latitude, longitude, type.
    """
    # Fetch geocoded data for each location with delay to respect rate limits
    geo_data = []
    for loc in locations:
        geo_data.append(fetch_location_data(geolocator, loc))
        time.sleep(1)  # Delay 1 second between requests to avoid rate limits
    return pd.DataFrame(geo_data)



# Example usage: Run this script directly to create a CSV of geocoded locations
if __name__ == "__main__":
    # Create geolocator instance
    geo = get_geolocator()

    # List of locations to geocode
    locations = [
        "Museum of Modern Art",
        "iuyt8765(*&)",
        "Alaska",
        "Franklin's Barbecue",
        "Burj Khalifa"
    ]

    # Build DataFrame with geocoded data
    df = build_geo_dataframe(geo, locations)

    # Save DataFrame to CSV
    df.to_csv("./geo_data.csv")
