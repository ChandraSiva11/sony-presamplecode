"""Adding string to the touple"""


def main():
    """Main function doc string"""
    tupl1 = ("banana", "apple")
    tupl2 = ('orange',)
    print(type(tupl2))
    tupl3 = tupl1 + tupl2
    print('Tuple ->', tupl3)


if __name__ == '__main__':
    main()
