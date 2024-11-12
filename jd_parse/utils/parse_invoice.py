import re
from abs_parser import JDParser

class InvoiceParserFactory():
    @staticmethod
    def get_invoice_parser(length=None, prefix="", suffix=""):
        num_len = '[0-9]+' if length == None else pattern = '[0-9]{' + str(length) + '}'
        pattern = prefix + num_len + suffix
        InvoiceParser = type('AnonymousJDParser', (JDParser), {
            'parse': lambda jd: re.search(pattern, jd).group()
        })
        return InvoiceParser