import threading

sum_result = 0
prod_result = 1

def Sum(arr):

    global sum_result
    sum_result = 0

    for i in arr:
        sum_result = sum_result + i


def Product(arr):

    global prod_result
    prod_result = 1

    for i in arr:
        prod_result = prod_result * i


def main():

    print("Enter number of elements")
    no = int(input())

    arr = []

    for i in range(no):
        print("Enter number")
        val = int(input())
        arr.append(val)

    print("Input List:", arr)

    t1 = threading.Thread(target=Sum, args=(arr,))
    t2 = threading.Thread(target=Product, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", prod_result)


if __name__ == "__main__":
    main()
