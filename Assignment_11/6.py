def main():
    no = int(input("Enter number: "))
    temp = no
    rev = 0

    while no > 0:
        digit = no % 10
        rev = rev * 10 + digit
        no = no // 10

    if temp == rev:
        print("Palindrome number")
    else:
        print("Not a palindrome number")

if __name__ == "__main__":
    main()
