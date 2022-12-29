import re

date_regex = re.compile(r'''
    (0[1-9]|[1-2][0-9]|3[0-1])  # DD
    /                           # /
    (0[1-9]|1[0-2])             # MM
    /                           # /
    ([1-2][0-9]{3})             # YYYY
   ''', re.VERBOSE)


def check_valid_date(unchecked_date):
    date = date_regex.search(unchecked_date)
    if date is None:
        return False

    day = date_regex.search(unchecked_date).group(1)
    month = date_regex.search(unchecked_date).group(2)
    year = date_regex.search(unchecked_date).group(3)

    if month == ('04' or '06' or '09' or '11'):
        if int(day) > 30:
            return False
    if month == '02':
        leap_year = (int(year) % 4 == 0) and not (int(year) % 100 == 0 and not int(year) % 400 == 0)
        if int(day) > 28:
            if leap_year is False:
                return False
    if month == ('01' or '03' or '05' or '07' or '08' or '10' or '12'):
        if int(day) > 31:
            return False

    return True


temp_date = '29/02/2010'
print(check_valid_date(temp_date))
