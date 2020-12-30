def main():
    default_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    less_that_5 = [num for num in default_list if num < 5]
    print("Numbers less than 5 are:")
    [print(num, end=' ') for num in less_that_5]
    print("")


if __name__ == '__main__':
    main()
