import datetime


def main():
    name = input("Give me your name: ")
    age = int(input("Enter your age: "))
    year = datetime.datetime.now().year + (100 - age)

    print(f"{name}, you will turn 100 years old at {year}")


if __name__ == "__main__":
    main()
