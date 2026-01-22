def main():
    no = int(input("Enter number: "))
    count = 0

    if no == 0:
        count = 1
    else:
        while no != 0:
            no = no / 10
            count += 1

    print("Length of number is:", count)

if __name__ == "__main__":
    main()
