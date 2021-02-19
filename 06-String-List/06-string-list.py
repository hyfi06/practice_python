def main():
    word = input("Give me a text: ")
    string = word.replace(' ','').lower()
    if string == string[::-1]:
        print(f"{word} is a palindrome!")
    else:
        print(f"Sorry, {word} is not a palindrome")


if __name__ == '__main__':
    main()
