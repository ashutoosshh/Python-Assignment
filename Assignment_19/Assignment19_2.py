def main():

    print("Enter first number")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    mult = lambda a,b : a * b

    ans = mult(no1, no2)

    print("Multiplication is:", ans)


if __name__ == "__main__":
    main()
