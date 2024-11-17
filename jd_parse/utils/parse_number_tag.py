import re
from jd_parse.utils.abs_parser import JDParser

class NumberTagParserFactory():
    @staticmethod
    def get_invoice_parser(length=None, prefix="", suffix=""):
        num_len = '[0-9]+' if length == None else '[0-9]{' + str(length) + '}'
        pattern = prefix + num_len + suffix
        InvoiceParser = type('NumberTagParser', (JDParser,), {
            'parse': lambda jd: re.search(pattern, jd).group()
        })
        return InvoiceParser