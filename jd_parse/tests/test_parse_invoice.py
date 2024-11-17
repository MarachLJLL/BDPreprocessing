from django.test import SimpleTestCase
from jd_parse.utils.parse_number_tag import NumberTagParserFactory

class TestParseInvoice(SimpleTestCase):
    rid_parser = NumberTagParserFactory.get_invoice_parser(length=5)
    allegis_parser = NumberTagParserFactory.get_invoice_parser(suffix='TD')
    rbss_parser =  NumberTagParserFactory.get_invoice_parser(length=4, prefix='RBSS')
    def test_resourceID(self):
        jd_parsed = TestParseInvoice.rid_parser.parse('Limgenco12345')
        rid = '12345'
        self.assertEquals(jd_parsed, rid)
    
    def test_allegis(self):
        jd_parsed = TestParseInvoice.allegis_parser.parse('Marach60012345TD1')
        allegis_invoice = '60012345TD'
        self.assertAlmostEquals(jd_parsed, allegis_invoice)
    
    def test_RBSS(self):
        rbss_parsed = TestParseInvoice.rbss_parser.parse('LuisRBSS2004Hi')
        allegis_invoice = 'RBSS2004'
        self.assertAlmostEquals(rbss_parsed, allegis_invoice)

        