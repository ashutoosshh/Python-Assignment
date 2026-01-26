from functools import reduce

def ChkPrime(no):

    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def main():

    print("Enter number of elements")
    n = int(input())

    arr = []

    for i in range(n):
        print("Enter number")
        val = int(input())
        arr.append(val)

    print("Input List:", arr)

    # Filter prime numbers
    fil = list(filter(lambda x: ChkPrime(x), arr))
    print("List after filter:", fil)

    # Map - multiply by 2
    mp = list(map(lambda x: x * 2, fil))
    print("List after map:", mp)

    # Reduce - find maximum
    result = reduce(lambda a, b: a if a > b else b, mp)
    print("Output of reduce:", result)


if __name__ == "__main__":
    main()
