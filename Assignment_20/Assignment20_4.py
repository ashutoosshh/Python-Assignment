import threading

def Small(st):

    count = 0
    t = threading.current_thread()

    for ch in st:
        if ch.islower():
            count = count + 1

    print("\nThread Name:", t.name)
    print("Thread ID:", t.ident)
    print("Small letters count:", count)


def Capital(st):

    count = 0
    t = threading.current_thread()

    for ch in st:
        if ch.isupper():
            count = count + 1

    print("\nThread Name:", t.name)
    print("Thread ID:", t.ident)
    print("Capital letters count:", count)


def Digits(st):

    count = 0
    t = threading.current_thread()

    for ch in st:
        if ch.isdigit():
            count = count + 1

    print("\nThread Name:", t.name)
    print("Thread ID:", t.ident)
    print("Digits count:", count)


def main():

    print("Enter a string")
    st = input()

    t1 = threading.Thread(target=Small, args=(st,), name="Small")
    t2 = threading.Thread(target=Capital, args=(st,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(st,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()
