"""Module doc string"""


def main():
    """Main function doc string"""
    # print('File name test ->', __file__)
    # print('File path','/'.join(__file__.split('/')[0:-1])+'/')
    st_date = '2018-05-14T02:52:39.032001'
    end_date = '2020-07-17T12:57:29.000151'

    date1, time1 = st_date.split('T')
    y1, m1, d1 = date1.split('-')
    tim1 = time1.split('.')
    time1 = tim1[0]
    h1, min1, sec1 = time1.split(':')
    print(date1, time1)
    h1 = int(h1)
    min1 = int(min1)
    sec1 = int(sec1)
    y1 = int(y1)
    m1 = int(m1)
    d1 = int(d1)

    date2, time2 = end_date.split('T')
    y2, m2, d2 = date2.split('-')
    tim2 = time2.split('.')
    time2 = tim2[0]
    h2, min2, sec2 = time2.split(':')
    print(date2, time2)
    h2 = int(h2)
    min2 = int(min2)
    sec2 = int(sec2)
    y2 = int(y2)
    m2 = int(m2)
    d2 = int(d2)

    if sec2 >= sec1:
        sec_diff = sec2 - sec1
    else:
        min2 -= 1
        sec_diff = 60 + sec2 -sec1

    if min2 >= min1:
        min_diff = min2 - min1
    else:
        h2 -= 1
        min_diff = 60 + min2 - min1

    if h2 >= h1:
        hour_diff = h2 - h1
    else:
        d2 -= 1
        hour_diff = 24 + h2 - h1

    if d2 >= d1:
        day_diff = d2 - d1
    else:
        m2 -= 1
        day_diff = 30 + d2 - d1

    if m2 >= m1:
        mon_diff = m2 - m1
    else:
        y2 -= 1
        mon_diff = 12 + m2 - m1

    yer_diff = y2 -y1

    if yer_diff > 0:
        print(yer_diff, 'year', mon_diff, 'month ago')
    elif mon_diff > 0:
        print(mon_diff, 'month ago')
    elif day_diff > 0:
        print(day_diff, 'days ago')
    elif hour_diff > 0:
        print(hour_diff, 'hours ago')
    elif min_diff > 0:
        print(min_diff, 'minutes ago')
    else:
        print(sec_diff, 'seconds ago')


if __name__ == '__main__':
    main()
