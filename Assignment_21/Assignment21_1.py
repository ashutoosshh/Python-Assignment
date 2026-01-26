import threading

def ChkPrime(no):

    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def Prime(arr):

    print("Prime Numbers:")
    for i in arr:
        if ChkPrime(i):
            print(i)


def NonPrime(arr):

    print("Non Prime Numbers:")
    for i in arr:
        if not ChkPrime(i):
            print(i)


def main():

    print("Enter number of elements")
    no = int(input())

    arr = []

    for i in range(no):
        print("Enter number")
        val = int(input())
        arr.append(val)

    print("Input List:", arr)

    t1 = threading.Thread(target=Prime, args=(arr,))
    t2 = threading.Thread(target=NonPrime, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
