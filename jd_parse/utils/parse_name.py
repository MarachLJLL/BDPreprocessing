import re
from jd_parse.utils.abs_parser import JDParser

class NameParser(JDParser):
    @staticmethod
    def parse(jd):
        _regex = '[A-Z][a-z]{2,}'
        matches = set(match.group() for match in re.finditer(NameParser._regex, jd)) 
    
    def match(jd, name):
        pass