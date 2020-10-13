"""Doc String"""
from datetime import datetime


def time_difference(time_in):
    """Main function Doc string"""
    str_time = datetime.strptime(time_in, '%Y-%m-%dT%H:%M:%S.%fZ')
    end_time = datetime.now()
    diff = end_time - str_time
    # print("Difference ->", diff)
    return  diff