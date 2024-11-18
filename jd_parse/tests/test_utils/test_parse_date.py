from django.test import SimpleTestCase
from jd_parse.utils.parse_date import DateParser
from datetime import datetime

class TestParseDate(SimpleTestCase):
    def test_simple_date(self):
        date_parsed = DateParser.parse("Jan24")
        expected_date = datetime(month=1, year=2024, day=1)
        self.assertEquals(date_parsed,expected_date)
    
    def test_get_date_with_space_char(self):
        normal = DateParser.parse("Aug24")
        spaced = DateParser.parse("Aug-24")
        self.assertEquals(normal, spaced)
        
    def test_get_second_date(self):
        date_parsed = DateParser.parse("Aug24foobarJan24")
        expected_date = datetime(month=1, year=2024, day=1)
        self.assertEquals(date_parsed,expected_date)
    
        