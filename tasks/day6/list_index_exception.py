"""Module Doc string"""


def main():
    """Main function doc string"""
    list1 = [43, 1, 2, 5, 43, 50, 100, 43]
    # print(dir(list1))
    # print(help(list1.index))
    num_index = list1.count(60) if 60 in list1 else -1
    print("List index n0 ->", num_index)


if __name__ == '__main__':
    main()
