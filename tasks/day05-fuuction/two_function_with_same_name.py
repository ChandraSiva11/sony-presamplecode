"""Script to check two functions with same name"""


def func_name(aa_, bb_):
    """Doc string for function1"""
    print('Function1 Addition', aa_+bb_)


def func_name(aa_, bb_, cc_):
    """Doc string, Its considering only the function declared second"""
    print('Function2 Addition', aa_+bb_+cc_)


def main():
    """Main function doc string"""
    func_name(aa_=10, bb_=29, cc_=40)


if __name__ == '__main__':
    main()
