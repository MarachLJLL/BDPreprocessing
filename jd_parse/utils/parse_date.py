from jd_parse.utils.abs_parser import JDParser
import re
from datetime import datetime
  
class DateParser(JDParser):
    _months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
               'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
               'October', 'November', 'December']
    
    # Regular expression to match "Month-YY" or "Month-YYYY" format
    _regex = r'(' + '|'.join(_months) + r').?([0-9]{4}|[0-9]{2})'

    @staticmethod
    def convert_datetime(output):
        # Extract the month part and convert it to an integer (1-12)
        month_str, year_suffix = output
        month = (DateParser._months.index(month_str[:3]) % 12) + 1  # Month number (1-12)

        # Convert the year suffix to a full year (e.g., 12 becomes 2012)
        year = int(year_suffix)
        if year < 100:  # Handle two-digit year as part of the 21st century
            year += (datetime.now().year // 100) * 100

        # Create a datetime object for the first day of that month
        return datetime(year, month, 1)

    @staticmethod
    def parse(jd):
        matches = list(re.finditer(DateParser._regex, jd))  # Get all matches as a list
        if matches:
            last_match = matches[-1]  # Get the last match
            output = last_match.groups()  # Capture month and year suffix
            jd_date = DateParser.convert_datetime(output)
            return jd_date
        else:
            return None
