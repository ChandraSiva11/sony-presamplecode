"""This is the test script to check the function functionality"""


def is_range(num):
    """This is the function to check the no is with in range doc string"""
    if isinstance(num, int):
        # print('Number',num)
        if num >= 100:
            # print('Input value is more than 100')
            return False
        elif bool(num < 100) and bool(num > 0):
            # print('Input value is in between 0 and 100')
            return True
        else:
            # print("Input value is not in the range")
            return False
    else:
        # print('Its not integer')
        return False


def main():
    """This the main function doc string"""
    inputs = [1, 2, 3, 4, 5, 6, 1000, 1.0, -20, 137, 59, 'siva']
    for ele in inputs:
        ret_val = is_range(ele)
        if ret_val == True:
            print(ele, ' -> Input is with in range ->', ret_val)
        else:
            print(ele, ' -> Input is not not in range ->', ret_val)


if __name__ == '__main__':
    main()
