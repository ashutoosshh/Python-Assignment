import threading

def Maximum(arr):

    max = arr[0]

    for i in arr:
        if i > max:
            max = i

    print("Maximum number is:", max)


def Minimum(arr):

    min = arr[0]

    for i in arr:
        if i < min:
            min = i

    print("Minimum number is:", min)


def main():

    print("Enter number of elements")
    no = int(input())

    arr = []

    for i in range(no):
        print("Enter number")
        val = int(input())
        arr.append(val)

    print("Input List:", arr)

    t1 = threading.Thread(target=Maximum, args=(arr,))
    t2 = threading.Thread(target=Minimum, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
