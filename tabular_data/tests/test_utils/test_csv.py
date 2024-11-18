from django.test import SimpleTestCase
from tabular_data.utils.csv import CSV

class TestParseDate(SimpleTestCase):
    def test_col_to_index_zero_index(self):
        col = 'a'
        index = CSV.col_to_index(col)
        self.assertEquals(index, 0)
    
    def test_col_to_index_single_letter(self):
        col = 'o'
        index = CSV.col_to_index(col)
        self.assertEquals(index, 14)
        
    def test_col_to_index_multiple_letters(self):
        col = 'bc'
        index = CSV.col_to_index(col)
        self.assertEquals(index, 54)


    
        