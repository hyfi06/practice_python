def main():
    num = int(input("Enter a number: "))
    divisors = [i for i in range(2, num) if num % i == 0]
    print(f"Divisors of {num} are: {divisors}")


if __name__ == '__main__':
    main()
