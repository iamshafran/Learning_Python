import unittest
from city_functions import get_city_country


class CityFunctionsTestCase(unittest.TestCase):
    """Test functions for 'city_functions.py'."""

    def test_city_country(self):
        """Do entries like 'Santiago, Chile' work?"""
        formatted_city_country = get_city_country("Santiago", "Chile")
        self.assertEqual(formatted_city_country, "Santiago, Chile")

    def test_city_country_population(self):
        """Do entries like 'Santiago, Chile - population 5000000' work?"""
        formatted_city_country_population = get_city_country(
            "Santiago", "Chile", "5000000"
        )
        self.assertEqual(
            formatted_city_country_population, "Santiago, Chile - population 5000000"
        )


unittest.main()