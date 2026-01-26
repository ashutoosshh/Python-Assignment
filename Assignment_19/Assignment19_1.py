def main():

    print("Enter number")
    no = int(input())

    power = lambda x : x * x

    ans = power(no)

    print("Result is:", ans)


if __name__ == "__main__":
    main()
