import threading

def EvenList(arr):

    sum = 0
    print("Even Numbers:")

    for i in arr:
        if i % 2 == 0:
            print(i)
            sum = sum + i

    print("Sum of Even Numbers:", sum)


def OddList(arr):

    sum = 0
    print("Odd Numbers:")

    for i in arr:
        if i % 2 != 0:
            print(i)
            sum = sum + i

    print("Sum of Odd Numbers:", sum)


def main():

    print("Enter number of elements")
    no = int(input())

    arr = []

    for i in range(no):
        print("Enter number")
        val = int(input())
        arr.append(val)

    print("Input List:", arr)

    t1 = threading.Thread(target=EvenList, args=(arr,))
    t2 = threading.Thread(target=OddList, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
