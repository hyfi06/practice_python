def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    common_elements = [num for num in set(a) if num in b]
    
    print(f"The common elements are: {common_elements}")
    


if __name__ == '__main__':
    main()
