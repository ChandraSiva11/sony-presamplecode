"""Hex Convertion of dictionary Elements"""
# import json


student_data = [
    {
        "student_name" : "Vachan ram",
        "marks" : [25, 25, 51, 0x05, 18, 80, 31, 80, 83, 25, 38, 55, 88, 64, 91]
    },
    {
        "student_name" : "Saketh ram",
        "marks" : [32, 19, 33, 54, 42, 14, 73, 40, 7, 51, 0x0B, 91, 9, 29, 11]
    },
    {
        "student_name" : "Sanketh",
        "marks" : [93, 82, 28, 91, 99, 45, 47, 13, 0x01, 89, 91, 65, 100, 3, 47]
    },
    {
        "student_name" : "Hruday",
        "marks" : [99, 8, 1, 18, 10, 20, 30, 8, 46, 83, 27, 18, 50, 34, 10]
    },
    {
        "student_name" : "Samvad",
        "marks" : [11, 19, 100, 85, 95, 58, 41, 67, 12, 22, 81, 30, 71, 5, 50]
    },
    {
        "student_name" : "Knowledge",
        "marks" : [95, 72, 72, 42, 3, 18, 13, 23, 25, 44, 63, 70, 94, 71, 24]
    },
    {
        "student_name" : "Saketh ram",
        "marks" : [33, 6, 13, 32, 78, 27, 100, 17, 71, 56, 68, 52, 65, 82, 67]
    }
    ]

book_index = [
    {
        "book_id" : 5678923,
        "marks" : [25, 25, 51, 5, 18, 80, 31, 80,
           83, 25, 38, 55, 88, 64, 91]
    },
    {
        "book_id" : 9876532579,
        "marks" : [32, 19, 33, 54, 42, 14, 73, 40, 7,
           51, 11, 91, 9, 29, 11]
    },
    {
        "book_id" : 91278364,
        "marks" : [93, 82, 28, 91, 99, 45, 47, 13,
           1, 89, 91, 65, 100, 3, 47]
    },
    {
        "book_id" : 12369863,
        "marks" : [99, 8, 1, 18, 10, 20, 30, 8, 46,
           83, 27, 18, 50, 34, 10]
    },
    {
        "book_id" : 32578934,
        "marks" : [11, 19, 100, 85, 95, 58, 41, 67,
           12, 22, 81, 30, 71, 5, 50]
    },
    {
        "book_id" :  35782345,
        "marks" : [95, 72, 72, 42, 3, 18, 13, 23,
           25, 44, 63, 70, 94, 71, 24]
    },
    {
        "book_id" : 87512321,
        "marks" : [33, 6, 13, 32, 78, 27, 100, 17,
           71, 56, 68, 52, 65, 82, 67]
    }
]


def hex_convert(decimal_dict, name):
    """Hex convert doc string"""
    dict_hex_data = []
    for st_det in decimal_dict:
        in_dict = {}
        in_dict[name] = st_det[name]
        # print('\t Name ->',st_det[name])
        marks = []
        for mark in st_det['marks']:
            # print('\t Marks ->',hex(mark))
            he_val = hex(mark)
            if len(he_val) <= 3:
                he_li = list(he_val)
                he_li.insert(2, '0')
                he_val = ''.join(he_li)
                # print(help(he_li.insert))
                # exit(0)
            # print(he_val)
            marks.append(he_val)
            # marks.append(hex(mark).rstrip('\''))
        in_dict['marks'] = marks
        dict_hex_data.append(in_dict)
    return dict_hex_data


def print_fun(dictionary):
    """Formated print function doc string"""
    count = 0
    print('[')
    for hex_st_detail in dictionary:
        print('\t{')
        for key, value in hex_st_detail.items():
            if key == 'student_name':
                print('\t\t"' + key + '":', '"'+str(value) +'",')
            elif key == 'book_id':
                print('\t\t"' + key + '":', str(value)+',')
            else:
                print('\t\t', '"'+key+'"', ':', '[ %s ]' % ', '.join(map(str, value)))
        count += 1
        if count < len(dictionary):
            print('\t},')
        else:
            print('\t}')
    print(']')


def validate_hex_convert(dec_data, hex_data, name):
    hex_recvd_data = hex_convert(dec_data, name)
    print('Validation -> ', hex_recvd_data)
    for i in  range(0, len(hex_recvd_data[0]['marks'])):
        # print('Elements ->', hex_recvd_data[0]['marks'][i], hex_data[0]['marks'][i])
        assert hex_recvd_data[0]['marks'][i] == hex_data[0]['marks'][i], "Vlidation Failed"


def main():
    "Main function doc string"
    student_hex_data = hex_convert(student_data, 'student_name')
    print('Student hex dictionary --->\n---------------------------')
    print_fun(student_hex_data)
    #print(dir(json.dumps(student_hex_data,indent=2)))
    book_index_hex_data = hex_convert(book_index, 'book_id')
    print('Books hex dictionary --->\n-------------------------')
    print_fun(book_index_hex_data)
    #print(dir(json.dumps(book_index_hex_data,indent=2)))

    sample_decimal = [{'marks' : [1, 2, 3, 10, 11, 12]}]
    expected_op = [{'marks' : ['0x01', '0x02', '0x03', '0x0a', '0x0b', '0x0c']}]
    validate_hex_convert(sample_decimal, expected_op, 'marks')



if __name__ == "__main__":
    main()
