import unittest

from country_codes import get_country_code

class CountryCodesTestCase(unittest.TestCase):
    """Tests for the get_country_code.py function."""

    def test_default_country_name(self):
        """Do names like 'Belgium' work?"""
        country_code = get_country_code('Belgium')
        self.assertEqual(country_code, 'be')

    def test_special_country_name(self):
        """Do names like 'Hong Kong SAR, China' work?"""
        country_code = get_country_code('Hong Kong SAR, China')
        self.assertEqual(country_code, 'hk')

    def test_country_name_none(self):
        """Do names like 'Utopia' return None?"""
        country_code = get_country_code('Utopia')
        self.assertEqual(country_code, None)

unittest.main()
