def ChkPrime(no):
    if no < 2:
        return False

    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            return False
    return True


def ListPrime():
    n = int(input("Enter number of elements: "))
    arr = []
    total = 0

    for i in range(n):
        num = int(input("Enter number: "))
        arr.append(num)

    for x in arr:
        if ChkPrime(x):
            total = total + x

    print("Sum of prime numbers is:", total)


if __name__ == "__main__":
    ListPrime()
