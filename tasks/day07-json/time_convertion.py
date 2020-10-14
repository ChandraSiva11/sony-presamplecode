"""Mocule doc string"""
from datetime import datetime


def main():
    """Main function Doc string"""
    str_time = datetime.strptime('2020-07-17T12:57:29.000001Z', '%Y-%m-%dT%H:%M:%S.%fZ')
    end_time = datetime.now()
    diff = end_time - str_time
    print("Difference ->", diff)


def test_function():
    """Test Function Doc String"""
    test_date_time = datetime.now()
    print(test_date_time.strftime('%a')) # abrivated Locale weekday name
    print(test_date_time.strftime('%A')) # full Locale weekday name
    print(test_date_time.strftime('%b')) # abrivated Locale month name
    print(test_date_time.strftime('%B')) # full Locale month name
    print(test_date_time.strftime('%c')) # Date and time representation
    print(test_date_time.strftime('%d')) # month day number
    print(test_date_time.strftime('%H')) # hour 24 hour format
    print(test_date_time.strftime('%I')) # hour 12 hour format
    print(test_date_time.strftime('%j')) # day no of the year
    print(test_date_time.strftime('%m')) # month number (01-12)
    print(test_date_time.strftime('%M')) # Minute (00-59)
    print(test_date_time.strftime('%p')) # AM or PM
    print(test_date_time.strftime('%S')) # seconds (00-59)
    print(test_date_time.strftime('%w')) # week day number (0-sunday, 1-monday,..)
    print(test_date_time.strftime('%W')) # week number of the year
    print(test_date_time.strftime('%x')) # date expression
    print(test_date_time.strftime('%X')) # time expression
    print(test_date_time.strftime('%y')) # last 2 digit year
    print(test_date_time.strftime('%Y')) # 4 digit year
    print(test_date_time.strftime('%Z')) # Time zone name (no characters if time zone not exist)
    print(test_date_time.strftime('%%')) # A percentage character

if __name__ == '__main__':
    main()
    test_function()
