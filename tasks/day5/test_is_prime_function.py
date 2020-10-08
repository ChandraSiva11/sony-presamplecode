"""This is the test script to check the function functionality"""


def is_prime(num):
    """This is the prime function doc string"""
    for i in range(2, num):
        # print('Num ->', num)
        if num % i == 0:
            return False
    return True


def main():
    """This the main function doc string"""
    inputs = [(1, True), (3, True), (6, False), (9, False), (29, True)]
    for ele in inputs:
        ret_val = is_prime(ele[0])
        if ret_val == ele[1]:
            print(ele, 'Input is validated and its prime->', ret_val)
        else:
            print(ele, 'Input is validated and its not prime->', ret_val)


if __name__ == '__main__':
    main()
