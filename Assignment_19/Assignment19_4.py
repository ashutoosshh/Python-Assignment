from functools import reduce

def main():

    print("Enter number of elements")
    no = int(input())

    arr = []

    for i in range(no):
        print("Enter number")
        val = int(input())
        arr.append(val)

    print("Input List:", arr)

    fil = list(filter(lambda x : x % 2 == 0, arr))
    print("List after filter:", fil)

    mp = list(map(lambda x : x * x, fil))
    print("List after map:", mp)

    result = reduce(lambda a,b : a + b, mp)
    print("Output of reduce:", result)


if __name__ == "__main__":
    main()
