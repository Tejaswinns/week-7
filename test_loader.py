import unittest
import pandas as pd
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        # Test known valid locations
        geolocator = get_geolocator()
        locations = [
            ("Museum of Modern Art", 40.7618552, -73.9782438, "museum"),
            ("USS Alabama Battleship Memorial Park", 30.684373, -88.015316, "park")
        ]
        results = [fetch_location_data(geolocator, loc[0]) for loc in locations]
        for i, (name, lat, lon, typ) in enumerate(locations):
            self.assertEqual(results[i]["location"], name)
            self.assertAlmostEqual(results[i]["latitude"], lat, places=2)
            self.assertAlmostEqual(results[i]["longitude"], lon, places=2)
            self.assertTrue(pd.isna(results[i]["type"]))

    def test_invalid_location(self):
        # Test an invalid location
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")
        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertTrue(pd.isna(result["latitude"]))
        self.assertTrue(pd.isna(result["longitude"]))
        self.assertTrue(pd.isna(result["type"]))
        
if __name__ == "__main__":
    unittest.main()
